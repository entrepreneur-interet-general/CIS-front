
console.log("::: cis-notification-dismisser.js is loaded") ;

// cf : https://codepen.io/martincarlin87/pen/yewgNy

$(document).on('click', '.notification > button.delete', function() {
	$(this).parent().addClass('is-hidden');
	return false;
});