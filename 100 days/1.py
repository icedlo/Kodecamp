# shopping_list=["njahi", "butter","flour","bread","milk"]

# for index, item in enumerate(shopping_list):
#     print(f"{index+1}.{item}")

#create a shopping list where user can add , remove, view 

shopping_list=[]

def show_menu():
    print("----Your shopping list----")
    print("Enter your choice (1-5):")
    print("choice 1: Display  list")
    print("choice 2:Add item ")
    print("choice 3:Remove item")
    print("choice 4: clear list")
    print("exit")

while True:
        show_menu()
        choice= input("select your choice")

        
if choice==1:
  print("----Your shopping list----")
  if not shopping_list:
          
      print("you have an empty shopping list")
  else:
for index,item in enumerate(shopping_list):
                print(f"{index+1}.{item}")
elif choice==2:
item=input("enter item to add:")
           shopping_list.append(item)
           print (f"{item} has been added ")

elif  choice==3:
           item=input("enter item to delete")
           for item  in shopping_list:
              shopping_list.remove(item)
              print (f"{item} has been deleted")
           else:
              print(f"{item} does not exist")

elif choice==4:
           shopping_list.clear()
           print ("shopping list has been cleared")  

elif choice==5:
           print("Goodbye")
           break 

else:
           print("invalid ") 
                  
              