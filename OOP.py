class Books():
    genre = None
    publisher = None
    author = None
    year = None

    def set_data(self, genre, publisher, author, year):
        self.genre = genre
        self.publisher = publisher
        self.author = author
        self.year = year

    def get_data(self):
        return print(f"Genre: {self.genre}\nPublisher: {self.publisher}\nAuthor: {self.author}\nRelease Year: {self.year}")

WhispersInTheShadows = Books()
WhispersInTheShadows.set_data("Classics", "Penguin Random House", "C.S Lewis", 1992)
WhispersInTheShadows.get_data()