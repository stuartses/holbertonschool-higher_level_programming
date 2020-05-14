// toggle class on click in DIV#toggle_header

$('div#toggle_header').click(function () {
  $('header').toggleClass('green');
  $('header').toggleClass('red');
});
