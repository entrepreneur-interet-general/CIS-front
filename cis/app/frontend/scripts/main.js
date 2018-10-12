import Vue from 'vue';
import Vuex from 'vuex';
import {csvParse} from 'd3-dsv';

import NavBar from './components/NavBar.vue';
import SearchFilters from './components/SearchFilters.vue';
import CISMap from './components/CISMap.vue';
import Footer from './components/Footer.vue';

Vue.use(Vuex)

const filterDescriptions = [].concat(CHOICES_FILTERS_TAGS, CHOICES_FILTERS_PARTNERS);
const selectedFilters = new Map()
for(const f of filterDescriptions){
    selectedFilters.set(f.name, new Set())
}

const store = new Vuex.Store({
    strict: true,
    state: {
        filterDescriptions,
        selectedFilters,
        user: {
            // TODO import user infos to the client-side
            userName: 'DAV BRU',
            userSurname: 'HARDCODED'
        },
        projects: []
    },
    mutations: {
        toggleSelectedFilter (state, {filter, value}) {
            const selectedValues = state.selectedFilters.get(filter)
            if(selectedValues.has(value))
                selectedValues.delete(value)
            else 
                selectedValues.add(value)

            // trigger re-render
            state.selectedFilters = new Map(state.selectedFilters)
        },
        emptyOneFilter (state, {filter}) {
            state.selectedFilters.set(filter, new Set())

            // trigger re-render
            state.selectedFilters = new Map(state.selectedFilters)
        },
        setProjects(state, {projects}){
            console.log('projects', projects)
            state.projects = projects;
        }
    }
})

fetch('http://cis-openscraper.com/api/data?token=pwa&results_per_page=1000')
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

document.addEventListener('DOMContentLoaded', () => {
    
    new Vue({
        el: document.querySelector('nav'),
        render: createElement => createElement(
            NavBar, 
            {
                props: {
                    logo: '/static/logos/CIS/CIS_beta_logo_LD.png',
                    brand: 'Carrefour des Innovations Sociales',
                    user: store.state.user
                }
            }
        )
    })
    
    new Vue({
        el: document.querySelector('#navbar-filters'),
        store,
        render: createElement => createElement(
            SearchFilters, 
            {
                props: {
                    filterDescriptions
                }
            }
        )
    })
    
    new Vue({
        el: document.querySelector('.map'),
        store,
        render: createElement => createElement(
            CISMap
        )
    })
    
    new Vue({
        el: document.querySelector('footer'),
        render: createElement => createElement(
            Footer
        )
    })

}, {once: true})  
