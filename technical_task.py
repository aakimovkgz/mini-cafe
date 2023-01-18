# 1. Create some class (min 5 attributes, min 3 method) (create 5 class objects) all attributes should be private
# 2. Create class and use inheritance (наследования) create sub class
# 3. Use second task`s class for polymorphism.



# Project name
# Mini cafe

# Purpose: Create a solution to change R-keeper to own cafe system

# Cafe
# Employee
# Food
# Menu
# Order
# Receipt


# Cafe
# - id
# - name
# - address
# - phone number
# - work start time
# - work end time
# - work days (1, 2, 3, 4, 5, 6, 7)
# - service percent (default - 0.05 %)
# - status (Work, Unwork, Repair, Cleaning day)
# - is active (True, False)
# - create date
# - update date


# Employee
# - id
# - cafe id
# - Last name
# - First name
# - phone number
# - password
# - date of birth
# - passport id
# - status (Work, Unwork, Sick, Decree, Dismissed, Holiday)
# - is active (True, False)
# - work start date
# - work end date
# - create date
# - update date


# Food
# - id
# - name
# - image
# - description
# - price (10.00)
# - weight (gram)
# - category (First, Second, Candy, Hot drink, Drink, Breakfast, Salad, Snacks)
# - employee id
# - create date
# - update date


# Menu
# - id
# - name
# - [food_id, food_id]
# - start date
# - end date
# - is active (True, False)
# - employee id
# - create date
# - update date


# Order
# - id
# - employee id
# - foods [
#    [food_id, quantity],
#    [food_id, 3]
# ]
# - total
# - cafe id
# - create date
# - update date

# Receipt
# - id
# - order id
# - status (Payed, Unpayed, Rejection, Free)
# - create date
# - update date



# All classes should be in module models.py
# All objects should be store at database.py
# All process should be at views.py
# In main.py collect all logic


# Cafe, Employee, Food, Menu
# - Create
# - Update

# Order, Receipt
# - Create


#######################################################
# ATTENTION id not mutable
# Get order only when cafe is work (id now between cafe start work time and end work time)
# ID it`s autoincrement ID should unique
# EMP_ID = 1
# EMP_ID += 1
#######################################################


# Bussness process
## It s command for client
# 1 Show menu (by categoties)
# 2 Create order
#      get food and quontity
#      after order create show to client order detail
#      after order create automaticly create receipt

## It s command for employee
# 11 Create Employee or update
# 22 Create Food or update
# 33 Create Cafe or update
# 44 Create Menu or update
# 55 Update receipt status (order id)
# 66 break 

# Google help, Internet help
