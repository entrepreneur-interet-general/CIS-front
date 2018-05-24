	

// function to toggle the "is-hovered" class of any element 
// function ToggleActive() {
// 	$(this).toggleClass('is-hovered');
//   };

	
// function to hide/show #userOtherStructureField
function DisplaySiretAndOtherStructureNameField(){

	console.log("DisplayOtherStructureNameField...");

	var selected_option = $('#userPartnerStructure').val();
	console.log("selected_option : ", selected_option );

	if (selected_option === 'other') {
		$('#userOtherStructureField').show();
		$('#userStructureProfileField').show();
		$('#userWishesFields').show();
		$('#userSiretField').show();
	}
	if (selected_option != 'other') {
		$("#userOtherStructureField").hide();
		$('#userStructureProfileField').hide();
		$('#userWishesFields').hide();
		$("#userSiretField").hide();
	}

};


// function to hide/show #userOtherStructureField
function ToggleModifyPassword(){

	console.log("ToggleModifyPassword...");

	var is_modify_active = $('#showModifyPwdBtn').hasClass("is-hovered");
	console.log("is_modify_active : ", is_modify_active );

	
	if (is_modify_active === false) {
		$('#userModifyPassword').show();
		$('#showModifyPwdBtn').addClass('is-hovered');
	}
	else {
		$('#userModifyPassword').hide();
		$('#showModifyPwdBtn').removeClass('is-hovered');
	}

};


$(document).ready(function() {

	// run function when load or change on #userStructure select input
	// cf : 
	$("#userPartnerStructure").bind( 'change load', function() {
		DisplaySiretAndOtherStructureNameField() 
	});
	$("#userPartnerStructure").trigger( 'change');

	// $("#showModifyPwdBtn").bind( 'change', function() {
	// 	ToggleModifyPassword() 
	// });
})
