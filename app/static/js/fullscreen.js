var element = document.getElementById('element');
var fullscreen = document.getElementById('fullscreen');
var isFull = false;
console.log('hello')


function launchIntoFullscreen() {
			console.log('start fullscreen');
      	  $('html, body').animate({scrollTop: '0px'}, 500);
          $('#comments-box,.video-info,.current-sub,.top-slider,.no-top,.navbar-default,.player-arrow-right,.player-arrow-left').removeClass('fadein').addClass('fadeout')
          $('#player-box').removeClass('player-shrink').addClass('player-grow')
          $('iframe').removeClass('iframe-shrink').addClass('iframe-grow')
          isFull = true
          console.log('finish fullscreen')
};

function exitFullscreen() {
          $('#comments-box,.video-info,.current-sub,.top-slider,.no-top,.navbar-default,.player-arrow-right,.player-arrow-left').css('opacity', '0').addClass('fadein').removeClass('fadeout')
          $('#player-box').removeClass('player-grow').addClass('player-shrink')
          $('iframe').removeClass('iframe-grow').addClass('iframe-shrink')

          isFull = false
};

function idleLogout() {

    function resetTimer() {
	exitFullscreen();
    clearTimeout(t);
    t = setTimeout(launchIntoFullscreen, 5000);  // time is in milliseconds
    };

    var t;
    console.log('t set')
    resetTimer();
    console.log('reset')
    window.onload = resetTimer;
    window.onmousemove = resetTimer;
    window.onmousedown = resetTimer; // catches touchscreen presses
    window.onclick = resetTimer;     // catches touchpad clicks
    window.onscroll = resetTimer;    // catches scrolling with arrow keys
    window.onkeypress = resetTimer;
	

};

idleLogout();



/*
$(document).ready(function () {


    $('body').on('keydown',function(e){
      if(e.which===65 && isFull===false){
      	  $('html, body').animate({scrollTop: '0px'}, 500);
          $('#comments-box,.video-info,.current-sub,.top-slider,.no-top,.navbar-default,.player-arrow-right,.player-arrow-left').removeClass('fadein').addClass('fadeout')
          $('#player-box').removeClass('player-shrink').addClass('player-grow')
          $('iframe').removeClass('iframe-shrink').addClass('iframe-grow')
          isFull = true
      }
      if(e.which===83 && isFull===true){
          $('#comments-box,.video-info,.current-sub,.top-slider,.no-top,.navbar-default,.player-arrow-right,.player-arrow-left').css('opacity', '0').addClass('fadein').removeClass('fadeout')
          $('#player-box').removeClass('player-grow').addClass('player-shrink')
          $('iframe').removeClass('iframe-grow').addClass('iframe-shrink')

          isFull = false
      }
    });

});

*/