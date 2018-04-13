
// - - - - - - - - - - - - - - - - - - - - - - //
// initiate query values
// - - - - - - - - - - - - - - - - - - - - - - //


// initiate data as strigified json


// initiate query fields
var q_search_for	= { "search_for" 			: [] } ; // aka #q_free_input

var q_domains 		= { "limit_by_domains" 		: [] } ;
var q_localisations = { "limit_by_places" 		: [] } ; 
var q_partners		= { "limit_by_partners" 	: [] } ;
var q_methods		= { "limit_by_methods" 		: [] } ;
var q_publics		= { "limit_by_publics" 		: [] } ;
var q_token			= "test"



// - - - - - - - - - - - - - - - - - - - - - - //
// MAIN AJAX REQUEST
// - - - - - - - - - - - - - - - - - - - - - - //
// cf : https://www.sitepoint.com/use-jquerys-ajax-function/ 


// ROADMAP : TO DO !!!
// 1ST : QUERY OPENSCRAPER FOR FIELDS' IDS 					<-- IN DATAMODEL
// 2ND : QUERY OPENSCRAPER FOR PARTNERS' IDS 				<-- IN CONTRIBUTORS
// 3RD : QUERY OPENSCRAPER FOR DATA ACCORDING TO FILTERS 	<-- IN DATA SCRAPED
// 4TH : RASSEMBLE ALL THAT TO FEED VUE.JS					<-- IN VUE.JS

// TO DO 
// send specific JWT token to openscraper for authentication



function ajax_err(request, error) {
	console.log(request);
	console.log(error);
}
function ajax_ok(data) {
	console.log( "SUCCESS >>> " ) ;
	alert("json successfully loaded...")
	console.log(data) ;
}

function ajax_query_to_openscraper( ) {
	
	//  TO DO 

	// get filters values

	// build data slug
	var query_slug 		= "search_for=coco" ;

	// 

	// build ajax request
	// https://stackoverflow.com/questions/23984586/reply-to-ajax-request-using-tornado 
	// https://stackoverflow.com/questions/26896679/tornado-cannot-read-json-ajax-requests 
	let r = {

		type 			: 'GET', //'POST' not working with openscraper because of _xsrf missing
		crossDomain 	: true,
		crossOrigin		: true, 

		// url 			: 'http://www.cis-openscraper.com/api/data',	// query deployed openscraper instance
		url 			: 'http://localhost:8000/api/data', 			// query local openscraper instance
		
		data			:  query_slug ,
		
		// headers		: {'X-XSRFToken' : 'token' }, 		// not needed if not post method

		// data			: {'token': 'test_token'},
		// data 		: JSON.stringify({new_val : $(this).text()}),

		dataType		: 'json',
		// contentType		: 'application/json',
		// dataType 		:"jsonp",
		// jsonp			: false,
		// jsonpCallback	: "myJsonMethod",
		
		success 		: function( data ){
			console.log( "SUCCESS ! >>> " ) ;
			// alert("json successfully loaded...")

			console.log( "SUCCESS ! >>> raw json data : " ) ;
			console.log( data ) ;

			console.log( "SUCCESS ! >>> raw data as json.stringify : " ) ;
			console.log(JSON.stringify( data )) ;

			q_data = data ;
			// q_data = JSON.stringify(data) ;
			// q_data = JSON.parse(data) ;
			
			return q_data ;
		},

		error 			: function(httpReq,status,exception){
			console.log( "ERROR >>> " ) ;
			alert(status+" "+exception);
			return {"status" : "error", "exception": exception }
		}
		
	}

	// run ajax request
	// $.ajax(r);
	return new Promise(function(resolve, reject) {
		$.ajax(r).done(resolve).fail(reject);
	});
}


// // with callback
// function ajax_to_os(callback) {
// 	result = ajax_query_to_openscraper() ;
// 	callback(result) 
// }


// with promise
// function ajax_to_os() {
// 	return new Promise((resolve, reject) => {
// 		var a = ajax_query_to_openscraper() ;
// 		console.log(a);
// 		resolve(a)
// 	})
// }

// function call_ajax_os() {
// 	ajax_to_os()
// 		.then( function(res){
// 			console.log(res);
//			return res ; }
// 		)
// }


function call_ajax_os() {
	ajax_query_to_openscraper()
		.then( function(res){
			console.log(">>> after then() / res : ") ;
			console.log(res);
			return res ;
		})
}


// - - - - - - - - - - - - - - - - - - - - - - //
// bind ajax query to button(s) 
// - - - - - - - - - - - - - - - - - - - - - - //


$(document).ready(function() {

	// $("#query-openscraper-button").on("click", ajax_query_to_openscraper);
	$("#query-openscraper-button").on("click", call_ajax_os );

});


