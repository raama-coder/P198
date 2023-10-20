while True:
  total = 0
  customer_Name = input("Enter your name: ")
  
  while True:
    quantity = int(input("Enter Quantity of items:"))
    items = int(input("Enter Number of items:"))
    total = quantity*items
    repeat = input("Do you want to add more items(y/Y/n/N): ")
    
    if repeat=='n' or repeat=='N':
      break
    
    print("_"*50)
    print("Name: ",customer_Name)
    print("Total Cost: ",total)
    print()
    print("Thank you for shopping with us!")
    print("_"*50)
    
    new_customer = input("Go to Next Customer(y/Y/n/N)")
    
    if new_customer=='n' or new_customer=='N':
      break