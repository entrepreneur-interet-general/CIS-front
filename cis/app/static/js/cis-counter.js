

console.log("::: cis-counter.js is loaded ") ;


function RunCounter () {

	setTimeout( function() {

		// from : http://jsfiddle.net/MbRE9/2/
		$('.Count').each(function () {
			$(this).prop('Counter',0).animate({
				Counter: $(this).text()
			}, {
				duration: 2500,
				easing: 'swing',
				step: function (now) {
					$(this).text(Math.ceil(now));
				}
			});
		}), 
		1000 // time for timeout in milliseconds
	});
};


// $( document ).ready(function() {

// 	RunCounter() ;

// })