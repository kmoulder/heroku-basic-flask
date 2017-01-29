/**
 * Created by mould_000 on 9/4/2016.
 */
<!-- FULLSCREEN -->

var isFull

    $(document).on('click', '.toggle-button', function() {
        $(this).toggleClass('toggle-button-selected');
        fullscreenToggle = !fullscreenToggle;
    });

function launchIntoFullscreen() {
    if(isFull===false && fullscreenToggle===true && allowFullscreen===true){
           console.log('start fullscreen');
      	  $('html, body').animate({scrollTop: '0px'}, 500);
          $('#comments-box,.video-info,.current-sub,.top-slider,.no-top,.navbar-default,.player-arrow-right,.player-arrow-left').removeClass('fadein').addClass('fadeout')
          $('#player-box').removeClass('player-shrink').addClass('player-grow')
          $('iframe').removeClass('iframe-shrink').addClass('iframe-grow')
          isFull = true
          console.log('finish fullscreen')
        };
};

function exitFullscreen() {
    if(isFull===true){
          $('#comments-box,.video-info,.current-sub,.top-slider,.no-top,.navbar-default,.player-arrow-right,.player-arrow-left').css('opacity', '0').addClass('fadein').removeClass('fadeout')
          $('#player-box').removeClass('player-grow').addClass('player-shrink')
          $('iframe').removeClass('iframe-grow')
          isFull = false
        };
};




function idleLogout() {

    function resetTimer() {
	exitFullscreen();
    clearTimeout(t);
    t = setTimeout(launchIntoFullscreen, 10000);  // time is in milliseconds
    };

    var t;
    console.log('t set')
    resetTimer();
    console.log('reset')
    window.onload = resetTimer;
    window.onmousedown = resetTimer; // catches touchscreen presses
    window.onclick = resetTimer;     // catches touchpad clicks
    window.onscroll = resetTimer;    // catches scrolling with arrow keys
    window.onkeypress = resetTimer;


};

idleLogout();
