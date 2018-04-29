

// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //
// VUE.JS FUNCTIONS
// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //


// following tutorial for now...
// cf : https://fr.vuejs.org/v2/guide/

// Vue_custom.config.delimiters =  ['[[',']]'] ;

var custom_delimiters =  ['[[',']]'] 
// Vue.config.delimiters =  ['[[',']]'] ;


console.log("::: cis-vue-components.js is loaded") ;


// - - - - - - - - - - - - - //
// COMPONENTS 
// - - - - - - - - - - - - - //




// - - - - - - - - - - - - - //
// MAIN FILTERS DISPLAYERS
// - - - - - - - - - - - - - //

// NOTE : what a fucking headheache !!!!
// cf : https://vuejs.org/v2/guide/components-custom-events.html
// cf : http://steveholgado.com/posts/vue-component-v-model-multiple-checkboxes/ 
// cf : https://jsfiddle.net/0ckqpk2g/3/
// cf : https://jsfiddle.net/Herteby/bgoLcy40/ 

Vue.component('v-filter-categ-item', {

	delimiters	: custom_delimiters,
	props		: ['filter', 'f_checked', 'value'],
	model: {
		prop : 'f_checked',
		event: 'change'
	  },
	template	: `
					<a class="navbar-item">

						<div class="field">

							<input 	class="is-checkradio is-default is-normal" 
									type="checkbox" 

									:id="filter.id" 
									:value="filter.id" 
									
									change="$emit('change', $event.target.value)"
									@change="updateChecked"

									>
							<label :for="filter.id">
								[[ filter.fullname ]]
							</label>

						</div>

					</a>
				`,
	methods 	: {
		updateChecked : function(e) {

			var current_value = e.target.value ;
			console.log("+++ current_value : ", current_value  ) ;

			if(this.f_checked.includes(current_value)){
				this.f_checked.splice(this.f_checked.indexOf(current_value), 1)
			} else {
				this.f_checked.push(current_value)
			}

			console.log("+++ this.f_checked : ", this.f_checked  ) ;

		}
	}

})

/* 
Vue.component('v-filters-list', {

	delimiters	: custom_delimiters,
	props		: ['checkboxes_list'],
	template	: `
					<span 	v-bind:id="checkboxes_list.name"
							class="navbar-item navbar-item-filter has-dropdown is-hoverable">

						<a class="navbar-link">
							<span>[[ checkboxes_list.fullname ]]</span>
						</a>

						<div class="navbar-dropdown">

							<!-- checkboxes loop -->
							< v-filter-item 
								v-for="checkbox in checkboxes_list.choices"
								v-bind:filter="checkbox"
								v-model="f_checked"
								>
							</ v-filter-item>
							

							<!--
							<a class="navbar-item"
								v-for="filter in checkboxes_list.choices"
								>

								<div class="field">
		
									<input 	class="is-checkradio is-default is-normal" 
											type="checkbox" 
		
											v-bind:id="filter.id" 
											v-bind:value="filter.name" 
											
											v-model="f_checked"
											
											v-on:change="updateChecked"
											
											>
									<label v-bind:for="filter.id">
		
										[[ filter.fullname ]]
									
									</label>
		
								</div>
		
							</a>
							-->


							<!-- footer -->
							<div class="columns is-centered ">

								<div class="column is-half">
									<div class="navbar-item">
										<a class="button is-text is-fullwidth">
											Effacer
										</a>
									</div>
								</div>

								<div class="column is-half">
									<div class="navbar-item">
										<a class="button is-text is-fullwidth">
											Valider
										</a>
									</div>
								</div>

							</div>

						</div>
							
					</span>
				`,
	methods 	: {
		updateChecked : function() {
			console.log("this.f_checked", this.f_checked  ) ;
			this.$emit('input', this.f_checked )
			// this.$emit('input', function(e){
			// 	if(this.f_checked.includes(this.value)){
			// 		this.f_checked.splice(this.f_checked.indexOf(this.value), 1)
			// 	} else {
			// 		this.f_checked.push(this.value)
			// 	}
			// })

		}
	}

})
*/

// DECLARE FIELDS TO RETRIEVE FROM OPENSCRAPER RAW DATA
// WARNING !!! FIELDS NAMES COULD CHANGE --> DATAMODEL IN OPENSCRAPER IS FLEXIBLE !!!
// TO DO :
// GET FIELDS FROM API OR SETUP IN DB CIS_FRONT + BACKOFFICE
// q_results.

var numb_default_images		= 16 ;
var deft_imageUrl_large 	= "/static/illustrations/textures/large_fiche_" ;
var deft_imageUrl_medium 	= "/static/illustrations/textures/medium_fiche_" ;
var deft_imageUrl_thin 		= "/static/illustrations/textures/thin_fiche_" ;


var max_title_length		= 55 ;
var max_abstract_length		= 120 ;

var imageFieldName			= "image(s) du projet" ;
var titleFieldName			= "titre du projet" ;
var abstractFieldName 		= "résumé du projet" ;
var tagsFieldName 			= "tags" ;

var adressFieldName 		= "adresse du projet" ;
var projectholderFieldName 	= "structure porteuse" ;

var linksrcFieldName 		= "link_src" ;
var linkdataFieldName 		= "link_data" ;
var linkWebsiteFieldName 	= "website" ;

var spideridFieldName 		= "spider_id" ;




// - - - - - - - - - - - - - //
// MAIN RESULTS DISPLAYERS
// - - - - - - - - - - - - - //

// Vue.component('v-results-tiles-colmuns', {
// 	delimiters	: custom_delimiters,
// 	props		: ['queryResults','resultsPerPage'],

// 	template	: `	<template v-for="results_part in queryResults">
// 						<div class="tile is-parent is-3 is-vertical">
// 							<v-results-item 
// 								v-for="d in results_part" 
// 								v-bind:item="d"
// 							>
// 							</v-results-item>
// 						</div>
// 					</template>
// 				`,
// 	computed 	: {

// 	}
// })

Vue.component('v-results-item', {
	// Le composant search-item accepte maintenant une
	// « prop » qui est comme un attribut personnalisé.
	// Cette prop est appelée results.

	delimiters	: custom_delimiters,
	props		: ['item', 'showproject'],

	template	: `
					<div class="column is-12">
						
						<div class="card proj-card">
							
							<!-- image -->
							<div class="card-image">
								<figure class="image">
									<a 	href="#user-results-top"
										:project_id="item._id" 
										@click="showproject(item=item)"
									>
										<img 	:src="getCardImage" 
												alt="image du projet" 
												class="proj-card-img"
										>
									</a>
								</figure>
							</div>
							
							<div class="card-content">

								<!-- adress -->
								<div class="content">
									<span class="icon has-text-light">
										<i class="fas fa-location-arrow "></i>
									</span>
									<span class="subtitle is-6">
										[[ getAdress ]]
									</span>
								</div>



								<!-- title -->
								<p class="title is-5">
									<a 	class="a_big"
										href="#user-results-top"
										:project_id="item._id" 
										@click="showproject(item=item)"
										>
										[[ trimTitle ]]
									</a>
								</p>





								<!-- abstract -->
								<div class="content">
									<p class="subtitle is-6">[[ trimAbstract ]]</p>
								</div>

								<!-- tags -->
								<div class="content" v-if="isTags">
									<template 	v-for="tag_ in getTags ">
										<span class="tag">[[ tag_ ]]</span> &nbsp;
									</template>
								</div>


							</div>
						
							<footer class="card-footer">
									<!-- link source -->
									<a 	:href="getBestLink" 
										class="card-footer-item tooltip is-tooltip-top"
										data-tooltip="lien vers la page du projet chez le sourceur"
										target="_blank"
										>
										<span class="icon">
											<i class="fas fa-link "></i>
										</span>
									</a>

									<!-- link contributor -->
									<a 	v-if="getLinkContributor" 
										:href="getLinkContributor" 
										class="card-footer-item tooltip is-tooltip-top"
										:data-tooltip="getNameContributor"
										target="_blank"
										>
										<span class="icon">
											<i class="fas fa-info-circle "></i>
										</span>
									</a>

									<!-- link website -->
									<a 	v-if="getLinkWebsite" 
										:href="getLinkWebsite" 
										class="card-footer-item tooltip is-tooltip-top"
										data-tooltip="lien vers le site du projet"
										target="_blank"
										>
										<span class="icon">
											<i class="fas fa-external-link-alt "></i>
										</span>
									</a>

							</footer>

						</div>

					</div>

					`,
	
	computed : {
		
		// IMAGE
		getCardImage : function() {
			var imageUrl = this.item[imageFieldName] ;
			
			if (imageUrl == undefined){

				// default image if no scrapped image
				var randomInt =  Math.floor( ( Math.random() * numb_default_images ) + 1 ); 
				
				//// choose thick default image
				var imageUrl_ = deft_imageUrl_medium + randomInt + ".png";
			
			} else {
				var imageUrl_ = imageUrl[0] ;
				// TO DO : check if image url contains 'logo', 'tampon', or that kind of shitty stuff...
				// 
			}
			return imageUrl_
		},

		// ADRESS
		getAdress : function() {
			var adress = this.item[adressFieldName] ;
			if (adress == undefined | adress == "" ){
				var adress_ = "(adresse non définie)"
			} else {
				var adress_ = adress[0]
			}
			return adress_
		},


		// LINKS
		getLinkSrc : function() {
			var link = this.item[linksrcFieldName] ;
			if (link == undefined ){
				return false
			} 
			return link
		},
		getLinkData : function() {
			var link = this.item[linkdataFieldName] ;
			if (link == undefined ){
				return false
			} 
			return link
		},
		getLinkWebsite : function() {
			var link = this.item[linkWebsiteFieldName] ;
			if (link == undefined ){
				return false
			} 
			return link
		},
		getLinkContributor : function(){
			var spider_id = this.item[spideridFieldName];
			return spiders_infos[spider_id]["page_url"]
		},
		getNameContributor : function(){
			var spider_id = this.item[spideridFieldName];
			return "partagé par : " + spiders_infos[spider_id]["name"]
		},
		getBestLink : function() {
			var bestLink ;
			var linkData = this.getLinkData ; 
			if (linkData === false ) {
				bestLink = this.getLinkSrc ;
			} else {
				bestLink = linkData ;
			}
			return bestLink ; 
		},

		// TEXTS
		trimTitle : function() {
			var title = this.item[titleFieldName] ;
			if (title == undefined ){
				var title_ = "(projet sans titre)"
			} else {
				var title_  = title[0] ;
				var tail ;

				title_size	= title_.length ; 
				( title_size > max_title_length ) ? tail = " ..."  : tail = "" ;
				title_		= title_.slice(0,max_title_length) + tail ;
			}
			return title_ 
		},
		trimAbstract : function() {
			var abstract = this.item[abstractFieldName];
			if (abstract == undefined ){
				var abstract_ 	= "(projet sans résumé)"
			} else {
				var abstract_  	= abstract[0] ;
				var tail ;

				abstract_size	= abstract_.length ; 
				( abstract_size > max_abstract_length ) ? tail = " ..."  : tail = "" ;
				abstract_		= abstract_.slice(0,max_abstract_length) + tail ;
			}
			return abstract_ 
		},

		// TAGS
		isTags : function(){
			var tags = this.item[tagsFieldName] ;
			if (tags == undefined ){
				return false
			} else {
				return true
			}
		},
		getTags : function() {
			var tags = this.item[tagsFieldName] ;
			if (tags == undefined ){
				tags = [""]
			} else {
				// TO DO --> normalize tags from nomenclature
				tags = tags ;
			}
			return tags
		},

	},

	methos	: {

		// showProject : function () {
		// 	console.log("... showProject ...") ; 
		// 	var item_id = this.item["_id"]
		// 	console.log("... showProject / item_id : ", item_id) ; 
		// 	// showProjectInfos( project_id = item_id ) ; 
		// },

	}

})


Vue.component('v-results-one-item', {

	delimiters	: custom_delimiters,
	props		: ['item'],

	template	: `	
					<div class="columns">


						<!-- COLUMN LEFT -->
						<div class="column is-6 is-offset-1">

							<div class="card proj-card">

								<div class="card-content">

									<!-- title -->
									<p class="title is-3">
										<a 	class="a_big"
											:href="getBestLink"
											target="_blank" 
											>
											[[ getTitle ]]
										</a>
									</p>

									<!-- adress -->
									<div class="content">
										<span class="icon has-text-light">
											<i class="fas fa-location-arrow "></i>
										</span>
										<span class="subtitle is-6">
											[[ getAdress ]]
										</span>
									</div>

									<!-- abstract -->
									<div class="content">
										<p class="subtitle is-4">
											Description : 
										</p>
										<p class="subtitle is-6">[[ getFullAbstract ]]</p>
									</div>

								</div>
							
							</div>

							<br>

							<div class="card proj-card">

								<div class="card-content">

									<!-- Structure -->
									<div class="content">
										<p class="subtitle is-4">
											Structure
										</p>
										
										<p>
											nom de la structure : 
											<a	v-if="getBestLink"
												:href="getBestLink"
												target="_blank"
											>
											[[ getProjectHolder ]]
											</a>
										</p>


										<p> 
											site internet : 
											<a	v-if="getLinkWebsite"
												:href="getLinkWebsite"
												target="_blank"
											>
												<span class="icon">
													<i class="fas fa-external-link-alt "></i>
												</span>
												[[ getLinkWebsite[0] ]]
											</a>
											<span v-else>
												(non renseigné)
											</span>
										</p>
									</div>

									<!-- Contact -->
									<!--
									<div class="content">
										<p class="subtitle is-4">
											Contact
										</p>
										<p>
											porteur de projet : 
										</p>
									</div>
									-->

								</div>
							
							</div>


						</div>


						<!-- COLUMN RIGHT -->
						<div class="column is-4">
							
							<!-- SHARED BY -->
							<div class="card proj-card">

								<!-- shared by -->
								<div class="card-content">
									<p>
										Projet ajouté par : 
											<strong>
											<a 	:href="getBestLink" 
												target="_blank"
												class="has-text-primary"
												>
												[[ getNameContributor ]]
											</a>
											</strong>
									</p>

									<br>
									
									<a 	:href="getBestLink" 
										target="_blank"
										>
										<span class="icon">
											<i class="fas fa-link "></i>
										</span>
										Voir le projet sur le site sourceur
									</a>
								</div>

							</div>
						
							<br>

							<!-- IMAGE -->
							<div class="card proj-card">

								<!-- image -->
								<div class="card-image">
									<figure class="image">
										<a 	:href="getBestLink" 
											target="_blank"
										>
											<img 	:src="getCardImage" 
													alt="image du projet" 
													class="proj-card-img"
											>
										</a>
									</figure>
								</div>

							</div>
						
							<br>


							
							<!-- tags -->
							<div class="content">
								<p class="title is-5">
									Mot-clés 
								</p>
								<template 	
									v-if="isTags"
									v-for="tag_ in getTags "
									>
									<span class="tag">[[ tag_ ]]</span>&nbsp;
								</template>
								<p v-else>
									(non renseigné)
								<p>
							</div>


							<!-- share item -->
							<div class="content" >

								<p class="title is-5">
									Partagez ce projet
								</p>

								<p>
									<a 	id="btn_cis_proj_facebook"
										class="button is-text" 
										href="https://www.facebook.com/TouteslesInnoSo/" 
										>
										<span class="icon has-text-primary">
											<i class="fab fa-lg fa-facebook"></i>
										</span>
									</a>

									<a 	id="btn_cis_proj_twitter"
										class="button is-text" 
										href="https://twitter.com/touteslesinnoso"
										>
										<span class="icon has-text-primary">
											<i class="fab fa-lg fa-twitter"></i>
										</span>
									</a>

								</p>

							</div>


						</div>


					</div>
				`,
	
	methods		: {

		getFullText : function (textArray) {
			var full_text = "" ;
			textArray.forEach( function(text) {
				if (text != undefined ) {
					full_text += text + " " ;
				}
			});
			return full_text
		},

	},

	computed : {

		// IMAGE
		getCardImage : function() {
			var imageUrl = this.item[imageFieldName] ;
			
			if (imageUrl == undefined){

				// default image if no scrapped image
				var randomInt =  Math.floor( ( Math.random() * numb_default_images ) + 1 ); 
				
				//// choose thick default image
				var imageUrl_ = deft_imageUrl_medium + randomInt + ".png";
			
			} else {
				var imageUrl_ = imageUrl[0] ;
				// TO DO : check if image url contains 'logo', 'tampon', or that kind of shitty stuff...
				// 
			}
			return imageUrl_
		},

		// ADRESS
		getAdress : function() {
			var adress = this.item[adressFieldName] ;
			if (adress == undefined | adress == "" ){
				var adress_ = "(adresse non définie)"
			} else {
				var adress_ = this.getFullText(adress) ;
			}
			return adress_
		},

		// TEXTS
		getTitle : function() {
			var title = this.item[titleFieldName] ;
			if (title == undefined ){
				var title_ = "(projet sans titre)"
			} else {
				title_ = this.getFullText(title) ;
			}
			return title_ 
		},
		getFullAbstract : function() {
			var abstract = this.item[abstractFieldName];
			// console.log( abstract ) ;
			if (abstract == undefined ){
				var abstract_ 	= "(projet sans résumé)"
			} else {
				abstract_ = this.getFullText(abstract) ;
			}
			return abstract_ 
		},
		getProjectHolder : function() {
			var project_holder = this.item[projectholderFieldName];
			// console.log( project_holder ) ;
			if (project_holder == undefined ){
				var project_holder_ 	= "(non renseigné)"
			} else {
				project_holder_ = this.getFullText(project_holder) ;
			}
			return project_holder_ 
		},

		// TAGS
		isTags : function() {
			var tags = this.item[tagsFieldName] ;
			if (tags == undefined ){
				return false
			} else {
				return true
			}
		},
		getTags : function() {
			var tags = this.item[tagsFieldName] ;
			if (tags == undefined ){
				tags = [""]
			} else {

				// TO DO --> normalize tags from nomenclature
				tags = tags ;
			}
			return tags
		},


		// LINKS
		getLinkSrc : function() {
			var link = this.item[linksrcFieldName] ;
			if (link == undefined ){
				return false
			} 
			return link
		},
		getLinkData : function() {
			var link = this.item[linkdataFieldName] ;
			if (link == undefined ){
				return false
			} 
			return link
		},
		getLinkWebsite : function() {
			var link = this.item[linkWebsiteFieldName] ;
			if (link == undefined ){
				return false
			} 
			return link
		},
		getLinkContributor : function() {
			var spider_id = this.item[spideridFieldName];
			return spiders_infos[spider_id]["page_url"]
		},
		getNameContributor : function() {
			var spider_id = this.item[spideridFieldName];
			return spiders_infos[spider_id]["name"]
		},
		getBestLink : function() {
			var bestLink ;
			var linkData = this.getLinkData ; 
			if (linkData === false ) {
				bestLink = this.getLinkSrc ;
			} else {
				bestLink = linkData ;
			}
			return bestLink ; 
		},

	}

})


