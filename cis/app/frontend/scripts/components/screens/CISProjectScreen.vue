<template>
    <div>
        <NavBar :logo="logo" :brand="brand"/>

        <main v-if="project">
            <div class="container">

                <a class="back" @click="goBack">
                    <img src="/static/icons/icon_arrow1.svg">
                    <span>
                        Retour aux résultats de recherche
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
                        <div class="added" v-if="spider">
                            <div>
                                <div>
                                    Projet ajouté par 
                                    <a :href="spider.page_url" target="_blank">
                                        {{spider.name}}
                                    </a>
                                </div>
                                <div v-if="project.pageAtSourcer">
                                    <a :href="project.pageAtSourcer" class="link-at-sourcer" target="_blank">
                                        <img src="/static/icons/icon_link.svg">
                                        Voir ce projet sur le site
                                    </a>
                                </div>
                            </div>
                            <img v-if="spider.logo_url" :src="spider.logo_url">
                        </div>
                        <img class="illustration" :src="project.image"/>
                        <div v-if="Array.isArray(project.tags) && project.tags.length >= 1" class="content">
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
        spider({spiders}){ return spiders && this.project && spiders[this.project.spiderId] }
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


<style lang="scss" scoped>
@import '../../../styles/cis-colors.scss';
@import '../../../styles/cis-misc.scss';

main{
    background-color: $cis-grey-background;
    margin-top: $cis-navbar-height;
}

a.back{
    padding: 1em 0;
    display: block;

    color: $cis-text-color;

    img{
        height: 1.5em;
        transform: translateY(0.4em);
    }

    span{
        margin-left: 1em;
    }
}

.columns{
    margin-top: 0;
}

.illustration{
    width: 100%;
    margin-bottom: 1em;
}

.description, .added{
    background-color: white;
    padding: 1em;
    margin-bottom: 1em;
}

.description{
    h1{
        font-weight: bold;
    }

    p{
        margin-bottom: 1em;
    }
    
    a{
        color: $cis-primary;
        border-bottom: 1px solid $cis-primary;
    }
} 


.added {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: left;

    .link-at-sourcer img{
        max-height: 1.1em;
        transform: translateY(0.2em);
    }

    img{
        height:100%;
    }

    a{
        color: $cis-primary;
        font-weight: bold;
    }
}

.content{
    h2{
        font-weight: bold;
    }

    .tag{
        background-color: #767676;
        color: white;
        margin-right: 1em;
        margin-bottom: 0.5em;
    }
}
</style>