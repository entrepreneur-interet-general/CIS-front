

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

var imageFieldName			= "image(s) du projet" ;
var titleFieldName			= "titre du projet" ;
var abstractFieldName 		= "résumé du projet" ;
var tagsFieldName 			= "tags" ;

var adressFieldName 		= "adresse du projet" ;
var projectholderFieldName 	= "structure porteuse" ;

var linksrcFieldName 		= "link_src" ;
var linkdataFieldName 		= "link_data" ;
var websiteFieldName 		= "website" ;

var linkdataFieldName 		= "link_data" ;




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

						</div>

					</div>

					`,
	
	computed : {
		
		// MAINLY CATCH ERRORS

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
			if (adress == undefined ){
				var adress_ = "(adresse non définie)"
			} else {
				var adress_ = adress[0]
			}
			return adress_
		},

		trimTitle : function() {
			var title = this.item[titleFieldName] ;
			if (title == undefined ){
				var title_ = "(projet sans titre)"
			} else {
				var title_  = title[0] ;
				title_ 		= title_.slice(0,60) + " ..." ;
			}
			return title_
		},
		
		trimAbstract : function() {
			var abstract = this.item[abstractFieldName];
			if (abstract == undefined ){
				var abstract_ 	= "(projet sans résumé)"
			} else {
				var abstract_  	= abstract[0] ;
				abstract_		= abstract_.slice(0,120) + " ..." ;
			}
			return abstract_ + " ..." 
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


