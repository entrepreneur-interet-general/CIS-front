<template>
    <footer class="footer">
        <div class="container">
            <div class="content is-small">
                <div class="columns">
                    <div class="column is-4 is-offset-2">
                        <h3>
                            <strong class="has-text-primary"> Le Carrefour des innovations sociales </strong>
                        </h3>
                        
                        <br>

                        <p>
                            <a class="modal-button" data-target="modal_who" aria-haspopup="true"> 
                                Qui sommes-nous ?  
                            </a>
                        </p>
                        
                        <p>
                            <a class="modal-button" data-target="modal_charte" aria-haspopup="true"> 
                                La charte du collectif 
                            </a>
                        </p>
                        
                        <p>
                            <a class="modal-button" data-target="modal_legal" aria-haspopup="true"> 
                                Mentions légales 
                            </a>
                        </p>

                        <p>
                            <a class="modal-button" data-target="modal_feedback_tester" aria-haspopup="true"> 
                                Vos retours d'utilisateur
                            </a>
                        </p>
                        
                        <p>
                            <a href="https://github.com/entrepreneur-interet-general/CIS-front" target="_blank"> 
                                Code source 
                            </a>
                        </p>
                    </div>


                    <div class="column is-4">

                        <h3>
                            <strong class="has-text-primary">Newsletter</strong>
                        </h3>

                        <MailchimpSubscribe></MailchimpSubscribe>

                        <h3 style="margin-top: 0.5em">
                            <strong class="has-text-primary">Contactez-nous</strong>
                        </h3>
                        <p>
                            Pour toute question, écrivez-nous à : <br>
                            <a 	id="btn_mailto_footer" 
                                href="mailto:contact@carrefourdesinnovationssociales.fr">
                                contact@carrefourdesinnovationssociales.fr
                            </a>
                        </p>

                        <h3 style="margin-top: 1em">
                            <strong class="has-text-primary"> Suivez-nous </strong>
                        </h3>
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

<style>

</style>