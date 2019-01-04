<template>
    <div class="column is-12">    
        <div class="card proj-card">

            <router-link :to="`/project/${project.id}`" class="card-image">
                <img class="proj-card-img" :src="project.image" :alt="'illustration du projet' + project.title" >
            </router-link>
            
            <div class="card-content">
                <div class="content" v-if="project.address.trim().length > 1">
                    <span class="icon has-text-light">
                        <i class="fas fa-location-arrow"></i>
                    </span>
                    <span class="subtitle is-6">
                        {{project.address.slice(0, 100)}}
                    </span>
                </div>

                <p class="title is-5">
                    <router-link :to="`/project/${project.id}`">
                        {{project.title}}
                    </router-link>
                </p>

                <div class="content">
                    <p class="subtitle is-6">{{summary}}</p>
                </div>

                <div class="content" v-if="Array.isArray(project.tags) && project.tags.length >=1">
                    <span v-for="tag in project.tags" class="tag" :key="tag">
                        {{tag}}
                    </span>
                </div>
            </div>

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
.card-image {
    min-height: 100px;
}

.card-image img{
    width: 100%;
}

.proj-card {
	border-radius: 3px ;
	box-shadow : 5px 5px 9px rgba(10, 10, 10, 0.1), 0 0 0 0px rgba(10, 10, 10, 0.1) ; 
}

.proj-card-img {
	border-radius : 3px 3px 0px 0px ;
}

.card-content .tag{
    margin-right: 0.5em;
    margin-bottom: 0.5em;
    
    padding: 0.2em 1em;

    background-color: #767676;
    color: white;

    font-size: 12px;
}
</style>