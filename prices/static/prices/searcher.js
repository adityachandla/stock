$(function(){
	$('.loader').hide();
	$('#searchButton').click(function(){
		var value = $('#searchText').val();
		$.ajax({
			'url': '',
			'data': {'search':value},
			'success':function(data){
				$('#outputDiv').empty();
				$('#outputDiv').append(data);
			}
		});
	});

	$(document).ajaxStart(function(){
	  $('.loader').show();
	  $('.container').css('opacity',0.4);
	  $('.loader').css('opacity',1);
	});

	$(document).ajaxComplete(function(){
	  $(".loader").hide();
	  $('.container').css('opacity',1)
	});
});