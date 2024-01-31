class Music:
    def __init__(self, title, artist, duration, genre, release_year, album=None):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.genre = genre
        self.release_year = release_year
        self.album = album

    def play(self):
        # Здесь может быть логика воспроизведения трека
        print("Играет трек:", self.title)

    def get_info(self):
        info = f"Название: {self.title}\nИсполнитель: {self.artist}\nДлительность: {self.duration} секунд\nЖанр: {self.genre}\nГод выпуска: {self.release_year}"
        if self.album:
            info += f"\nАльбом: {self.album}"
        return info

    def change_genre(self, new_genre):
        self.genre = new_genre

# Пример использования класса Music
# Создание экземпляра музыкального трека
song = Music("Bohemian Rhapsody", "Queen", 354, "Rock", 1975, "A Night at the Opera")

# Вывод информации о треке
print(song.get_info())

# Изменение жанра трека
song.change_genre("Rock, Opera")
print("Новый жанр трека:", song.genre)

# Воспроизведение трека
song.play()