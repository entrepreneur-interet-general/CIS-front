
$(document).on('click', '.notification > button.delete', function() {
	$(this).parent().addClass('is-hidden');
	return false;
});