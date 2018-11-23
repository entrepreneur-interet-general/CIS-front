<template>
    <section>
        <header class="container">

            <div class="inline-filters" v-if="selectedFilters.length >= 1">
                <span class="all">
                    Supprimer tous les filtres
                    <button @click="clearAllFilters">x</button>
                </span>
                <span v-for="{filter, value} in selectedFilters" :key="filter+value">
                    {{
                        filterDescriptions
                            .find(f => f.name === filter)
                            .choices
                            .find(c => c.name === value)
                            .fullname
                    }}
                    <button @click="clearFilter({filter, value})">x</button>
                </span>
            </div>
        </header>

        <div class="container" v-if="pending">
            <div class="pending">Recherche en cours...</div>
        </div>

        <div class="container" v-if="!pending && view === VIEW_LIST">
            <CISSearchResultsCountAndTabs :view="view" @viewChange="setView"/>
            
            <div class="columns" v-if="view === VIEW_LIST && total > 0" >
                <div class="column is-3" v-for="(projectColumn, i) in projectColumns" :key="i">
                    <div class="columns is-multiline">
                        <CISProjectCard v-for="project in projectColumn" :key="project.id" :project="project"/>
                    </div>
                </div>
            </div>

            <div class="no-result" v-if="view === VIEW_LIST && total === 0">(Aucun résultat)</div>
        </div>

        <CISMap v-if="view === VIEW_MAP" :view="view" @viewChange="setView"/>

    </section>
</template>

<script>
import {mapState} from 'vuex'
import CISProjectCard from './CISProjectCard.vue'
import CISMap from './CISMap.vue'
import CISSearchResultsCountAndTabs from './CISSearchResultsCountAndTabs.vue'

import {VIEW_MAP, VIEW_LIST} from '../constants.js'

const COLUMN_COUNT = 4;

const DEFAULT_SHOW_COUNT = 50;
const MORE_PROJECTS_ON_SCROLL_COUNT = 20;

const SCROLL_BEFORE_BOTTOM_TRIGGER = 500;



let scrollListener;

export default {
    name: 'SearchResults',

    components: {
        CISProjectCard, CISMap, CISSearchResultsCountAndTabs
    },

    data(){
        return {
            VIEW_MAP, 
            VIEW_LIST,
            showCount: DEFAULT_SHOW_COUNT,
            view: VIEW_LIST
        }
    },

    watch: {
        projects(prev, next){
            this.showCount = DEFAULT_SHOW_COUNT;
        }
    },

    computed: {
        projectColumns(){
            const {projects} = this.$store.state.search.answer.result;

            if(projects){
                const columnsData = Array(COLUMN_COUNT).fill().map(() => []);
                
                projects.slice(0, this.showCount).forEach((p, i) => {
                    columnsData[i%COLUMN_COUNT].push(p);
                })
                
                return columnsData
            }
        },
        ...mapState({
            filterDescriptions: 'filterDescriptions',
            selectedFilters: ({search}) => {
                const {selectedFilters} = search.question
                const filters = []

                for(const [filter, values] of selectedFilters){
                    for(const value of values){
                        filters.push({filter, value})
                    }
                }

                return filters
            },
            pending: ({search}) => !!search.answer.pendingAbort,
            projects: ({search}) => search.answer.result && search.answer.result.projects,
            total: ({search}) => search.answer.result && search.answer.result.total,
            
        })
    },

    methods: {
        setView(view){
            this.view = view;
        },
        clearAllFilters(){
            this.$store.dispatch( 'clearAllFilters' )
        },
        clearFilter({filter, value}){
            this.$store.dispatch( 'toggleFilter', {filter, value} )
        }
    },

    mounted(){
        scrollListener = () => {
            if (
                window.innerHeight + window.scrollY >= (document.body.offsetHeight - SCROLL_BEFORE_BOTTOM_TRIGGER)
            ) {
                if(this.$store.state.search.answer.result && this.showCount < this.$store.state.search.answer.result.projects.length){
                    this.showCount = this.showCount + MORE_PROJECTS_ON_SCROLL_COUNT
                }
            }
        }

        window.addEventListener('scroll', scrollListener, {passive: true})
    },

    beforeDestroy(){
        window.removeEventListener('scroll', scrollListener)

        scrollListener = undefined;
    }
    
}
</script>

<style scoped>
header > .inline-filters{
    padding-top: 1.5em;
}

header > .inline-filters span{
    white-space: nowrap;
    border: 1px solid #767676;
    background-color: #767676;

    color: white;

    border-radius: 3px;

    padding: 0.2em 0 0.2em 1em;
    margin-right: 0.5em;
    font-size: 0.9em;
}

header > .inline-filters span button{
    border: 0;
    padding: 0.2em 1em;
    margin: 0;

    font-size: 1.2em;
    font-weight: bold;
    height: 100%;

    color: currentColor;
    background-color: transparent;

    cursor: pointer;
    
}

header > .inline-filters span.all{

    background-color: white;

    color: #767676;
}


section{
    background-color: #d9d9d9;
}

.no-result{
    text-align: center;
    padding: 2em;
}
.pending{
    text-align: center;
    padding: 2em;
}

</style>
