from MovieClass import Customer
import os 

customers_List = []
movies = []


#Checks if the customers list been created or not then one needs to be created to store customers data in the customer.txt file 
def readfile():
    if os.path.exists("customer.txt"):
        with open("customer.txt" , "r") as file:
            lines = file.readlines()
            #loops througn the customers data 
            for line in lines:
                lineData = line.strip().split(",")
                name = lineData[0]
                email = lineData[1]
                movies = lineData[2].split(",")
                fines = float(lineData[3])

                customers_List.append(Customer(name ,email, movies, fines))

        for c in customers_List:
                    print(f"{c.customername}, {c.customerEmail}, Movies:{c.customerMoviesrented}, fines:{c.customerfinesowed:.2f}")

    print("Total customers loaded:" , len(customers_List))


#Reads data from the movies.txt file
def load_movies(filename="Movies.txt"):
    try:
        with open(filename , "r") as f:
            return[line.strip() for line in f if line.strip()]
    except:
        print("Movies.txt not found")
        return []
    
#Displays the movie that the customers has rented 
def rent_movie():
    name = input("Enter your name: ")
    movie = input("Enter a movie to rent: ")

    for c in customers_List:
        if c.customername == name :
            c.customermoviesrented.append(movie)
            print(f"{name} rented {movie}")
            return
    print("Customer not found.Please add customer first")

#Add the customers information
def add_customer():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    new_customer = Customer(name,email, [], 0.0)
    customers_List.append(new_customer)

    with open("customer.txt", "a") as file:
        file.write(f"{name}, {email},,0.0\n")

    print(f"Customer {new_customer.customername}added succesfully")

def display_customers():
    name = input("Enter your name: ")
    movie = input("Enter a movie to return: ")

    for c in customers_List:
        if movie in c.customermoviesrented:
            c.customermoviesrented.remove(movie)
            print(f"{name} returned {movie}") 

             #asks the customers if the mvoie was returnted late if so yes/no and checks if the customers has outstanding fines
            late = input("Was the movie returned late yes/no: ")
            if late == "yes":
                days_late = int(input("Enter the number of days late: "))
                fine = days_late *5
                c.customerfinesowed += fine
                print(f"fines of {fine} added to {name} account")
                return
            else:
                print(f"{name} did not rent {movie}")
                return
        print("Customer not found.Add customer ")

#Checks if the customer has outstanding rentels or not 
def viewoutstanding_rentels():
    if not customers_List:
        print("No customer found")
        return

    for c in customers_List:
        if c.customermoviesrented:
            print(f"{c.customername} has rented the movie")
        else:
            print(f"{c.customername} has no outstanding rentels")

#checks if the customer owes or not 
def viewoutstanding_fines():
    if not customers_List:
        print("Customer not found")
        return

    for c in customers_List:
        if c.customerfinesowed:
            print(f"{c.customername} owes {c.customerfinesowed} in fines")
        else:
            print(f"{c.customername} has no outstanding finesowed ")

#Checks customers fines and tell them how much to pay if they outstanding fines
def pay_fines():
    name = input("Enter your name: ")
    amount = float(input("Enter amount to pay: "))

    for c in customers_List:
        if c.customername == name:
            c.customerfinesowed -= amount
            if c.customerfinesowed < 0:
                c.customerfinesowed = 0
                print(f"{name} payed {amount} and Remaining fines: {c.customerfinesowed}")
                save_customers()
                return
            
    print("Customer not found")

#saves the customers information to the customer.txt 
def save_customers():
    with open("customer.txt", "w") as file:
        for c in customers_List:
            movies = ",".join(c.customermoviesrented)
            fines = c.customerfinesowed
            file.write(f"{c.customername},{c.customeremail},{movies},{fines}\n")



#Main menu loop to run continously until users chooses to exit
def main():

    global movies
    movies = load_movies()

    while True:
        print("\n Movie Rental Menu \n"
              "1.Rent Movie \n"
              "2.Add Customer \n"
              "3.Return Movie \n"
              "4.View Outstanding Rentals \n"
              "5.View Outstanding fines \n"
              "6.Pay fines \n"
              "0.close application")

        user_choice = input("Select a option: ")

        if user_choice == "1":
            rent_movie()
        elif user_choice == "2":
            add_customer()
        elif user_choice == "3":
            display_customers()
        elif user_choice == "4":
            viewoutstanding_rentels()
        elif user_choice == "5":
            viewoutstanding_fines()
        elif user_choice == "6":
            pay_fines()
        elif user_choice == "0":
            save_customers()
            print("Closing application")
            break
        else:
            print("Invalid input")

print(main())
            
