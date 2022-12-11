import re


def sign(inp):
    private = re.fullmatch(r"[АBЕКМНОРСТУХ]{1}\d{3}[АBЕКМНОРСТУХ]{2}\d{2,3}?", inp)
    taxi = re.fullmatch(r"[АBЕКМНОРСТУХ]{2}\d{3}\d{2,3}?", inp)
    if private:return f"Private"
    if taxi:return f"Taxi"
    return f"Fail"



trials = ["С227НА777", "КУ22777", "Т22В7477","М227К19У9", " С227НА777"]

#for x in trials:
#    print(sign(x))


def sp_re(inp):
    words = re.split(r'\W+', inp)
    return words


#print(sp_re("Он --- серо-буро-малиновая редиска!! >>>:-> А не кот. www.kot.ru"))

text = """
In the shadows of the forest that flanks the crimson plain by the
side of the Lost Sea of Korus in the Valley Dor, beneath the hurtling
moons of Mars, speeding their meteoric way close above the bosom of
the dying planet, I crept stealthily along the trail of a shadowy
form that hugged the darker places with a persistency that proclaimed
the sinister nature of its errand.

For six long Martian months I had haunted the vicinity of the
hateful Temple of the Sun, wifoo.@ya.ru, foo@.ya.ru PARTLY: boo@ya_ru, -boo@ya.ru-, foo№boo@ya.ruthin whose slow-revolving shaft, far
beneath the surface of Mars, my princess lay entombed--but whether
alive or dead I knew not.serge'o-lupin@mail.ru  Had Phaidor's slim blade found that
beloved heart?  Time only would reveal the truth.
"""

def emails(inp):
    match = re.findall(r"[^ +-.№]{1}(?:\w|[-''""+_]){1,63}@(?:\w|[-.]){1,254}[^ +-.№]{1}", inp)
    return match



def emails2(inp):
    match = re.findall(r"\w(?:\w|[а-яА-Я]|['_+-]){1,63}@(?:[+-]|[A-Za-z]){1,100}\.?[A-Za-z]+", inp)
    return match

#print(emails2("serge'o-lupin@mail.ru- это важно."))
#print(emails2("NO: foo.@ya.ru, foo@.ya.ru PARTLY: boo@ya_ru, -boo@ya.ru-, foo№boo@ya.ru"))
#print(emails2(text))


def abrs(inp):
    match = re.findall(r"[А-ЯA-Z]{2}(?:[А-ЯA-Z]| )*", inp)
    print(match)
    return list(map(lambda x : x.strip(), match))

print(abrs("Это курс информатики соответствует ФГОС и ПООП, это подтверждено ФГУ ФНЦ НИИСИ РАН, а также FFOFF F"))



def  change_time(text):
    #match = re.findall(r"(?:0[1-9]|1[1-9]|2[1-4])(?:[:-][0-5][0-9]){1,2}", text)

    return re.sub(r"(?:0[1-9]|1[1-9]|2[1-4])(?:[:-][0-5][0-9]){1,2}", "(TBD)", text, count=0)

    splited = re.split(r"[\n;,.! ]", text)
    res = []


    for word in splited:
        if word == "":
            continue
        if word in match:
            word = word.replace(word, "(TBD)")
        res.append(word)
    else:
        res = " ".join(res)

    return res


def close_words(inp):
    match = re.findall(r"олень", inp)
    return match


#text = "Уважаемые! Если вы к 90:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю. PS. С отношением 25:50 всё нормально!"
#print(change_time(text))

#text = "Уважаемые! Если вы к 09:100 не вернёте чемодан, то уже в 09:!0:01 я за себя не отвечаю. PS. С отношением 25:50 всё нормально!"
#print(change_time(text))


text = "Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю. PS. С отношением 25:50 всё нормально!"

print(change_time(text))

#print(close_words("Да он олень, а не заяц!"))
"""
text = "11PavalRamzanAhmat123Fr"
match = re.findall(r"[a-zA-Z]+", text)
print(match)
match = re.findall(r"[a-zA-Z]+", text)
print(match)
"""

    
    
def format_digs(inp):
    res = {}

    copy = inp


    match = re.findall(r"\d+", inp)

    m = sorted(list(map(int, match)),reverse = True)

    for dig in m:
        h = hash(str(dig))
        copy = copy.replace(str(dig), str(h))

    
    for st in match:
        if len(st) > 3:
            
            h = hash(st)
            
            new_st = ""
            
            t = 1
            for i in range(len(st)-1, -1, -1):
                new_st += st[i]
                if t % 3 == 0:
                    new_st += ","

                t += 1
                            
            new_st  = "".join(list(reversed(new_st))).strip(",")


            copy = copy.replace(str(h), new_st)
        else:
            h = hash(st)
            copy = copy.replace(str(h), st)
            
    return copy

        
            

        


text = """
12 мало 
лучше 123 
1234 почти 
12354 хорошо 
стало 123456 
супер 1234567
"""
import string
import random

pucns = string.punctuation



text = "JPY1000, CAD10 hdue32 Cad12"

sp = re.split(r"\W+",text)

#sp = re.split(r"[\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~] ",text)


##print(sp)

text = "JPY1000 CAD10 hdue32 Cad12"
match = re.findall(r"[A-Z]+\s*\d+", text)
#print(match)

def my_func(st):
    if "." in st:
        return float(st)
    return int(st)

def code_decode(num):
    pass

def cube(text):
    match = re.findall(r"\d+(?:\.\d+)?", text)
    res = {}
    copy = text

    m = sorted(list(map(my_func, match)),reverse = True)

    print(m)
    
    for dig in m:
        num = dig**3
        code = "*" * random.randint(1, 100000)
        res[code] = num
        text = text.replace(str(dig), code)
        

    res = dict(sorted([item for item in res.items()], key = lambda x : len(x[0]), reverse = True))

    for key, value in res.items():
        text = text.replace(key,str(value))
    return text
        

print(cube("Было закуплено 101.1 единиц 12 техники по 4.5 рублей."))




def dates(text):
    match = re.findall(r"\b(?:0?[1-9]|1[0-2]){1}[:\\/]?(?:0?[1-9]|[1-2][1-9]|3[0-1]){1}[:\\/]?\d{4}", text)
    return math[0].strip("()")

    print(match)


#dates("546 rjjlk5453 89 oe4434k 10/02/2022")

#(?:\d{3}(?:\s|-)?){2}\d{4}


def city_code(st):
    #match = re.findall(r"\+\d?[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}",st)


    
    match = re.findall(r"(?:\+\d{1,2}?|\d{1,2}?)?[\s-]?\(?\d{3}\)?[\s-]?\d{3}(?:[\s-]?\d{2}){2}",st)
    #match = re.findall(r"[(]?\d{3}[)]?(?=[0-9 -]{7,})",st)
    print(match)
    #return match[0].strip("() ")

#print(city_code("8(123)456-78-90"))
#print(city_code("+7(123)456-78-90"))
print(city_code("+123456-78-90"))
#print(city_code("7(123) 456-78-90"))

#print(city_code("+1 416 555 9292"))

#print(city_code("4035555678"))
