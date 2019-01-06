<template>
    <div>
        <NavBar :logo="logo" :brand="brand"/>
        <SearchWithFilters/>
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
        'logo', 'brand'
    ],
}
</script>

<style>
main{
    margin-top: calc(60px + 52px);
}
</style>