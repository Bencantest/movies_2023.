

import random
#create a heirachy of class
class HorrorMovies:
    def __init__(self):
        self.movie_name = ""
        self.movie_rate = 0.0

     # pass the variable name as an argument when calling the getdata function

    def personal_details(self):  # personal details will verify the user
        Name = str(input("Enter name: "))
        print("\n")
        print("Parental guidance is a necessity")
        Age = int(input("Enter your Age: "))

        if Age < 16:  #
            print("Sorry, " + Name + ", we cannot accept you.")
            return
        "\n"

        print("Welcome, " + Name + "! You can enter a horror movie.\n")
        self.getdata(Name)
        #this allows getdata to fetch the details in the personal_details function

    def getdata(self, Name):
        self.movie_name = str(input("Enter a horror movie: "))
        print("\n")
        self.movie_rate = float(input("What was the approximate rating: "))

        if 2 <= self.movie_rate <= 4.9:#if rate >= but <=4.9

            #dictionary with key:values of movie:rate
            h_movies = {
                'The devil come at night': 4.0,
                'Pollen': 4.5,
                'Black demon': 4.1,
                'Night stalker': 3.9,
                'Fangs out': 2.4,
                'Motion detected': 3.4,
                'Caviar': 2.9,
                'My house': 3.6,
                'Marry Fuck Kill': 3.6,
                'Dark lullabies': 3.7,
                'House of inequity': 3.7,
                'Third saturday in October': 4.3,
                'Tank': 4.6,
                'Fear': 3.5,
                'Sound of silence': 4.1,
                'Pillow party massacre': 3.2,
                'Human Resources': 4.3,
                'Arctic Void': 4.7,
                'In the Forest': 3.7,
                'Exploited': 4.1,
                'The Huntress of Auschwitz': 3.1,
                'Followers': 3.3
            }

            suggested_movies = [movie for movie, rating in h_movies.items() if
                                rating >= self.movie_rate and rating <= 4.9]
            if suggested_movies:
                random_movies = random.sample(suggested_movies, 2 )
                print("Randomly predicted a horror movie with an IMDB rating of", self.movie_rate, "or higher:")
                # use a for loop to predict a movie from the dict and its rate along side
                # prints both the key and value of prediction
                for movie in random_movies:
                    print(f"{movie} >>> Rate : {h_movies[movie]}")
            else:
                print("No horror movies found for the given rating range.")
        elif 5 <= self.movie_rate <= 6.4:
            h_movies = {
                'The boogeyman': 6.3, 'Dark nature': 5.9, 'Stay out of the basement': 5.3,
                'Malum':5.9, 'Heusera':6.1, 'Creature': 6.4, 'Renfield': 6.4,
                'The popes exorcist': 6.1, 'From black': 5, 'Clock': 5, 'The elderly': 5.4,
                'Envys men': 5.9, 'You are killing me': 6, 'Minera': 5.4, 'Kids vs Aliens': 5.2,
                'Phenomena': 5.3, 'Rippers revenge': 5.3, 'family dinner': 5.7, 'Tinnitus': 5.5,
                'Consecration': 5.1, 'Unseen': 5.6, 'Unwelcome': 5, 'Spoonful of sugar': 5,
                'Knock at the cabin': 6.1, 'Infinity pool': 6.1
            }

            suggested_movies = [movie for movie, rating in h_movies.items() if
                                rating >= self.movie_rate and rating <= 6.4]
            if suggested_movies:
                random_movies = random.sample(suggested_movies, 4)
                print("Randomly predicted a horror movie with an IMDB rating of", self.movie_rate, "or higher:")
                for movie in random_movies:
                    print(f"{movie} >>> Rate : {h_movies[movie]}")
            else:
                print("No horror movies found for the given rating range.")
        elif 6.5 <= self.movie_rate <= 10:
            print("Dear" +Name+" we will list of movies whose rates are within 6.5 and 10 as per IMDB \n")
            h_movies = {
                'Smoking causes coughing': 6.5,
                'Razzennest': 6.5, 'Nefarious': 6.6,
                'Scream VI': 6.6, 'wolf garden': 6.9,
                'Tin and Tina': 6.6, 'The pale blue eye': 6.6,
                'Evil dead rise':6.8
            }

            suggested_movies = [movie for movie, rating in h_movies.items() if
                                rating >= self.movie_rate and rating <= 10]

            if suggested_movies:
                random_movies = random.sample(suggested_movies, 2)
                print("Randomly predicted a horror movie with an IMDB rating of", self.movie_rate, "or higher:")
                for movie in random_movies:
                    print(f"{movie} >>> Rate : {h_movies[movie]}")
            else:
                print("No horror movies found for the given rating range.\n"
                      "Kindly try a lower rate")


    def putdata(self):
        print("Movie that has been watched:", self.movie_name)
        print("Movie rate:", str(self.movie_rate))


# create another class for ACtion movies
# AS  at 6/10/2023 there are 128 action movies that have been produced
#this is based on our source of data

class Actionmovies:
    def __init__(self):
        self.movie_name = ""
        self.movie_rate = 0.0

    def personal_details(self):
        name = str(input("Enter name: "))
        print("\n")
        print("Parental guidance is a necessity")

        year = 2023
        year_of_birth = int(input("Please fill (e.g. 1996): "))
        age = year - year_of_birth

        while True:
            input_age = int(input("Enter your Age: "))
            if input_age == age:
                print("You're honest! Your age matches with the year of birth.")
                break
            else:
                print("Your age does not match with the year of birth. Please try again.")

        print("\n")
        print("Name:", name)
        print("Age:", age)
        self.getdata(name)

    def getdata(self, name):
        self.movie_name = str(input("Enter Action Movie watched:"))
        print('\n')
        self.movie_rate = float(input("What was the rating:"))

        if 0<= self.movie_rate <=5:
            print('\n')
            print(" This are the action movies with rate 0-5 as per IMDB \n ")

            #create a dict containing the movies and thir rate
            action_movies = {
                'Black lotus': 4.2, 'The bestman': 3.8,
                'Knights of the zodiac': 4.6, 'Come ou fighting': 3.6,
                'Transmutators': 2.1,
                'Firenado': 4.8, 'one ranger':4.7,
                'Mexican Connection': 3.3,
                'Snag':4.1, 'Assassin Club': 4.6,
                'The Tomorrow Job':4.7,
                'Breakout':4.2, 'Peter Pan & Wendy': 4.1,
                'Assassin': 3.1, 'The Siege': 3.4,
                'Gunfight at Rio Bravo': 4.3,
                'The Stalking Fields': 3.1,
                'Johnny & Clyde': 3.4,
                'Righteous Thieves': 4,
                'Sayen': 4.5, 'The Weapon': 2.4,
                'Ambush': 4.1, 'Condors Nest': 4,
                'Little Dixie': 4.9,
                'The Locksmith': 4.8,
                'Night Train': 3.6, 'Detective Knight: Independence': 3.4,
                'Imani': 3.3, 'Black Warrant': 4.5,
                'Transfusion': 5, 'Almighty Zeus': 4.8,
                'Bullet Train Down': 3.2,
                'Guardians of Time': 3.5,
                'Operation Seawolf': 3.3, 'Sky High': 4.4

            }
            predict_movies = [ movie for movie, rating in action_movies.items()if rating >= self.movie_rate and rating <= 5]
            if predict_movies:
                random_movies = random.sample(predict_movies, 1)
                print(" prediction of a movie with the rate", self.movie_rate, "and above")

                #use a for loop to predict a movie from the dict and its rate along side
                #prints both the key and value of prediction
                for movie in random_movies:
                    print(f"{movie} >>> IMDB:{action_movies[movie]}")

            else:
                print(" No action with such rating.")


        elif 5<= self.movie_rate <= 6.5:
            action_movies = {
                'Fast X': 6.3, 'Ride on': 6.5, 'Mercy':6.3,
                'Father & Soldier': 5.8, 'Teen Wolf: The Movie': 5.5,
                'Kandahar': 6.2, 'Hypotonic':5.6, 'Mothers day': 5.2,
                'To catch a killer': 6.6, 'The rush call': 5.6,
                'Crossfire': 5.5, 'The mother': 5.5, 'Dead shot':5.5,
                'Bear man': 5.5, 'Mafia Mamma': 5.3,
                'Ghosted': 5.8, 'Chupa': 5.5,
                'Ant-Man and the Wasp: Quantumania': 6.2,
                'Butch Cassidy and the Wild Bunch': 5,
                'One Day as a Lion': 5.2, '65': 5.4,
                'Shazam! Fury of the Gods': 6,
                'Murder Mystery 2': 5.7, 'Bad City': 6,
                'The Match-Stick Flame 2: Lunada Bay': 5.4,
                'Operation Fortune': 6.3,
                'The Point Men': 6, 'Among the Beasts': 6.5,
                'plane': 6.5, 'Shotgun Wedding': 5.4, 'Jung_E': 5.4,
                'The Old Way': 5.4, 'Sky High': 5.6,
                'Dragonheart: Battle for the Heartfire': 5.3

            }
            predict_movies = [ movie for movie, rating in action_movies.items()if rating >= self.movie_rate and rating <= 6.5]
            if predict_movies:
                random_movies = random.sample( predict_movies, 2)
                print("prediction of a movie with the rate", self.movie_rate, "and above")
                for movie in random_movies:
                    print(f"{movie} >>> IMDB:{action_movies[movie]}")

            else:
                print(" sorry" + name + ", there is no action movie with such a rating ")
        elif 6.6 <= self.movie_rate <= 7.5:
            action_movies = {
                'Transformers rise of beasts': 6.6,
                'AKA': 6.6, 'SISU': 7.0, 'Rhino': 6.6,
                'The last kingdom':6.9,
                'Dungeons & Dragons': 7.4,
                'The wandering earth II': 7.1,
                'Polite society': 6.8, 'New Gods: Yang Jian': 6.6,
                'Kill Boksoon': 6.6,
                'Mortal Kombat Legends: Snow Blind': 6.6
            }
            predict_movies = [ movie for movie, rating in action_movies.items() if rating >= self.movie_rate and rating <= 7.5]
            if predict_movies:
                random_movies = random.sample(predict_movies, 2)
                print("prediction of a movie with the rate", self.movie_rate, " and above")
                for movie in random_movies:
                    print(f"{movie} >>> IMDB:{action_movies[movie]}")

            else:
                print(" sorry" + name + ", there is no action movie with such a rating ")

        elif 7.6 <= self.movie_rate <= 10:
            action_movies = {
                'Blood and Gold': 8.2,
                'Guy Ritchies the covenant': 7.6,
                'The fist of condor': 7.8,
                'John wick 4': 8.1,
                'Guardians of the Galaxy 3': 8.3,
                'Spider-man Across the spider-verse': 9.1

            }
            predict_movie = [movie for movie, rating in action_movies.items()if rating >= self.movie_rate and rating <= 10]
            if predict_movie:
                random_movie = random.sample( predict_movie, 1)
                print(" Action movie with the rate", self.movie_rate, " and above")
                for movie in random_movie:
                    print(f"{movie} >>> IMDB:{action_movies[movie]}")

            else:
                print(" sorry" + name + ", there is no action movie with such a rating ")

    def putdata(self):
        print("Movie that has been watched:", self.movie_name)
        print("Movie rate:", str(self.movie_rate))

def Movies():
    print("WHICH GENRE OF MOVIES ARE YOU INTERESTED IN? \n"
          "1. Horror \n"
          "2. Action \n")
    #create a dictionary that maps to the available classes i.e Horrormovies and Actionmovies

    genre_classes = {
        '1': HorrorMovies,
        '2': Actionmovies
    }

    #ask user for genre of interest
    genre_select = input("Enter genre Number:")
    Genre_select = int(genre_select)
    if Genre_select == 1:
        a= HorrorMovies()
        a.personal_details()
        a.putdata()
    elif Genre_select == 2:
        b = Actionmovies()
        b.personal_details()
        b.putdata()


Movies()
