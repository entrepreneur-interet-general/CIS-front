




// following tutorial for now...
// cf : https://fr.vuejs.org/v2/guide/

Vue.component('todo-item', {
	// Le composant todo-item accepte maintenant une
	// « prop » qui est comme un attribut personnalisé.
	// Cette prop est appelée todo.
	props: ['todo'],
	template: '<li>{{ todo.text }}</li>'
})




var app = new Vue({

	el: '#vue_test',
	delimiters: ['[[',']]'],
	
	data: {
		message		: 'Bienvenue in vue.js ...',
		seen		: false,
		mess_hover 	: 'Bienvenue...' + new Date().toLocaleString(),
		todos		: [
			{ text: 'Apprendre JavaScript' },
			{ text: 'Apprendre Vue' },
			{ text: 'Créer quelque chose de génial' }
			]
	},
	
	methods: {
		reverseMessage: function () {
			this.message = this.message.split('').reverse().join('')
		}
	},


})