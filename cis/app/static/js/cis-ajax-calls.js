
// initiate data_search value
var data_search = {} ;




// https://stackoverflow.com/questions/23984586/reply-to-ajax-request-using-tornado 


function ajax_err(request, error) {
	console.log(request);
	console.log(error);
}
function ajax_ok(data) {
	console.log(data);
	// alert(data);},
}
function query_openscraper() {
	
	let r = {

		// url 			: 'http://www.cis-openscraper.com/api/data',
		url 			: 'http://localhost:8000/api/data?search_for=coco',
		crossDomain 	: true,
		
		// headers		: {'X-XSRFToken' : 'token' },
		// data			: {'token': 'test_token'},

		type 			: 'GET', //'POST' not working with openscraper because of _xsrf missing
		// data 		: JSON.stringify({new_val : $(this).text()}),
		
		// dataType		: 'json',
		contentType		: 'application/json',
		data			: JSON.stringify( $(this) ),
		
		success 	: ajax_ok,
		error		: ajax_err

	}

	$.ajax(r);
}

$(document).ready(function() {
	$("#query-openscraper-button").on("click", query_openscraper);
});


