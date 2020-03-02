
print ("hi welcome to my bookshop!")
print ("/n")

running=True

while running==True:

    print ("1  add a book title.")
    print ("2  edit an existing book title.")
    print ("3  delete a book title.")
    print ("4  end the programme.")

    command=input ("please enter 1, 2, 3, or bye" ,)
    if command==("1"):
        print ("please enter what book title you want to add")
    elif command==("2"):
        print("please enter the book title you want to edit")
    elif command==("3"):
        print ("please enter the book title you want to delete")
    elif command==("4"):
        print ("goodbye")
        running=False
    else:
        print ("you didnt enter anything please enter what you want to do")
       

