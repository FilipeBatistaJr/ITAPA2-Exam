#Question 1.3
def main():
    creature = Vertabrate()
    print(creature.msg())
    print(isinstance(creature, Animal))

class Animal:
    def msg(self):
        return("Can Move.")
class Vertabrate:
    def msg(self):
        return("Has a backbone.")
main()
#output will determine whether or nor the animal has a backbone or can move


#Question 1.4
def sum (x, y=10):
    return x + y
print(sum(10))
#output will be 20

#Question 1.5
import copy
from distutils import text_file
from msilib.schema import ListBox
a = ['Ndai', 'Tariro', ['Eunice', 'Doreen']]
b = copy.deepcopy(a)
a is b
#There is no effective output from this code

#Question 2
#the following program allows a user to create an index of names 
#which will allow the user to enter names into the index
#allows the user to search names entered into the index
#change names entered into the index
#has error handling
name_list = []

num_of_names = int(input("How many names will you be adding?: "))

while num_of_names != 0:
    name = input("Enter your name: ")
    name_list.append(name)
    num_of_names -= 1

print(name_list)

search = input("Enter a name to be searched: ")

if search in name_list:
    print (f"{search} found in index {name_list.index(search)}")
    change = input(f"Do you wish to change this name?" ({search}) \n" f"Y/N: ").upper()
    if change == 'Y':
        new_name = input("Enter new name: ")
        name_list[name_list.index(search)] = new_name
        print("Name has been changed.")
        print(name_list)
    elif change == 'N':
        print(name_list)
    else:
        print("Please enter either Y/N.")
else:
    print("Name not found...")

#Question3
#this program opens a txt file with a list of colors on the users PC
#then the user will be prompted to enter a singular letter, e.g; W = White 
#the program will return all the colors associated with the letter entered
def main():
    def display():
        text_file = open("txtFile.txt", "w")
        text_file.close()

        text_file = open("Users/user-pc/Desktop/Colors.txt", "r")
        for color in text_file:
            color_list = []
            color_list.append(color)
        print(color_list)
        text_file.close()
    display()

    def search_color():
        import re
        search = input("Enter a letter: ").upper()
        if len(search) > 1:
            print ("Please enter only one letter.")
            search = input("Enter a letter: ").upper()
        else:
            c_string =''
            color_list = []
            for add in color_list:
                c_string += add 

            pattern = re.compile(f'[{search}]....')
            matches = pattern.findall(c_string)

            for found in matches:
                print(found)
        def results():
            result_list = []
            for found in matches:
                result_list.append(found)
                print(result_list)
            results()
        search_color()
main ()

#Question 4
#program to determine the gcd, greatest common denomitator between two numbers
def fractions(a,b):
    fractions.gcd(a,b)
import fractions

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number: "))

def reduce(a,b):
    if a==b: return 1, 1
    x = max(a,b); y = min(a,b)

    while True:
        x %=y
        
        if x==0: break

        if x < y: temp = x; x = y; y = temp;
        
        return int(a/y), int(b/y)
print("The gcd of {} and {} is {}".format(num1, num2, fractions.gcd(num1, num2)))

#Question 5
#this program will sort students according to which Campus
#they attend
from tkinter import *
from tkinter import messagebox

top = Tk()
top.title("Campus")
top.geometry("300x250")

Person = Listbox(top, height = 10
                 width = 15,
                 bg = "white",
                 activestyle = 'dotbox',
                 font = "Helvetica" ,
                 fg = "black")
Person.insert(1, "Lance Krasner")
Person.insert(2, "Karin Soderlund")
Person.insert(1, "Tess Biscombe")
Person.insert(1, "Annemie Parkin")
Person.insert(1, "Olika Saikoolal")
Person.insert(1, "Kyle Knicklebein")
Person.insert(1, "Karin Sonderlund")
Person.insert(1, "Claris Mhike")
Person.insert(1, "Rafiq Manan")
Person.insert(1, "Anri Pienaar")
Person.insert(1, "Tendai Muzanenhamo")

label = Label(top, text = "Eduvos Campuses")
Campus = Listbox(top, height = 10
                width = 15,
                bg = "white",
                activestyle = 'dotbox',
                font = "Helvetica",
                fg = "black").grid(row=1, coloumn=0, coloumnspan=3)
Campus.insert(1, "Bedfordview")
Campus.insert(2, "Bloemfontein")
Campus.insert(3, "Cape Town Claremont")
Campus.insert(4, "Cape Town Tygarvalley")
Campus.insert(5, "Durban")
Campus.insert(6, "East London")
Campus.insert(7, "Mbombela")
Campus.insert(8, "Midrand")
Campus.insert(9, "Nelson Mandela Bay")
Campus.insert(10, "Potchefstroom")
Campus.insert(11, "Pretoria")

Person.sort()
Campus.sort()

label.pack()
ListBox.pack()
top.mainloop()