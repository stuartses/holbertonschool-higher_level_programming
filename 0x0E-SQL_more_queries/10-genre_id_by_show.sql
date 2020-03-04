-- List data from to relationed by id
-- List tv_shows.title if is found in tv_show_genres and sort bu title and genre_id
SELECT tv_shows.title, genre_id FROM tv_shows, tv_show_genres WHERE tv_show_genres.show_id = tv_shows.id ORDER BY tv_shows.title, tv_show_genres.genre_id;
