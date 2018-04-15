

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

// DEBUGGING - TUTORIAL
// Vue.component('todo-item', {
// 	// Le composant todo-item accepte maintenant une
// 	// « prop » qui est comme un attribut personnalisé.
// 	// Cette prop est appelée todo.

// 	delimiters	: custom_delimiters,
// 	props		: ['todo'],
// 	template	: '<li>[[ todo ]]</li>',

// })


// DECLARE FIELDS TO RETRIEVE FROM OPENSCRAPER RAW DATA
// WARNING !!! FIELDS NAMES COULD CHANGE --> DATAMODEL IN OPENSCRAPER IS FLEXIBLE !!!
// TO DO :
// GET FIELDS FROM API OR SETUP IN DB CIS_FRONT + BACKOFFICE
// q_results.

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
var websiteFieldName 		= "website" ;

var spideridFieldName 		= "spider_id" ;




// MAIN RESULTS DISPLAYER
Vue.component('v-results-item', {
	// Le composant search-item accepte maintenant une
	// « prop » qui est comme un attribut personnalisé.
	// Cette prop est appelée results.

	delimiters	: custom_delimiters,
	props		: ['item'],

	template	: `
					<div class="column is-3">

						<div class="card">
							
							<!-- image -->
							<div class="card-image">
								<figure class="image">
									<img v-bind:src="getImage" alt="image du projet">
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
								<p class="title is-5">[[ trimTitle ]] </p>






								<!-- abstract -->
								<div class="content">
									<p class="subtitle is-6">[[ trimAbstract ]]</p>
								</div>

								<!-- tags -->
								<div class="content" v-if="isTags">
									<template v-for="tag_ in getTags ">
										<span class="tag">[[ tag_ ]]</span>
									<template>
								</div>


							</div>
						
							<footer class="card-footer">
									<!-- link source -->
									<a 	v-bind:href="getLinkSrc" 
										class="card-footer-item tooltip is-tooltip-top"
										data-tooltip="lien vers le site sourceur"
										target="_blank"
										>
										<span class="icon">
											<i class="fas fa-link "></i>
										</span>
									</a>

									<!-- link data -->
									<a 	v-bind:href="getLinkData" 
										class="card-footer-item tooltip is-tooltip-top"
										data-tooltip="lien vers la page du projet chez le sourceur"
										target="_blank"
										>
										<span class="icon">
											<i class="fas fa-external-link-alt "></i>
										</span>
									</a>

									<!-- link contributor -->
									<a 	v-bind:href="getLinkContributor" 
										class="card-footer-item tooltip is-tooltip-top"
										v-bind:data-tooltip="getNameContributor"
										target="_blank"
										>
										<span class="icon">
											<i class="fas fa-info-circle "></i>
										</span>
									</a>
							</footer>

						</div>

					</div>

					`,
	
	computed : {
		
		getImage : function() {
			var imageUrl = this.item[imageFieldName] ;
			if (imageUrl == undefined){
				var randomInt =  Math.floor((Math.random() * 8) + 1); 
				var imageUrl_ = "/static/illustrations/textures/textures_encarts_fiches_texture "+ randomInt +".png" ;
			} else {
				var imageUrl_ = imageUrl[0] ;
				// TO DO : check if image url contains 'logo', 'tampon', or that kind of shitty stuff...
				// 
			}
			return imageUrl_
		},

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
			var link = this.item[linkwebsiteFieldName] ;
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



	}

})


// Vue.component('v-results-list', {
// 	// Le composant search-item accepte maintenant une
// 	// « prop » qui est comme un attribut personnalisé.
// 	// Cette prop est appelée results.

// 	delimiters	: custom_delimiters,
// 	props		: ['item'],
// 	template	: '<div class="column is-3"> [[ item["titre du projet"] ]] </div>',

// })


