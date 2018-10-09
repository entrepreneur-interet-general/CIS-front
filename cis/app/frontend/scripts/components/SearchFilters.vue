<template>
    <div class="navbar is-white is-fixed-top" id="navbar-filters" role="menubar" aria-label="filters navigation">
        <div class="container">
            
            <!--
            <span class="navbar-burger burger" data-target="navbar-search-filters">
                <span></span>
                <span></span>
                <span></span>
            </span> 
            -->

            <div id="navbar-search-filters" class="navbar-menu">

                <div class="navbar-start">

                    <span v-for="filter in filterDescriptions" 
                        v-bind:key="filter.name"
                        v-bind:id="filter.name"
                        class="navbar-item navbar-item-filter has-dropdown is-hoverable">

                        <a :class='["navbar-link", {"has-text-primary has-text-weight-semibold" : filter.is_active } ]'>
                            <span>
                                {{ filter.fullname }}
                            </span>
                        </a>

                        <div :id="filter.name" class="navbar-dropdown">

                            <FilterItem 
                                v-for="choice in filter.choices"
                                :key="choice.name"
                                :item="choice"
                                v-model="f_checked"
                                >
                            </FilterItem>
                        
                            <div class="navbar-item">
                                <a 	class="button is-text is-fullwidth has-text-primary"
                                    @click="f_cleanCheckedFromCheckboxesList(choices.name)">
                                    Effacer
                                </a>
                            </div>
                        </div>
                    </span>


                    <span	id="sources_"
                            class="navbar-item navbar-item-filter has-dropdown is-hoverable">

                        <a 	:class='["navbar-link", {"has-text-primary has-text-weight-semibold has-background-primary" : f_filters_partners_active } ]'>

                            <span>
                                Contributeurs
                            </span>
                        </a>

                        <div class="navbar-dropdown">

                            <FilterItem 
                                v-for="choice in f_filters_partners"
                                :key="choice.name"
                                :item="choice"
                                v-model="f_checked_partners"
                                >
                            </FilterItem>

                                
                            <!-- footer -->
                        
                            <div class="navbar-item">
                                <a 	class="button is-text is-fullwidth has-text-primary"
                                    @click="f_cleanCheckedFromCheckboxesList('sources_')"
                                    >
                                    Effacer
                                </a>
                            </div>  
                        </div>
                    </span>
                </div>

                <!--
                {# FOR DEBUGGING PURPOSES #}
                
                <div class="navbar-end">

                    <div class="navbar-item">
                        {# <span>[[ f_checked ]]</span> #}
                        {# <span>[[ f_checked_as_code_tags ]]</span> #}
                        {# <span>[[ f_checked_as_src_tags ]]</span> #}
                    </div>

                    <div class="navbar-item">
                        {# <span>[[ f_checked ]]</span> #}
                        {# <span>[[ f_checked_as_code_tags ]]</span> #}
                        {# <span>[[ f_checked_as_src_tags ]]</span> #}
                    </div>

                    <div class="navbar-item">
                        {# <span>[[ f_checked_partners ]]</span> #}
                        {# <button class="button" id="query-openscraper-infos-button"> #}
                        </button>
                    </div>

                </div>
                
                -->

            </div>
        </div>
    </div>
</template>

<script>
import FilterItem from './FilterItem.vue'

export default {
    components: {
        FilterItem
    },
	props: ['filterDescriptions', 'f_filters_partners']
}
</script>

<style>

</style>