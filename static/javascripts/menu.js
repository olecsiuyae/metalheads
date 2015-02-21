var main = function() {
  $('.icon-menu').click(function() {
    $('.header').animate({
      top: "0px"
    }, 200);
  });

  $('#page-wrap').click(function() {
    $('.header').animate({
      top: "-50px"
    }, 200);
  });
};


$(document).ready(main);