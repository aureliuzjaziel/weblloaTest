jQuery(document).ready(function($) {

    'use strict';

        $(".Modern-Slider").slick({
            autoplay:true,
            speed:1000,
            slidesToShow:1,
            slidesToScroll:1,
            pauseOnHover:false,
            dots:true,
            fade: true,
            pauseOnDotsHover:true,
            cssEase:'linear',
           // fade:true,
            draggable:false,
            prevArrow:'<button class="PrevArrow"></button>',
            nextArrow:'<button class="NextArrow"></button>', 
          });

        $('#nav-toggle').on('click', function (event) {
            event.preventDefault();
            $('#main-nav').toggleClass("open");
        });


        $('.tabgroup > div').hide();
            $('.tabgroup > div:first-of-type').show();
            $('.tabs a').click(function(e){
              e.preventDefault();
                var $this = $(this),
                tabgroup = '#'+$this.parents('.tabs').data('tabgroup'),
                others = $this.closest('li').siblings().children('a'),
                target = $this.attr('href');
            others.removeClass('active');
            $this.addClass('active');
            $(tabgroup).children('div').hide();
            $(target).show();
          
        })



        $(".box-video").click(function(){
          const video = $('video', this)[0];
          if (video) {
            video.play();
            $(this).addClass('open');
          }
        });

        $('.owl-carousel').owlCarousel({
            loop:true,
            margin:30,
            responsiveClass:true,
            responsive:{
                0:{
                    items:1,
                    nav:true
                },
                600:{
                    items:2,
                    nav:false
                },
                1000:{
                    items:3,
                    nav:true,
                    loop:false
                }
            }
        })



        var contentSection = $('.content-section, .main-banner');
        var navigation = $('nav');
        
        //when a nav link is clicked, smooth scroll to the section
        navigation.on('click', 'a', function(event){
            event.preventDefault(); //prevents previous event
            smoothScroll($(this.hash));
        });
        
        //update navigation on scroll...
        $(window).on('scroll', function(){
            updateNavigation();
        })
        //...and when the page starts
        updateNavigation();
        
        /////FUNCTIONS
        function updateNavigation(){
            contentSection.each(function(){
                var sectionName = $(this).attr('id');
                var navigationMatch = $('nav a[href="#' + sectionName + '"]');
                if( ($(this).offset().top - $(window).height()/2 < $(window).scrollTop()) &&
                      ($(this).offset().top + $(this).height() - $(window).height()/2 > $(window).scrollTop()))
                    {
                        navigationMatch.addClass('active-section');
                    }
                else {
                    navigationMatch.removeClass('active-section');
                }
            });
        }
        function smoothScroll(target){
            $('body,html').animate({
                scrollTop: target.offset().top
            }, 800);
        }


        $('.button a[href*=#]').on('click', function(e) {
          e.preventDefault();
          $('html, body').animate({ scrollTop: $($(this).attr('href')).offset().top -0 }, 500, 'linear');
        });


});

// Código modal
document.addEventListener("DOMContentLoaded", function () {
    const botonesAbrir = document.querySelectorAll(".abrir-modal");

    botonesAbrir.forEach((boton) => {
        boton.addEventListener("click", function (e) {
            e.preventDefault();
            const modal = this.parentElement.querySelector(".mi-modal");
            modal.style.display = "block";

            // Cerrar con la X
            const cerrar = modal.querySelector(".cerrar");
            cerrar.addEventListener("click", function () {
                modal.style.display = "none";
            });

            // Cerrar al hacer clic en cualquier parte del documento que no sea el contenido del modal
            setTimeout(() => {
                document.addEventListener("click", function cerrarAlClickFuera(e) {
                    // Si el clic NO fue dentro del contenido del modal ni en el botón de abrir
                    if (!modal.contains(e.target) && !boton.contains(e.target)) {
                        modal.style.display = "none";
                        document.removeEventListener("click", cerrarAlClickFuera); 
                    }
                });
            }, 10); 
            

            // Cerrar con la tecla Escape
            document.addEventListener("keydown", function (e) {
                if (e.key === "Escape") {
                    modal.style.display = "none";
                }
            });
        });
    });
});

