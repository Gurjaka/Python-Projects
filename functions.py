# დავალება 1, შეასრულეთ ყველა არითმეტიკული ოპერაცია
def MathEquations():
    a = int(input("Choose first number: "))
    b = int(input("Choose second number: "))
    print(a, "+", b, "=", a+b) 
    print(a, "-", b, "=", a-b) 
    print(a, "*", b, "=", a*b)
    print(a, "/", b, "=", a/b)
    print(a, "//", b, "=", a//b)
    print(a, "**", b, "=", a**b)
    print(a, "%", b, "=", a%b)

def MathEquationsChoice():
    a = int(input("Choose first number: "))
    b = int(input("Choose second number: "))
    operator = input("Choose one of the following operators: + ; - ; * ; / ; // ; **; % ; ")
    
    if operator == "+":
        print(a, "+", b, "=", a+b)
    elif operator == "-": 
        print(a, "-", b, "=", a-b) 
    elif operator == "*":
        print(a, "*", b, "=", a*b)
    elif operator == "/":
        print(a, "/", b, "=", a/b)
    elif operator == "//":
        print(a, "//", b, "=", a//b)
    elif operator == "**":
        print(a, "**", b, "=", a**b)
    elif operator == "%":
        print(a, "%", b, "=", a%b)
    else:
        print("Not correct option")
        quit()

def MathEquationsChoiceLoop():
    try:
        while (True):
            a = int(input("Choose first number: "))
            b = int(input("Choose second number: "))

            while (True):
                operator = input("Choose one of the following operators: + ; - ; * ; / ; // ; **; % ; ")
                if operator == "+":
                    print(a, "+", b, "=", a+b)
                elif operator == "-": 
                    print(a, "-", b, "=", a-b) 
                elif operator == "*":
                    print(a, "*", b, "=", a*b)
                elif operator == "/":
                    print(a, "/", b, "=", a/b)
                elif operator == "//":
                    print(a, "//", b, "=", a//b)
                elif operator == "**":
                    print(a, "**", b, "=", a**b)
                elif operator == "%":
                    print(a, "%", b, "=", a%b)
                else:
                    print("Not correct option")
                again = input("Want to choose another operation? (yes/no): ")
                if again == "yes":
                    variables = input("Would you like to change number? (yes/no): ")
                    if variables == "yes":
                        break
                    elif variables == "no":
                        continue
                elif again == "no":
                    quit()
    except ValueError:
        print("Not a Number")

def HelloPython():
    print("Hello, Python!")

def HelloSaxeli():
    name = "Gurami"
    print("Hello", name, "!")

def YouAreAge():
    age = int(input("Input your age: "))
    number = 19

    if age > number:
        print("You are adult")
    if age < number:
        print("You still got a long way to go")

def YouAreAgeLoop():
    import time
    number = 19
    while (True):
        try:
            age = int(input("Enter your age: "))
            if age > number :
                print("You are დიდი")
                tryagain = input("Want to try again? (yes/no): ")
                if tryagain == "yes":
                    continue
                elif tryagain == "no":
                    print("See you later!")
                    time.sleep(2)
                    break
            elif age < number:
                print("You are პატარა")
                tryagain = input("Want to try again? (yes/no): ")
                if tryagain == "yes":
                    continue
                elif tryagain == "no":
                    print("See you later!")
                    time.sleep(2)
                    break
        except ValueError:
            print("Nan, try again")

def ricxvebisjami():
    number1 = int(input("Choose first number: "))
    number2 = int(input("Choose second number: "))

    if number1 + number2 >= 50:
        print("ricxvebi didia")
    elif number1 + number2 <= 50:
        print("ricxvebi pataraa")

def ricxvebiluwi():
    number = int(input("Sheiyvanet ricxvi: "))
    if number % 2 == 0:
        print("Your number is even")
    else:
        print("Your number is odd")

def saxeli():
    name = "Gurami"
    name2 = input("What is your name: ")
    if name == name2:
        print("Gamarjoba " + name2)
    else:
        print("ar gicnob " + name2)

def gicnob():
    name = "Gurami"
    surname = "Esartia"
    
    name2 = input("Your name: ")
    surname2 = input("Your surname: ")

    if name == name2 and surname == surname2:
        print("I know you")
    else:
        print("I don't know you")

def interval():
    number = int(input("Input your number: "))
    if number > -50 and number < 20:
        print("Moxvda intervals tavshi")
    else:
        print("Ver moxvda intervals tavshi")

def xaker():
    Login = "Gurami"
    password = "rame"
 
    Login2 = input("Login: ")
    password2 = input("password: ")
    if Login == Login2 and password == password2:
        print("Tqven gaiaret avtorizacia")
    elif Login == Login2 or password == password2:
        print("Kidev scadet")
    else:
        print("Xakeri xar")

def RandJami():
    import random
    number1 = random.randint(0,1000)
    number2 = random.randint(0,1000)
    jami = number1 + number2

    print(jami)

def Randtoloba():
    import random
    number1 = random.randint(0,1000)
    number2 = random.randint(0,1000)
    
    if number1 > number2:
        print("Pirveli ricxvi metia")
    elif number1 < number2:
        print("Meore ricxvi metia")
    elif number1 == number2:
        print("Ricxvebi tolia")

def RandLuwoba():
    import random

    number1 = int(input("Choose number: "))
    number2 = random.randint(0,1000)

    if number1 % 2 == 0 and number2 % 2 == 0:
        print("Orive luwia")
    elif number1 % 2 == 0 or number2 % 2 == 0:
        print("Erterti luwia")
    else: 
        print("Orive kentia")

def RandAtwilad():
    import random
    number = random.uniform(0,1000)

    print(number)
    
    number = number // 1

    print(number)

    if number % 2 == 0:
        print("even")
    else:
        print("odd")

def ArsebitiSaxeli():
    try:
        while (True):
            ArsebitiSaxeli = input("Please input name: ")
            Number = int(input("Please input quantity: "))
            if Number == 1 or Number == 0:
                print(str(Number), ArsebitiSaxeli)
                print("Arsebiti saxeli mxolobitia")
            # Irregular plurars
            elif Number > 1 and ArsebitiSaxeli == "foot":
                print(str(Number), "feet")
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "tooth":
                print(str(Number), "teeth")
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "goose":
                print(str(Number), "geese")
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "man":
                print(str(Number), "men")
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "woman":
                print(str(Number), "women")
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "mouse":
                print(str(Number), "mice")
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "louse":
                print(str(Number), "lice")
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "die":
                print(str(Number), "dice")
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "ox":
                print(str(Number), "oxen")
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "child":
                print(str(Number), "children")
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "person":
                print(str(Number), "people")
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "penny":
                print(str(Number), "pence")
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "sheep":
                print(str(Number), ArsebitiSaxeli)
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "fish":
                print(str(Number), ArsebitiSaxeli)
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "moose":
                print(str(Number), ArsebitiSaxeli)
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "swine":
                print(str(Number), ArsebitiSaxeli)
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "buffalo":
                print(str(Number), ArsebitiSaxeli)
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "shrimp":
                print(str(Number), ArsebitiSaxeli)
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "deer":
                print(str(Number), ArsebitiSaxeli)
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "trout":
                print(str(Number), ArsebitiSaxeli)
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "sheep":
                print(str(Number), ArsebitiSaxeli)
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "alga":
                print(str(Number), "algae")
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "larva":
                print(str(Number), "larvae")
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "appendix":
                print(str(Number), "appendices/appendixes")
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "vortex":
                print(str(Number), "vortices/vortexes")
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "roof":
                print(str(Number), "roofs")
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "piano":
                print(str(Number), "pianos")
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "canto":
                print(str(Number), "cantos")
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "photo":
                print(str(Number), "photos")
                print("arsebiti saxeli aris mravlobiti")
            elif Number > 1 and ArsebitiSaxeli == "zero":
                print(str(Number), "zeros")
                print("arsebiti saxeli aris mravlobiti") 
            elif Number > 1 and ArsebitiSaxeli[-1:] == "f" or Number > 1 and ArsebitiSaxeli[-2:] == "fe":
                print(str(Number), ArsebitiSaxeli[:-1] + "ves")
                print("arsebiti saxeli aris mravlobiti")
                explaination = input("Want to see an explaination? (yes/no): ")
                if explaination == "yes":
                    print("""\nSome nouns ending in "-f" or "-fe" change the ending to "-ves" for the plural.
    This is common for words like "leaf" (leaves) and "knife" (knives).
    However, there are exceptions where you just add "-s" (like "roof" becomes "roofs").""")
            elif Number > 1 and ArsebitiSaxeli[-1:] == "y":
                print(str(Number), ArsebitiSaxeli[:-1] + "ies")
                print("arsebiti saxeli aris mravlobiti")
                explaination = input("Want to see an explaination? (yes/no): ")
                if explaination == "yes":
                    print("""If a noun ends in a consonant followed by 'y,' change the 'y" to "i" and add "-es."
For example, "party" becomes "parties" and "sky" becomes "skies." 
However, if the consonant before the "y" is a vowel, just add "-s" (like "monkey" becomes "monkeys").""")
            elif Number > 1 and ArsebitiSaxeli[-1:] == "s" or Number > 1 and ArsebitiSaxeli[-1:] == "x" or Number > 1 and ArsebitiSaxeli[-1:] == "z":
                print(str(Number), ArsebitiSaxeli + "es")
                print("arsebiti saxeli aris mravlobiti")
                explaination = input("Want to see an explaination? (yes/no): ")
                if explaination == "yes":
                    print("""Nouns that end in -s, -sh, -ch, -x, or -z usually take "-es" for the plural form.
This is because adding just "-s" might make the pronunciation awkward, like "bus" (buses) or "church" (churches).
There are some exceptions where you double the consonant before adding "-es" (discussed below).""")
            elif Number > 1 and ArsebitiSaxeli[-1:] == "o":
                print(str(Number), ArsebitiSaxeli + "es")
                print("arsebiti saxeli aris mravlobiti")
                explaination = input("Want to see an explaination? (yes/no): ")
                if explaination == "yes":
                    print("""Plurals of words ending in -o are usually made by adding -es.
But of course, there are exceptions.
(Aren’t there always?) Some words ending in -o that are borrowed from other languages take only an s to make a plural, such as pianos, cantos, photos, and zeros.
Cello, which is an abbreviation of the Italian word violoncello, can be pluralized in the traditional way, as celli, or the commonly accepted anglicized way, as cellos.""")
            elif Number > 1 and ArsebitiSaxeli[-2:] == "ch" or Number > 1 and ArsebitiSaxeli[-2:] == "sh":
                print(str(Number), ArsebitiSaxeli + "es")
                print("arsebiti saxeli aris mravlobiti")
                explaination = input("Want to see an explaination? (yes/no): ")
                if explaination == "yes":
                    print("""Nouns that end in -s, -sh, -ch, -x, or -z usually take "-es" for the plural form.
This is because adding just "-s" might make the pronunciation awkward, like "bus" (buses) or "church" (churches).
There are some exceptions where you double the consonant before adding "-es" (discussed below).""")
            elif Number > 1 and ArsebitiSaxeli[-2:] == "us":
                print(str(Number), ArsebitiSaxeli[:-2] + "i")
                print("arsebiti saxeli aris mravlobiti")
                explaination = input("Want to see an explaination? (yes/no): ")
                if explaination == "yes":
                    print("""To make a word ending in -us plural, change -us to -i.
Many plurals of words ending in -us have anglicized versions, formed by simply adding -es.
The latter method sounds more natural in informal settings.
If there is an anglicized version that is well accepted, this will be noted in the dictionary entry for the word you are using.""")
            elif Number > 1 and ArsebitiSaxeli[-2:] == "is":
                print(str(Number), ArsebitiSaxeli[:-2] + "es")
                print("arsebiti saxeli aris mravlobiti")
                explaination = input("Want to see an explaination? (yes/no): ")
                if explaination == "yes":
                    print("""Nouns with an -is ending can be made plural by changing -is to -es.
Some people have a hard time remembering that the plural of crisis is crises and the plural of axis is axes, but crisises and axises are incorrect.""")
            elif Number > 1 and ArsebitiSaxeli[-2:] == "on":
                print(str(Number), ArsebitiSaxeli[:-1] + "a")
                print("arsebiti saxeli aris mravlobiti")
                explaination = input("Want to see an explaination? (yes/no): ")
                if explaination == "yes":
                    print("These Greek words change their -on ending to -a.")
            elif Number > 1 and ArsebitiSaxeli[-2:] == "um":
                print(str(Number), ArsebitiSaxeli[:-1] + "a")
                print("arsebiti saxeli aris mravlobiti")
                explaination = input("Want to see an explaination? (yes/no): ")
                if explaination == "yes":
                    print("""Words ending in -um shed their -um and replace it with -a to form a plural.
The plurals of some of these words are far better known than their singular counterparts.""")
            elif Number > 1 and ArsebitiSaxeli[-2:] == "ex" or Number > 1 and ArsebitiSaxeli[-2:] == "ix":
                print(str(Number), ArsebitiSaxeli[:-2] + "ces/", ArsebitiSaxeli[:-2] + "xes")
                print("arsebiti saxeli aris mravlobiti")
                explaination = input("Want to see an explaination? (yes/no): ")
                if explaination == "yes":
                    print("Nouns ending in -ix are changed to -ices in formal settings, but sometimes -xes is perfectly acceptable.")
            elif Number > 1:
                print(str(Number), ArsebitiSaxeli + "s")
                print("arsebiti saxeli aris mravlobiti")
            else:
                print("Negative number")
            try_again = input("Would you like to try another word? (yes/no): ")
            if try_again == "yes":
                continue
            elif try_again == "no":
                break
    except ValueError:
        print("NaN")
ArsebitiSaxeli()