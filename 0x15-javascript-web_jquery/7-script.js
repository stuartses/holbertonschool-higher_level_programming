// fetch a url and insert value in DIV#character

$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  success: function (response) {
    $('div#character').text(response.name);
  }
});
