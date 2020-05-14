// fetch a url and insert in DIV#hello

$.ajax({
  type: 'GET',
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  success: function (response) {
    $('div#hello').text(response.hello);
  }
});
