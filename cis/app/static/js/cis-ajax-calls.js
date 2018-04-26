
console.log("::: cis-ajax-call.js is loaded") ;

// - - - - - - - - - - - - - - - - - - - - - - //
// initiate query variables
// - - - - - - - - - - - - - - - - - - - - - - //

// initiate and wrap all query fields in a variable

var meta_config_name 	= $('meta[name="config_name"]').attr("content") ;
console.log("::: current config_name in meta : ", meta_config_name ) ; 

var meta_token 			= $('meta[name="user_token"]').attr("content") ;
console.log("::: current token in meta : ", meta_token ) ; 



// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //
// CUSTOM FUNCTIONS TO UPDATE / BUILD QUERY SLUG (AKA data_q_slug for AJAX)
// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //


// here just for debug usage and debug function 'build_q_slug'

var q_wrapper		= {

	token				: meta_token, // "cis_front_token",

	search_for 			: [] , // aka #q_search_for

	// search_in			: [],
	spider_id			: [ "all" ],

	search_in_tags 		: [] ,
	search_in_adress 	: [] ,


	added_by			: null,
	all_results			: false,
	is_complete			: false,

	results_per_page	: 50,
	sort_by				: null,

};


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

var url_api_root_dev	= 'http://localhost:8000' ;
var url_api_root_prod	= 'http://www.cis-openscraper.com' ;

var url_api_data	= '/api/data' ;
var url_api_infos	= '/api/infos' ;

// choose api url depending on config_name
var url_root ; 
if (meta_config_name == "production") {
	url_root 		= url_api_root_prod ;
} else {
	url_root 		= url_api_root_dev ;
};

var api_url_current 		= url_root + url_api_data ;
var api_url_current_infos	= url_root + url_api_infos ; 

console.log("api_url_current")

// MAIN AJAX FUNCTION AS PROMISE
function ajax_query_to_openscraper( url_arg=api_url_current, data_q_slug = "search_for=" ) {
	
	console.log( "AJAX >>> url_arg 	   			: ", url_arg ) ;
	console.log( "AJAX >>> data_q_slug 			: ", data_q_slug ) ;
	console.log( "AJAX >>> data_q_slug.length 	: ", data_q_slug.length ) ;

	// build ajax request options
	// cf : https://stackoverflow.com/questions/23984586/reply-to-ajax-request-using-tornado 
	// cf : https://stackoverflow.com/questions/26896679/tornado-cannot-read-json-ajax-requests 

	let request_options = {

		type 			: 'GET', //'POST' not working with openscraper as long as _xsrf is either wrong or missing
		
		crossDomain 	: true,
		// crossOrigin		: true, 
		// cors 			: true,
		// secure			: true,
		
		// WARNING : somtimes slug is very long so response could be denied even is CORS is enabled...
		// cf : https://openclassrooms.com/forum/sujet/probleme-avec-cross-origin-request-node
		// header			: {'Access-Control-Allow-Origin': "*" },
		// header  		: {"Content-Length": data_q_slug.length }, 
		// header			: {'Access-Control-Allow-Origin': "http://carrefourdesinnovationssociales.fr/" },
		// headers		: {'X-XSRFToken' : 'token' }, 		// not needed if not post method

		//// SWITCH TO URL_DEV IF SIMULTANEOUSLY DOING TESTS ON OPENSCRAPER SOURCE CODE
		url 			: url_arg ,

		// WARNING / POSSIBLE ERROR : "414 Request-URI Too Large" on nginx if data_q_slug is very long... 
		// cf : http://gbanis.com/blog/howto-troubleshoot-nginx-error-uri-too-large 
		// resolved with : https://stackoverflow.com/questions/23732147/configuring-nginx-for-large-uris 
		data			: data_q_slug ,
		
		// data			: {'token': 'test_token'},
		// data 		: JSON.stringify({new_val : $(this).text()}),

		// contentType		: 'application/json',
		dataType		: 'json',
		// dataType		: 'script',
		// dataType 		:"jsonp",
		// jsonp			: false,
		// jsonpCallback	: "myJsonMethod",
		
		success 		: function( data ){
			// console.log( "AJAX response >>> " ) ;
			// alert("json successfully loaded...")

			console.log( "AJAX response ! >>> raw json data : " ) ;
			console.log( data ) ;

			// console.log( "AJAX response ! >>> raw data as json.stringify : " ) ;
			// console.log(JSON.stringify( data )) ;

			q_data = data ;
			// q_data = JSON.stringify(data) ;
			// q_data = JSON.parse(data) ;
			
			return q_data ;
		},

		error 			: function ( httpReq,status,exception ){
			console.log( "AJAX >>> ERROR !!! " ) ;
			alert( status + " " + exception );
			return { "status" : "error", "exception": exception }
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


function call_ajax_os( url_arg=api_url_current, data_q_slug="") {
	
	console.log(">>> call_ajax_os / data_q_slug : ", data_q_slug )
	console.log(">>> call_ajax_os / data_q_slug : ", data_q_slug )
	
	ajax_query_to_openscraper( url_arg, data_q_slug )
		.then( function(res){
			console.log(">>> call_ajax_os / after then() / res : ") ;
			console.log(res);
			return res ;
		})
}


// var SRC_INFOS = call_ajax_os(url_arg=api_url_current_infos ) ;
var SRC_INFOS = [] ;
// var SRC_INFOS = {
// 	"fullname"	: "Sourceurs", 
// 	"name"		: "sources_", 
// 	"choices"	: []
// };
ajax_query_to_openscraper( url_arg=api_url_current_infos, data_q_slug="" )
	.then( function(res){
		SRC_INFOS["choices"] = res ;
		console.log(">>> SRC_INFOS >>> ", SRC_INFOS ) ;
	});


// - - - - - - - - - - - - - - - - - - - - - - //
// bind ajax query to button(s) 
// - - - - - - - - - - - - - - - - - - - - - - //

// FOR DEBUGGING PURPOSES
$(document).ready(function() {


	$("#query-openscraper-button")
		.on("click", 
			function() { 
				// for debugging purposes
				call_ajax_os(url_arg=api_url_current, data_q_slug="search_for=coco&token=test_token" );
			}
		);

	$("#query-openscraper-infos-button")
		.on("click", 
			function() { 
				// for debugging purposes
				call_ajax_os(url_arg=api_url_current_infos );
			}
		);

});


