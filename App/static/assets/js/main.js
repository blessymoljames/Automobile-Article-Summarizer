/*
Template Name: wroot
Template URI: https://themes.crazyenter.com/static/wroot
Description: wroot - Multipurpose Creative Website Template. Full responsive clean code and easy to use.
Author: crazyEnter
Author URI: https://crazyenter.com
Version: 1.0.0
*/

(function ($) {
    "use strict";

    /* ------------------------------------------------------ */
    /* preloader */
    $(window).on('load', function(){
            $('.spinner-section').fadeOut('slow', function(){
            $(this).remove();
        });
    });

    /* ------------------------------------------------------ */
    /* Fixed Header */
    $(window).on('scroll', function(event) {
        var window_width = $(window).width();
        var scrollValue = $(window).scrollTop();
        if (window_width > 991) {
            if (scrollValue >= 160) {
                $('header').addClass('affix animated fadeIn');
            } else {
                $('header').removeClass('affix animated fadeIn');
            }
        }
    });

    /* ------------------------------------------------------ */
    /* Navbar Menu Active */
    var url = window.location;
    var $navmenu_a = $('.navbar-nav li a');

    $('.navbar-nav li a[href="' + url + '"]').parent().addClass('active');
    $navmenu_a.filter(function () {
        return this.href == url;
    }).parent().addClass('active');

    /* ------------------------------------------------------ */
    /* Search Option */
    // search function variable
    var menuSearch = $('.menu-search');
    var bodyTag = $('body');
    var closeButton = $('.close-button');
    var searchField = $('.search-field');

    // search functions
    menuSearch.on('click', function (e) {
        e.stopPropagation();
        bodyTag.addClass('active-search');
    });

    /* remove search animation by body click */
    closeButton.on('click', function (e) {
       bodyTag.removeClass('active-search');
    });

    bodyTag.on('click', function (e) {
        $(this).removeClass('active-search');
    });
    searchField.on('click', function(e){
        e.stopPropagation();
    });

    /* ------------------------------------------------------ */
    /* About Slider */
    $('.about-slider').owlCarousel({
        items: 1,
        autoplay: true,
        loop: true,
        mouseDrag: true,
        nav: true,
        dots: false,
        navText: [
            "<i class='fas fa-angle-left'></i>",
            "<i class='fas fa-angle-right'></i>"
        ]
    });

    /* ------------------------------------------------------ */
    /* Progress */
    var $skill_progress = $('.circle');
    $skill_progress.waypoint(function () {
        /*** Circle Progress ***/
        // First circle Progress
        var Counter1st = $('.first.circle');
        Counter1st.circleProgress({
            value: 0.75,
            size: 150,
            startAngle: 4.5,
            thickness: 10,
            emptyFill: "transparent",
            animation: {
                duration: 2200
            },
            fill: {
                color: "#00ABC9"
            }
        }).on('circle-animation-progress', function (event, progress) {
            $(this).find('strong').html(Math.round(75 * progress) + '%');
        });

        // Second circle Progress
        var Counter2nd = $('.second.circle');
        Counter2nd.circleProgress({
            value: 0.80,
            size: 150,
            startAngle: 4.5,
            thickness: 10,
            emptyFill: "transparent",
            animation: {
                duration: 2200
            },
            fill: {
                color: "#00ABC9"
            }
        }).on('circle-animation-progress', function (event, progress) {
            $(this).find('strong').html(Math.round(80 * progress) + '%');
        });

        // Third circle Progress
        var Counter3rd = $('.third.circle');
        Counter3rd.circleProgress({
            value: 1,
            size: 150,
            startAngle: 4.5,
            thickness: 10,
            emptyFill: "transparent",
            animation: {
                duration: 2200
            },
            fill: {
                color: "#00ABC9"
            }
        }).on('circle-animation-progress', function (event, progress) {
            $(this).find('strong').html(Math.round(100 * progress) + '%');
        });

    	// skill bar progress
        $('.progress-bar').css({
            animation: "animate-positive 2.5s",
            opacity: "1"
        });
        
        this.destroy();
    }, 
    {
        offset: '100%'
    });

    /* ------------------------------------------------------ */
    /* Isotop jQuery */
    var $grid = $('.portfolio-list');
    $grid.isotope({
      itemSelector: '.single-port',
      percentPosition: true,
      masonry: {
        // use outer width of grid-sizer for columnWidth
        columnWidth: '.col-xl-3'
      }
    });

    // filter items on button click
    $('.port-navigation li').on( 'click', function() {
    	var filterValue = $(this).attr('data-filter');
    	$grid.isotope({ filter: filterValue });
    });

    // 	add portfolio navigation class
    $('.port-navigation li').on('click', function(){
        $('.port-navigation li').removeClass("active");
        $(this).addClass("active");
    });

    // layout Isotope after each image loads
    $grid.imagesLoaded().progress( function() {
        $grid.isotope('layout');
    });

    /* ------------------------------------------------------ */
    /* Testimonial owlCarousel */
    $('.testimonial-list').owlCarousel({
        items:1,
        dots: true,
        dotsContainer: "#owl-thumbs"
    });

    /* ------------------------------------------------------ */
    /* Client List */
    $('.best-client-list').owlCarousel({
        loop: true,
        margin: 30,
        autoplay: true,
        slideTransition: 'linear',
        autoplaySpeed: 3000,
        dots: false,
        autoplayHoverPause: true,
        responsive:{
            0:{
                items:1,
            },
            576:{
                items:2,
            },
            767:{
                items:3,
            },
            992:{
                items:4,
            },
            1000:{
                items:6,
            }
        }
    });

    /* ------------------------------------------------------ */
    /* Member List */
    $('.member-list').owlCarousel({
        loop: true,
        margin: 30,
        dots: true,
        responsive:{
            0:{
                items:1,
            },
            600:{
                items:2,
            },
            992:{
                items:3,
            }
        }
    });

    /* ------------------------------------------------------ */
    /* Masonry Grid Post */
    $('.gird-post').masonry({
        columnWidth: '.col-12',
        itemSelector: '.blog-post'
    });

    /* ------------------------------------------------------ */
    /* Tooltip */
    $('[data-toggle="tooltip"]').tooltip()

    /* ------------------------------------------------------ */
    /* Testimonial owlCarousel */
    $('.portfolio-slider').owlCarousel({
        items:1,
        autoplay: true,
        autoplaySpeed: 1500,
        dots: true
    });

    /* ------------------------------------------------------ */
    /* Single Service Active Class */
    $('.single-service-list li a').on('click', function(){
        $('.single-service-list li').removeClass("active");
        $('.single-service-list li').addClass("active");
    });

    /* ------------------------------------------------------ */
    /* Video Modal */
    $('.video-button').on('click', function(e) {
        e.preventDefault();
        $('#' + $(this).data('modal-id')).modal();
    });
    // Stop Video by click close.
    $('.close').on('click', function() {
        $('iframe').attr('src', $('iframe').attr('src'));
    });

    /* ------------------------------------------------------ */
    /* Wow JS */
    var window_width = $(window).width();
    if (window_width > 767) {
        new WOW().init();
    }

    /* ------------------------------------------------------ */
    /* Contact From */
    $('#submit').on('click', function() {
        $.post("contact.php", $("#contact-form").serialize(), function(response) {
            $('#form-info').fadeIn().html(response);
            $('#form-info').delay(2000).fadeOut();
        });
        return false;
    });
    
}(jQuery));	