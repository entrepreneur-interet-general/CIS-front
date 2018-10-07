import Vue from 'vue';
import Brand from './components/Brand.vue';

console.info('Coucou !!')

new Vue({
    el: '#brand',
    render: createElement => createElement(
        Brand, 
        {
            props: {
                logo: '/static/logos/CIS/CIS_beta_logo_LD.png',
                brand: 'Carrefour des Innovations Sociales' 
            }
        }
    )
})