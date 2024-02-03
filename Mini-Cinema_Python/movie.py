class Hours:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        
    def __str__(self):
        return f"{self.start_time} - {self.end_time}"

class Movie:
    def __init__(self,name, director, year, genre, duration, imdb, hours, price):
        self.name = name
        self.director = director
        self.year = year
        self.genre = genre
        self.duration = duration
        self.imdb = imdb
        self.hours = hours
        self.price = price
        
    def show_info(self):
        return"""
Which movie would you like to watch?
1. Dune
2. No Time to Die
3. Spider-Man: No Way Home
4. Shang-Chi and the Legend of the Ten Rings
5. A Quiet Place Part II
"""

    def hoursM(self, session):
        counter = 1
        for i in session:
            print(f"{counter}) {i}",end="")
            print("")
            counter += 1
    
    def year_info(self,year):
        return "Old Category" if int(year) < 2000 else "New Category"
    
    def duration_info(self,durationVal):
        return "Short movie" if int(durationVal) < 120 else "Long movie"
    
    def rating_info(self, ratingVal):
        i = int(ratingVal)
        if   i < 6: return "E"
        elif i < 7: return "D"
        elif i < 8: return "C"
        elif i < 9: return "B"
        elif i <= 10: return "A"                    