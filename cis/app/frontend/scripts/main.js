import Vue from 'vue';
import Vuex from 'vuex';
import VueRouter from 'vue-router'
import {csvParse} from 'd3-dsv';

import CISCartoScreen from './components/screens/CISCartoScreen.vue';
import SearchScreen from './components/screens/SearchScreen.vue';

import {searchProjects} from './cisProjectSearchAPI.js';


Vue.use(VueRouter)
Vue.use(Vuex)

const filterDescriptions = [].concat(CHOICES_FILTERS_TAGS, CHOICES_FILTERS_PARTNERS);
const selectedFilters = new Map()
for(const f of filterDescriptions){
    selectedFilters.set(f.name, new Set())
}

function uniformizeProject(p){
    const TEXTURE_COUNT = 16;

    if(!p.image){
        // add texture as image
        // so it's a deterministic function, let's use the id to determine which texture is used
        p.image = `/static/illustrations/textures/medium_fiche_${ (parseInt(p.id.substr(p.id.length - 6), 16)%TEXTURE_COUNT) + 1}.png`
    }
    else{
        p.image = p.image[0]
    }

    return p;
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
        user: {
            // TODO import user infos to the client-side
            userName: 'DAV BRU',
            userSurname: 'HARDCODED'
        },
        projects: [],
        
        selectedFilters,
        searchedText: ''
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
            state.projects = projects.map(uniformizeProject);
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
        }
    }
})

/*
fetch('http://cis-openscraper.com/api/data?token=pwa&results_per_page=5000')
.then(r => r.json())
.then(data => {
    const {query_results: projects} = data;
    const projectWithValidAddress = projects
    .filter(p => Array.isArray(p['adresse du projet']))
    const addresses = projectWithValidAddress.map(p => p['adresse du projet'].join(' '))

    const adressesCSV = 'adresse\n' + addresses.join('\n')
    const adresseCSVBANBody = new FormData();
    adresseCSVBANBody.append('data', new File([adressesCSV], 'adresses.csv'))

    return fetch('https://api-adresse.data.gouv.fr/search/csv/', {
        method: 'POST',
        body: adresseCSVBANBody,
    })
    .then(r => r.text())
    .then(geolocsTxt => {
        const geolocs = csvParse(geolocsTxt);

        projectWithValidAddress.forEach((p, i) => {
            p.geoloc = geolocs[i];
        })

        store.commit('setProjects', {projects: projectWithValidAddress})
    });

})
.catch(err => console.error('CIS data or BAN data error', err))
*/

const routes = [
    { path: '/carto', component: CISCartoScreen, props(route){
        return {
            logo: '/static/logos/CIS/CIS_beta_logo_LD.png',
            brand: 'Carrefour des Innovations Sociales',
            filterDescriptions
        }
    } },
    { path: '/spa-search', component: SearchScreen, props(route){
        return {
            logo: '/static/logos/CIS/CIS_beta_logo_LD.png',
            brand: 'Carrefour des Innovations Sociales',
            filterDescriptions
        } }
    }
]

const router = new VueRouter({
    mode: 'history',
    routes
})

document.addEventListener('DOMContentLoaded', () => {

    new Vue({
        el: document.querySelector('#vue-content'),
        router,
        store,
        render: h => h( Vue.component('router-view') )
    })

}, {once: true})  
