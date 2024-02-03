from human import *
from mall import *
from movie import *
from money import *

t = """Who will be logged in?
1. Worker
2. Normal Person
Your choice: """

try:
    _whois = int(input(t))
    
    if _whois == 1:
        name = Worker().who_is()
        print(f"Your choice was: {name}")
    elif _whois == 2:
        name = Normal_Person().who_is()
        print(f"Your choice was: {name}")
    else:
        exit("Wrong input")    
except ValueError:
    exit("Enter valid value")         
#whois_end

_Deniz_Mall = Deniz_Mall("Baku",3,9)
_Ganjlik_Mall = Ganjlik_Mall("Baku",4,16)
_Ganja_Mall = Ganja_Mall("Ganja",5,25)
_Mall_28 = Mall_28("Baku",6,36)
_Port_Baku_Mall = Port_Baku_Mall("Baku",4,26)

print("")
print(_Deniz_Mall.info())

try:
    selectMall = int(input("Your choice: "))

    if selectMall == 1:
        _selected_mall_name = "Deniz Mall"
        _selected_mall = _Deniz_Mall
    elif selectMall == 2:
        _selected_mall_name = "Ganjlik Mall"
        _selected_mall = _Ganjlik_Mall
    elif selectMall == 3:
        _selected_mall_name = "Ganja Mall"
        _selected_mall = _Ganja_Mall
    elif selectMall == 4:
        _selected_mall_name = "28 Mall"
        _selected_mall = _Mall_28
    elif selectMall == 5:
        _selected_mall_name = "Port Baku Mall"
        _selected_mall = _Port_Baku_Mall
    else:
        exit("Wrong input")
except ValueError:
    exit("Enter valid value")
    
print("")
print(_selected_mall.working_time())

print("")
y_age = input("Your age: ")
_selected_mall.age(y_age)

print("")
is_vac = input("You vaccinated? default='Active': ")

print("")

print(_selected_mall.vaccination(is_vac))

print(f"""
        Welcome to {_selected_mall_name}
            
        Location: {_selected_mall.location}

        Floor: {_selected_mall.floor}

        Hall Count: {_selected_mall.hall_count}
        """)

session1 = Hours(12,14)        
session2 = Hours(14,16)        
session3 = Hours(16,18) 

Mov1 = Movie("Dune", "Denis Villeneuve", 2021, "Science Fiction, Adventure", "156", 7.5, [session1,session2,session3], "15")
Mov2 = Movie("No Time to Die", "Cary Joji Fukunaga", 2021, "Action, Adventure", "163", 7.5, [session1,session2], "15")
Mov3 = Movie("Spider-Man: No Way Home", "Jon Watts", 2021, "Action, Adventure, Science Fiction", "148", 8.5, [session1,session3], "15")
Mov4 = Movie("Shang-Chi and the Legend of the Ten Rings", "Destin Daniel Cretton", 2021, "Action, Adventure, Fantasy", "132", 7.6, [session1,session3], "15")
Mov5 = Movie("A Quiet Place Part II", "John Krasinski", 2021, "Horror, Thriller", "97", 7.5, [session2,session3], "15")

print(Mov1.show_info())

try:
    ys = int(input("Your selection: "))
    if ys == 1:
        _selected_movie = Mov1
    elif ys == 2:
        _selected_movie = Mov2
    elif ys == 3:
        _selected_movie = Mov3
    elif ys == 4:
        _selected_movie = Mov4
    elif ys == 5:
        _selected_movie = Mov5                    
    else:
        exit("Wrong input")      
except ValueError:
    exit("Enter valid value")

print(f"""
    Name: {_selected_movie.name}
    Director: {_selected_movie.director}
    Year: {_selected_movie.year}
    Genre: {_selected_movie.genre}
    Rating: {_selected_movie.imdb}
    Duration: {_selected_movie.duration}
    Price: {_selected_movie.price} AZN
    """)
print(_selected_movie.year_info(_selected_movie.year))
print(_selected_movie.duration_info(_selected_movie.duration))

print()

print("choice your session")
_selected_movie.hoursM(_selected_movie.hours)
choice_select = int(input("Enter choice: "))
if choice_select == 1:
    _selected_chois = _selected_movie.hours[0]
elif choice_select == 2:
    _selected_chois = _selected_movie.hours[1]    
elif choice_select == 3:
    _selected_chois = _selected_movie.hours[2]
else:
    exit("Wrong input")    

print()

print("Your choice:",_selected_chois)

print()

want_to_buy = input("Do you want to buy a ticket? Yes/No: ")

if want_to_buy != "Yes":
    exit()
    
print()

setMoney = int(input("Enter money: "))

getMoney = Money(setMoney)
print(f"Your current money is {getMoney.get_money()} AZN")

print()

print(getMoney.set_money(_selected_movie.name,_selected_movie.price))