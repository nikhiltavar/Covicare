(function ($) {
	"use strict";

	// Preloader
	function preloader() {
		if ($(".preloader").length) {
			$(window).on("load", function () {
				$(".preloader").fadeOut();
				$(".preloader").delay(50).fadeOut("slow");
			});
		}
	}
	preloader();

	// Shop Detail Page add quantity
	function shop_quantity() {
		$(document).ready(function () {
			$(".ms-minus").on("click", function () {
				var $input = $(this).parent().find("input");
				var count = parseInt($input.val()) - 1;
				count = count < 1 ? 1 : count;
				$input.val(count);
				$input.change();
				return false;
			});
			$(".ms-plus").on("click", function () {
				var $input = $(this).parent().find("input");
				$input.val(parseInt($input.val()) + 1);
				$input.change();
				return false;
			});
		});
	}
	shop_quantity();

	// Owl Carousel
    function ms_three_blog_carousel() {
		$('#ms_three_blog').owlCarousel({
			navText: [
				"<div class='nav-btn prev-slide'></div>",
				"<div class='nav-btn next-slide'></div>",
			],
			loop:true,
			margin:30,
			dots:false,
			nav:true,
			autoplay: 500,
			smartSpeed: 1000,
			responsive:{
				0:{
					items:1
				},
				600:{
					items:2
				},
				1000:{
					items:2
				}
			}
		});
	 }
	 ms_three_blog_carousel();

	// Testimonial Accordions
	function testimonial_carousel() {
		$(".owl-carousel").owlCarousel({
			navText: [
				"<div class='nav-btn prev-slide'></div>",
				"<div class='nav-btn next-slide'></div>",
			],
			loop: true,
			margin: 10,
			nav: true,
			dots: false,
			responsive: {
				0: {
					items: 1,
				},
				600: {
					items: 1,
				},
				1000: {
					items: 1,
				},
			},
		});
	}
	testimonial_carousel();

	// Counters
	function counter() {
		var a = 0;
		$(window).scroll(function () {
			var oTop = $("#counter").offset().top - window.innerHeight;
			if (a == 0 && $(window).scrollTop() > oTop) {
				$(".counter-value").each(function () {
					var $this = $(this),
						countTo = $this.attr("data-count");
					$({
						countNum: $this.text(),
					}).animate(
						{
							countNum: countTo,
						},

						{
							duration: 2000,
							easing: "swing",
							step: function () {
								$this.text(Math.floor(this.countNum));
							},
							complete: function () {
								$this.text(this.countNum);
								//alert('finished');
							},
						}
					);
				});
				a = 1;
			}
		});
	}
	counter();

	

})(jQuery);
