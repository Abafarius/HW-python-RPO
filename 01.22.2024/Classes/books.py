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
        self.age = years
        self.health

        
