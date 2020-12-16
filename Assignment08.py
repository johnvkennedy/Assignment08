# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Jack Kennedy,12/12/2020,Adding Code for Assignment):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Jack Kennedy 12/15/2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    # -- Field --
    strProductName = ""

    # -- Constructor --
    def __init__(self, product_name: str, product_price: float):
        # -- Attributes --
        self.__product_name = product_name
        self.__product_price = product_price

    # -- Properties --
    # Product Name = !ONLY CHANGES THE CASE!
    @property
    def product_name(self): # Getter
        return str(self.__product_name).title() # Title Case

    @property
    def product_price(self): # Getter with Error Handling
        try:
            return float(self.__product_price) # No Need for Title
        except:
            raise Exception("! - Error - ! Letter's aren't numerical prices.")

    @product_price.setter
    def product_price(self, value):
        if float(value).isnumeric() == True:
            self.__product_price = value
        else:
            raise Exception("Letter's aren't prices.")

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:

    #Methods

    # Saves current list to the text file
    @staticmethod
    def save_data_to_file():
        objFile = open("products.txt", "a")
        for row in lstOfProductObjects:
            objFile.write(row["Product"] + "," + row["Price"] + "\n")
        objFile.close()
        print("===== The current table has been saved =====\n")

    # Creates a text file if none exists
    @staticmethod
    def create_file_for_data (file_name):
        try:
            objFile = open(file_name,"x")
            objFile.close()
        except:
            print("File Loaded Up - Only Shows if No File")

    # Loads up data in text file
    @staticmethod
    def read_data_from_file(file_name, lstOfProductObjects):
        objFile = open(file_name,"r")
        for row in objFile:
            txtdata = row.split(",")
            dicRow = {"Product": txtdata[0], "Price": txtdata[1].strip()}
            lstOfProductObjects.append(dicRow)
        objFile.close()
        return lstOfProductObjects

    # Displays current data in list
    @staticmethod
    def print_current_data_in_list(lstOfProductObjects):
        print("--------------------------------------------\n"
              "\tThis is the current data in the table.\n"
              "--------------------------------------------\n"
              "==============")
        print("Row - Product - Price")
        counter = 0
        for row in lstOfProductObjects:
            print(f'{counter} | {row["Product"]} | {row["Price"]} |')
            counter += 1
        print("==============")
        return lstOfProductObjects

    # Adds Data to Primary List
    @staticmethod
    def add_data_to_list(product, price, lstOfProductObjects):
        dicRow = {"Product": product, "Price": price}
        lstOfProductObjects.append(dicRow)
        print("\n=====", product, "has been added with priority", price, "=====")

# Presentation (Input/Output)  -------------------------------------------- #

class IO:
    # Greetings
    @staticmethod
    def greetings():
        print("==============================================\n"
              "\t Hello amazing user!\n"
              "\t This script is made to allow you to\n"
              "\t create a list showing a product and\n"
              "\t the price that you put in. The table \n"
              "\t Will always be displayed with the menu.\n\n"
              "\t First it will open the file to keep\n"
              "\t previously existing data then you the\n"
              "\t user may interact with that data.\n\n"
              "\t            !IMPORTANT!\n"
              "\t DATA IS ONLY SAVED WHEN THE OPTION\n"
              "\t       IS CHOSEN IN THE MENU!\n"
              "==============================================")

    # Menu
    @staticmethod
    def print_menu_tasks():
        print("""
                *** Menu of Options ***
                1) Add a new Product
                2) Save Data to File        
                3) Exit Program
                """)

    # Menu Choice
    def input_menu_choice(self):
        choice = str(input("Which option would you like to perform? [1 to 5] - "))
        print()
        return choice

    # Continue Option
    @staticmethod
    def input_press_to_continue(optional_message=''):
        print(optional_message)
        input('Press the [Enter] key to continue.')

    # Yes or No Input
    @staticmethod
    def input_yes_no_choice(message):
        return str(input(message)).strip().lower()

# Main Body of Script
FileProcessor.create_file_for_data("products.txt")
FileProcessor.read_data_from_file("products.txt",lstOfProductObjects)
IO.greetings()
while True:
    FileProcessor.print_current_data_in_list(lstOfProductObjects)
    IO.print_menu_tasks()
    strChoice = IO.input_menu_choice("self")

    if strChoice.strip() == '1':
        getinfo = Product(input("-------------------------------------------------\n"
                                         "\tYou've chosen to add to the current table.\n"
                                         "\tWhat product do you wish to add?\n"
                                         "-------------------------------------------------\n"
                                         "\tEnter New Product: "),
                                input("\n---------------------------------------------------------------\n"
                                         "\tWhat price do you wish to designate to this task?\n"
                                         "\tExamples: 1.99.\n"
                                         "---------------------------------------------------------------\n"
                                         "\tEnter Price for Product: "))
        # User data goes through the constructor and properties
        pdct1 = getinfo.product_name
        price1 = str(getinfo.product_price)
        FileProcessor.add_data_to_list(pdct1,price1,lstOfProductObjects)

    elif strChoice.strip() == '2':
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == 'y':
            FileProcessor.save_data_to_file()
        else:
            IO.input_press_to_continue("Save Cancelled!")

    elif strChoice == '3':  # Exit Program
        print("Goodbye!")
        break  # and Exit