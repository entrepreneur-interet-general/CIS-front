	
	
	
// function to hide / show #userOtherStructureField
function DisplaySiretAndOtherStructureNameField(){

	console.log("DisplayOtherStructureNameField...");

	var selected_option = $('#userStructure').val();
	console.log("selected_option. : ", selected_option );

	if (selected_option === 'other') {
		$('#userOtherStructureField').show();
		// $('#userSiretField').show();
	}
	if (selected_option != 'other') {
		$("#userOtherStructureField").hide();
		// $("#userSiretField").hide();
	}

};



// $(document).ready(function() {

	// run function when load or change on #userStructure select input
	$("#userStructure").bind( 'load change', function() {
		DisplaySiretAndOtherStructureNameField() 
	});

// })
