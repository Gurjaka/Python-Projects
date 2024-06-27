#ამოცანა: დაამატეთ ორი ობიექტი ფეხბურთელების სახით, და დაამატეთ მეთოდები: ასაკის და ნომრის ცალცალკე გამოსატანად. 
#ასევე დააამატეთ მეთოდი რომელიც გამოიტანს ატრიბუტრბს შემდეგი ფორმით: სახელი: Khvicha Kvaratskhelia, ასაკი: 23, ნაკრებში მაისურის ნომერი: "7"
class Footballer:
    def __init__(self, name, surname, age, number):
        self.name = name
        self.surname = surname
        self.age = age
        self.number = number
    
    def get_full_name(self):
        return print(f"{self.name} {self.surname}")
    
    def get_age(self):
        return print(self.age)
    
    def get_number(self):
        return print(self.number)
    
    def get_data(self):
        return print(f"სახელი: {self.name} {self.surname}, ასაკი: {self.age}, ნაკრებში მაისურის ნომერი: {self.number}")
    
kvara = Footballer("Khvicha", "Kvaratskhelia", 23, "7")
mamarda = Footballer("Giorgi", "Mamardashvili", 24, "25")

kvara.get_full_name()
kvara.get_age()
kvara.get_number()
kvara.get_data()

mamarda.get_full_name()
mamarda.get_age()
mamarda.get_number()
mamarda.get_data()
