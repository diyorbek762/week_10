def build_sales_log(sales_list):
    result_dictionary={}
    # Logic: Loop through the list, clean the data, 
    for employee in sales_list:
        splitted_list=employee.split("|")
        employeeID, item_name, price=splitted_list
        if employeeID not in result_dictionary:
           result_dictionary[employeeID]=float(price)
        else:
            result_dictionary[employeeID]=(result_dictionary[employeeID])+float(price)    
    highest_sale=0
    best_salesman=''
    for each_employee, individual_sales in result_dictionary.items():
        if highest_sale<individual_sales:
            highest_sale=individual_sales
            best_salesman=each_employee
    print('Sales Report:')
    for each_ID, sales_amount in result_dictionary.items():
        print(f"{each_ID}: ${sales_amount:.2f}")
    print("-"*20)
    print(f"Top Performer is {best_salesman} with ${highest_sale:.2f}")

    


            



    
    # and build a dictionary where:
# Key: EmployeeID (String)
# Value: A running Total Sum (Float) of their sales. 
# (Note: Unlike Variant 1, you are summing immediately, not storing a list).
sales_list = [
    "E101|Laptop|1200.00",
    "E102|Mouse|25.50",
    "E101|Monitor|300.00",
    "E103|Headphones|150.00",
    "E102|Keyboard|50.00",
    "E103|Laptop|1000.00",
    "E101|Mousepad|15.00"
]
build_sales_log(sales_list)

# Sales Report:
# E101: $1515.00
# E102: $75.50
# E103: $1150.00
# --------------------
# Top Performer is E101 with $1515.00