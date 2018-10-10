import Vue from 'vue';
import Vuex from 'vuex';

import NavBar from './components/NavBar.vue';
import SearchFilters from './components/SearchFilters.vue';
import Footer from './components/Footer.vue';

Vue.use(Vuex)

const filterDescriptions = [].concat(CHOICES_FILTERS_TAGS, CHOICES_FILTERS_PARTNERS);
const selectedFilters = new Map()
for(const f of filterDescriptions){
    selectedFilters.set(f.name, new Set())
}

const store = new Vuex.Store({
    state: {
        selectedFilters,
        user: {
            // TODO import user infos to the client-side
            userName: 'DAV BRU',
            userSurname: 'HARDCODED'
        }
    },
    mutations: {
        toggleSelectedFilter ({filter, value}) {
            const selectedValues = selectedFilters.get(filter)
            if(selectedValues.has(value))
                selectedValues.delete(value)
            else 
                selectedValues.add(value)
        }
    }
})


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
        el: document.querySelector('footer'),
        render: createElement => createElement(
            Footer
        )
    })

}, {once: true})  
