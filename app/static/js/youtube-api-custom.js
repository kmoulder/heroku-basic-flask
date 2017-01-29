/**
 * Created by mould_000 on 9/3/2016.
 */
<!-- YOUTUBE API -->

    // create youtube player


    var player;
    function onYouTubePlayerAPIReady() {
        player = new YT.Player('player', {
          height: '656',
          width: '100%',
          videoId: videoid,
          playerVars: { 'autoplay': 0, 'autohide': 1,'rel':0, 'iv_load_policy': 3, 'start': startTime },
          events: {
            'onReady': onPlayerReady,
            'onStateChange': onPlayerStateChange
          }
        });
    }

    // autoplay video
    function onPlayerReady(event) {
        event.target.playVideo();
    }

    // when video ends
    function onPlayerStateChange(event) {
        if(event.data === 0) {
            next_video();
        }
       // if(!playing){
       //     allowFullscreen = false;
       // }
        else {
            allowFullscreen = true;
        }
    }
