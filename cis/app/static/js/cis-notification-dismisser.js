
console.log("::: cis-notification-dismisser.js is loaded") ;


// NOTIFICATIONS DISMISSER
// cf : https://codepen.io/martincarlin87/pen/yewgNy

$(document).on('click', '.notification > button.delete', function() {
	$(this).parent().addClass('is-hidden');
	return false;
});

$(document).on('click', 'article > .message-header > button.delete', function() {
	$(this).parent().addClass('is-hidden');
	return false;
});



// TO RECHECK IN ORDER TO DEAL WITH SAFARI BUG WITH IFRAME DISPLAY

function resizeIframe () {
	var iframe_H = $("#iframe_card_body").height() ;
	console.log("------- iframe_H : ", iframe_H) ;
	$("iframe").height(iframe_H + "px") ;
};

// $(document).on("click", ". btn-feedback-iframe", function(){
// 	resizeIframe()
// }
