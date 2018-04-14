

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
	// Vue.component('todo-item', {
	// 	// Le composant todo-item accepte maintenant une
	// 	// « prop » qui est comme un attribut personnalisé.
	// 	// Cette prop est appelée todo.

	// 	delimiters	: custom_delimiters,
	// 	props		: ['todo'],
	// 	template	: '<li>[[ todo ]]</li>',

	// })


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


	// - - - - - - - - - - - - - //
	// VUE APPS - SEARCH INPUT 
	var cis_v_search_for = new Vue({
		
		el			: '#navbar-search-input',
		delimiters	: custom_delimiters,

		data		: {
			q_message		: "no request for now...",
			q_search_string : "",
			q_results		: {},
		},

		created		: function() {
			console.log(">>> cis_v_search_for / initiating ... "); 
			console.log(">>> cis_v_search_for / this.q_search_string 		: " + this.q_search_string); 
		},

		methods		: {
			
			// main query function to openscraper
			v_queryOpenScraper: function(e) {
				
				console.log("cis_v_search_for / call_ajax ... ") ; 

				// _this = this ;
				this.q_message = "ajax request is being sent : "+ this.q_search_string;

				console.log(">>> before .then() / _this.q_message : ") ;
				console.log(this.q_message) ;
				
				// generate slug
				var q_slug = "search_for="+ this.q_search_string ;
				
				// call ajax function 
				ajax_query_to_openscraper( data_q_slug=q_slug )
					
					.then( function(q_data){
						
						// reset vars
						this.q_message = "json received";
						this.q_results	= q_data ; 

						console.log(">>> after then() / q_data : ") ;
						console.log(q_data) ;

						console.log(">>> after then() / _this.q_message : ") ;
						console.log(this.q_message) ;

						console.log(">>> after then() / _this.q_data : ") ;
						console.log(this.q_results) ;
					}
				) ;

			},
		},
		computed	: {
			// TO DO 
		},
		watch 		: {
			'q_search_for' : {
				function (newVal, oldVal) {
					// cette fonction de rappel sera appelée quand `cis_v_search_for.q_search_for` changera
					console.log("$watch( q_search_for ) --> newVal : ", newVal + " / oldVal :" + oldVal ) ; 
				}
			},
			'q_results' : {
				deep : true 
			}
		}

	})
	

	// - - - - - - - - - - - - - //
	// VUE APPS - FILTERS 
	var cis_v_filters = new Vue({
		
		el			: '#navbar-search-filters',
		delimiters	: custom_delimiters,
		data		: {
			q_dict 	: q_wrapper,
		},
		methods		: {
			// TO DO 
		},
		computed	: {
			// TO DO 
		},
		created		: function() {
			// TO DO 
		}
	})


	// - - - - - - - - - - - - - //
	// VUE APPS - SEARCH RESULTS 
	var cis_v_search_results = new Vue({
		
		el			: '#user-results',
		delimiters	: custom_delimiters,
		data		: {
			results 	: null ,
		},
		methods		: {
			// TO DO 
		},
		computed	: {
			// TO DO 
		},
		created		: function() {
			console.log(">>> cis_v_search_results / initiating ... "); 
			console.log(">>> cis_v_search_results / this.results 		: " + this.results); 
		}
	})

	// - - - - - - - - - - - - - //
	// VUE APPS - SEARCH 
	// var cis_v_search = new Vue({

	// 	// el			: '#vue_test', //'#user-switch',
	// 	el			: '#vue_test',
	// 	delimiters	: custom_delimiters,
		
	// 	// data container
	// 	data: {
			
	// 		message			: 'Bienvenue in vue.js ...',
	// 		seen			: false,
	// 		mess_hover 		: 'Bienvenue...' + new Date().toLocaleString(),

	// 		todos			: todos_var, 

	// 		q_dict 			: q_wrapper,
	// 		q_message 		: "nothing for now in q_results",
	// 		q_results		: {},

	// 	},
		
	// 	computed : {
	// 	// 	results_data(){
	// 	// 		return this.results_data
	// 	// 	}
	// 	},

	// 	// run this when vue app is created
	// 	created : function() {
	// 		console.log(">>> cis_v_search / initiating ... "); 
	// 		console.log(">>> cis_v_search / this.message 	: " + this.message); 
	// 		console.log(">>> cis_v_search / this.q_message : " + this.q_message); 
	// 		console.log(">>> cis_v_search / this.q_results : "); 
	// 		console.log( this.q_results ); 

	// 		// TO DO : run ajax query at start to fill q_results with default data

	// 	},

	// 	methods: {
	// 		reverseMessage: function () {
	// 			this.message = this.message.split('').reverse().join('')
	// 		},
	// 		v_queryOpenScraper: function(e) {
				
	// 			_this = this ;
	// 			_this.q_message = "ajax request is being sent";

	// 			console.log(">>> before .then() / _this.q_message : ") ;
	// 			console.log(_this.q_message) ;

	// 			ajax_query_to_openscraper()
	// 				.then( function(q_data){

	// 					console.log(">>> after then() / q_data : ") ;
	// 					console.log(q_data) ;

	// 					_this.q_message = "now ok";
	// 					console.log(">>> after then() / _this.q_message : ") ;
	// 					console.log(_this.q_message) ;

	// 					_this.q_results	= q_data ; 
	// 					console.log(">>> after then() / _this.q_data : ") ;
	// 					console.log(_this.q_results) ;
	// 				}
	// 			) ;

	// 		},
	// 	},

	// 	// watch nested object :
	// 	// cf : https://vuejs.org/v2/api/#watch
	// 	watch : {
	// 		'q_results' : { 
	// 			handler : function (new_results, old_results) {
	// 				// cette fonction de rappel sera appelée quand `cis_v_search.q_results` changera
					
	// 				console.log( "$watch( q_results ) --> old_results : " ) ; 
	// 				console.log( "old_results.status : ", old_results.status ) ; 
	// 				console.log( old_results ) ; 
					
	// 				console.log( "$watch( q_results ) --> new_results : " ) ; 
	// 				console.log( "new_results.status :", new_results.status ) ; 
	// 				console.log( new_results ) ; 
	// 			},
	// 			deep : true,
	// 		},
	// 		'message' : { 
	// 			function (newVal, oldVal) {
	// 				// cette fonction de rappel sera appelée quand `cis_v_search.message` changera
	// 				console.log("$watch( q_message ) --> newVal : ", newVal + " / oldVal :" + oldVal ) ; 
	// 			}
	// 		},
	// 	}

	// })













	
// })