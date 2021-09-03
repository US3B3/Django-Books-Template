//  course section owl carousel
$(".course_owl-carousel").owlCarousel({
    autoplay: true,
    loop: true,
    margin: 5,
    autoHeight: true,
    nav: true,
    navText: ['<i class="fa fa-angle-left" aria-hidden="true"></i>', '<i class="fa fa-angle-right" aria-hidden="true"></i>'],
    autoWidth: true
});

// google_map js 
function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(40.712775, -74.005973),
        zoom: 18,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}

// fancybox
$(document).ready(function() {
    $('.fancybox').fancybox({
      padding   : 0,
      maxWidth  : '100%',
      maxHeight : '100%',
      width   : 560,
      height    : 315,
      autoSize  : true,
      closeClick  : true,
      openEffect  : 'elastic',
      closeEffect : 'elastic'
    });
  });

// tepeye dön
var mybutton = document.getElementById("myBtn");
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

// fotogaleri
function onClick(element) {
    document.getElementById("img01").src = element.src;
    document.getElementById("modal01").style.display = "block";
    var captionText = document.getElementById("caption");
    captionText.innerHTML = element.alt;
  }

