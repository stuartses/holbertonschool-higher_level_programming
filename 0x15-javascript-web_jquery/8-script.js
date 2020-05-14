// fetch a url and insert in UL#list_movies

$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  success: function (response) {
    const movies = response.results;
    for (let i = 0; i < movies.length; i++) {
      $('#list_movies').append('<li>' + movies[i].title + '</li>');
    }
  }
});
