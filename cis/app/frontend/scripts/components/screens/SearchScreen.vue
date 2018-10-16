<template>
    <div>
        <NavBar :logo="logo" :brand="brand" :user="user" />
        <SearchFilters :filterDescriptions="filterDescriptions"/>
        <main>
            Recherche...<br/>
            Recherche...<br/>
            Recherche...<br/>
            Recherche...<br/>
            Recherche...<br/>
            Recherche...<br/>
            Recherche...<br/>
            Recherche...<br/>
            Recherche...<br/>
            Recherche...<br/>
            Recherche...<br/>
            Recherche...<br/>
        </main>
        <Footer/>
    </div>
</template>

<script>
import {mapState} from 'vuex'

import NavBar from '../NavBar.vue';
import SearchFilters from '../SearchFilters.vue';
import Footer from '../Footer.vue';

export default {
    components: {
        NavBar, SearchFilters, Footer
    },
    props: [
        'logo', 'brand', 'filterDescriptions'
    ],
    
    computed: mapState([
        'user'
    ])
}
</script>
