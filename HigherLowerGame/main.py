import database
import random
import os

def account_selector(db):
    name = db["name"]
    description = db["description"]
    country = db["country"]
    followers = db["follower"]
    return f"{name} - a {description} from {country}"

def check_answer(follower_count,foll_count1,foll_count2):
       if foll_count1 < foll_count2:
           if follower_count == 1:
               return False
           else:
             return True
               #return print("Invalid input!,please choose from either 1 or 2.")

       else:
           if follower_count == 1:
               return True
           else:
               return False

db2 = random.choice(database.data)
score = 0
flag = True
while flag:
    print(database.logo)
    db1 = db2
    db2 = random.choice(database.data)
    while db1 == db2:
        db2 = random.choice(database.data)

    print(f"compare 1: {account_selector(db1)}")
    print(database.vs)
    print(f"compare 2: {account_selector(db2)}")
    follower_count = int(input("Who has more followers count type 1 or type 2: "))
    foll_count1 = db1["follower"]
    foll_count2 = db2["follower"]


    is_correct = check_answer(follower_count, foll_count1, foll_count2)



    os.system('cls')
    if is_correct:
        score += 1
        print(f"You are right, your score is {score}")
    else:
        if follower_count == 3:
            print("Invalid input!,please choose from either 1 or 2.")
            flag = False
        else:
           print(f"Your guess is wrong your score is {score}")
           flag = False

