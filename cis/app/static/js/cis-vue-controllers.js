

// $( document ).ready(function() {


	console.log("::: cis-vue-controllers.js is loaded") ;

	
	// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //
	// DATA UTILS
	// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //


	// random number to display missing photos as illustrations
	function randomIntFromInterval(min=1,max=8){
		return Math.floor(Math.random()*(max-min+1)+min);
	}


	// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //
	// VUE.JS GLOBAL VARS AND UTILS
	// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //


	// following tutorial for now...
	// cf : https://fr.vuejs.org/v2/guide/

	// Vue_custom.config.delimiters =  ['[[',']]'] ;

	var custom_delimiters =  ['[[',']]'] 
	// Vue.config.delimiters =  ['[[',']]'] ;

	var spiders_infos ;

	
	function getUserToken() {
		
		// get token from meta in html 

		var meta_token = $('meta[name="user_token"]').attr("content") ;
		console.log("::: current token in meta : ", meta_token ) ; 
		
		return meta_token
	}

	// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //
	// VUE.JS FUNCTIONS
	// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //

/*	///// COMPONENTS ---> MIGRATED IN cis-vue-components.js
	// - - - - - - - - - - - - - // 
	// COMPONENTS ---> MIGRATED IN cis-vue-components.js
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


	// MAIN RESULTS DISPLAYER
	Vue.component('v-results-item', {
		// Le composant search-item accepte maintenant une
		// « prop » qui est comme un attribut personnalisé.
		// Cette prop est appelée results.

		delimiters	: custom_delimiters,
		props		: ['item'],
		// template	:  '<div class="column is-3"><div class="card"><div class="column is-3"> [[ item["titre du projet"] ]] </div></div></div>',
		template	:  `<div class="column is-3">

							<div class="card">
								
								<div class="card-image">
									<figure class="image">
										<img v-bind:src="returnImage" alt="Placeholder image">
									</figure>
								</div>
								
								<div class="card-content">
	
									<p class="title is-5">[[ getTitle ]] </p>

									<div class="content">
										<p class="subtitle is-6">@[[ trimAbstract ]]</p>
									</div>


								</div>

							</div>
						</div>`,
		computed : {

			returnImage : function() {
				var imageUrl = this.item['image(s) du projet'] ;
				if (imageUrl == undefined){
					var randomInt =  Math.floor((Math.random() * 8) + 1); 
					var imageUrl_ = "/static/illustrations/textures/textures_encarts_fiches_texture "+ randomInt +".png" ;
				} else {
					var imageUrl_ = imageUrl[0] ;
				}
				return imageUrl_
			},

			getTitle : function() {
				var title = this.item["titre du projet"] ;
				if (title == undefined ){
					var title_ = "(projet sans titre)"
				} else {
					var title_ = title[0]
				}
				return title_
			},

			trimAbstract : function() {
				var fullAbstract = this.item["résumé du projet"][0] ;
				return fullAbstract.slice(0,100) + "..." 
			},
		}

	})


	Vue.component('v-results-list', {
		// Le composant search-item accepte maintenant une
		// « prop » qui est comme un attribut personnalisé.
		// Cette prop est appelée results.

		delimiters	: custom_delimiters,
		props		: ['item'],
		template	: '<div class="column is-3"> [[ item["titre du projet"] ]] </div>',

	})
*/





	
	// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //
	// CONTROLLERS 
	// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //

	// for displaying
	var columns_indices 	= [0,1,2,3];

	// declare default vars here 
	var search_string   	= "" ;

	// var search_tags			= [] ;
	var search_in_domains 	= [] ;
	var search_in_location 	= [] ;
	var search_in_partners 	= [] ;
	var search_in_publics 	= [] ;
	var search_in_methods 	= [] ;

	var results_per_page 	= 40 ;

	// var token_openscraper	= "call_from_cis_front" ;		
	// var token_openscraper	= meta_token ;		
	var token_openscraper	= getUserToken() ;		

	var results 			= {} ;
	var page_n				= 1 ;
	var page_max			= 1 ;

	var count_results 		= 0 ;
	var count_start			= 1 ;
	var count_stop			= 1 ;

	var count_results_total = 0 ;
	var default_message 	= "no request for now..." ;

	var sort_by				= null ;
	var shuffle_seed		= randomIntFromInterval() ; 

	// declare vue instances variable names
	var v_navbar_search_input, v_navbar_search_filters, v_results ;


	// // ONLY FIRE THIS CONTROLLER IF '#user-results' exists
	// var is_user_results = $('#user-results') ; 
	// console.log("::: is_user_results.length : ", is_user_results.length ) ;



	// if (is_user_results.lenght === 1 ) {

	// - - - - - - - - - - - - - //
	// VUE APPS - SEARCH RESULTS --> dispatcher to box cards
	v_results = new Vue({
		
		el			: '#user-results',
		delimiters	: custom_delimiters,

		data		: {
			
			// columns display variables
			d_columns			: columns_indices,
			d_number_of_columns : columns_indices.length , 
			d_items_per_column 	: results_per_page/columns_indices.length,
			d_columns_width 	: 12/columns_indices.length,

			// d_test		: ["lalala", "oyoyo", "lalala", "oyoyo", "lalala", "oyoyo"],
			d_results		: results, 
			d_page_n		: page_n,
			d_page_max		: page_max,

			d_count  		: count_results, 
			d_count_tot		: count_results_total,

			d_count_start 	: count_start, 
			d_count_stop  	: count_stop, 
			d_results_per_page	: results_per_page,

			// d_tags			: search_tags,
			// d_as_list 	: [] ,

		},

		methods		: {

			// go to next page
			v_page_up : function() {
				console.log("--- v_results -M- v_page_up...")
				var next_p_queried = this.d_page_n + 1 ;
				// this.d_page_n += 1 ;				
				(next_p_queried > this.d_page_max ) ? this.d_page_n = this.d_page_max : this.d_page_n = next_p_queried ;
			},

			// go to previous page
			v_page_down : function() {
				console.log("--- v_results -M- v_page_down...")
				// this.d_page_n -= 1 ; 
				var next_p_queried = this.d_page_n - 1 ;
				(next_p_queried <=0 ) ? this.d_page_n = 1 : this.d_page_n = next_p_queried ;
			},

			// reset q_shuffle_seed
			reShuffleResults : function(){
				console.log("- v_navbar_search_input / call_ajax ... ") ; 
				v_navbar_search_input.q_shuffle_seed = randomIntFromInterval(min=1, max=1000);
			},
			
			// resort result array
			resortArray : function(columnIndex) {
	
				console.log("*** v_results / resortArray...");
				
				var arrayResultsForColumn = [] ;
				
				var fullResultsArray = this.d_results['query_results'] ;
				
				for( var i = columnIndex ; i < fullResultsArray.length; i += this.d_number_of_columns ) {  // take every i + d_number_of_columns element
					arrayResultsForColumn.push(fullResultsArray[i]);
				}

				return arrayResultsForColumn ;

			},
		},

		computed	: {
			///
		},

		created		: function() {
			console.log(">>> v_results / initiating ... "); 
			console.log(">>> v_results / this.d_count 		: " + this.d_count); 
			console.log(">>> v_results / this.d_tags 		: " + this.d_tags); 
			console.log(">>> v_results / this.d_list 		: " + this.d_list); 
		},

		watch 		: {

			// TO TRY
			'd_page_n' : function(newVal, oldVal){
				console.log("--- v_results -W- d_page_n / oldVal : " + oldVal + " / newVal : " + newVal );
				console.log("--- v_results -W- d_page_n / this.d_page_n : ", this.d_page_n );
				// this.d_page_n = newVal ;
				v_navbar_search_input.q_page_n = newVal ; //this.d_page_n ; 

			},

			'd_results' : 

				function (new_results, old_results) {

					// this function will be called when chenge in `v_results.d_results`
					
					console.log( "--- v_results -W- d_results --> old_results : " ) ; 
					// console.log( "--- v_results / old_results.status : ", old_results.status ) ; 
					console.log( old_results ) ; 
					
					console.log( "--- v_results -W- d_results --> new_results : " ) ; 
					// console.log( "--- v_results / new_results.status :", new_results.status ) ; 
					console.log( new_results ) ; 

					this.d_count 		= new_results.query_log.count_results ;
					this.d_count_tot 	= new_results.query_log.count_results_tot ;
					// this.d_page_n 		= new_results.query_log.query.page_n ;
					this.d_page_max 	= new_results.query_log.page_n_max ;
					
					this.d_count_stop	= this.d_count * this.d_page_n ;

					start_page_n 		= this.d_count_stop - this.d_results_per_page + 1 ;
					// this.d_count_start  = this.d_count_stop - this.d_results_per_page + 1 ;
					(start_page_n <=0 ) ? this.d_count_start = 1 : this.d_count_start = start_page_n ;

					console.log( "--- v_results / this.d_count : ", this.d_count ); 
				},
			
		}
	})
	// }




	// TO DO 
	// - - - - - - - - - - - - - //
	// VUE APPS - FILTERS 
	v_navbar_search_filters = new Vue({
		
		el			: '#navbar-search-filters',
		delimiters	: custom_delimiters,

		data		: {
			// TO DO : 
			// retrieve all filters buttons created on the fly by flask-jinja
			// as vue data vars... 

			q_search_string : search_string ,
			
			q_dict 			: q_wrapper,

		},

		created		: function() {
			console.log(">>> v_navbar_search_filters / initiating ... "); 
			console.log(">>> v_navbar_search_filters / this.q_search_string : " + this.q_search_string); 
		},

		// methods		: {
		// 	// TO DO 
		// },

		computed	: {
			// TO DO 
		},

	})








	// - - - - - - - - - - - - - //
	// VUE APPS - SEARCH INPUT 
	v_navbar_search_input = new Vue({
		
		el			: '#navbar-search-input',
		delimiters	: custom_delimiters,

		data		: {
			q_message			: default_message,

			q_token				: token_openscraper,

			q_search_string 	: search_string,

			q_search_in_domains 	: search_in_domains,
			q_search_in_location 	: search_in_location,
			q_search_in_partners 	: search_in_partners,
			q_search_in_publics 	: search_in_publics,
			q_search_in_methods 	: search_in_methods,

			q_results_per_page 	: results_per_page,
			q_page_n			: page_n,

			q_shuffle_seed		: shuffle_seed,
			q_sort_by			: sort_by,
			
			q_is_results		: false,
		},

		created		: function() {
			console.log(">>> v_navbar_search_input / initiating ... "); 
			console.log(">>> v_navbar_search_input / this.q_search_string 		: " + this.q_search_string ); 
			console.log(">>> v_navbar_search_input / run : this.v_queryOpenScraper() "); 	
			this.v_queryOpenScraper() ;
		},

		methods		: {

			// main query function to openscraper
			v_queryOpenScraper: function(reset_page_n=false) {
				
				console.log("- v_navbar_search_input / call_ajax ... ") ; 
				
				// TO DO 
				// show loading page css

				console.log("- v_navbar_search_input / reset_page_n : ", reset_page_n) ; 
				if (reset_page_n == true ){
					this.q_page_n = 1 ;
				}
				// _this = this ;
				this.q_message = "request sent : "+ this.q_search_string;

				console.log("- v_navbar_search_input -M- / before .then() / _this.q_message : ") ;
				console.log(this.q_message) ;

				console.log("- v_navbar_search_input -M- / before .then() / this.q_results_per_page :", this.q_results_per_page ) ;
				v_results.d_results_per_page 	= this.q_results_per_page ;
				v_results.d_page_n 				= this.q_page_n ;

				// TO DO CLEANER --> WRITE A METHOD !!
				// generate slug
				var q_slug = 	 "page_n=" + this.q_page_n
								+ "&token=" + this.q_token
								+ "&shuffle_seed=" + this.q_shuffle_seed 
								+ "&search_for=" + this.q_search_string 
								+ "&results_per_page=" + this.q_results_per_page 
								
								// TO DO 
								// + "&spider_id=" + this.q_search_in_partners
								// + "&search_in_tags=" + this.q_search_in_methods
								// + "&search_in_tags=" + this.q_search_in_domains
								// + "&search_in_tags=" + this.q_search_in_locations
								// + "&search_in_tags=" + this.q_search_in_publics
							;

				console.log("- v_navbar_search_input -M- / before .then() / q_slug : ", q_slug ) ;
				
				// setTimeout for debugging ...
				// setTimeout( function(){
					// call ajax function 
					ajax_query_to_openscraper( data_q_slug=q_slug )
						
						.then( function( q_data ){
							
							// reset spiders_infos 
							spiders_infos = q_data.spiders_dict ; 

							// reset vars
							this.q_message = "json received";
							// this.q_results	= q_data ; 
							
							// TO DO 
							// hide loading page css

							// pass data to other Vue instance
							console.log("- v_navbar_search_input -M- / after then() / passing q_data to v_results.d_results ... ") ;
							v_results.d_results 			= q_data ;

							// console.log("- v_navbar_search_input / after then() / q_data : ") ;
							// console.log(q_data) ;

							console.log("- v_navbar_search_input -M- / after then() / this.q_message : ") ;
							console.log(this.q_message) ;

							// console.log("- v_navbar_search_input / after then() / _this.q_data : ") ;
							// console.log(this.q_results) ;

						}

					);
				// },1000)

			},
		},
		computed	: {
			// TO DO 
		},
		watch 		: {

			// TO TRY
			'q_page_n' : function(newVal, oldVal){
				console.log("--- v_navbar_search_input -W- q_page_n --> oldVal : " + oldVal + " / newVal : " + newVal );
				console.log("--- v_navbar_search_input -W- q_page_n --> run : this.v_queryOpenScraper() ");
				this.v_queryOpenScraper();
			},

			'q_shuffle_seed' : function(newVal, oldVal){
				console.log("--- v_navbar_search_input -W- q_shuffle_seed --> oldVal : " + oldVal + " / newVal: " + newVal );
				console.log("--- v_navbar_search_input -W- q_shuffle_seed --> run : this.v_queryOpenScraper() ");
				this.v_queryOpenScraper();
			}

			// 'q_search_string' : 
			
			// 	function (newVal, oldVal) {
			// 		//  this function will be called when chenge in `cis_v_search_for.q_search_for`
			// 		console.log("--- v_navbar_search_input / $watch( q_search_for ) --> newVal : ", newVal + " / oldVal :" + oldVal ) ; 
			// 		// this.q_search_string = newVal ; 
			// 		search_string = newVal ; 
					
			// 	},

		}

	})
	



















/*  // FROM TUTORIAL : cf : https://fr.vuejs.org/v2/guide/index.html 
	// - - - - - - - - - - - - - //
	// VUE APPS - SEARCH 
	var tutorial_v_search = new Vue({

		// el			: '#vue_test', //'#user-switch',
		el			: '#vue_test',
		delimiters	: custom_delimiters,
		
		// data container
		data: {
			
			message			: 'Bienvenue in vue.js ...',
			seen			: false,
			mess_hover 		: 'Bienvenue...' + new Date().toLocaleString(),

			todos			: todos_var, 

			q_dict 			: q_wrapper,
			q_message 		: "nothing for now in q_results",
			q_results		: {},

		},
		
		computed : {
		// 	results_data(){
		// 		return this.results_data
		// 	}
		},

		// run this when vue app is created
		created : function() {
			console.log(">>> cis_v_search / initiating ... "); 
			console.log(">>> cis_v_search / this.message 	: " + this.message); 
			console.log(">>> cis_v_search / this.q_message : " + this.q_message); 
			console.log(">>> cis_v_search / this.q_results : "); 
			console.log( this.q_results ); 

			// TO DO : run ajax query at start to fill q_results with default data

		},

		methods: {
			reverseMessage: function () {
				this.message = this.message.split('').reverse().join('')
			},
			v_queryOpenScraper: function(e) {
				
				// this = this ;
				this.q_message = "ajax request is being sent";

				console.log(">>> before .then() / this.q_message : ") ;
				console.log(this.q_message) ;

				ajax_query_to_openscraper()
					.then( function(q_data){

						console.log(">>> after then() / q_data : ") ;
						console.log(q_data) ;

						this.q_message = "now ok";
						console.log(">>> after then() / this.q_message : ") ;
						console.log(this.q_message) ;

						this.q_results	= q_data ; 
						console.log(">>> after then() / this.q_data : ") ;
						console.log(this.q_results) ;
					}
				) ;

			},
		},

		// watch nested object :
		// cf : https://vuejs.org/v2/api/#watch
		watch : {
			'q_results' : 
				function (new_results, old_results) {
					// cette fonction de rappel sera appelée quand `cis_v_search.q_results` changera
					
					console.log( "$watch( q_results ) --> old_results : " ) ; 
					console.log( "old_results.status : ", old_results.status ) ; 
					console.log( old_results ) ; 
					
					console.log( "$watch( q_results ) --> new_results : " ) ; 
					console.log( "new_results.status :", new_results.status ) ; 
					console.log( new_results ) ; 
				},

			'message' :  
				function (newVal, oldVal) {
					// cette fonction de rappel sera appelée quand `cis_v_search.message` changera
					console.log("$watch( q_message ) --> newVal : ", newVal + " / oldVal :" + oldVal ) ; 
				}
			,
		}

	})
*/













	
// })