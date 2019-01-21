<template>
    <SearchScreenSqueleton :logo="logo" :brand="brand" mainClass="list">
        <SearchResultsList/>
    </SearchScreenSqueleton>
</template>

<script>
import {mapState} from 'vuex'

import SearchScreenSqueleton from '../SearchScreenSqueleton.vue'
import SearchResultsList from '../SearchResultsList.vue';

export default {
    name: 'SearchListScreen',
    components: {
        SearchScreenSqueleton, SearchResultsList
    },
    props: [
        'logo', 'brand'
    ]
}
</script>

<style>
.list .filter-feedback{
    padding-bottom: 0;
}
</style>