/**
 * Created by narendra on 9/3/17.
 */

$(document).ready(function(){

    $('.homepage-slider').owlCarousel({
        loop:true,
        nav:false,
        animateIn: 'fadeInRight',
        items: 1,
        slideBy: 1,
        scrollPerPage: true,
        stagePadding: 0,
        smartSpeed: 8000,
        dots: false,
        autoplay: true,
        margin: 20,
        lazyLoad: true,
        autoplayTimeout: 2500,
        autoplayHoverPause: false
    });

});