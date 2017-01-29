$(document).ready(function(){
    $('.bxslider').bxSlider({
        slideWidth: 150,
        minSlides: 1,
        maxSlides: 5,
        moveSlides: 1,
        slideMargin: 10,
        pager: false,
    });

    $('.video-slider').bxSlider({
        video: true,
        useCSS: false,
        pager: false,
        controls: false,
    });

    $('.nav-slider').bxSlider({
        slideWidth: 300,
        minSlides: 2,
        maxSlides: 5,
        moveSlides: 2,
        slideMargin: 10,
        pager: false,
    });

    $('.tab-slider-1').bxSlider({
        slideWidth: 300,
        minSlides: 2,
        maxSlides: 5,
        moveSlides: 1,
        slideMargin: 10,
        pager: false,
    });

    $('.tab-slider-2').bxSlider({
        slideWidth: 300,
        minSlides: 2,
        maxSlides: 5,
        moveSlides: 1,
        slideMargin: 10,
        pager: false,
    });

    $('.tab-slider-3').bxSlider({
        slideWidth: 300,
        minSlides: 2,
        maxSlides: 5,
        moveSlides: 1,
        slideMargin: 10,
        pager: false,
    });

    $('.tab-slider-4').bxSlider({
        slideWidth: 300,
        minSlides: 2,
        maxSlides: 5,
        moveSlides: 1,
        slideMargin: 10,
        pager: false,
    });

    var callbacks = {
        loadOnTabs: function(e){
            $('.tabs .bx-viewport').css('height','155px');
            $('.tabs .bx-viewport .slide').css('width','300px');
        },
        
        loadOnNav: function (e) {
            $('.navbar-collapse .bx-viewport').css('height', '32px');   
            $('.navbar-collapse .bx-viewport li').css('width','130px');
        },

        preventDefault: function (e) {
            //e.preventDefault();
        }
    }

    $('.nav-tabs li').on('click', callbacks.loadOnTabs );
    $('.navbar-toggle').on('click', callbacks.loadOnNav );

    $('.video > .bx-wrapper .bx-controls-direction a').on('click', callbacks.preventDefault );
});