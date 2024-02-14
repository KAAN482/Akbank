class library:
    def __init__(self) -> None:
        self.file=open("books.txt","a+")
        
        


    def destructor(self):
        self.file.close()
        print("File is closed.")

    def listbooks(self):
        with open("books.txt") as file:
            content = file.read().splitlines()
            if not content:
                print("There is no book in the library yet...")
            else:
                for line in content:
                    print(line)

    def addbook(self):
        title=input("Book Title:")
        author=input("Book Author:")
        release=input("First Release Year:")
        while not release.isdigit():
            print("Please enter year with numbers...")
            release=input("First Release Year:")
        pages=input("Number of Pages:")
        while not pages.isdigit():
            print("Please enter pages with numbers...")
            pages=input("Number of Pages:")


        book=f"{title},{author},{release},{pages}\n"

        booklist=[title,author,release,pages]
        
        


        with open("books.txt", "a+") as file:
            file.seek(0) 
            content = file.read().splitlines() 
            checklist = [line.strip().split(",") for line in content]
            
            found = False
            for books in checklist:
                if booklist == books:
                    found = True
                    print("This book already in library...")
                    break

            if not found:
                file.write(book) 
                print("Book has been added.")




    def removebook(self):
        title = input("Book Title:").strip()
        with open("books.txt") as file:
            content = file.readlines()
        
        found = False
        newcontent = []
        
        for line in content:
            if title != line.split(',')[0].strip():
                newcontent.append(line)
            else:
                found = True
        
        if found:
            with open("books.txt", "w") as file:
                file.writelines(newcontent)
            print("Book has been deleted.")
        else:
            print("There is no book with the given title.")

lib=library()



while True:
    print("*** MENU *** \n1)List Books \n2)Add Book\n3)Remove Book \n4)Quit")
    user = input("Enter your choice: ")

    if not user.isdigit():
        print("Please enter a number...")
    else:
        user = int(user)
        
        if user==1:
            lib.listbooks()
        elif user==2:
            lib.addbook()
        elif user==3:
            lib.removebook()
        elif user==4:
            lib.destructor()
            break

        else:
            print("Wrong input. Try again...")

        

            



            