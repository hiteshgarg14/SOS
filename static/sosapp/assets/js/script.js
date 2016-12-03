$(document).ready(function() {
    "use strict";


//=================================================
//==================== Pre-loader==================
//==================================================

	// makes sure the whole site is loaded
	$(window).load(function() {
		// will first fade out the loading animation
		$(".spinner").fadeOut();
		//then background color will fade out slowly
		$(".pre-loader").delay(200).fadeOut("slow");
	});

//====================================================
//==================Navigation========================
//====================================================


  if ( matchMedia( 'only screen and (min-width: 769px)' ).matches ) {
		$(window).scroll(function() {
		   var $scrollHeight = $(window).scrollTop();
			  if ($scrollHeight > 120) {
				$('#header nav').addClass('addbg').slideDown(400);
			  } else {
				$('#header nav').removeClass('addbg');
			  }
	   });
  }

     $(window).scroll(function() {
         var $scrollHeightt = $(window).scrollTop();
           if ($scrollHeightt > 60 ) {
             $('#single-header-top nav').addClass("navbar-fixed-top");
           } else{
             $('#single-header-top nav').removeClass("navbar-fixed-top");
           }
     });



//   =======================================================
//   =======================Countdown=======================
//   =======================================================


	 $('.countdown').countdown({
		 date: "June 7, 2087 15:03:25",
		  render: function(data) {
			$(this.el).html("<div>"
			+ this.leadingZeros(data.days)
			+ " <span>days</span></div><div>"
			+ this.leadingZeros(data.hours)
			+ " <span>hours</span></div><div>"
			+ this.leadingZeros(data.min)
			+ " <span>minute</span></div><div>"
			+ this.leadingZeros(data.sec)
			+ " <span>sec</span></div>");
	  }
	 });
	 $('.countdown1').countdown({
		 date: "June 7, 2087 15:03:25",
		  render: function(data) {
			$(this.el).html("<div>"
			+ this.leadingZeros(data.days)
			+ " <span>days</span></div><div>"
			+ this.leadingZeros(data.hours)
			+ " <span>hours</span></div><div>"
			+ this.leadingZeros(data.min)
			+ " <span>minute</span></div><div>"
			+ this.leadingZeros(data.sec)
			+ " <span>second</span></div>");
	  }
	 });



//====================================================
//===========Appearence of navigation=================
//====================================================

	  $('.header-top .nav, header .nav').onePageNav({
		scrollThreshold: 0.2, // Adjust if Navigation highlights too early or too late
		scrollOffset: 68 //Height of Navigation Bar
	  });

//====================================================
//=============== For navigation======================
//====================================================

    $('.navbar-collapse ul li a').click(function() {
        $('.navbar-toggle:visible').click();
    });

    $('.search-btn').click(function() {
        $('.search-box').toggle();
    });

//====================================================
//===============Text Slider on Banner================
//====================================================

    $('.flex_text').flexslider({
        animation: "slide",
            selector: ".slides li",
            controlNav: false,
            directionNav: false,
            slideshowSpeed: 4000,
            touch: true,
            useCSS: false,
            direction: "vertical",
			before: function(slider){
			 var height = $('.flex_text').find('.flex-viewport').innerHeight();
			 $('.flex_text').find('li').css({ height: height + 'px' });
        }
    });




//===================================================
//=======================-Mix it up==================
//===================================================

        $('.gallery-list').mixItUp();


//===================================================
//================ Magnific Image Popup==============
//===================================================

    $('.gallery-popup').magnificPopup({
      type:'image',
      closeBtnInside:true,
      // Delay in milliseconds before popup is removed
      removalDelay: 300,

      // Class that is added to popup wrapper and background
      // make it unique to apply your CSS animations just to this exact popup
      mainClass: 'mfp-fade',
      gallery: {
          enabled: true, // set to true to enable gallery

          preload: [0,2], // read about this option in next Lazy-loading section

          navigateByImgClick: true,

          //arrowMarkup: '<button title="%title%" type="button" class="mfp-arrow mfp-arrow-%dir%"></button>', // markup of an arrow button

          closeMarkup: '<button title="%title%" class="mfp-close"><i class="mfp-close-icn">&times;</i></button>',

          tPrev: 'Previous (Left arrow key)', // title for left button
          tNext: 'Next (Right arrow key)', // title for right button
          //tCounter: '<span class="mfp-counter">%curr% of %total%</span>' // markup of counter
        }
   });




//=============================================================
//=============== Animate and WOW Animation====================
//============================================================

	new WOW().init();


// ------------- Magnific Video Popup--------------

 	$('.play').magnificPopup({
	  disableOn: 700,
	  type: 'iframe',
	  mainClass: 'mfp-fade',
	  removalDelay: 160,
	  preloader: false,
	  fixedContentPos: false
	});

  $('.play-2').magnificPopup({
    disableOn: 700,
    type: 'iframe',
    mainClass: 'mfp-fade',
    removalDelay: 160,
    preloader: false,
    fixedContentPos: false
  });



//=====================================================
//======================== COUNTER=====================
//=====================================================

    $('.counter').counterUp({
        delay: 20,
        time: 1000
    });

//=====================================================
//=================== Scroll to top====================
//=====================================================

$(window).scroll(function() {
   if ($(this).scrollTop() > 200) {
      $('#go-to-top a').fadeIn('slow');
      } else {
      $('#go-to-top a').fadeOut('slow');
    }
});


$('#go-to-top a').on( "click",function(){
  $("html,body").animate({ scrollTop: 0 }, 750);
  return false;
});

//====================================
var inputBox = $('.form-control');

inputBox.on('focus', function() {
   $(this).closest('.form-group').addClass('active');
});

inputBox.on('blur', function() {
   if( $(this).val() === "" ) {
      $(this).closest('.form-group').removeClass('active');
   }
});


//=====================================================
//================= SmoothSroll========================
//=====================================================

var scrollAnimationTime = 1200,
   scrollAnimation = 'easeInOutExpo';
$('a.scrollto').bind('click.smoothscroll', function (event) {
   event.preventDefault();
   var target = this.hash;
   $('html, body').stop().animate({
       'scrollTop': $(target).offset().top
   }, scrollAnimationTime, scrollAnimation, function () {
       window.location.hash = target;
   });
});

//=====================================================
//================banner window fit ===================
//=====================================================

if ( matchMedia( "(min-width: 769px) and (max-height: 700px)" ).matches ) {
  var height = $(window).height();

  $('.banner').css('height', height + 'px');
  $('.banner .banner-img').css('height', height + 'px');
}


 var height = $(window).height();
  $('.banner.video-bg').css('height', height + 'px');


//====================================================
//=====================  STELLAR =====================
//====================================================


$(window).stellar({
  horizontalScrolling: false
});


//========================================================
//====================== Placeholder======================
//========================================================

$(function() {
    // Invoke the plugin
    $('input, textarea').placeholder();
});




 // --------------Newsletter-----------------------

	$(".newsletter-signup").ajaxChimp({
		callback: mailchimpResponse,
		url: "http://codepassenger.us10.list-manage.com/subscribe/post?u=6b2e008d85f125cf2eb2b40e9&id=6083876991" // Replace your mailchimp post url inside double quote "".
	});

	function mailchimpResponse(resp) {
		 if(resp.result === 'success') {

			$('.newsletter-success').html(resp.msg).fadeIn().delay(3000).fadeOut();

		} else if(resp.result === 'error') {
			$('.newsletter-error').html(resp.msg).fadeIn().delay(3000).fadeOut();
		}
	};



  // --------------Contact Form Ajax request-----------------------

    $('.contact_form').on('submit', function(event){
    event.preventDefault();

    // $this = $(this);

    var data = {
      name: $('#name').val(),
      phone: $('#phone').val(),
      email: $('#email').val(),
      // subject: $('#subject').val(),
      message: $('#message').val()
    };

    $.ajax({
      type: "POST",
      url: "/",
      data: data,
      success: function(msg){
	     $('.contact-success').fadeIn().delay(3000).fadeOut();
      }
    });
  });





//=================================
//===  IE10 ON WINDOWS 8 FIX    ====
//===================================


if (navigator.userAgent.match(/IEMobile\/10\.0/)) {
  var msViewportStyle = document.createElement('style')
  msViewportStyle.appendChild(
    document.createTextNode(
      '@-ms-viewport{width:auto!important}'
    )
  )
  document.querySelector('head').appendChild(msViewportStyle)
}

/*========================================
=        Swipe menu for circles          =
========================================*/

    $('.horizon-swiper').horizonSwiper();



/*=============================================
=            navigate using button            =
=============================================*/

    $('.navigate-me').on('click',function(){
      window.location = $(this).data('href');
    });




});
