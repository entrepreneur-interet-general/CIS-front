	
	
	
// function to hide / show #userOtherStructureField
function DisplayOtherStructureNameField(){

	console.log("DisplayOtherStructureNameField...");

	var selected_option = $('#userStructure').val();
	console.log("selected_option. : ", selected_option );

	if (selected_option === 'other') {
		$('#userOtherStructureField').show();
	}
	if (selected_option != 'other') {
		$("#userOtherStructureField").hide();
	}

};


$(document).ready(function() {

	// run function when load or change on #userStructure select input
	$("#userStructure").bind( 'load change', function() {
		DisplayOtherStructureNameField() 
	});

})
