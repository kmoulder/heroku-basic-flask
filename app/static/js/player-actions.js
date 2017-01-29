function next_video() {
        start = start + 1;
        $.getJSON('/next/'+subreddit+'/'+start, function(data) {
            videoid = data.url;
            titleText = data.title;
            previous = data.prev;
            newDuration = data.duration;
            tshift = data.timeshift;

            if(previous===0){
                $('.player-arrow-left').css('display', 'none')
                console.log("undisplay")
            }
            else {
                $('.player-arrow-left').css('display', 'block')
                console.log("display")
            }
            $('#player').remove();
            $('#holder').append('<div id="player"></div>');
            $('#title-text').html(titleText);
            $('#duration').html("&nbsp;("+newDuration+")&nbsp;");
            ;
            onYouTubePlayerAPIReady();
            if(isFull===true){
                $('iframe').addClass('iframe-grow')
            }
        });

        $('#comments-box').load('/comments/'+subreddit+'/'+start);
        $("#comments-box").delay(2000).animate({ scrollTop: 0 }, "slow");

        return false;

    }