<template>
    <div>
        <NavBar :logo="logo" :brand="brand" :user="user" />
        <SearchWithFilters :filterDescriptions="filterDescriptions"/>
        <main>
            <CISMap/>
        </main>
        <Footer/>
    </div>
</template>

<script>
import {mapState} from 'vuex'

import NavBar from '../NavBar.vue';
import SearchWithFilters from '../SearchWithFilters.vue';
import CISMap from '../CISMap.vue';
import Footer from '../Footer.vue';

export default {
    components: {
        NavBar, SearchWithFilters, CISMap, Footer
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