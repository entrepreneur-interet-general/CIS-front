<template>
    <SearchScreenSqueleton :logo="logo" :brand="brand" mainClass="map">
        <SearchResultsMap/>
    </SearchScreenSqueleton>
</template>

<script>
import {mapState} from 'vuex'

import SearchScreenSqueleton from '../SearchScreenSqueleton.vue'
import SearchResultsMap from '../SearchResultsMap.vue';

export default {
    name: 'SearchMapScreen',
    components: {
        SearchScreenSqueleton, SearchResultsMap
    },
    props: [
        'logo', 'brand'
    ]
}
</script>

<style>
.map .filter-feedback{
    padding-bottom: 1rem;
}
</style>