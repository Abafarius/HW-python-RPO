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
        if self.age < 10:
            self.health -= self.age * 0.01
        elif self.age < 100:
            self.health -= self.age * 0.9
        elif self.age < 1000:
            self.health -= self.age *2.5

    def get_tear_book(self, page, damage):
        self.health -= damage
        self.pages -= page    

war_of_the_worlds = Books(50, 50, 288, 10, "sci-fi")
print("Информация о книге:")
print("Название:", "War of the Worlds")
print("Ширина:", war_of_the_worlds.width)
print("Высота:", war_of_the_worlds.height)
print("Количество страниц:", war_of_the_worlds.pages)
print("Жанр:", war_of_the_worlds.genre)
print("Здоровье:", war_of_the_worlds.health)
print("Возраст:", war_of_the_worlds.age)

war_of_the_worlds.get_new_page(10)
print("После чтения 10 страниц:", "Количество страниц:", war_of_the_worlds.pages)

war_of_the_worlds.get_older(5)
print("После старения на 5 лет:", "Здоровье:", war_of_the_worlds.health)

war_of_the_worlds.get_tear_book(50, 400)
print("После повреждения книги:", "Здоровье:", war_of_the_worlds.health)
print("После повреждения книги:", "Количество страниц:", war_of_the_worlds.pages)
