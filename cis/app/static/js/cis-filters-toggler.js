


$(document).ready(function() {

	console.log("::: cis-filter-toggler.js is loaded") ;

	var navbar_filters = $("#navbar-filters"); 

	var toggler_filters = "filters_on" ; 
	if ( navbar_filters.css('display') == 'none'){
		toggler_filters = "filters_off"
	}

	// var filter_toggler = $(".filters-toggler"); 
	// console.log(filter_toggler) ;

	function toogle_filters_display () { 
		console.log("--- toggling filters ---") ; 
		// navbar_filters.css("display", navbar_filters.css("display") === 'none' ? '' : 'none');	
		toggler_filters === 'filters_on' ? 'filters_off' : 'filters_on' ;	
		navbar_filters.toggle();	
	};

	// show or hide navbar-filters with click on elements with class .filters-toggler
	// cf : https://stackoverflow.com/questions/38149437/jquery-functions-not-working-after-click-button
	$(document).on("click", ".filters-toggler", function(){

		// console.log(this.id) ;
		console.log(toggler_filters) ;

		// checking if current filter toggler is input
		if (this.id === "q_search_for"){
			if (toggler_filters === "filters_off"){
				toogle_filters_display() ;
			}
		}
		else {
			toogle_filters_display() ; 
		}
	
	});

});