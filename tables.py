
user_choice = int(input("enter your number : "))
with open(f"table_of{user_choice}.txt" , "w") as f :
    for i in range(1 , 11):
        tables = f"{user_choice} x {i} = {user_choice*i}\n"
        f.write(tables)
    

        
        