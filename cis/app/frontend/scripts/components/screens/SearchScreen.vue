<template>
    <div>
        <NavBar :logo="logo" :brand="brand" :user="user" />
        <SearchWithFilters :filterDescriptions="filterDescriptions"/>
        <main>
            <SearchResults/>
        </main>
        <Footer/>
    </div>
</template>

<script>
import {mapState} from 'vuex'

import NavBar from '../NavBar.vue';
import SearchWithFilters from '../SearchWithFilters.vue';
import SearchResults from '../SearchResults.vue';
import Footer from '../Footer.vue';

export default {
    components: {
        NavBar, SearchWithFilters, SearchResults, Footer
    },
    props: [
        'logo', 'brand', 'filterDescriptions'
    ],
    
    computed: mapState([
        'user'
    ])
}
</script>

<style>
main{
    margin-top: calc(70px + 52px);
}
</style>