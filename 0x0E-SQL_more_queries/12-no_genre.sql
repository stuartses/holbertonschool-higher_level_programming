-- Retrieve data from to relationed by id
-- List tv_shows and genres with a LEFT JOIN where NULL is found
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id WHERE tv_show_genres.show_id is NULL ORDER BY tv_shows.title, tv_show_genres.genre_id;
