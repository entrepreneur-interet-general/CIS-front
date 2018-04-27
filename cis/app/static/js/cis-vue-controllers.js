

// $( document ).ready(function() {


	console.log("::: cis-vue-controllers.js is loaded") ;


	// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //
	// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //
	// DATA UTILS
	// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //
	// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //


	// random number to display missing photos as illustrations
	function randomIntFromInterval(min=1,max=8){
		return Math.floor(Math.random()*(max-min+1)+min);
	}

	// sort an array of objects of partners
	// cf : https://stackoverflow.com/questions/1129216/sort-array-of-objects-by-string-property-value-in-javascript 
	function compare(a,b) {
		if (a.name < b.name)
		  return -1;
		if (a.name > b.name)
		  return 1;
		return 0;
	}



	// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //
	// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //
	// VUE.JS GLOBAL VARS AND UTILS
	// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //
	// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //


	// following tutorial for now...
	// cf : https://fr.vuejs.org/v2/guide/

	// Vue_custom.config.delimiters =  ['[[',']]'] ;

	var custom_delimiters =  ['[[',']]'] 
	// Vue.config.delimiters =  ['[[',']]'] ;

	var spiders_infos ;

	// TO DO : implement for real
	function getUserToken() {
		
		// get token from meta in html 

		var meta_token = $('meta[name="user_token"]').attr("content") ;
		console.log("::: current token in meta : ", meta_token ) ; 
		
		return meta_token
	}



	// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //
	// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //
	// VUE.JS FUNCTIONS
	// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //
	// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //

	

	// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //
	// CONTROLLERS 
	// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //




	// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  //
	// VUE APPS - USER INDEX (HOME) 
	// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  //

	var infos_counts = { 
		"spiders"	: 0 , 
		"projects"	: 0 ,
	}; 


	v_user_home = new Vue({
		
		el			: '#user-home',
		delimiters	: custom_delimiters,

		data		: {

			h_counts : infos_counts ,

		},

		created		: function() {
			console.log(">>> v_user_home / initiating ... "); 
			this.h_queryOpenScraper_infos() ;	
		},

		methods		: {
			
			h_queryOpenScraper_infos : function() {

				var h_counts 	= this.h_counts ;

				console.log("- v_user_home / this.h_counts : ", this.h_counts ) ;

				ajax_query_to_openscraper( url_arg=api_url_current_infos, data_q_slug="" )
					
					.then( function(res){
					
						console.log("- v_user_home / res : ", res ) ;

						h_counts["spiders"]		= res["counts"]["spiders_tested"] ;
						h_counts["projects"]	= res["counts"]["data"] ;
						RunCounter();			

				})
				
			},
		},

		// watch 		: {

		// 	'h_counts' : function(newVal, oldVal){
		// 		console.log("--- v_navbar_search_filters -W- h_counts --> oldVal : " + oldVal + " / newVal : " + newVal );
		// 		// RunCounter();
		// 	},

		// },

	});



	// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  //
	// VUE APPS - SEARCH RESULTS --> dispatcher to box cards
	// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  //


	// for displaying
	var columns_indices 	= [0,1,2,3];

	// declare default vars here 
	var search_string   	= "" ;

	var search_in_tags 		= [] ;
	// var search_in_domains 	= [] ;
	// var search_in_partners 	= [] ;
	// var search_in_publics 	= [] ;
	// var search_in_methods 	= [] ;
	var search_in_adresses 	= [] ;
	var search_in_spiders 	= [] ;

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
	var shuffle_seed		= randomIntFromInterval(min=1, max=1000) ; 

	// declare vue instances variable names
	var v_navbar_search_input, v_navbar_search_filters, v_results ;


	// // ONLY FIRE THIS CONTROLLER IF '#user-results' exists
	// var is_user_results = $('#user-results') ; 
	// console.log("::: is_user_results.length : ", is_user_results.length ) ;

	// if (is_user_results.lenght === 1 ) {

	v_results = new Vue({
		
		el			: '#user-results',
		delimiters	: custom_delimiters,

		data		: {
			
			// columns display variables
			d_columns			: columns_indices,
			d_number_of_columns : columns_indices.length , 
			d_items_per_column 	: results_per_page/columns_indices.length,
			d_columns_width 	: 12/columns_indices.length,

			d_results			: results, 
			
			d_page_n			: page_n,
			d_page_max			: page_max,

			d_loading			: true,
			d_count  			: count_results, 
			d_count_tot			: count_results_total,

			d_count_start 		: count_start, 
			d_count_stop  		: count_stop, 
			d_results_per_page	: results_per_page,

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

			// ajax_query_to_openscraper( url_arg=api_url_current_infos, data_q_slug="" )
			// 	.then( function(res){
			// 		SRC_INFOS = res ;
					console.log(">>> v_results / initiating ... "); 
					console.log(">>> v_results / this.d_count 	: " + this.d_count); 
					console.log(">>> v_results / this.d_tags 	: " + this.d_tags); 
					console.log(">>> v_results / this.d_list 	: " + this.d_list); 
			// });
		},

		watch 		: {

			// TO TRY
			'd_page_n' : function(newVal, oldVal){
				console.log("--- v_results -W- d_page_n / oldVal : " + oldVal + " / newVal : " + newVal );
				console.log("--- v_results -W- d_page_n / this.d_page_n : ", this.d_page_n );
				// this.d_page_n = newVal ;
				v_navbar_search_input.q_page_n = newVal ; //this.d_page_n ; 

			},

			'd_results' : function (new_results, old_results) {

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



	// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  //
	// VUE APPS - FILTERS 
	// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  //
	
	console.log("::: tags var initialisation ... ")
	console.log("::: CHOICES_FILTERS_TAGS 		: ", CHOICES_FILTERS_TAGS )
	console.log("::: CHOICES_FILTERS_PARTNERS 	: ", CHOICES_FILTERS_PARTNERS )
	console.log("::: CHOICES_FILTERS_GEOLOC 	: ", CHOICES_FILTERS_GEOLOC )
	// console.log("::: CATEGORIES_CIS_DICT 	  	: ", CATEGORIES_CIS_DICT )
	console.log("::: CATEGORIES_CIS_DICT_FLAT 	: ", CATEGORIES_CIS_DICT_FLAT)
	// console.log("::: NOMENCLATURE_CIS_DICT 		: ", NOMENCLATURE_CIS_DICT)
	// console.log("::: NORMALIZATION_TAGS_SOURCES_CIS 		: ", NORMALIZATION_TAGS_SOURCES_CIS)
	console.log("::: NORMALIZATION_TAGS_SOURCES_CIS_DICT 	: ", NORMALIZATION_TAGS_SOURCES_CIS_DICT)



	v_navbar_search_filters = new Vue({
		
		el			: '#navbar-search-filters',
		delimiters	: custom_delimiters,

		data		: {

			// retrieve all filters buttons created on the fly by : 
			// flask-jinja |OR| ajax request to distant API in the future (TO DO)
			// --> as vue data vars..
			
			f_filters_tags		: CHOICES_FILTERS_TAGS, 		
			f_categories 		: CATEGORIES_CIS_DICT_FLAT,		// codes for every filters
			f_normalization		: NORMALIZATION_TAGS_SOURCES_CIS_DICT, 
			
			f_checked			: [],

			f_checked_as_code_tags	: [], 
			f_checked_as_src_tags 	: [], 

			// f_is_partners 		: false , 
			f_filters_partners	: SRC_INFOS, 
			// f_filters_partners	: CHOICES_FILTERS_PARTNERS["choices"], 
			// f_filters_partners	: CHOICES_FILTERS_PARTNERS, 
			f_checked_partners	: [],
		},

		created		: function() {
			console.log(">>> v_navbar_search_filters / initiating ... "); 
			console.log(">>> v_navbar_search_filters / this.f_categories : ", this.f_categories); 
			this.f_queryOpenScraper_infos() ;	
		},

		methods		: {
			
			f_queryOpenScraper_infos : function() {

				var f_filters_partners = this.f_filters_partners ;

				console.log("- v_navbar_search_filters / this.f_filters_partners : ", this.f_filters_partners ) ;

				ajax_query_to_openscraper( url_arg=api_url_current_infos, data_q_slug="" )
					
					.then( function(res){
					
						console.log("- v_navbar_search_filters / res : ", res ) ;

						// f_filters_partners["choices"] = [] ;
						// f_filters_partners["choices"].push(res["spiders"]["spiders_list"]) ;
						
						res["spiders"]["spiders_list"].forEach( function (spider, index) {
							Vue.set(f_filters_partners, index, spider) 
						})
						f_filters_partners.sort(compare) ; 
						// this.f_is_partners = true ;
						console.log("- v_navbar_search_filters / this.f_filters_partners : ", f_filters_partners ) ;

				});

				
			},

			f_update_checked_spider_id : function () {
				console.log("- v_navbar_search_input -M- f_update_checked_as_spider_id ... ") ; 
				v_navbar_search_input.q_search_in_spiders = this.f_checked_partners ;
			},

			f_update_checked_as_tags_codes : function() {

				console.log("- v_navbar_search_input -M- f_update_checked_as_tags_codes ... ") ; 
				var f_categories 			= this.f_categories ;
				var f_normalization 		= this.f_normalization ;

				var f_checked_as_code_tags 	= this.f_checked_as_code_tags = [] ;
				var f_checked_as_src_tags 	= this.f_checked_as_src_tags = [] ;

				this.f_checked.forEach( function( filter ) {
					
					// console.log("- v_navbar_search_input -M- filter : ", filter) ; 

					// get corresponding_codes for each filter && f_categories
					// E.G : filter     --> f_categories[filter]
					// E.G : "evaluate" --> ["EVA"]
					var corresponding_codes = f_categories[filter] ;
					
					// push it to f_checked_as_code_tags
					f_checked_as_code_tags.push( corresponding_codes ) ;
					
					// get src tags from corresponding_code && f_normalization 
					var temp_src_tags = [] ;
					corresponding_codes.forEach( function(code) {
						temp_src_tags.push( f_normalization[code] ) ;
					});
					f_checked_as_src_tags.push( temp_src_tags ) ;
					
				}) ;

				// update q_search_in_tags inside v_navbar_search_input
				v_navbar_search_input.q_search_in_tags = f_checked_as_src_tags ;

				// reset page_n
				v_navbar_search_input.q_page_n 	= 1 ;

				// show loader
				v_results.d_count 				= 0 ;

			},

			f_cleanCheckedFromCheckboxesList : function(checkboxes_list_name) {
				
				console.log("- v_navbar_search_input -M- f_cleanTagsFromCheckboxesList ... ") ; 
				console.log("- v_navbar_search_input -M- checkboxes_list :", checkboxes_list_name) ; 
				
				if ( checkboxes_list_name === 'sources_' ) {
					var f_checked = this.f_checked_partners ;
					// get corresponding checkboxes 
					var corresponding_checkboxes 	= $("#sources_").find("input") ; 
				} else {
					var f_checked = this.f_checked ;
					// get corresponding checkboxes 
					var regex_for_checkboxes 		= 'input[id^="' + checkboxes_list_name + '"]:checked' ;
					var corresponding_checkboxes 	= $(regex_for_checkboxes) ; 
				}

				// // get corresponding checkboxes 
				// var regex_for_checkboxes 		= 'input[id^="' + checkboxes_list_name + '"]:checked' ;
				// var corresponding_checkboxes 	= $(regex_for_checkboxes) ; 
				console.log("- v_navbar_search_input -M- corresponding_checkboxes :", corresponding_checkboxes ) ; 

				// clear f_checked from corresponding values 
				corresponding_checkboxes.each(function() {
					var checked_value = $(this).val() ;
					f_checked.splice( $.inArray(checked_value, f_checked), 1 );
				}),

				// uncheck corresponding checkboxes
				corresponding_checkboxes.prop('checked', false); // Unchecks it
			},

		},

		computed	: {
			// TO DO 
		},

		watch		: {
			
			'f_filters_partners' : function(newVal, oldVal){
				console.log("--- v_navbar_search_filters -W- f_filters_partners --> oldVal : " + oldVal + " / newVal : " + newVal );
			},

			'f_checked' : function(newVal, oldVal){
				// launch f_update_checked_as_tags_codes() if f_checked changes
				// note : newVal === oldVal because of v-model ... I guess ...
				console.log("--- v_navbar_search_filters -W- f_checked --> oldVal : " + oldVal + " / newVal : " + newVal );
				console.log("--- v_navbar_search_filters -W- f_checked --> run : this.f_update_checked_as_tags_codes() ");
				this.f_update_checked_as_tags_codes();
			},

			'f_checked_partners' : function(newVal, oldVal){
				// launch f_update_checked_as_tags_codes() if f_checked changes
				// note : newVal === oldVal because of v-model ... I guess ...
				console.log("--- v_navbar_search_filters -W- f_checked_partners --> oldVal : " + oldVal + " / newVal : " + newVal );
				console.log("--- v_navbar_search_filters -W- f_checked_partners --> run : this.f_update_checked_spider_id() ");
				this.f_update_checked_spider_id();
			},


		},

	})






	// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  //
	// VUE APPS - SEARCH INPUT 
	// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  //

	v_navbar_search_input = new Vue({
		
		el			: '#navbar-search-input',
		delimiters	: custom_delimiters,

		data		: {
			
			// debug 
			// q_message			: default_message,

			// token
			q_token				: token_openscraper,

			// free text
			q_search_string 	: search_string,

			// tags for query
			q_search_in_tags		: search_in_tags,



			// TO DO : spiders ( aka partners )
			q_search_in_spiders		: search_in_spiders,

			// TO DO : adresses ( aka locations )
			q_search_in_adresses 	: search_in_adresses,



			// pagination
			q_results_per_page 	: results_per_page,
			q_page_n			: page_n,

			// shuffle & sort
			q_shuffle_seed		: shuffle_seed,
			q_sort_by			: sort_by,
			
			// full url string for API call with ajax
			// q_full_url			: "",

			// 
			q_is_results		: false,
		},

		created		: function() {
			console.log(">>> v_navbar_search_input / initiating ... "); 
			console.log(">>> v_navbar_search_input / this.q_search_string 		: " + this.q_search_string ); 
			console.log(">>> v_navbar_search_input / run : this.v_queryOpenScraper() "); 
			this.v_queryOpenScraper() ;
		},
		
		computed	: {
			// TO DO 
			// createAjaxUrl 	: function() {
			// 	var url = "gnaaaaa" ;
			// 	return url
			// },
		},
		
		methods		: {

			createAjaxSlug 	: function() {
				// initiate slug
				var slug =	  "page_n=" + this.q_page_n
							+ "&token=" + this.q_token
							+ "&shuffle_seed=" + this.q_shuffle_seed 
							+ "&search_for=" + this.q_search_string 
							+ "&results_per_page=" + this.q_results_per_page 
				;
				
				this.q_search_in_tags.forEach( function( tags_list ) {
					tags_list_as_string = "" ; 
					tags_list.forEach( function(tag) {
						tags_list_as_string += tag + "," 
					});
					slug += "&search_in_tags=" + tags_list_as_string
				}) ;

				this.q_search_in_spiders.forEach( function( spider_id ) {
					slug += "&spider_id=" + spider_id
				}) ;

				// return q_slug to v_queryOpenScraper
				return slug
			},

			// main query function to openscraper
			v_queryOpenScraper : function(reset_page_n=false) {
				
				console.log("- v_navbar_search_input / call_ajax with v_queryOpenScraper method ... ") ; 
				
				// TO DO 
				// show loading page css

				console.log("- v_navbar_search_input / reset_page_n : ", reset_page_n) ; 
				if (reset_page_n == true ){
					this.q_page_n = 1 ;
				}
				// _this = this ;
				this.q_message = "request sent : " + this.q_search_string;

				console.log("- v_navbar_search_input -M- / before .then() / _this.q_message : ") ;
				console.log(this.q_message) ;

				console.log("- v_navbar_search_input -M- / before .then() / this.q_results_per_page :", this.q_results_per_page ) ;
				// v_results.d_count 				= 0 ;
				v_results.d_results_per_page 	= this.q_results_per_page ;
				v_results.d_page_n 				= this.q_page_n ;
				v_results.d_loading 			= true ;


				// generate slug
				var q_slug = this.createAjaxSlug() ;
				console.log("- v_navbar_search_input -M- / before .then() / q_slug : ", q_slug ) ;
				// this.q_full_url = q_slug ;

				// setTimeout for debugging ...
				// setTimeout( function(){
				// call ajax function 
				ajax_query_to_openscraper( url_arg=api_url_current, data_q_slug=q_slug )
					
					.then( function( q_data ){
						
						// reset spiders_infos 
						spiders_infos = q_data.spiders_dict ; 

						// reset vars
						// this.q_message = "json received";
						// this.q_results	= q_data ; 
						
						// TO DO 
						// hide loading page css

						// pass data to other Vue instance
						console.log("- v_navbar_search_input -M- / after then() / passing q_data to v_results.d_results ... ") ;
						v_results.d_loading 			= false ;
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

		watch 		: {

			
			'q_page_n' : function(newVal, oldVal){
				console.log("--- v_navbar_search_input -W- q_page_n --> oldVal : " + oldVal + " / newVal : " + newVal );
				console.log("--- v_navbar_search_input -W- q_page_n --> run : this.v_queryOpenScraper() ");
				this.v_queryOpenScraper();
			},

			'q_shuffle_seed' : function(newVal, oldVal){
				console.log("--- v_navbar_search_input -W- q_shuffle_seed --> oldVal : " + oldVal + " / newVal: " + newVal );
				console.log("--- v_navbar_search_input -W- q_shuffle_seed --> run : this.v_queryOpenScraper() ");
				this.v_queryOpenScraper();
			},

			'q_search_in_tags' : function(newVal, oldVal){
				console.log("--- v_navbar_search_input -W- q_search_in_tags --> oldVal : " + oldVal + " / newVal: " + newVal );
				this.v_queryOpenScraper();
			},

			'q_search_in_spiders' : function(newVal, oldVal){
				console.log("--- v_navbar_search_input -W- q_search_in_spiders --> oldVal : " + oldVal + " / newVal: " + newVal );
				this.v_queryOpenScraper();
			},
			
			// 'q_search_string' : function (newVal, oldVal) {
			// 	// 		//  this function will be called when chenge in `cis_v_search_for.q_search_for`
			// 	// 		console.log("--- v_navbar_search_input / $watch( q_search_for ) --> newVal : ", newVal + " / oldVal :" + oldVal ) ; 
			// 	// 		// this.q_search_string = newVal ; 
			// 	// 		search_string = newVal ; 
				
			// 	// show loader
			// 	v_results.d_count 				= 0 ;
			// },

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