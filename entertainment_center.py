import media
import fresh_tomatoes

# Instances of the Movie class defined in media.py
toy_story = media.Movie("Toy Story","A story of a boy and his toys","http://images.m-magazine.com/uploads/posts/image/46533/toy-story-hotel.jpg","https://www.youtube.com/watch?v=vwyZH85NQC4")
avatar = media.Movie("Avatar","A story of an avatar and a tree","https://www.movieposter.com/posters/archive/main/98/MPW-49246","http://www.youtube.com/watch?v=8KAtG68bIUc")
there_will_be_blood = media.Movie("There Will Be Blood","A story of family, religion, hatred, oil and madness, focusing on a turn-of-the-century prospector in the early days of the business.","http://ia.media-imdb.com/images/M/MV5BMjAxODQ4MDU5NV5BMl5BanBnXkFtZTcwMDU4MjU1MQ@@._V1_.jpg","https://www.youtube.com/watch?v=f3THVbr4hlY")
fargo = media.Movie("Fargo","Jerry Lundegaard's inept crime falls apart due to his and his henchmen's bungling and the persistent police work of the quite pregnant Marge Gunderson.","https://upload.wikimedia.org/wikipedia/en/a/ac/Fargo.jpg","https://www.youtube.com/watch?v=EB4PmbfG4bw")
argo = media.Movie("Argo","Acting under the cover of a Hollywood producer scouting a location for a science fiction film, a CIA agent launches a dangerous operation to rescue six Americans in Tehran during the U.S. hostage crisis in Iran in 1980.","http://ia.media-imdb.com/images/M/MV5BMTc3MjI0MjM0NF5BMl5BanBnXkFtZTcwMTYxMTQ1OA@@._V1_SY1000_CR0,0,675,1000_AL_.jpg","https://www.youtube.com/watch?v=w918Eh3fij0")
annie_hall = media.Movie("Annie Hall","Neurotic New York comedian Alvy Singer falls in love with the ditzy Annie Hall.","http://ia.media-imdb.com/images/M/MV5BMTU1NDM2MjkwM15BMl5BanBnXkFtZTcwODU3OTYwNA@@._V1_SY1000_CR0,0,666,1000_AL_.jpg","https://www.youtube.com/watch?v=TBzHphcc2Jw")

movies = [toy_story, avatar, there_will_be_blood, fargo, argo, annie_hall]

# this line uses the webbrowser module which we have access to
# because we imported media.py in this file
# and media.py imported webbbrowser
fresh_tomatoes.open_movies_page(movies)


