




// following tutorial for now...
// cf : https://fr.vuejs.org/v2/guide/

Vue.config.delimiters =  ['[[',']]'] ;




Vue.component('todo-item', {
	// Le composant todo-item accepte maintenant une
	// « prop » qui est comme un attribut personnalisé.
	// Cette prop est appelée todo.

	delimiters: ['[[',']]'],

	props: ['todo'],
	template: '<li>[[ todo.text ]]</li>'
})




var app_test = new Vue({

	el: '#vue_test', //'#user-switch',
	delimiters: ['[[',']]'],
	
	data: {
		message			: 'Bienvenue in vue.js ...',
		results_count	: 678,
		seen			: false,
		mess_hover 		: 'Bienvenue...' + new Date().toLocaleString(),
		todos			: [
			{ text: 'Apprendre JavaScript' },
			{ text: 'Apprendre Vue' },
			{ text: 'Intégrer Vue au moteur de recherche' },
			{ text: 'Passer à la prochaine app' }
			]
	},
	
	methods: {
		reverseMessage: function () {
			this.message = this.message.split('').reverse().join('')
		}
	},


})


// var app = new Vue({

// 	el: '#cis_app',
// 	delimiters: ['[[',']]'],
	
// 	data: {
// 		results_count		: 678,
// 	},
	

// })