<template>
    <div>
        <NavBar :logo="logo" :brand="brand"/>

        <main v-if="project">
            <div class="container">

                <a class="back" @click="goBack">
                    <span class="icon has-text-primary">
                        <i class="fas fa-arrow-left"></i>
                    </span>
                    <span>
                        retour aux résultats de recherche
                    </span>
                </a>

                <div class="columns">

                    <div class="column is-5 is-offset-1">
                        <div class="description">
                            <h1 class="title is-3">{{project.title}}</h1>
                            <p v-if="project.address">{{project.address}}</p>
                            <p>{{project.description}}</p>

                            <div v-if="project.projectPartners">
                                <h2 class="title is-4">Structure</h2>
                                <p>{{project.projectPartners}}</p>
                            </div>

                            <a v-if="project.website" :href="project.website" target="_blank">Voir le site du projet</a>
                        </div>
                    </div>

                    <div class="column is-5">
                        <div class="added" v-if="spiders && project && spiders[project.spiderId]">
                            Project ajouté par 
                            <a :href="project.pageAtSourcer || spiders[project.spiderId].page_url" target="_blank">
                                {{spiders[project.spiderId].name}}
                            </a>
                        </div>
                        <img :src="project.image"/>
                        <div class="content">
                            <h2 class="title is-5">Catégories</h2>
                            <span v-for="tag in project.tags" class="tag" :key="tag">
                                {{tag}}
                            </span>
                        </div>
                    </div>

                </div>
            </div>
        </main>

        <NotFoundError v-if="!project"/>
        
        <Footer/>
    </div>
</template>

<script>
import {mapState} from 'vuex'

import NavBar from '../NavBar.vue';
import NotFoundError from '../NotFoundError.vue';
import Footer from '../Footer.vue';

export default {
    components: {
        NavBar, NotFoundError, Footer
    },
    props: [
        'logo', 'brand'
    ],
    
    computed: mapState({
        project: 'displayedProject',
        spiders: 'spiders'
    }),

    mounted(){
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
        goBack(e){
            e.preventDefault()
            this.$router.back()
        }
    }

}
</script>


<style scoped>
main{
    background-color: #f6f6f6;
    margin-top: calc(60px);
}

a.back{
    padding: 1em 0;
    display: block;
}

.columns{
    margin-top: 0;
}

.columns .column img{
    width: 100%;
    margin-bottom: 1em;
}

.description, .added{
    background-color: white;
    padding: 1em;
    margin-bottom: 1em;
}

.description h1{
    font-weight: bold;
}

.description p {
    margin-bottom: 1em;
}

.description a{
    color: #592d7b;
    border-bottom: 1px solid #592d7b;
}

.added a{
    color: #592d7b;
    font-weight: bold;
}

.content h2{
    font-weight: bold;

}

.content .tag{
    background-color: #767676;
    color: white;
    margin-right: 1em;
    margin-bottom: 0.5em;
}
</style>