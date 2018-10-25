<template>
    <div>
        <NavBar :logo="logo" :brand="brand"/>

        <main>
            <div class="container">

                <a class="back" href="/spa-search" @click="goBack">
                    <span class="icon has-text-primary">
                        <i class="fas fa-arrow-left"></i>
                    </span>
                    <span>
                        retour aux résultats de recherche
                    </span>
                </a>

                <div class="columns">

                    <div class="column is-6">
                        <div class="description">
                            <h1 class="title is-1">{{project.title}}</h1>
                            <p v-if="project.address">{{project.address}}</p>
                            <p>{{project.description}}</p>

                            <h2 class="title is-2">Structure</h2>
                            <p>{{project.partners}}</p>
                            <a :href="project.url">Voir le site du projet</a>
                        </div>
                    </div>

                    <div class="column is-6">
                        <div class="added" v-if="spiders && project && spiders[project.spiderId]">Project ajouté par <a :href="spiders[project.spiderId].page_url">{{spiders[project.spiderId].name}}</a></div>
                        <img :src="project.image"/>
                        <div class="content">
                            <h2 class="title is-2">Categories</h2>
                            <span v-for="tag in project.tags" class="tag" :key="tag">
                                {{tag}}
                            </span>
                        </div>
                        <div>
                            <h2 class="title is-2">Partagez ce projet ?</h2>
                        </div>
                    </div>

                </div>
            </div>
        </main>
        
        <Footer/>
    </div>
</template>

<script>
import {mapState} from 'vuex'

import NavBar from '../NavBar.vue';
import Footer from '../Footer.vue';

export default {
    components: {
        NavBar, Footer
    },
    props: [
        'logo', 'brand'
    ],
    
    computed: mapState({
        project: 'displayedProject',
        spiders: 'spiders'
    }),

    mounted(){
        console.log('mounted', window.pageXOffset, window.pageYOffset)

        // hack to scroll top because vue-router scrollBehavior thing doesn't seem to work on Firefox on Linux at least
        const int = setInterval(() => {
            if(window.pageYOffset < 50){
                clearInterval(int)
            }
            else{
                window.scrollTo(0, 0)
            }
        }, 100);
    },

    methods: {
        goBack(){
            this.$router.go(-1)
        }
    }

}
</script>


<style scoped>
main{
    background-color: #f6f6f6;
    margin-top: calc(70px);
}

a.back{
    padding: 1em 0;
    display: block;
}

.columns{
    margin-top: 0;
}


.description, .added{
    background-color: white;
}
</style>