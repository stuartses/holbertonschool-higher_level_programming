/* updates the text color of the HTML tag HEADER
   when the user clicks on the tag DIV#red_header
*/

$('#red_header').click(function () {
  $('header').css('color', '#FF0000');
});
