class Books:
    width = 0
    height = 0
    pages = 0
    genre = ""
    health = 1000
    age = 0

    def __init__(self, width, height, pages, age, genre):
        self.width = width
        self.height = height
        self.pages = pages
        self.age = age
        self.health -= age*0.2 
        self.genre = genre
        if age < 10:
            self.health -= age * 0.01
        elif age < 100:
            self.health -= age * 0.9
        elif age < 1000:
            self.health -= age *2.5
            
   
    def get_new_page(self, page):
        self.pages += page

    def get_older(self, years):
        self.age += years
        self.health -= years*0.01
    
    def get_tear_book(self, page, damage):
        self.pages -= page
        self.health -= damage

book1 = Books(50, 50, 100, 2, "Sci-fi")

print("Before adding new pages: ", book1.pages)
book1.get_new_page(10)
print("After adding new pages: ", book1.pages)
print("Book's current physical condition: ", book1.health)
print("Book's current age: ", book1.age)
book1.get_older(3)
print("3 years left. Book's current age: ", book1.age)
print("Book's current physical condition after 3 years: ", book1.health)

book1.get_tear_book(52, 500)
print("After tearing book pages: ", book1.pages)
print("After tearing book physical condition: ", book1.health)





        
