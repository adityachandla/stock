$(function(){
	var weekly = false;
	var daily = false;
	var monthly = false;
	$('.loader').hide();

	$('#weeklyButton').click(function(){
		if(weekly === false){
			$.ajax({
				'url': window.location.pathname,
				'data': {'get_data_for':'weekly'},
				'success': function(data){
					$('#weeklyDiv').append(data);
				}
			});
			weekly = true;
		}
	});


	$('#dailyButton').click(function(){
		if(daily === false){
			$.ajax({
				'url': window.location.pathname,
				'data': {'get_data_for':'daily'},
				'success': function(data){
					$('#dailyDiv').append(data);
				}
			});
			daily = true;
		}
	});

	$('#monthlyButton').click(function(){
		if(monthly === false){
			$.ajax({
				'url': window.location.pathname,
				'data': {'get_data_for':'monthly'},
				'success': function(data){
					$('#monthlyDiv').append(data);
				}
			});
			monthly = true;
		}
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