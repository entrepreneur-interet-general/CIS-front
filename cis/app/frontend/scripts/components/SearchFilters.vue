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
                        :key="filter.name"
                        :id="filter.name"
                        class="navbar-item navbar-item-filter has-dropdown is-hoverable">

                        <a :class='["navbar-link", {"has-text-primary has-text-weight-semibold" : filter.is_active } ]'>
                            <span>
                                {{ filter.fullname }}
                            </span>
                        </a>

                        <div :id="filter.name" class="navbar-dropdown">

                            <a class="navbar-item" v-for="choice in filter.choices" :key="choice.name">
                                <div class="field">
                                    <input 	class="is-checkradio is-default is-normal" 
                                            :id="choice.name" 
                                            type="checkbox" 
                                            :checked="selectedFilters.get(filter.name).has(choice.name)"
                                            @input="toggleSelectedFilter({filter: filter.name, value: choice.name})"
                                            >
                                    <label :for="choice.name">
                                        {{ choice.fullname }}
                                    </label>
                                </div>
                            </a>
                        
                            <div class="navbar-item">
                                <a 	class="button is-text is-fullwidth has-text-primary"
                                    @click="emptyOneFilter({filter: filter.name})">
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
import {mapMutations, mapState} from 'vuex'

export default {
    props: ['filterDescriptions'],
    computed: mapState([
        'selectedFilters', 'test'
    ]),
    methods: {
        ...mapMutations([
            'toggleSelectedFilter',
            'emptyOneFilter'
        ])
    }
}
</script>

<style>

</style>