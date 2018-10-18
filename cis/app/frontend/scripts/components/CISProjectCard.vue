<template>
    <div class="column is-12">    
        <div class="card proj-card">

            <!-- TODO change to <router-link> -->
            <a class="card-image">
                <img class="proj-card-img" :src="project.image" :alt="'illustration du projet' + project.title" >
            </a>
            
            <div class="card-content">
                <div class="content">
                    <span class="icon has-text-light">
                        <i class="fas fa-location-arrow"></i>
                    </span>
                    <span class="subtitle is-6">
                        {{project.address}}
                    </span>
                </div>

                <p class="title is-5">
                    <!-- TODO change to <router-link> -->
                    <a class="a_big">
                        {{project.title}}
                    </a>
                </p>

                <div class="content">
                    <p class="subtitle is-6">{{summary}}</p>
                </div>

                <div class="content" v-if="project.tags">
                    <span v-for="tag in project.tags" class="tag" :key="tag">
                        {{tag}}
                    </span>
                </div>
            </div>
        
            <footer class="card-footer">
                <a v-if="project.url" :href="project.url" class="card-footer-item"
                    title="lien vers le site du projet" target="_blank">
                    <span class="icon">
                        <i class="fas fa-external-link-alt"></i>
                    </span>
                </a>
            </footer>

        </div>
    </div>
</template>

<script>
import { mapState } from "vuex";

const MAX_SUMMARY_LENGTH = 120;

export default {
    components: {},

    props: ["project"],

    computed: {
        summary(){
            const {description = '(projet sans résumé)'} = this.project
            
            const tail = description.length > MAX_SUMMARY_LENGTH ? '...' : '';

            return description.slice(0, MAX_SUMMARY_LENGTH) + tail
        }
    }
};
</script>

<style scoped>
.card-image img{
    width: 100%;
}
</style>