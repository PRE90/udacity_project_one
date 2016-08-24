import media
import fresh_tomatoes

# Instances of the Movie class defined in media.py
le_grand_bleu = media.Movie("Le Grand Bleu",
                            "The rivalry between Enzo and Jacques, two "
                            "childhood friends and now world-renowned free "
                            "divers, becomes a beautiful and perilous journey "
                            "into oneself and the unknown.",
                            "https://upload.wikimedia.org/wikipedia/en/c/c5/"
                            "Big_Blue_poster_200px.jpg",
                            "https://www.youtube.com/watch?v=pvU_qqOnlAM")
holy_motors = media.Movie("Holy Motors",
                          "From dawn to dusk, a few hours in the shadowy life "
                          "of a mystic man named Monsieur Oscar.",
                          "http://t2.gstatic.com/images?q=tbn:ANd9GcRlkTqFs"
                          "HBVJu0msk0ac-YeTywm7arTvBhkUSeYy_tuXTHdqoSh",
                          "https://www.youtube.com/watch?v=NWu9WjEcdbk")
there_will_be_blood = media.Movie("There Will Be Blood",
                                  "A story of family, religion, hatred, oil and"
                                  " madness, focusing on a turn-of-the-century "
                                  "prospector in the early days of the "
                                  "business.",
                                  "http://ia.media-imdb.com/images/M/MV5BMjAxOD"
                                  "Q4MDU5NV5BMl5BanBnXkFtZTcwMDU4MjU1MQ@@._V1_"
                                  ".jpg",
                                  "https://www.youtube.com/watch?v=FeSLPELpMeM")
fargo = media.Movie("Fargo",
                    "Jerry Lundegaard's inept crime falls apart due to his and "
                    "his henchmen's bungling and the persistent police work of"
                    " the quite pregnant Marge Gunderson.",
                    "https://upload.wikimedia.org/wikipedia/en/a/ac/Fargo.jpg",
                    "https://www.youtube.com/watch?v=EB4PmbfG4bw")
interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole in "
                           "space in an attempt to ensure humanity's survival.",
                           "http://ia.media-imdb.com/images/M/MV5BMjIxNTU4Mz"
                           "Y4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SY1000_CR0,"
                           "0,640,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")
annie_hall = media.Movie("Annie Hall",
                         "Neurotic New York comedian Alvy Singer falls in love"
                         " with the ditzy Annie Hall.",
                         "http://ia.media-imdb.com/images/M/MV5BMTU1NDM2MjkwM1"
                         "5BMl5BanBnXkFtZTcwODU3OTYwNA@@._V1_SY1000_CR0,0,666,"
                         "1000_AL_.jpg",
                         "https://www.youtube.com/watch?v=TBzHphcc2Jw")

movies = [le_grand_bleu, holy_motors, there_will_be_blood,
          fargo, interstellar, annie_hall]

# this line uses the webbrowser module which we have access to
# because we imported media.py in this file
# and media.py imported webbbrowser
fresh_tomatoes.open_movies_page(movies)


