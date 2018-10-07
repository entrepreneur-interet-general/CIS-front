import Vue from 'vue';
import NavBar from './components/NavBar.vue';

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
}, {once: true})  
