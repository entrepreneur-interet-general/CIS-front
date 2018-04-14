
console.log("::: cis-ajax-call.js is loaded") ;

// - - - - - - - - - - - - - - - - - - - - - - //
// initiate query variables
// - - - - - - - - - - - - - - - - - - - - - - //

// initiate and wrap all query fields in a variable

var q_wrapper		= {

	token				: "cis_front_token",

	search_for 			: [] , // aka #q_search_for

	search_in			: [],
	spider_id			: [ "all" ],

	search_in_domains 	: [] ,
	search_in_places 	: [] , 
	search_in_partners 	: [] ,
	search_in_methods 	: [] ,
	search_in_publics 	: [] ,

	added_by			: null,
	all_results			: false,
	is_complete			: false,

	results_per_page	: 50,
	sort_by				: null,

};



// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //
// CUSTOM FUNCTIONS TO UPDATE / BUILD QUERY SLUG (AKA data_q_slug for AJAX)
// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

// TO DO :
// function to transform object into a string
// cf : https://gist.github.com/lucasdavila/4331999
function wrapper_to_string (object, glue='=', separator='&', adder='+') { 

	return $.map(	Object.getOwnPropertyNames(object), 
					function(k) { 
						return [ k, object[k] ].join(glue) 
					}).join(separator);
}

// simpler function to call join_wrapper
function build_q_slug ( q_wrapper ) {

	var q_slug = wrapper_to_string(q_wrapper) ; 

	return q_slug
}



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
// send specific JWT token proper to CIS front --> to openscraper for authentication



// function ajax_err(request, error) {
// 	console.log(request);
// 	console.log(error);
// }
// function ajax_ok(data) {
// 	console.log( "SUCCESS >>> " ) ;
// 	alert("json successfully loaded...")
// 	console.log(data) ;
// }

// MAIN AJAX FUNCTION AS PROMISE
function ajax_query_to_openscraper( data_q_slug = "search_for=coco" ) {
	
	// build ajax request options
	// https://stackoverflow.com/questions/23984586/reply-to-ajax-request-using-tornado 
	// https://stackoverflow.com/questions/26896679/tornado-cannot-read-json-ajax-requests 

	let request_options = {

		type 			: 'GET', //'POST' not working with openscraper because of _xsrf missing
		crossDomain 	: true,
		crossOrigin		: true, 

		// url 			: 'http://www.cis-openscraper.com/api/data',	// query deployed openscraper instance
		url 			: 'http://localhost:8000/api/data', 			// query local openscraper instance
		
		data			:  data_q_slug ,
		
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

		error 			: function ( httpReq,status,exception ){
			console.log( "ERROR >>> " ) ;
			alert(status+" "+exception);
			return {"status" : "error", "exception": exception }
		}
		
	}

	// run ajax request as Promise 
	// cf : https://www.stephanboyer.com/post/107/fun-with-promises-in-javascript 
	// $.ajax(request_options);
	return new Promise(function(resolve, reject) {
		$.ajax(request_options).done(resolve).fail(reject);
	});
}


// // with callback
// function ajax_to_os(callback) {
// 	result = ajax_query_to_openscraper() ;
// 	callback(result) 
// }


function call_ajax_os(data_q_slug="") {
	
	console.log(">>> call_ajax_os / data_q_slug : ", data_q_slug )
	
	ajax_query_to_openscraper( data_q_slug )
		.then( function(res){
			console.log(">>> call_ajax_os / after then() / res : ") ;
			console.log(res);
			return res ;
		})
}


// - - - - - - - - - - - - - - - - - - - - - - //
// bind ajax query to button(s) 
// - - - - - - - - - - - - - - - - - - - - - - //


$(document).ready(function() {

	$("#query-openscraper-button")
		.on("click", 
			function() { 
				// for debugging purposes
				call_ajax_os(data_q_slug="search_for=coco&token=test_token" );
			}
		);

});


