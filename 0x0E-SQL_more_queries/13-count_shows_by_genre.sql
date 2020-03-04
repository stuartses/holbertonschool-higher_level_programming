-- Retrieves count of genres found with tv shows
-- List the genres that has show and counts
SELECT tv_genres.name, COUNT(tv_show_genres.genre_id) AS 'number_of_shows' FROM tv_genres, tv_show_genres WHERE tv_genres.id = tv_show_genres.genre_id GROUP BY tv_genres.id ORDER BY number_of_shows DESC;
