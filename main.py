# Hotel Management System Project using Core Python
import re  # email pattern verification module

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # email pattern
upi_pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z]+$' # upi id pattern

class Add_account:
    def __init__(self, name, age, phone, address, email, location):
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address
        self.email = email
        self.location = location

    def view_rooms(self):
        print("------ ROOM TYPES AVAILABLE ------")
        print("1. Single Room         ₹1500/day")
        print("2. Double Room         ₹2500/day")
        print("3. Deluxe Room         ₹3500/day")
        print("4. Super Deluxe Room   ₹4500/day")
        print("5. Executive Suite     ₹7500/day")
        print("6. Presidential Suite  ₹12000/day")
        print("7. Family Room         ₹5000/day")
        print("----------------------------------")


class Booking(Add_account):
    def __init__(self, name, age, phone, address, email, location, room_type, check_in, check_out, total_members, price):
        super().__init__(name, age, phone, address, email, location)
        self.room = room_type
        self.checkin = check_in
        self.checkout = check_out
        self.total = total_members
        self.price = price

    def prints(self):
        print("--------------Your Receipt------------")
        print("Name          : ", self.name)
        print("Age           : ", self.age)
        print("Phone no      : ", self.phone)
        print("Address       : ", self.address)
        print("Email         : ", self.email)
        print("Location      : ", self.location)
        print("Room Type     : ", self.room)
        print("Check-In      : ", self.checkin)
        print("Check-Out     : ", self.checkout)
        print("Total Members : ", self.total)
        print("Total Price   : ₹", self.price * self.total)
        print("-----------------Thank you-----------")


class Food(Add_account):
    def __init__(self, name, age, phone, address, email, location, food_name, food_price,quantity):
        super().__init__(name, age, phone, address, email, location)
        self.foodname = food_name
        self.foodprice = food_price
        self.quantity = quantity

    def foods_list(self):
        print("------ FOOD MENU ------")
        print("1. Idli (4 pcs)              ₹40")
        print("2. Dosa                      ₹60")
        print("3. Poori                     ₹50")
        print("4. Pongal                    ₹55")
        print("5. Veg Fried Rice            ₹90")
        print("6. Chicken Fried Rice        ₹120")
        print("7. Veg Noodles               ₹100")
        print("8. Chicken Noodles           ₹130")
        print("9. Parotta (2 pcs)           ₹45")
        print("10. Chicken Gravy            ₹110")
        print("11. Mutton Gravy             ₹150")
        print("12. Paneer Butter Masala     ₹130")
        print("13. Veg Meals                ₹100")
        print("14. Non-Veg Meals            ₹150")
        print("15. Curd Rice                ₹60")
        print("16. Ice Cream (Cup)          ₹50")
        print("17. Fresh Juice              ₹70")
        print("18. Tea                      ₹20")
        print("19. Coffee                   ₹25")
        print("20. Water Bottle (1L)        ₹20")
        print("--------------------------")

    def food_recipt(self):
        print("--------------Food Recipt------------------")
        print("Your Ordered Foods : ",self.foodname)
        print("Quantity : ",self.quantity)
        print("Price of Your foods : ₹",self.foodprice * self.quantity)
        print("---------------Thank You------------------")

class Payments(Add_account):
    def __init__(self,name,age,phone,email,total_members,price,check_in,check_out,food_name,food_price,quantity,mode,upi_id,upi_pin):
        super().__init__(name, age, phone, address, email, location)
        self.total = total_members
        self.price = price
        self.checkin = check_in
        self.checkout = check_out
        self.food_name = food_name
        self.quantity = quantity
        self.mode = mode
        self.upi = upi_id
        self.password = upi_pin
        self.foodprice = food_price

    def success_bill(self):
        print("---------------Praveen's Hotel-----------------")
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Phone : ",self.phone)
        print("Email : ",self.email)
        print("Total Members : ",self.total)
        print("Mode of Pay : ",self.mode)
        print("UPI Id : ",self.upi)
        print("Check-in : ",self.checkin)
        print("Check-Out : ",self.checkout)
        total_value =  (self.foodprice * self.quantity ) + (self.total * self.price)
        print("Total Price :  ₹", total_value)
        print("-------------------Thank you visit again !!!--------------")

# User inputs handles


while True:
    print("---------------Praveen's Hotel-----------------")
    print("=====> 1. Add Account")
    print("=====> 2. View Rooms")
    print("=====> 3. Booking Rooms")
    print("=====> 4. Foods List ")
    print("=====> 5. Payments ")
    print("=====> 6. Exit")

    request = input("Enter Youir Choice (1 - 6 ): ")
    if(request == "1"):
          name = input("Enter Your Name : ").lower()
          age = int(input("Enter Your age : "))
          phone = input("Enter your phone number : +91 ").lower()
          if(len(phone) == 10):
              address = input("Write Your Address : ").lower()
              email = input("Enter your Email like (name123@gmail.com): ").lower()
              if re.match(email_pattern, email):
                location = input("Enter your Location : ").lower()
                addAccounts = Add_account(name,age,phone,address,email,location)
                print("Account Created Successfully !!!")
                
                   
              else:
                print("Invalid Email ")
          else:
              print("Invalid phone Number")
    
    elif(request == "2"):
        Add_account.view_rooms(1)

    
    elif(request == "3"):
        Add_account.view_rooms(1)

        room_type= input("Enter the Room Type (1 - 7) : ").lower()
        if(room_type == "1"):
            price = 1500
        elif(room_type == "2"):
            price = 2500
        elif(room_type == "3"):
            price = 3500
        elif(room_type == "4"):
            price = 4500
        elif(room_type == "5"):
            price = 7500
        elif(room_type == "6"):
            price = 12000
        elif(room_type == "7"):
            price = 5000
        else:
            print("Invalid Room Number !!!")

        check_in = input("Enter the Check-in date : ")
        check_out = input("Enter the Check-out date : ")
        total_members = int(input("Enter the count of Totak members : "))
        price = int(price)
        try:
            values = Booking(name, age, phone, address, email, location, room_type, check_in, check_out, total_members, price)
            values.prints()
        except:
            print("Please first Create an Account !!!")
        

    elif(request == "4"):
        Food.foods_list(2)
        food_name = input("Enter the name of food : ").lower()
        quantity = int(input("Enter the Quantity of Food : "))

        if(food_name == "idli"):
            food_price = 40
        elif(food_name == "dosa"):
            food_price = 60
        elif(food_name == "poori"):
            food_price = 50
        elif(food_name == "pongal"):
            food_price = 55
        elif(food_name == "veg fried rice"):
            food_price = 90
        elif(food_name == "chicken fried rice"):
            food_price = 120
        elif(food_name == "veg noodles"):
            food_price = 100
        elif(food_name == "chicken noodles"):
            food_price = 130
        elif(food_name == "parotta"):
            food_price = 45
        elif(food_name == "chicken gravy"):
            food_price = 110
        elif(food_name == "mutton gravy"):
            food_price = 150
        elif(food_name == "paneer butter masala"):
            food_price = 130
        elif(food_name == "veg meals"):
            food_price = 100
        elif(food_name == "non veg meals"):
            food_price = 150
        elif(food_name == "curd rice"):
            food_price = 60
        elif(food_name == "ice cream"):
            food_price = 50
        elif(food_name == "fresh juice"):
            food_price = 70
        elif(food_name == "tea"):
            food_price = 20
        elif(food_name == "coffee"):
            food_price = 25
        elif(food_name == "water bottle"):
            food_price = 20
        else:
            print("Ivalid Food !!!!")
        
        try:
            foodsdata = Food( name, age, phone, address, email, location, food_name, food_price,quantity)
            foodsdata.food_recipt()
        except:
            print("Please first Create an Account !!!")

        
    elif(request == "5"):
        mode = input("Enter the Payment gateway ( Gpay,PayTm,PhonePay ) : ")
        upi_id = input("Enter your UPI ID : ")
        if re.match(upi_pattern, upi_id):
            upi_pin = input("Enter the UPI pin : ")
            if(len(upi_pin) <= 6):
                print("Redirecting Payment Gatway .....")
                print("Payment Successfull !!!!")
                print("Colllect Your Recipt !!! ")

                try:
                    pay = Payments(name,age,phone,email,total_members,price,check_in,check_out,food_name,food_price,quantity,mode,upi_id,upi_pin)
                    pay.success_bill()
                except:
                    print("Please first Create an Account !!!")
    
    

    
        else:
            print("Invalid UPI ID")


    elif(request == "6"):
        print('Exited Successfully !!!!!')
        break


            
        
        




    else:
        print(" Invalid Choice selected !!!! ")
              
          
                        
      


        
        

        



        

        
        



        

        
        
        
    
    
