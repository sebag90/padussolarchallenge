$(document).ready(function(){


	$("#container").css("height",($(window).height()));
	$("img#logo").css("margin-top",(($(window).height()/2)-150));
	$("img#logo").css("margin-left",(($(window).width()/2)-191));
	$("#ragionesociale").css("margin-top",($(window).height()/2)+50);


});


$(window).resize(function() {
	$("#container").css("height",($(window).height()));
	$("img#logo").css("margin-top",(($(window).height()/2)-150));
	$("img#logo").css("margin-left",(($(window).width()/2)-191));
	$("#ragionesociale").css("margin-top",($(window).height()/2)+50);
});