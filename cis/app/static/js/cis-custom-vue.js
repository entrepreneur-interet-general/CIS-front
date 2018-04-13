

// - - - - - - - - - - - - - //
// DATA
// - - - - - - - - - - - - - //

// instanciate main data object for search
var results_data = {

	status 			: "naaaah",
	results_count 	: 789 ,
	results_list 	: [
		null
	]

} ;


// initiate container for results from openscraper
// var data_results = { 		"status" 		: "ajax not queried yet..." ,
// 							"query_log"		: { },
// 							"query_results"	: []
// 						} ;

// var data_results_new = { 	"status" 		: "this is new !" ,
// 							"query_log"		: { "yo" : "foo" },
// 							"query_results"	: [ {"A" : "B"}, "C"]
// 						} ;



// from tutorial
var todos_var			= [
	{ id:1, text: 'Apprendre JavaScript' },
	{ id:2, text: 'Apprendre Vue' },
	{ id:3, text: 'Intégrer Vue au moteur de recherche' },
	{ id:4, text: 'Passer à la prochaine app' }
]



// - - - - - - - - - - - - - //
// VUE.JS FUNCTIONS
// - - - - - - - - - - - - - //


// following tutorial for now...
// cf : https://fr.vuejs.org/v2/guide/

// var Vue_custom = new Vue({}) ;
// Vue_custom.config.delimiters =  ['[[',']]'] ;


Vue.config.delimiters =  ['[[',']]'] ;


// - - - - - - - - - - - - - //
// COMPONENTS 
// - - - - - - - - - - - - - //

Vue.component('todo-item', {
	// Le composant todo-item accepte maintenant une
	// « prop » qui est comme un attribut personnalisé.
	// Cette prop est appelée todo.

	delimiters	: ['[[',']]'],
	props		: ['todo'],
	template	: '<li>[[ todo ]]</li>',

})


 
// - - - - - - - - - - - - - //
// APP
// - - - - - - - - - - - - - //

var cis_vue_app = new Vue({

	el: '#vue_test', //'#user-switch',
	delimiters: ['[[',']]'],
	
	// data container
	data: {
		
		message			: 'Bienvenue in vue.js ...',
		seen			: false,
		mess_hover 		: 'Bienvenue...' + new Date().toLocaleString(),

		todos			: todos_var, 

		q_message 		: "nothing for now in q_results",
		q_results		: {},

	},
	
	// computed : {
	// 	results_data(){
	// 		return this.results_data
	// 	}
	// },

	// run this when vue app is created
	created : function() {
		console.log(">>> initaiting vue app : cis_vue_app"); 
		console.log(">>> this.message : " + this.message); 
		console.log(">>> this.q_results : "); 
		console.log(this.q_results); 
	},

	methods: {
		reverseMessage: function () {
			this.message = this.message.split('').reverse().join('')
		},
		v_queryOpenScraper: function(e) {
			
			_this = this ;

			_this.q_message = "ajax request is being sent";

			console.log(">>> before .then() / _this.q_message : ") ;
			console.log(_this.q_message) ;

			ajax_query_to_openscraper()
				.then( function(q_data){

					console.log(">>> after then() / q_data : ") ;
					console.log(q_data) ;

					_this.q_message = "now ok";
					console.log(">>> after then() / _this.q_message : ") ;
					console.log(_this.q_message) ;

					_this.q_results	= q_data ; 
					console.log(">>> after then() / _this.q_data : ") ;
					console.log(_this.q_results) ;
				}
			) ;

		},
	},

	// watch nested object :
	// cf : https://vuejs.org/v2/api/#watch
	watch : {
		'q_results' : { 
			handler : function (newVal, oldVal) {
				console.log("$watch( q_results ) --> newVal : ", newVal + " / oldVal :" + oldVal ) ; 
			},
			deep : true,
		}
	}

})


// $watch est une méthode de l'instance
cis_vue_app.$watch('message', function (newVal, oldVal) {
	// cette fonction de rappel sera appelée quand `cis_vue_app.message` changera
	console.log("$watch( message ) --> newVal : ", newVal + " / oldVal :" + oldVal ) ; 
})


// $watch est une méthode de l'instance
cis_vue_app.$watch('todos', function (newVal, oldVal) {
	// cette fonction de rappel sera appelée quand `cis_vue_app.todos` changera
	console.log("I'm watching you, todos...") ; 
})