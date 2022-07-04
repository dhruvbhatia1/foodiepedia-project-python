import mysql.connector as con
mydb = con.connect(host = "localhost", user="root", password = "dhruv", database= "foodiepedia")
cur1 = mydb.cursor()

def Replace(char):
    Dict = {'Slash ' : '/', 'percin ': '%', 'andana ': '&', 'qqq ': ',', 'flstop ' : '.', 'quoquo ': '\'', 'douquo' : '\"', 'braopn' : '(', 'bracls ': ')', 'dasdash ' : '-' , 'clonal ' : ':', 'exclamam ' : '!', 'starento ' : '*' , 'newlinene ': '\n', 'plussh ': '+' , 'lessthein ' : '<', 'slashsh': '/', 'semeclon' : ';'}
    for i in Dict:
        char = char.replace(i, Dict[i])
    return char


def veg():
    cur1.execute("select dish from veg")
    dishes = ''
    for i in cur1:
        dishes += ((str(i)[2:len(i)-4]) + '\n')
    return dishes
def nonveg():
    cur1.execute("select dish from nonveg")
    dishes = ''
    for i in cur1:
        dishes += ((str(i)[2:len(i) - 4]) + '\n')
    return dishes
def seafood():
    cur1.execute("select dish from seafood")
    dishes = ''
    for i in cur1:
        dishes += ((str(i)[2:len(i) - 4]) + '\n')
    return dishes
def dessert():
    cur1.execute("select dish from desserts")
    dishes = ''
    for i in cur1:
        dishes += ((str(i)[2:len(i) - 4]) + '\n')
    return dishes


def veg_ingred(dish_name):
    cur1.execute("select ingredients from veg where dish = \'" + dish_name + "\'")
    
    x = ''
    for i in cur1:
        x = (str(i)[2:len(i)-4])
    x= Replace(x)
    return x
def nonveg_ingred(dish_name):
    cur1.execute("select ingredients from nonveg where dish = \'" + dish_name + "\'")
    
    x = ''
    for i in cur1:
        x = (str(i)[2:len(i)-4])
    x =  Replace(x)
    return x
def seafood_ingred(dish_name):
    cur1.execute("select ingredients from seafood where dish = \'" + dish_name + "\'")
    
    x = ''
    for i in cur1:
        x = (str(i)[2:len(i)-4])
    x =  Replace(x)
    return x
def desserts_ingred(dish_name):
    cur1.execute("select ingredients from desserts where dish = \'" + dish_name + "\'")
    global x
    x = ''
    res = cur1.fetchall()
    for i in res:
        x = (str(i)[2:len(i)-4])
    x = Replace(x)
    return x
def veg_recipe(dish_name):
    cur1.execute("select recipe from veg where dish = \'" + dish_name + "\'")
    
    x = ''
    for i in cur1:
        x = (str(i)[2:len(i)-4])
    x = Replace(x)
    return x

def nonveg_recipe(dish_name):
    cur1.execute("select recipe from nonveg where dish = \'" + dish_name + "\'")
    
    x = ''
    for i in cur1:
        x = (str(i)[2:len(i)-4])
    x = Replace(x)
    return x
def seafood_recipe(dish_name):
    cur1.execute("select recipe from seafood where dish = \'" + dish_name + "\'")
    
    x = ''
    for i in cur1:
        x = (str(i)[2:len(i)-4])
    x =  Replace(x)
    return x

def desserts_recipe(dish_name):
    global x
    x= ''
    cur1.execute("select recipe from desserts where dish = \'" + dish_name + "\'")
    res = cur1.fetchall()
    for i in res:
        x = (str(i)[2:len(i)-4])
    x = Replace(x)
    return x
def edit(DIR,cuisine,dish_name,new_value):
    repla = {'/': ' slashsh ', '%': ' percin ', '&': ' andana ', ',': ' qqq ', '.': ' flstop ', '\'': ' quoquo ',
             '\"': ' douquo ', '(': ' braopn ',
             ')': ' bracls ', '-': ' dasdash', ':': ' clonal ', '!': ' exclamam ',
             '*': ' starento ', '\n': ' newlinene ', '“': ' douqou ', '”': ' douqou ',
             '+': ' plussh ', '‹': ' lessthein ', '½': '1 slashsh 2', '¾': '3 slashsh 4',
             ';': ' semeclon ', 'â': '', '€': ' dasdash ', 'Â': '', '°': ''}
    chrstr = 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM1234567890 #%@$'

    if DIR == 0:
        new_dish = ''
        for i in new_value:
            if i in chrstr:
                new_dish += i
            elif i in repla:
                new_dish += repla[i]
        cur1.execute("update " + cuisine + " set dish = \'"+new_dish+"\' where dish = \'"+dish_name+"\'")
    elif DIR == 1:
        new_ingred = ''
        for i in new_value:
            if i in chrstr:
                new_ingred += i
            elif i in repla:
                new_ingred += repla[i]
        cur1.execute("update " + cuisine + " set ingredients = \'" + new_ingred + "\' where dish = \'" + dish_name + "\'")
    elif DIR == 2:
        new_rec = ''
        for i in new_value:
            if i in chrstr:
                new_rec += i
            elif i in repla:
                new_rec += repla[i]
        cur1.execute("update " + cuisine + " set recipe = \'" + new_rec + "\' where dish = \'" + dish_name + "\'")

    mydb.commit()

def delete(cuisine,dish_name):
    cur1.execute("delete from " + cuisine + " where dish = \'"+dish_name+"\'")
    mydb.commit()

def add(cuisine,dish_name,ingredients,recipe):
    repla = {'/': ' slashsh ', '%': ' percin ', '&': ' andana ', ',': ' qqq ', '.': ' flstop ', '\'': ' quoquo ',
             '\"': ' douquo ', '(': ' braopn ',
             ')': ' bracls ', '-': ' dasdash', ':': ' clonal ', '!': ' exclamam ',
             '*': ' starento ', '\n': ' newlinene ', '“': ' douqou ', '”': ' douqou ',
             '+': ' plussh ', '‹': ' lessthein ', '½': '1 slashsh 2', '¾': '3 slashsh 4',
             ';': ' semeclon ', 'â': '', '€': ' dasdash ', 'Â': '', '°': ''}
    chrstr = 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM1234567890 #%@$'
    new_ingred = ''
    for i in ingredients:
        if i in chrstr:
            new_ingred += i
        elif i in repla:
            new_ingred += repla[i]
    new_rec = ''
    for i in recipe:
        if i in chrstr:
            new_rec += i
        elif i in repla:
            new_rec += repla[i]
    new_dish = ''
    for i in dish_name:
        if i in chrstr:
            new_dish += i
        elif i in repla:
            new_dish += repla[i]
    cur1.execute("insert into " + cuisine + " values (\'"+new_dish+"\', \'"+new_ingred+"\', \'"+new_rec+"\')")
    mydb.commit()