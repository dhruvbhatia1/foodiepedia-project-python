import os
from pynput.keyboard import Key, Controller
from time import sleep


def create_database(password):
    k = Controller()
    v = open('Recipe.txt', 'r+')
    v.seek(0)
    nonveg = ['Tandoori Chicken', 'Chicken Tikka', 'Chicken Lababdar', 'Afghani Chicken', 'Chicken Biriyani', 'Mutton', 'Chicken Dumplings', 'Chilli Chicken', 'Chicken Wings', 'Ramen','Chicken Hakka Noodles','Lasagna','Grilled Chicken and Mozzarella Panini']
    veg = ['Veg Pizza', 'Shahi Paneer', 'Matar Paneer', 'Gobhi Aloo', 'Samosa', 'Spring Roll', 'Dahi Kebab', 'Rajma', 'Dal Makhani', 'Veg Sandwich']
    seafood = ['Goan Fish', 'Fish Orley', 'Beer Battered Fish', 'Tempura Sushi', 'Crab']
    dessink = ['Ice Cream Sundae', 'Waffle', 'Kheer', 'Cold Coffee']
    '''
    w,x,y,z=open('nonvegetarian','a+'),open('vegetarian.txt','a+'),open('seefood.txt','a+'),open('dessert.txt','a+')
    mo=['nonvegetarian.txt','vegetarian.txt','seefood.txt','dessert.txt']
    n=[w.write(water[0]), x.write(water[1]), y.write(water[2]), z.write(water[3])]
    '''
    repla={'/': ' slashsh ','%': ' percin ','&': ' andana ',',': ' qqq ','.': ' flstop ', '\'': ' quoquo ', '\"': ' douquo ','(': ' braopn ',
           ')': ' bracls ', '-': ' dasdash', ':': ' clonal ', '!': ' exclamam ',
           '*': ' starento ', '\n': ' newlinene ', '“': ' douqou ', '”': ' douqou ',
           '+': ' plussh ', '‹': ' lessthein ','½': '1 slashsh 2', '¾': '3 slashsh 4',
           ';': ' semeclon ', 'â': '', '€': ' dasdash ', 'Â': '', '°': ''}
    chrstr = 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM1234567890 #%@$'
    
    def pr(a):
        k.press(a)
        k.release(a)
    water=v.read()
    new_water = ''
    weird = []
    for i in water:
        if i in chrstr:
            new_water += i
        elif i in repla:
            new_water += repla[i]
        else:
            weird.append(i)
    print(new_water, weird, sep='\n')

    p = new_water.split('$$$')
    print(p)
    q0, q1, q2, q3 = p[0].split('@@@'), p[1].split('@@@'), p[2].split('@@@'), p[3].split('@@@')
    print(q3, len(q3), len(dessink))
    y1, y2, y3, y4 = {}, {}, {}, {}

    if len(q0) == len(nonveg) and len(q1) == len(veg) and len(q2) == len(seafood) and len(q3) == len(dessink):
        for t in range(len(nonveg)):
            y1[nonveg[t]] = [(q0[t].split('###'))[0], (q0[t].split('###'))[1]]
        for t in range(len(veg)):
            y2[veg[t]] = [(q1[t].split('###'))[0], (q1[t].split('###'))[1]]
        for t in range(len(seafood)):
            y3[seafood[t]] = [(q2[t].split('###'))[0], (q2[t].split('###'))[1]]
        for t in range(len(dessink)):
            y4[dessink[t]] = [(q3[t].split('###'))[0], (q3[t].split('###'))[1]]
    else:
        print(len(q0) == len(nonveg), len(q1) == len(veg), len(q2) == len(seafood), len(q3) == len(dessink))

    os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\MySQL\MySQL Server 5.7\MySQL 5.7 Command Line Client")
    sleep(3)
    for i in password:
        pr(i)
    pr(Key.enter)
    sleep(0.5)
    create = 'create database foodiepedia;'
    for i in create:
    	pr(i)
    pr(Key.enter)
    sleep(2)
    

    cc = 'use foodiepedia;'
    for i in cc:
        pr(i)
    pr(Key.enter)
    table1 = "create table veg(dish varchar(100), ingredients varchar(7000), recipe varchar(9000));"
    table2 = "create table nonveg(dish varchar(100), ingredients varchar(7000), recipe varchar(9000));"
    table3 = "create table seafood(dish varchar(100), ingredients varchar(7000), recipe varchar(9000));"
    table4 = "create table desserts(dish varchar(100), ingredients varchar(7000), recipe varchar(9000));"
    for i in table1:
        pr(i)
    pr(Key.enter)
    sleep(2)
    for i in table2:
        pr(i)
    pr(Key.enter)
    sleep(2)
    for i in table3:
        pr(i)
    pr(Key.enter)
    sleep(2)
    for i in table4:
        pr(i)
    pr(Key.enter)
    sleep(2)
    for j in y1:
        d1 = ('insert into nonveg'+' values(\''+str(j)+'\', \''+y1[j][0]+'\', \''+y1[j][1]+'\')')
        for i in d1:
            pr(i)
        sleep(3)
        pr(';')
        pr(Key.enter)
    sleep(2)
    for j in y2:
        d1 = ('insert into veg'+' values(\''+str(j)+'\', \''+y2[j][0]+'\', \''+y2[j][1]+'\')')
        for i in d1:
            pr(i)
        sleep(3)
        pr(';')
        pr(Key.enter)
    sleep(1)
    for j in y3:
        d1 = ('insert into seafood'+' values(\''+str(j)+'\', \''+y3[j][0]+'\', \''+y3[j][1]+'\')')
        for i in d1:
            pr(i)
        sleep(3)
        pr(';')
        pr(Key.enter)
    sleep(1)
    for j in y4:
        d1 = ('insert into desserts'+' values(\''+str(j)+'\', \''+y4[j][0]+'\', \''+y4[j][1]+'\')')
        for i in d1:
            pr(i)
        sleep(2)
        pr(';')
        pr(Key.enter)
    sleep(2)
a = 'school'
create_database(a)