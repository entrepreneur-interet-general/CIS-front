<template>
    <div id="navbarMain" class="navbar-menu">		
        <!--
            TODO : 
                - if user is authenticated (?) and page is search, then add searchbar (templates/navbars/navbar-search-input.html)
                - if user is authenticated (?) and page is a project, then add return button :
                <div class="navbar-item">
                    <a href="/search" class=" has-text-grey">
                        <span class="icon">
                            <i class="fa fa-arrow-left"></i>
                        </span>
                        <span class="name">Retour à la recherche</span>
                    </a>
                </div>
        -->

        <div class="navbar-end">
            <span class="navbar-item">

                <!--
                    TODO : if user is not authenticated, social network links + login button :

                    <a class="navbar-item " href="https://twitter.com/touteslesinnoso" target="_blank">
                        <span class="icon has-text-primary">
                            <i class="fab fa-2x fa-twitter"></i>
                        </span>
                    </a>

                    <a class="navbar-item " href="https://www.facebook.com/TouteslesInnoSo/" target="_blank">
                        <span class="icon has-text-primary ">
                            <i class="fab fa-2x fa-facebook"></i>
                        </span>
                    </a>

                    <div class="navbar-item">
                        <a id="btn_login" 
                            class="button is-primary is-outlined" 
                            href="/login">
                            <span>Connectez-vous</span>
                        </a>
                    </div>

                -->

                <div class="navbar-item">
                    <a class="button is-text" href="/infos/project">
                        Projet
                    </a>
                </div>

                <div class="navbar-item">
                    <a class="modal-button" data-target="modal_who" aria-haspopup="true">
                        Qui sommes-nous ?
                    </a>
                </div>

                <div class="navbar-item" >
                    <a id="btn_mailto_navbar" class="button is-text" href="mailto:contact@carrefourdesinnovationssociales.fr">
                        Contact
                    </a>
                </div>

                <!--
                    {# {% if user_infos.userAuthLevel in ["admin", "staff"] %}
                    <div 	class="navbar-item tooltip is-tooltip-bottom is-tooltip-warning is-tooltip multiline"
                            data-tooltip="espace d'administration du site réservé aux niveaux : staff et admin"
                        >
                        <a class="button is-warning is-outlined" href="/admin" target="_blank">
                            <span class="icon">
                                <i class="fas fa-lg fa-lock"></i>
                            </span>
                        </a>
                    </div>
                    {% endif %} #}
                -->

                <UserMenu v-if="user" :user="user"/>

            </span>
        </div>
    </div>
</template>

<script>
import UserMenu from './UserMenu.vue';

export default {
    components: {
        UserMenu
    },
    props: ['user']
}
</script>

<style>

</style>