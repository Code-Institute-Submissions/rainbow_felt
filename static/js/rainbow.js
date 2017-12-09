
$(document).ready(function(){
    // Set min height of main container on page load
    $("#main-container").css('min-height', $(window).height() + 'px');
    // Fade out and hide messages after 6 seconds
    $(".js-message").delay(6000).fadeOut('slow');
});


// On window resize change main container min-height
$(window).resize(function(){
    $("#main-container").css('min-height', $(window).height() + 'px');
});