<template>
    <div class="count-and-tabs">

        <div :class="['result-count-parent', open ? 'open' : undefined]">
            <div class="results-count">
                <span class="nb">{{pending ? '?' : total}}</span> 
                <span>projets trouvés</span>
            </div>
            <slot name="project"/>
        </div>

        <div class="buttons has-addons is-right">

            <router-link :to="`/recherche`" :class="['button', view === VIEW_LIST ? 'is-selected is-primary' : undefined]" >
                <img :src="`/static/icons/${view === VIEW_LIST ? 'icon_list_blanc.svg': 'icon_list.svg'}`">
                <span>liste</span>
            </router-link>

            <router-link :to="`/recherche/carte`" :class="['button', view === VIEW_MAP ? 'is-selected is-primary' : undefined]" >
                <img :src="`/static/icons/${view === VIEW_MAP ? 'icon_map_blanc.svg': 'icon_map.svg'}`">
                <span>carte</span>
            </router-link>

            <button disabled class="button is-normal tooltip is-tooltip-danger is-tooltip-bottom"
                data-tooltip="en construction">
                <img src="/static/icons/icon_dataviz.svg">
                <span>données</span>
            </button>

        </div>
    </div>
</template>

<script>
import {mapState} from 'vuex'

import {VIEW_LIST, VIEW_MAP} from '../constants.js'

export default {
    name: 'CISSearchResultsCountAndTabs',
    
    props: ['view', 'open'],

    data(){
        return {
            VIEW_MAP, 
            VIEW_LIST
        }
    },

    computed: {
        ...mapState({
            pending: ({search}) => !!search.answer.pendingAbort,
            total: ({search}) => search.answer.result && search.answer.result.total
        })
    }
}
</script>

<style lang="scss" scoped>

@import '../../styles/cis-colors.scss';

.count-and-tabs{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: flex-start;

    margin-bottom: 1em;

    .result-count-parent{
        padding-top: 1rem;
        padding: 0 1em;
        position: relative;
        left: -1em; /* TODO SASS : same absolute value as padding above*/
        max-width: 20em;

        background-color: transparent;

        &.open{
            background-color: $cis-grey-background;
            
            top: -1rem;
            padding-top: 1rem;
        }

        .results-count{
            padding: 0.5em 1em;

            background-color: white;
            border-radius: 3px;
            font-size: 1.2em;

            display: flex;
            flex-direction: row;
            align-items: center;

            .nb{
                color: $cis-primary;
                font-size: 1.3em;
                font-weight: bold;
                margin-right: 0.5em;
            }
        }
    }

    .buttons{
        & > *{
            width: 7em;
            justify-content: left;

            img{
                max-height: 1.8em;
            }

            span{
                margin-left: 0.2em;
            }

        }
    }

}


</style>
