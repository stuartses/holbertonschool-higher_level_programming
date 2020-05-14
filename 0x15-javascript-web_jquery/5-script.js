// toggle LI element on click in DIV#add_item

$('div#add_item').click(function () {
  $('ul.my_list').append('<li>Item</li>');
});
