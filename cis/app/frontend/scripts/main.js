import Vue from 'vue';
import Vuex from 'vuex';
import VueRouter from 'vue-router'
import {csvParse} from 'd3-dsv';

import SearchScreen from './components/screens/SearchScreen.vue';
import CISProjectScreen from './components/screens/CISProjectScreen.vue'

import {searchProjects, getProjectById, getSpiders} from './cisProjectSearchAPI.js';

Vue.use(VueRouter)
Vue.use(Vuex)


const filterDescriptions = [].concat(CHOICES_FILTERS_TAGS, CHOICES_FILTERS_PARTNERS);
const selectedFilters = new Map()
for(const f of filterDescriptions){
    selectedFilters.set(f.name, new Set())
}


function filterValuesToCISTags(filterValues){
    const cisTags = new Set();

    const categoriesByUITag = CATEGORIES_CIS_DICT_FLAT;
    const cisTagByCategory = NORMALIZATION_TAGS_SOURCES_CIS_DICT;

    let uiTags = [];
    for(const [filter, tags] of filterValues.entries()){
        uiTags = [...uiTags, ...([...tags].map(t => filter+t))]
    }

    for(const uiTag of uiTags){
        const categories = categoriesByUITag[uiTag];

        for(const category of categories){
            const categoriesCISTags = cisTagByCategory[category];

            for(const tag of categoriesCISTags){
                cisTags.add(tag);
            }
        }
    }

    return cisTags;
}


const store = new Vuex.Store({
    strict: true,
    state: {
        filterDescriptions,
        /*user: {
            // TODO import user infos to the client-side
            userName: 'DAV BRU',
            userSurname: 'HARDCODED'
        },*/
        projects: [],
        geolocByProjectId: new Map(),
        spiders: undefined,

        displayedProject: undefined,
        
        selectedFilters,
        searchedText: new URL(location).searchParams.get('text') || ''
    },
    mutations: {
        setSelectedFilters (state, {selectedFilters}) {
            // trigger re-render
            state.selectedFilters = new Map(selectedFilters)
        },
        setSearchedText (state, {searchedText}) {
            state.searchedText = searchedText
        },
        emptyOneFilter (state, {filter}) {
            state.selectedFilters.set(filter, new Set())

            // trigger re-render
            state.selectedFilters = new Map(state.selectedFilters)
        },
        setProjects(state, {projects}){
            state.projects = projects;
        },
        setDisplayedProject(state, {project}){
            state.displayedProject = project;
        },
        setSpiders(state, {spiders}){
            state.spiders = spiders
        },
        addGeolocs(state, {geolocByProjectId}){
            state.geolocByProjectId = new Map([...state.geolocByProjectId, ...geolocByProjectId])
        }
    },
    actions: {
        toggleFilter({state, commit, dispatch}, {filter, value}){
            const selectedFilters = state.selectedFilters
            const selectedValues = selectedFilters.get(filter)
            if(selectedValues.has(value))
                selectedValues.delete(value)
            else 
                selectedValues.add(value)
                
            commit('setSelectedFilters', {selectedFilters})
            dispatch('search')
        },

        emptyOneFilter({state, commit, dispatch}, {filter}){
            const selectedFilters = state.selectedFilters
            selectedFilters.set(filter, new Set())

            commit('setSelectedFilters', {selectedFilters})
            dispatch('search')
        },

        searchedTextChanged({commit, dispatch}, {searchedText}){
            commit('setSearchedText', {searchedText})
            dispatch('search')
        },

        search({state, commit}){
            const cisTags = filterValuesToCISTags(state.selectedFilters)

            searchProjects(state.searchedText, cisTags)
                .then(projects => {
                    console.log('projects pour', state.searchedText, cisTags)
                    console.log(projects)

                    commit('setProjects', {projects})
                }) 
                .catch(err => console.error('err search', text, err))
        },
        getSpiders({commit}){
            getSpiders()
            .then(spiders => {
                console.log('spiders', spiders)

                commit('setSpiders', {spiders})
            }) 
            .catch(err => console.error('err getSpiders', text, err))
        },
        findProjectsGeolocs({commit}, projects){
            console.log('findProjectsGeolocs', projects)

            const projectWithValidAddress = projects.filter(p => p['address'])
            const addresses = projectWithValidAddress.map(p => p['address'].replace(/[^(\w|\s)]/g, '').slice(0, 200) )

            const adressesCSV = 'adresse\n' + addresses.join('\n')
            const adresseCSVBANBody = new FormData();
            adresseCSVBANBody.append('data', new File([adressesCSV], 'adresses.csv'))

            return fetch('https://api-adresse.data.gouv.fr/search/csv/', {
                method: 'POST',
                body: adresseCSVBANBody,
            })
            .then(r => r.text())
            .then(geolocsTxt => {
                console.log('text', geolocsTxt)

                const geolocs = csvParse(geolocsTxt);
                console.log('geolocs', geolocs)


                const geolocByProjectId = new Map();

                projectWithValidAddress.forEach(({id}, i) => {
                    const {latitude, longitude} = geolocs[i];

                    geolocByProjectId.set(
                        id, 
                        (Number.isFinite(parseFloat(latitude)) && Number.isFinite(parseFloat(longitude))) ?
                            {latitude: parseFloat(latitude), longitude: parseFloat(longitude)} : 
                            false
                    )
                })

                projects.forEach(({id}) => {
                    if(!geolocByProjectId.has(id)){
                        geolocByProjectId.set(id, false)
                    }
                })

                commit('addGeolocs', {geolocByProjectId})
            });
        }
    }
})


const BRAND_DATA = Object.freeze({
    logo: '/static/logos/CIS/CIS_beta_logo_LD.png',
    brand: 'Carrefour des Innovations Sociales',
})

const routes = [
    { 
        path: '/bientot/recherche',
        component: SearchScreen, 
        props(route){
            return {
                filterDescriptions,
                ...BRAND_DATA
            }
        },
        beforeEnter(to, from, next){

            // get spiders data if they're not already here
            if(!store.state.spiders){
                store.dispatch('getSpiders');
            }

            next()
        }
    },
    {
        path: '/bientot/project/:id',
        component: CISProjectScreen, 
        props(route){
            return {
                ...BRAND_DATA
            }
        },
        beforeEnter(to, from, next){
            const {id} = to.params;
            console.log('beforeEnter /project/:id', id)

            const project = store.state.projects.find(p => p.id === id)

            // get project data
            if(!project){
                getProjectById(id)
                .then(project => {
                    store.commit('setDisplayedProject', {project})
                })
                .catch(err => console.error('project route error', err))
            }

            store.commit('setDisplayedProject', {project: project || {}})


            // get spiders data if they're not already here
            if(!store.state.spiders){
                store.dispatch('getSpiders');
            }

            next()
        }
    }
]



const router = new VueRouter({
    mode: 'history',
    routes,
    scrollBehavior (to, from, savedPosition) {
        return savedPosition ? savedPosition : { x: 0, y: 0 };
    }      
})

document.addEventListener('DOMContentLoaded', () => {

    new Vue({
        el: document.querySelector('#vue-content'),
        router,
        store,
        render: h => h( Vue.component('router-view') )
    })

}, {once: true})  
