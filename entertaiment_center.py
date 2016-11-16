import media
import fresh_tomatoes
# pylint: disable=C0103


toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")


dr_strange = media.Movie("Doctor Strange",
                         "A former neurosurgeon embarks on a journey"
                         "of healing only to be drawn into the world of the mystic arts.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMjM2ODA4MTM0M15BMl5BanBnXkFtZTgwNzE5OTYxMDI@._V1_SY1000_CR0,0,683,1000_AL_.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=HSzx-zryEgM")

inception = media.Movie("Inception",
                        "A thief, who steals corporate secrets through use of dream-sharing technology,"
                        "is given the inverse task of planting"
                        "an idea into the mind of a CEO.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

arrival = media.Movie("Arrival",
                      "A linguist is recruited by the military"
                      "to assist in translating alien communications.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTExMzU0ODcxNDheQTJeQWpwZ15BbWU4MDE1OTI4MzAy._V1_SY1000_CR0,0,640,1000_AL_.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=rNciXGzYZms")

madagascar = media.Movie("Madagascar",
                         "Spoiled by their upbringing with no idea what wild life is really"
                         "like, four animals from New York Central Zoo escape, unwittingly"
                         "assisted by four absconding penguins, and find themselves in"
                         "Madagascar, among a bunch of merry lemurs.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BN2I5YzFlYWEtZjRhNy00ZmQzLWJhNTktZGIwYjFjODdmNDgxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,666,1000_AL_.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=dm-eiFVtRws")

iron_man = media.Movie("Iron Man 3",
                       "When Tony Stark's world is torn apart by a formidable"
                       "terrorist called the Mandarin,"
                       "he starts an odyssey of rebuilding and retribution.",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkzMjEzMjY1M15BMl5BanBnXkFtZTcwNTMxOTYyOQ@@._V1_SY1000_SX700_AL_.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=YLorLVa95Xo")

movies = [toy_story, dr_strange, inception, arrival, madagascar, iron_man]

fresh_tomatoes.open_movies_page(movies)





