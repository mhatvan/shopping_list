### bei wrong input soll wieder user_add_item abgefragt werden von oben?

shopping_list = []

user_add_item = raw_input("Do you want to add an item to the list? Type in \"yes\" or \"no\": ")

while user_add_item == "yes" or user_add_item == "YES":
    shopping_list.append(raw_input("Please enter the name of the item: "))
    user_add_another_item = (raw_input("Ok, got it! Do you want to add another item to the list? Type in \"yes\" or \"no\": "))
    user_add_item = user_add_another_item

if user_add_item == "no" or user_add_item == "NO" :
        print("Ok fine, here is your list:"),
        if len(shopping_list) > 0:
            print (shopping_list)
        else:
            shopping_list.append("Shopping list empty!")
            print (shopping_list)
else:
    print("Wrong input.")
