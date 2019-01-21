<template>
    <section class="filter-feedback" v-if="selectedFilters.length >= 1">
        <div class="container inline-filters">
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
    </section>
</template>

<script>
import {mapState} from 'vuex'

export default {
    name: 'FiltersFeedback',
    computed: {
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
            }
        })
    },
    methods: {
        clearAllFilters(){
            this.$store.dispatch( 'clearAllFilters' )
        },
        clearFilter({filter, value}){
            this.$store.dispatch( 'toggleFilter', {filter, value} )
        }
    },
}
</script>

<style scoped>

.filter-feedback{
    width: 100%;
    background-color: #F6F6F6;
}

.filter-feedback > .inline-filters{
    padding-top: 1em;

    font-size: 12px;
}

.filter-feedback > .inline-filters span{
    white-space: nowrap;
    border: 1px solid #767676;
    background-color: #767676;

    color: white;

    border-radius: 3px;

    padding: 0.2em 0 0.2em 1em;
    margin-right: 0.5em;
    font-size: 0.9em;
}

.filter-feedback > .inline-filters span button{
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

.filter-feedback > .inline-filters span.all{

    background-color: white;

    color: #767676;
}

</style>