import CreateClass

movies = ["Return of The Liviing Dead", "Upgrade", "Who Framed Roger Rabbit"]
games = ["Bioshock", "Xcom 2", "Dead Space"]

myCollection = CreateClass.Collection(movies, games)

myCollection.SetFavGame("Xcom 2")
myCollection.SetFavMovie("Upgrade")
myCollection.DisplayColletion()