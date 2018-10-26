<template>
    <div id="navbarMain" class="navbar-menu">

        <div class="navbar-end">
            <span class="navbar-item">

                <a class="field is-grouped">
					<div class="navbar-item">
						<a class="button is-text" href="/bientot/recherche">
							<span>Moteur de recherche</span>
						</a>
					</div>

					<div class="navbar-item">
						<a class="button is-text" href="/bientot/le-projet">
							<span>Projet</span>
						</a>
					</div>

					<div class="navbar-item">
						<a class="button is-text" href="/bientot/qui-sommes-nous"> 
							<span>Qui sommes-nous ?</span>
						</a>
					</div>

					<div class="navbar-item">
						<a class="button is-text" href="/bientot/nous-rejoindre"> 
							<span>Nous rejoindre</span>
						</a>
					</div>
				</a>

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
