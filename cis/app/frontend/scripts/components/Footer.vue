<template>
	<footer class="footer">
		<div class="container">
			<div class="columns">

				<div class="column is-4 is-offset-2">
					<h2 class="has-text-primary"> Le Carrefour des innovations sociales </h2>
					
					<ul>
						<li>
							<a href="/qui-sommes-nous">Qui sommes-nous ?</a>
						</li>
						<li>
							<a href="https://github.com/entrepreneur-interet-general/CIS-front" target="_blank"> 
								Code source 
							</a>
						</li>
						<li>
							<a href="/login">Login</a>
						</li>
						<li>
							<a href="/admin">Admin</a>
						</li>
					</ul>
				</div>


				<div class="column is-4">
					<h2 class="has-text-primary">Newsletter</h2>

						<MailchimpSubscribe></MailchimpSubscribe>

						<h2 class="has-text-primary"><a href="/contact">Contactez-nous</a></h2>

					<h2 class="has-text-primary">Suivez-nous</h2>

					<div class="content is-medium">
						
						<a 	id="btn_cis_facebook"
							class="button is-primary" 
							href="https://www.facebook.com/TouteslesInnoSo/" >
							<span class="icon">
								<i class="fab fa-lg fa-facebook"></i>
							</span>
						</a>
						
						&nbsp;&nbsp;&nbsp;

						<a 	id="btn_cis_twitter"
							class="button is-primary" 
							href="https://twitter.com/touteslesinnoso" >
							<span class="icon ">
								<i class="fab fa-lg fa-twitter"></i>
							</span>
						</a>
						
					</div>
				</div>
			</div>
		</div>
	</footer>
</template>

<script>
import MailchimpSubscribe from './MailchimpSubscribe.vue'

export default {
	components: {
		MailchimpSubscribe
	}
}
</script>
