

// $( document ).ready(function() {





	console.log("::: cis-custom-vue.js is loaded") ;

	
	// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //
	// DATA
	// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //

	// from tutorial
	var todos_var			= [
		{ id:1, text: 'Apprendre JavaScript' },
		{ id:2, text: 'Apprendre Vue' },
		{ id:3, text: 'Intégrer Vue au moteur de recherche' },
		{ id:4, text: 'Passer à la prochaine app' }
	]



	// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //
	// VUE.JS FUNCTIONS
	// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //


	// following tutorial for now...
	// cf : https://fr.vuejs.org/v2/guide/

	// Vue_custom.config.delimiters =  ['[[',']]'] ;

	var custom_delimiters =  ['[[',']]'] 
	// Vue.config.delimiters =  ['[[',']]'] ;




	// - - - - - - - - - - - - - //
	// COMPONENTS 
	// - - - - - - - - - - - - - //

	// DEBUGGING - TUTORIAL
	Vue.component('todo-item', {
		// Le composant todo-item accepte maintenant une
		// « prop » qui est comme un attribut personnalisé.
		// Cette prop est appelée todo.

		delimiters	: custom_delimiters,
		props		: ['todo'],
		template	: '<li>[[ todo ]]</li>',

	})


	// MAIN RESULTS DISPLAYER
	Vue.component('cis-search-results', {
		// Le composant search-item accepte maintenant une
		// « prop » qui est comme un attribut personnalisé.
		// Cette prop est appelée results.

		delimiters	: custom_delimiters,
		props		: ['results'],
		template	: '<div> my results </div>',

	})






	// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //
	// CONTROLLERS 
	// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = //

	// declare default vars here 
	var search_string   = "" ;
	var search_tags		= [] ;
	var results 		= {} ;
	
	var count_results 	= 0 ;
	var default_message = "no request for now..." ;


	// declare vue instances variable names
	var v_navbar_search_input, v_navbar_search_filters, v_results ;




	// ONLY FIRE THIS CONTROLLER IF '#user-results' exists
	var is_user_results = $('#user-results') ; 
	console.log("::: is_user_results.length : ", is_user_results.length ) ;



	// if (is_user_results.lenght === 1 ) {

	// - - - - - - - - - - - - - //
	// VUE APPS - SEARCH RESULTS --> dispatcher to box cards
	v_results = new Vue({
		
		el			: '#user-results',
		delimiters	: custom_delimiters,

		data		: {

			d_results	: results, 

			d_count  	: count_results, 
			d_tags		: search_tags,

			d_as_list 	: [] ,

		},

		// methods		: [
		// 	update_d_results : function(new_results){
				
		// 	}
		// ],

		computed	: {
			// TO DO 
			myComputedFunction : function() {
				console.log() ; 
				return true
			}
		},

		created		: function() {
			console.log(">>> v_results / initiating ... "); 
			console.log(">>> v_results / this.d_count 		: " + this.d_count); 
			console.log(">>> v_results / this.d_tags 		: " + this.d_tags); 
			console.log(">>> v_results / this.d_list 		: " + this.d_list); 
		},

		watch 		: {
			
			'd_results' : 

				function (new_results, old_results) {

					// this function will be called when chenge in `v_results.d_results`
					
					console.log( "--- v_results / $watch( q_results ) --> old_results : " ) ; 
					console.log( "--- v_results / old_results.status : ", old_results.status ) ; 
					console.log( old_results ) ; 
					
					console.log( "--- v_results / $watch( q_results ) --> new_results : " ) ; 
					console.log( "--- v_results / new_results.status :", new_results.status ) ; 
					console.log( new_results ) ; 
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
			q_message		: default_message,
			q_search_string : search_string,
			// q_results		: results,
		},

		created		: function() {
			console.log(">>> v_navbar_search_input / initiating ... "); 
			console.log(">>> v_navbar_search_input / this.q_search_string 		: " + this.q_search_string ); 
		},

		methods		: {
			
			// main query function to openscraper
			v_queryOpenScraper: function(e) {
				
				console.log("- v_navbar_search_input / call_ajax ... ") ; 

				// _this = this ;
				this.q_message = "request sent : "+ this.q_search_string;

				console.log("- v_navbar_search_input / before .then() / _this.q_message : ") ;
				console.log(this.q_message) ;
				
				// generate slug
				var q_slug = "search_for="+ this.q_search_string ;
				console.log("- v_navbar_search_input / before .then() / q_slug : ", q_slug ) ;
				
				// setTimeout for debugging ...
				// setTimeout( function(){
					// call ajax function 
					ajax_query_to_openscraper( data_q_slug=q_slug )
						
						.then( function( q_data ){
							
							// reset vars
							this.q_message = "json received";
							// this.q_results	= q_data ; 
							
							// pass data to other Vue instance
							console.log("- v_navbar_search_input / after then() / passing q_data to v_results.d_results ... ") ;
							v_results.d_results = q_data ;

							// console.log("- v_navbar_search_input / after then() / q_data : ") ;
							// console.log(q_data) ;

							console.log("- v_navbar_search_input /after then() / this.q_message : ") ;
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

			'q_search_string' : 
			
				function (newVal, oldVal) {
					//  this function will be called when chenge in `cis_v_search_for.q_search_for`
					console.log("--- v_navbar_search_input / $watch( q_search_for ) --> newVal : ", newVal + " / oldVal :" + oldVal ) ; 
					// this.q_search_string = newVal ; 
					search_string = newVal ; 
					
				},

		}

	})
	









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













	
// })