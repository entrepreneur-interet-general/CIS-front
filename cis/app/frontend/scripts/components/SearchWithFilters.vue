<template>
    <div class="search-bar navbar is-white is-fixed-top" role="menubar" aria-label="filters navigation">
        <div class="container">

            <div class="search control is-expanded">
                <div class="image-container"><img src="/static/icons/icon_search_violet.svg"></div>
                <input 
                    type="search" 
                    v-model="searchedText"
                    class="input is-large is-light input-navbar" 
                    placeholder="Tapez un mot clé, un lieu, un projet…"
                    @input="searchedTextChanged"
                    >
            </div>

            <div class="navbar-end">

                <span v-for="filter in filterDescriptions" 
                    :key="filter.name"
                    :id="filter.name"
                    class="navbar-item navbar-item-filter has-dropdown is-hoverable">

                    <a :class='["navbar-link", {"has-text-weight-semibold" : selectedFilters.get(filter.name).size >= 1 } ]'>
                        <span>
                            {{ filter.fullname }}
                        </span>
                    </a>

                    <div :id="filter.name" class="navbar-dropdown is-right">

                        <a class="navbar-item" v-for="choice in filter.choices" :key="choice.name">
                            <div class="field">
                                <input 	class="is-checkradio is-default is-normal" 
                                        :id="choice.name" 
                                        type="checkbox" 
                                        :checked="selectedFilters.get(filter.name).has(choice.name)"
                                        :data-filter="filter.name"
                                        :data-choice="choice.name"
                                        @change="changeFilter"
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
    computed: 
        {
            ...mapState({
                selectedFilters: ({search}) => search.question.selectedFilters,
                'filterDescriptions': 'filterDescriptions'
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
        if(!this.$store.state.search.answer.result){
            this.$store.dispatch('searchedTextChanged', {searchedText: this.searchedText})
        }
    }
}
</script>

<style lang="scss" scoped>
@import '../../styles/cis-colors.scss';
@import '../../styles/cis-misc.scss';
@import '../../styles/rem.scss';

.search-bar {
    top: $cis-navbar-height;
    height: $cis-search-bar-height;

    font-size: $cis-navbar-font-size;
    
    .search{
        flex: 1;

        display: flex;
        flex-direction: row;
        //justify-content: center;
        align-items: center;

        .image-container{
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;

            img{
                width: rem(36px);
            }
        }

        input[type="search"]{
            height: 100%;
            border: 0;
        }
    }

    .navbar-end{
        
        .navbar-link::after{
            content: url("/static/icons/icon_chevron3.svg");
            border: 0;

            transform: none;

            margin-right: -0.5em;
            width: rem(20px);

            right: 1em;
            top: 47%;
        }

        .navbar-item{
            padding: 0.2em 0.2em;
            border-left: 1px solid #CBCBCB;
        }
    }
}

</style>