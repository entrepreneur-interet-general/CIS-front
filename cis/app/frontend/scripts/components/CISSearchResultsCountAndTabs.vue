<template>
    <div class="count-and-tabs">

        <div class="results-count">
            <span class="nb">{{pending ? '?' : total}}</span> 
            <span>projets trouvés</span>
        </div>

        <div class="buttons has-addons is-right">

            <button :class="['button', view === VIEW_LIST ? 'is-selected is-primary' : undefined]" 
                @click="$emit('viewChange', VIEW_LIST)">
                <span class="icon">
                    <i class="fas fa-list"></i>
                </span>
                <span>Liste</span>
            </button>

            <button :class="['button', view === VIEW_MAP ? 'is-selected is-primary' : undefined]"
                @click="$emit('viewChange', VIEW_MAP)">
                <span class="icon">
                    <i class="fas fa-map"></i>
                </span>
                <span>Carte</span>
            </button>

            <button disabled class="button is-normal tooltip is-tooltip-danger is-tooltip-bottom"
                data-tooltip="en construction">
                <span class="icon">
                    <i class="fas fa-chart-bar"></i>
                </span>
                <span>Données</span>
            </button>

        </div>
    </div>
</template>

<script>
import {mapState} from 'vuex'

import {VIEW_LIST, VIEW_MAP} from '../constants.js'

export default {
    name: 'CISSearchResultsCountAndTabs',
    
    props: ['view'],

    data(){
        return {
            VIEW_MAP, 
            VIEW_LIST
        }
    },

    computed: {
        ...mapState({
            pending: ({search}) => !!search.answer.pendingAbort,
            total: ({search}) => search.answer.result && search.answer.result.total,
            
        })
    },
}
</script>

<style scoped>
.count-and-tabs{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;

    padding-top: 1.5em;

    margin-bottom: 2em;
}

.count-and-tabs .results-count{
    padding: 0.5em 1em;

    background-color: white;
    border-radius: 3px;
    font-size: 1.2em;

    display: flex;
    flex-direction: row;
    align-items: center;
}

.count-and-tabs .results-count .nb{
    color: #532A7B;
    font-size: 1.3em;
    font-weight: bold;
    margin-right: 0.5em;
}
</style>
