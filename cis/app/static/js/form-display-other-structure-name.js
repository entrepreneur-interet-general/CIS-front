	
	
	
// function to hide/show #userOtherStructureField
function DisplaySiretAndOtherStructureNameField(){

	console.log("DisplayOtherStructureNameField...");

	var selected_option = $('#userPartnerStructure').val();
	console.log("selected_option. : ", selected_option );

	if (selected_option === 'other') {
		$('#userOtherStructureField').show();
		$('#userStructureProfileField').show();
		$('#userWishesFields').show();
		// $('#userSiretField').show();
	}
	if (selected_option != 'other') {
		$("#userOtherStructureField").hide();
		$('#userStructureProfileField').hide();
		$('#userWishesFields').hide();
		// $("#userSiretField").hide();
	}

};



$(document).ready(function() {

	// run function when load or change on #userStructure select input
	$("#userPartnerStructure").bind( 'load change', function() {
		DisplaySiretAndOtherStructureNameField() 
	});

})
