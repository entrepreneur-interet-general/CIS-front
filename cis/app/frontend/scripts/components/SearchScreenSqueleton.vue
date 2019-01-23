<template>
    <div>
        <NavBar :logo="logo" :brand="brand"/>
        <SearchWithFilters/>
        <main :class="mainClass">
            <FiltersFeedback/>
            <slot/>
        </main>
        <Footer/>
    </div>
</template>

<script>
import NavBar from './NavBar.vue';
import SearchWithFilters from './SearchWithFilters.vue';
import FiltersFeedback from './FiltersFeedback.vue';
import Footer from './Footer.vue';

export default {
    name: 'SearchScreenSqueleton',
    components: {
        NavBar, SearchWithFilters, FiltersFeedback, Footer
    },
	props: ['logo', 'brand', 'mainClass']
}
</script>

<style lang="scss">
@import '../../styles/cis-misc.scss';

main{
    margin-top: $cis-navbar-height + $cis-search-bar-height;
}
</style>