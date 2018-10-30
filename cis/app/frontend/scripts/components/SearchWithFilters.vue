<template>
    <div class="navbar is-white is-fixed-top" id="navbar-filters" role="menubar" aria-label="filters navigation">
        <div class="container">

            <div class="search control has-icons-left has-icons-right is-expanded">
                <input 
                    type="search" 
                    v-model="searchedText"
                    class="input is-large is-light input-navbar" 
                    placeholder="Tapez un mot clé, un lieu, un projet…"
                    @input="searchedTextChanged"
                    >
                <span class="icon is-normal is-left">
                    <i class="fas fa-search"></i>
                </span>
            </div>

            <div class="navbar-end">

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
                                        :data-filter="filter.name"
                                        :data-choice="choice.name"
                                        @input="changeFilter"
                                        >
                                <label :for="choice.name">
                                    {{ choice.fullname }}
                                </label>
                            </div>
                        </a>
                    
                        <div class="navbar-item">
                            <button class="button is-text is-fullwidth has-text-primary"
                                :data-filter="filter.name"
                                @click="emptyOneFilter({filter: filter.name})">
                                Effacer
                            </button>
                        </div>

                    </div>
                </span>
            </div>
        </div>
    </div>
</template>

<script>
import {mapState} from 'vuex'

export default {
    props: ['filterDescriptions'],
    computed: 
        {
            ...mapState({
                selectedFilters: ({search}) => search.question.selectedFilters
            }),
            searchedText: {
                get () { return this.$store.state.search.question.query },
                set (value) {
                    this.$store.dispatch('searchedTextChanged', {searchedText: value})
                }
            }
        },
    methods: {
        emptyOneFilter({filter}){
            this.$store.dispatch( 'emptyOneFilter', {filter} )
        },
        changeFilter({target}){
            this.$store.dispatch(
                'toggleFilter', 
                {filter: target.getAttribute('data-filter'), value: target.getAttribute('data-choice')}
            )
        }
    },
    mounted(){
        this.$store.dispatch('searchedTextChanged', {searchedText: this.searchedText})
    }
}
</script>
<style scoped>
.search{
    flex: 1;
}

input[type="search"]{
    height: 100%;
}

#navbar-filters .navbar-end{
    margin-right: 10em;
}


#navbar-filters .navbar-end .navbar-item{
    padding: 0.2em 0.2em;
}
</style>