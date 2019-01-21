<template>
    <section class="search-results-list">
        <div class="container" v-if="pending">
            <div class="pending">Recherche en cours...</div>
        </div>

        <div class="container" v-if="!pending">
            <CISSearchResultsCountAndTabs :view="VIEW_LIST"/>
            
            <div class="columns" v-if="total > 0" >
                <div class="column is-3" v-for="(projectColumn, i) in projectColumns" :key="i">
                    <div class="columns is-multiline">
                        <CISProjectCard v-for="project in projectColumn" :key="project.id" :project="project"/>
                    </div>
                </div>
            </div>

            <div class="no-result" v-if="total === 0">(Aucun résultat)</div>
        </div>
    </section>
</template>

<script>
import {mapState} from 'vuex'
import CISProjectCard from './CISProjectCard.vue'

import CISSearchResultsCountAndTabs from './CISSearchResultsCountAndTabs.vue'

import {VIEW_LIST} from '../constants.js'

const COLUMN_COUNT = 4;

const DEFAULT_SHOW_COUNT = 50;
const MORE_PROJECTS_ON_SCROLL_COUNT = 20;

const SCROLL_BEFORE_BOTTOM_TRIGGER = 500;


let scrollListener;

export default {
    name: 'SearchResultsList',

    components: {
        CISProjectCard, 
        CISSearchResultsCountAndTabs
    },

    data(){
        return {
            VIEW_LIST,
            showCount: DEFAULT_SHOW_COUNT,
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
            pending: ({search}) => !!search.answer.pendingAbort,
            projects: ({search}) => search.answer.result && search.answer.result.projects,
            total: ({search}) => search.answer.result && search.answer.result.total,
            
        })
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

/* TODO SASS : make a variable out of this background-value. Also used in CISSearchResultsCountAndTabs */
.search-results-list{
    background-color: #F6F6F6;
    width: 100%;

    padding-bottom: 0;
    padding-top: 1rem;
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
