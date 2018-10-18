<template>
    <section>
        <header class="container">
            <div class="results-count">{{count}} projets trouvés</div>

            <div class="buttons has-addons is-right">

                <button class="button is-normal is-primary is-selected">
                    <span class="icon">
                        <i class="fas fa-list"></i>
                    </span>
                    <span>Liste</span>
                </button>

                <button class="button is-normal tooltip is-tooltip-danger is-tooltip-bottom"
                    data-tooltip="en construction"
                    disabled
                    >
                    <span class="icon">
                        <i class="fas fa-map"></i>
                    </span>
                    <span>Carte</span>
                </button>

                <button class="button is-normal tooltip is-tooltip-danger is-tooltip-bottom"
                    data-tooltip="en construction"
                    disabled
                    >
                    <span class="icon">
                        <i class="fas fa-chart-bar"></i>
                    </span>
                    <span>Données</span>
                </button>

            </div>
        </header>
        <div class="container">
            <div class="columns">
                <div class="column is-3" v-for="(projectColumn, i) in projectColumns" :key="i">
                    <div class="columns is-multiline">
                        <CISProjectCard v-for="project in projectColumn" :key="project.id" :project="project"/>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import {mapState} from 'vuex'
import CISProjectCard from './CISProjectCard.vue'

const COLUMN_COUNT = 4;

export default {
    components: {
        CISProjectCard
    },

    computed: mapState({
        projectColumns: ({projects}) => {
            const projectByColumnCount = Math.ceil(projects.length/COLUMN_COUNT + 1)

            return Array(COLUMN_COUNT).fill().map((_, i) => {
                return projects.slice(projectByColumnCount*i, projectByColumnCount*(i+1))
            })
        },
        count: ({projects}) => projects.length
    })
    
}
</script>

<style scoped>
header{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

section{
    background-color: #d9d9d9;
}

</style>