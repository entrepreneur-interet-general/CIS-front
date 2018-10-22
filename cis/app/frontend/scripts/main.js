import Vue from 'vue';
import NavBar from './components/NavBar.vue';
import SearchFilters from './components/SearchFilters.vue';


document.addEventListener('DOMContentLoaded', () => {
    
    new Vue({
        el: document.querySelector('nav'),
        render: createElement => createElement(
            NavBar, 
            {
                props: {
                    logo: '/static/logos/CIS/CIS_beta_logo_LD.png',
                    brand: 'Carrefour des Innovations Sociales',
                    user: {
                        // TODO import user infos to the client-side
                        userName: 'DAV BRU',
                        userSurname: 'HARDCODED'
                    }
                }
            }
        )
    })
    
    new Vue({
        el: document.querySelector('#navbar-filters'),
        render: createElement => createElement(
            SearchFilters, 
            {
                props: {
                    filterDescriptions: CHOICES_FILTERS_TAGS,
                    f_filters_partners: CHOICES_FILTERS_PARTNERS[0] 
                }
            }
        )
    })

}, {once: true})  
