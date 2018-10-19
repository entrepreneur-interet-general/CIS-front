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

const DEFAULT_SHOW_COUNT = 80;
const MORE_PROJECTS_ON_SCROLL_COUNT = 20;

const SCROLL_BEFORE_BOTTOM_TRIGGER = 500;

let scrollListener;

export default {
    components: {
        CISProjectCard
    },

    data(){
        return {
            showCount: DEFAULT_SHOW_COUNT
        }
    },

    watch: {
        projects(prev, next){
            console.log('projects watch', prev === next, prev, next)
            this.showCount = DEFAULT_SHOW_COUNT;
        }
    },

    computed: {
        projectColumns(){
            const {projects} = this.$store.state;

            const columnsData = Array(COLUMN_COUNT).fill().map(() => []);
            
            projects.slice(0, this.showCount).forEach((p, i) => {
                columnsData[i%COLUMN_COUNT].push(p);
            })
            
            return columnsData
        },
        ...mapState({
            projects: 'projects',
            count: ({projects}) => projects.length
        })
    },

    mounted(){
        scrollListener = () => {
            if (
                window.innerHeight + window.scrollY >= (document.body.offsetHeight - SCROLL_BEFORE_BOTTOM_TRIGGER)
            ) {
                if(this.showCount < this.$store.state.projects.length){
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
header{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

section{
    background-color: #d9d9d9;
}

</style>