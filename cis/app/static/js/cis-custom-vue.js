

// - - - - - - - - - - - - - //
// DATA
// - - - - - - - - - - - - - //

// instanciate main data object for search
var results_data = {

	results_count : 789 ,
	results_list : [
		null
	]

} ;




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

	delimiters: ['[[',']]'],

	props: ['todo'],
	template: '<li>[[ todo.text ]]</li>'
})



// - - - - - - - - - - - - - //
// APP
// - - - - - - - - - - - - - //

var cis_vue_app = new Vue({

	el: '#vue_test', //'#user-switch',
	// delimiters: ['[[',']]'],
	
	data: {
		message			: 'Bienvenue in vue.js ...',
		seen			: false,
		mess_hover 		: 'Bienvenue...' + new Date().toLocaleString(),
		todos			: [
			{ text: 'Apprendre JavaScript' },
			{ text: 'Apprendre Vue' },
			{ text: 'Intégrer Vue au moteur de recherche' },
			{ text: 'Passer à la prochaine app' }
			],

		results_data 	: results_data,
	},
	
	methods: {
		reverseMessage: function () {
			this.message = this.message.split('').reverse().join('')
		}
	},


})
