<template>
    <div class="navbar-item is-hoverable has-dropdown ">                  
        <a class="navbar-item" href="/preferences/user_infos">
            <span class="icon has-text-primary">
                <i class="far fa-2x fa-user-circle"></i>
            </span>
        </a>
        <div class="navbar-dropdown is-boxed is-right">
            
            <a class="navbar-item" href="/preferences/user_infos">
                <strong> {{ user.userName }} {{ user.userSurname }} </strong> 
                <!--
                &nbsp;
                ( {{ user.userAuthLevel }} )
                -->
            </a>

            <hr class="navbar-divider">
            <a class="navbar-item" href="/preferences/user_infos">
                <span class="icon">
                    <i class="fas fa-cog"></i>
                </span>
                Vos informations
            </a>

            <hr class="navbar-divider">
            <a class="navbar-item" href="/preferences/user_password">
                <span class="icon">
                    <i class="fas fa-unlock"></i>
                </span>
                Changer le mot de passe
            </a>

            <!--
            {% if user_infos.userAuthLevel in ["admin", "staff"] %}
            <hr class="navbar-divider">
            {# <div 	class="navbar-item tooltip is-tooltip-bottom is-tooltip-warning is-tooltip-multiline"
                    data-tooltip="espace d'administration du site réservé aux niveaux : staff et admin"
                > #}
                {# <a class="button is-warning is-outlined" href="/admin" target="_blank"> #}
                <a class="navbar-item" href="/admin" target="_blank">
                    <span class="icon">
                        <i class="fas fa-lock"></i>
                    </span>
                    Espace Admin
                </a>
            {# </div> #}
            {% endif %}
            -->

            <a class="navbar-item" href="/logout">
                <button class="button is-fullwidth">
                    Se déconnecter
                </button>
            </a>
        </div>
    </div>
</template>

<script>
export default {
	props: ['user']
}
</script>
