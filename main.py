# VIT Bhopal Mess Feedback Python Program

users =["shivam","rahul"]      
user_pwds=["123","456"]

all_feedback =[]



#login code
def do_login():
    username=input("Enter username=")
    password=input("Enter password=")   
    for idx in range(len(users)):
        #checking username and password
        if users[idx]==username and user_pwds[idx]==password:
            print("Login successful")   
            show_menu(username)
            return

    # if no matched
    print  ("Invalid login,Try again")



#menu
def show_menu(current_user):
    while True:
        print("\n*** MENU ***")
        print("1.Give Feedback")
        print("2.View My Feedback")
        print("3.Average Rating")
        print ("4.Worst Rating Day")
        print("5.Logout")

        choice =input("Enter choice:- ")
        if choice=="1":
            add_feedback (current_user)
        elif choice=="2":
            show_user_feedback(current_user)
        elif choice== "3":
            calc_avg_rating()
        elif choice=="4":
            find_worst_day()
        elif choice =="5":
            print("Logging out:]")                    
            break
        else:
            print("Invalid choice! Please pick from menu")




#feedback section
def add_feedback(user):
    day=input("Enter day (Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Synday):-")

    # NOTE: assuming user enters valid numbers ,no validation for now
    taste_rating=int(input("Rate Taste (1to5)="))
    hygiene_rating=int(input("Rate Hygiene (1to5)="))
    qty_rating =int(input("Rate Quantity (1to5)="))

    entry = {
        "user":user,
        "day":day,
        "taste":taste_rating,
        "hygiene":hygiene_rating,
        "quantity":qty_rating
    }

    # storing feedback
    all_feedback.append(entry)

    # print(entry)   
    print("Feedback submitted successfully")



# viw user feedback
def show_user_feedback(user):
    print("\n--- YOUR FEEDBACK ---")
# check if anything exist
    has_data=False 
    for item in all_feedback:
        if item["user"]==user:
            print(item)                                         
            has_data =True

    if has_data== False:        
        print("No feedback found")              



#worst rate
def find_worst_day():
    if len(all_feedback)== 0:
        print("No data available")
        return

    lowest_avg=5                
    worst_rating= ""
    for fb in all_feedback:
        avg_val= (fb["taste"]+fb["hygiene"]+fb["quantity"])/3

        # checking if current is worst or not
        if avg_val < lowest_avg:
            lowest_avg=avg_val
            worst_rating=fb["day"]
    print("Worst Rating Day:", worst_rating)



#avg rate calulation
def calc_avg_rating():
    if len(all_feedback) ==0:
        print("No data available")
        return

    total=0
    num=0
    # going through each feedback
    for fb in all_feedback:
        # calculating avg per feedback
        avg_val =(fb["taste"]+fb["hygiene"]+fb["quantity"])/3

        total+=avg_val
        num+=1
    overall=total/num

    print("Overall Average Rating =",overall)

do_login()
