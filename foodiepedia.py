from tkinter import *
import tkinter.ttk as ttk
from tkinter.font import Font
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from tkinter.filedialog import askopenfilename
import sql_functions as sq
from tkinter import messagebox
global cuisine

def foodiepedia():
    def dessertClick():
        global cuisine
        cuisine='desserts'

        window_d = Toplevel()
        window_d.config(bg='gray')
        window_d.title('DESERT SECTION')

        title_frame_d = Frame(window_d)
        title_frame_d.config(bg='white')

        titlelabel_d= Label(window_d, text='FOODIEPEDIA', font='Gabriola 28')

        titlelabel_d.config(bg='white')
        titlelabel_d.pack(fill='x')

        res = sq.dessert()
        Item_List = res.split('\n')
        for i in Item_List:
            Item_List[Item_List.index(i)]=i.lower()
        fontStyle = Font(family="Lucida Grande", size=16, weight='bold')
        window_header = Label(window_d, text="PLEASE SELECT A DISH FROM THE MENU" + '\n', font=fontStyle)
        window_header.pack(fill='x')
        fontStyle = Font(family="Helvatica", size=14)
        window_label = Label(window_d, text=res + '\n', font=fontStyle)
        window_label.pack(fill='x')

        button_frame = Frame(window_d,background='grey')

        add_icon = PhotoImage(file=r"add.png")
        delete_icon = PhotoImage(file=r"delete.png")
        edit_icon = PhotoImage(file=r"edit.png")

        button3 = Button(button_frame, image=add_icon, command=add)
        button3.grid(row=0,column=2,padx=50,pady=5)
        
        button4 = Button(button_frame, image=delete_icon, command=delete)
        button4.grid(row=0,column=1,padx=50,pady=5)

        button5 = Button(button_frame, image=edit_icon, command=edit)
        button5.grid(row=0,column=0,padx=50,pady=5)

        button_frame.pack(anchor='se',fill='x')

        ttk.Separator(window_d, orient='horizontal').pack(expand='true',fill='x',ipady=5)

        # input box
        window_label2 = Label(window_d, text="Enter Dish Name", font=fontStyle)
        window_label2.pack(fill='x', padx=10, side=LEFT, pady=10, expand=TRUE)
        inputBox = Entry(window_d)
        inputBox.pack(fill='x', padx=10, side=LEFT, expand=TRUE)

        def resultWin_desserts():
            if (inputBox.get()).lower() in Item_List:
                window_res = Tk()
                window_res.config(bg='gray')
                window_res.title('RESULT')
                window_res.state("zoomed")

                title_frame_d = Frame(window_res)
                title_frame_d.config(bg='white')

                titlelabel_d = Label(window_res, text=(inputBox.get()).upper(), font='Gabriola 28')

                titlelabel_d.config(bg='white')
                titlelabel_d.pack(fill='x')

                scrollbar1 = Scrollbar(window_res, orient='vertical')
                scrollbar2 = Scrollbar(window_res, orient='vertical')

                ingredients = sq.desserts_ingred(inputBox.get())
                recipe = sq.desserts_recipe(inputBox.get())
                window_header1 = Label(window_res, text="\t   INGREDIENTS \t\t\t\t\t     RECIPE \t \t \t" , bg='grey',font='Gabriola 28', anchor='nw')
                window_header1.pack(fill='x')

                window_label1 = Text(window_res, font=("Helvatica",15), borderwidth=6, bg='white', wrap='word', width=50, height=27)
                window_label1.insert('end', ingredients)
                window_label1.configure(state="disabled")
                window_label1.config(yscrollcommand=scrollbar2.set)

                window_label2 = Text(window_res, font=("Helvatica",15), borderwidth=6, bg='white', wrap='word', width=50, height=27)
                window_label2.insert('end', recipe)
                window_label2.configure(state="disabled")
                window_label2.config(yscrollcommand=scrollbar1.set)

                window_label1.pack(fill='x', side='left')
                scrollbar2.config(command=window_label1.yview)
                scrollbar2.pack(fill='y', side='left', padx=3)
                scrollbar1.config(command=window_label2.yview)
                scrollbar1.pack(fill='y', side='right')
                window_label2.pack(fill='x')
                window_res.mainloop()
            else:
                online = messagebox.askyesno("Not Found", "Sorry, not in our menu.\nSearch online?")
                if online:
                    wait = messagebox.showinfo('Loading', 'Please wait.')
                    driver = webdriver.Chrome(ChromeDriverManager().install())
                    driver.get("https://www.google.com/search?q=" + inputBox.get().replace(' ', '+'))
        #window_d.bind("<Return>", resultWin_desserts)
        window_button = Button(window_d, text = 'SEARCH', command = resultWin_desserts)

        window_button.pack(fill = 'x', padx = 15, pady=15, expand = TRUE)
        window_d.mainloop()

    def seafoodClick():
        global cuisine
        cuisine='seafood'

        window_sf = Toplevel()
        window_sf.config(bg='gray')
        window_sf.title('SEAFOOD SECTION')

        title_frame_sf = Frame(window_sf)
        title_frame_sf.config(bg='white')

        titlelabel_sf = Label(window_sf, text='FOODIEPEDIA', font='Gabriola 28')

        titlelabel_sf.config(bg='white')
        titlelabel_sf.pack(fill='x')

        res = sq.seafood()
        Item_List = res.split('\n')
        for i in Item_List:
            Item_List[Item_List.index(i)]=i.lower()
        fontStyle = Font(family="Lucida Grande", size=16, weight='bold')
        window_header = Label(window_sf, text="PLEASE SELECT A DISH FROM THE MENU" + '\n', font=fontStyle)
        window_header.pack(fill='x')
        fontStyle = Font(family="Helvatica", size=14)
        window_label = Label(window_sf, text=res + '\n', font=fontStyle)
        window_label.pack(fill='x')

        button_frame = Frame(window_sf,background='grey')

        add_icon = PhotoImage(file=r"add.png")
        button3 = Button(button_frame, image=add_icon, command=add)
        button3.grid(row=0,column=2,padx=50,pady=5)

        delete_icon = PhotoImage(file=r"delete.png")
        button4 = Button(button_frame, image=delete_icon, command=delete)
        button4.grid(row=0,column=1,padx=50,pady=5)

        edit_icon = PhotoImage(file=r"edit.png")
        button5 = Button(button_frame, image=edit_icon, command=edit)
        button5.grid(row=0,column=0,padx=50,pady=5)

        button_frame.pack(anchor='se',fill='x')

        ttk.Separator(window_sf, orient='horizontal').pack(expand='true',fill='x',ipady=5)

        # input box
        window_label2 = Label(window_sf, text="Enter Dish Name", font=fontStyle)
        window_label2.pack(fill='x', padx=10, side=LEFT, pady=10, expand=TRUE)
        inputBox = Entry(window_sf)
        inputBox.pack(fill='x', padx=10, side=LEFT, expand=TRUE)
        def resultWin_seafood():
            if (inputBox.get()).lower() in Item_List:
                window_res = Tk()
                window_res.config(bg='gray')
                window_res.title('RESULT')
                window_res.state("zoomed")

                title_frame_d = Frame(window_res)
                title_frame_d.config(bg='white')

                titlelabel_d = Label(window_res, text=(inputBox.get()).upper(), font='Gabriola 28')

                titlelabel_d.config(bg='white')
                titlelabel_d.pack(fill='x')

                scrollbar1 = Scrollbar(window_res, orient='vertical')
                scrollbar2 = Scrollbar(window_res, orient='vertical')

                ingredients = sq.seafood_ingred(inputBox.get())
                recipe = sq.seafood_recipe(inputBox.get()) #.split('\n')
                window_header1 = Label(window_res, text="\t   INGREDIENTS \t\t\t\t\t     RECIPE \t \t \t", bg='grey', font='Gabriola 28', anchor='nw')
                window_header1.pack(fill='x')

                window_label1 = Text(window_res, font=("Helvatica",15), borderwidth=6, bg='white', wrap='word', width=50, height=27)
                window_label1.insert('end', ingredients)
                window_label1.configure(state="disabled")
                window_label1.config(yscrollcommand=scrollbar2.set)

                window_label2 = Text(window_res, font=("Helvatica",15), borderwidth=6, bg='white', wrap='word', width=50, height=27)
                window_label2.insert('end', recipe)
                window_label2.configure(state="disabled")
                window_label2.config(yscrollcommand=scrollbar1.set)

                window_label1.pack(fill='x', side='left')
                scrollbar2.config(command=window_label1.yview)
                scrollbar2.pack(fill='y', side='left', padx=3)
                scrollbar1.config(command=window_label2.yview)
                scrollbar1.pack(fill='y', side='right')
                window_label2.pack(fill='x')
                window_res.mainloop()
            else:
                online = messagebox.askyesno("Not Found", "Sorry, not in our menu.\nSearch online?")
                if online:
                    wait = messagebox.showinfo('Loading', 'Please wait.')
                    driver = webdriver.Chrome(ChromeDriverManager().install())
                    driver.get("https://www.google.com/search?q=" + inputBox.get().replace(' ', '+'))

        window_button = Button(window_sf, text='SEARCH', command=resultWin_seafood)

        window_button.pack(fill='x', padx=15, pady=15, expand=TRUE)

        window_sf.mainloop()

    def nonvegClick():
        global cuisine
        cuisine='nonveg'

        window_nveg = Toplevel()
        window_nveg.config(bg='gray')
        window_nveg.title('NON-VEGETARIAN SECTION')

        title_frame_nveg = Frame(window_nveg)
        title_frame_nveg.config(bg='white')

        titlelabel_nveg = Label(window_nveg, text='FOODIEPEDIA', font='Gabriola 28')

        titlelabel_nveg.config(bg='white')
        titlelabel_nveg.pack(fill='x')

        res = sq.nonveg()
        Item_List = res.split('\n')
        for i in Item_List:
            Item_List[Item_List.index(i)]=i.lower()
        fontStyle = Font(family="Lucida Grande", size=16, weight='bold')
        window_header = Label(window_nveg, text="PLEASE SELECT A DISH FROM THE MENU" + '\n', font=fontStyle)
        window_header.pack(fill='x')
        fontStyle = Font(family="Helvatica", size=14)
        window_label = Label(window_nveg, text=res + '\n', font=fontStyle)
        window_label.pack(fill='x')

        button_frame = Frame(window_nveg,background='grey')

        add_icon = PhotoImage(file=r"add.png")
        button3 = Button(button_frame, image=add_icon, command=add)
        button3.grid(row=0,column=2,padx=50,pady=5)

        delete_icon = PhotoImage(file=r"delete.png")
        button4 = Button(button_frame, image=delete_icon, command=delete)
        button4.grid(row=0,column=1,padx=50,pady=5)

        edit_icon = PhotoImage(file=r"edit.png")
        button5 = Button(button_frame, image=edit_icon, command=edit)
        button5.grid(row=0,column=0,padx=50,pady=5)

        button_frame.pack(anchor='se',fill='x')

        ttk.Separator(window_nveg, orient='horizontal').pack(expand='true',fill='x',ipady=5)

        # input box
        window_label2 = Label(window_nveg, text="Enter Dish Name", font=fontStyle)
        window_label2.pack(fill='x', padx=10, side=LEFT, pady=10, expand=TRUE)
        inputBox = Entry(window_nveg)
        inputBox.pack(fill='x', padx=10, side=LEFT, expand=TRUE)
        def resultWin_nonveg():
            if (inputBox.get()).lower() in Item_List:
                window_res = Tk()
                window_res.config(bg='gray')
                window_res.title('RESULT')
                window_res.state("zoomed")

                title_frame_d = Frame(window_res)
                title_frame_d.config(bg='white')

                titlelabel_d = Label(window_res, text=(inputBox.get()).upper(), font='Gabriola 28')

                titlelabel_d.config(bg='white')
                titlelabel_d.pack(fill='x')

                scrollbar1 = Scrollbar(window_res, orient='vertical')
                scrollbar2 = Scrollbar(window_res, orient='vertical')

                ingredients = sq.nonveg_ingred(inputBox.get())
                recipe = sq.nonveg_recipe(inputBox.get())
                window_header1 = Label(window_res, text="\t   INGREDIENTS \t\t\t\t\t     RECIPE \t \t \t", bg='grey', font='Gabriola 28', anchor='nw')
                window_header1.pack(fill='x')

                window_label1 = Text(window_res, font=("Helvatica",15), borderwidth=6, bg='white', wrap='word', width=50, height=27)
                window_label1.insert('end', ingredients)
                window_label1.configure(state="disabled")
                window_label1.config(yscrollcommand=scrollbar2.set)

                window_label2 = Text(window_res, font=("Helvatica",15), borderwidth=6, bg='white', wrap='word', width=50, height=27)
                window_label2.insert('end', recipe)
                window_label2.configure(state="disabled")
                window_label2.config(yscrollcommand=scrollbar1.set)

                window_label1.pack(fill='x', side='left')
                scrollbar2.config(command=window_label1.yview)
                scrollbar2.pack(fill='y', side='left', padx=3)
                scrollbar1.config(command=window_label2.yview)
                scrollbar1.pack(fill='y', side='right')
                window_label2.pack(fill='x')
                window_res.mainloop()
            else:
                online = messagebox.askyesno("Not Found", "Sorry, not in our menu.\nSearch online?")
                if online:
                    wait = messagebox.showinfo('Loading', 'Please wait.')
                    driver = webdriver.Chrome(ChromeDriverManager().install())
                    driver.get("https://www.google.com/search?q=" + inputBox.get().replace(' ', '+'))

        window_button = Button(window_nveg, text='SEARCH', command=resultWin_nonveg)
        window_button.pack(fill='x', padx=15, pady=15, expand=TRUE)
        window_nveg.mainloop()

    def vegClick():
        global cuisine
        cuisine='veg'

        window_veg=Toplevel()
        window_veg.config(bg='gray')
        window_veg.title('VEGETARIAN SECTION')

        title_frame_veg=Frame(window_veg)
        title_frame_veg.config(bg='white')

        titlelabel_veg = Label(window_veg, text='FOODIEPEDIA', font='Gabriola 28')
        titlelabel_veg.config(bg='white')
        titlelabel_veg.pack(fill='x')
        res = sq.veg()
        Item_List = res.split('\n')
        for i in Item_List:
            Item_List[Item_List.index(i)]=i.lower()

        fontStyle = Font(family="Lucida Grande", size=16, weight = 'bold')
        window_header = Label(window_veg, text = "PLEASE SELECT A DISH FROM THE MENU" + '\n', font=fontStyle)
        window_header.pack(fill='x')
        fontStyle = Font(family="Helvatica", size=14)
        window_label = Label(window_veg, text = res + '\n', font=fontStyle)
        window_label.pack(fill='x')

        button_frame = Frame(window_veg,background='grey')

        add_icon = PhotoImage(file=r"add.png")
        button3 = Button(button_frame, image=add_icon, command=add)
        button3.grid(row=0,column=2,padx=50,pady=5)

        delete_icon = PhotoImage(file=r"delete.png")
        button4 = Button(button_frame, image=delete_icon, command=delete)
        button4.grid(row=0,column=1,padx=50,pady=5)

        edit_icon = PhotoImage(file=r"edit.png")
        button5 = Button(button_frame, image=edit_icon, command=edit)
        button5.grid(row=0,column=0,padx=50,pady=5)

        button_frame.pack(anchor='se',fill='x')

        ttk.Separator(window_veg, orient='horizontal').pack(expand='true',fill='x',ipady=5)

        #input box
        window_label2 = Label(window_veg, text = "Enter Dish Name", font=fontStyle, bg='white')
        window_label2.pack(fill = 'x',padx = 10, side = LEFT, pady = 10, expand = TRUE)
        inputBox = Entry(window_veg)
        inputBox.pack(fill = 'x', padx = 10, side = LEFT, expand = TRUE)
        def resultWin_veg():
            if (inputBox.get()).lower() in Item_List:
                window_res = Tk()
                window_res.config(bg='gray')
                window_res.title('RESULT')
                window_res.state("zoomed")

                title_frame_d = Frame(window_res)
                title_frame_d.config(bg='white')

                titlelabel_d = Label(window_res, text=(inputBox.get()).upper(), font='Gabriola 28')

                titlelabel_d.config(bg='white')
                titlelabel_d.pack(fill='x')

                scrollbar1 = Scrollbar(window_res, orient='vertical')
                scrollbar2 = Scrollbar(window_res, orient='vertical')

                ingredients = sq.veg_ingred(inputBox.get())
                recipe = sq.veg_recipe(inputBox.get())
                window_header1 = Label(window_res, text="\t   INGREDIENTS \t\t\t\t\t     RECIPE \t \t \t", bg='grey',font='Gabriola 28', anchor='nw')
                window_header1.pack(fill='x')

                window_label1 = Text(window_res, font=("Helvatica",15), borderwidth=6, bg='white', wrap='word', width=50, height=27)
                window_label1.insert('end', ingredients)
                window_label1.configure(state="disabled")
                window_label1.config(yscrollcommand=scrollbar2.set)

                window_label2 = Text(window_res, font=("Helvatica",15), borderwidth=6, bg='white', wrap='word', width=50, height=27)
                window_label2.insert('end', recipe)
                window_label2.configure(state="disabled")
                window_label2.config(yscrollcommand=scrollbar1.set)

                window_label1.pack(fill='x', side='left')
                scrollbar2.config(command=window_label1.yview)
                scrollbar2.pack(fill='y', side='left', padx=3)
                scrollbar1.config(command=window_label2.yview)
                scrollbar1.pack(fill='y', side='right')
                window_label2.pack(fill='x')
                window_res.mainloop()
            else:
                online = messagebox.askyesno("Not Found", "Sorry, not in our menu.\nSearch online?")
                if online:
                    wait = messagebox.showinfo('Loading','Please wait.')
                    driver = webdriver.Chrome(ChromeDriverManager().install())
                    driver.get("https://www.google.com/search?q="+ inputBox.get().replace(' ','+'))

        window_button = Button(window_veg, text='SEARCH', command=resultWin_veg)
        window_button.pack(fill='x', padx=15, pady=15, expand=TRUE)

        window_veg.mainloop()
    
    def add():
        global cuisine
        cuisine = 'veg'
        cuisines = {'veg','nonveg','seafood','desserts'}

        add_window=Tk()
        add_window.title('FOODIEPEDIA')
        add_window.config(bg='gray')

        titleframe = Frame(add_window)
        titleframe.pack()

        titlelabel = Label(add_window, text='FOODIEPEDIA',font='Gabriola 26')
        titlelabel.pack(fill='x')

        frame1 = Frame(add_window,highlightbackground='black',highlightthickness=3)
        frame2 = Frame(add_window,highlightbackground='black',highlightthickness=3)
        frame3 = Frame(add_window,highlightbackground='black',highlightthickness=3)
        frame4 = Frame(add_window,highlightbackground='black',highlightthickness=3)

        global cuisine_var, dish_var
        x = {'veg':sq.veg(),'nonveg':sq.nonveg(),'seafood':sq.seafood(),'desserts':sq.dessert()}
        cuisine_var = StringVar(add_window)
        cuisine_var.set(cuisine)
        dish_var = x[cuisine]
        cuisine_menu = OptionMenu(frame1,cuisine_var,*cuisines)
        Label(frame1,text="Choose cuisine: ",font=("Helvatica",15)).pack(side='left',padx=50)
        cuisine_menu.pack(side='right',ipadx=30)

        def cuisine_change(*args):
            global dish_var, cuisine_var, dishes
            dish_var = x[cuisine_var.get()]
            dishes = dish_var.split('\n')
           

        cuisine_var.trace('w',cuisine_change)
        #print(dishes)
        dishes = dish_var.split('\n')
        Label(frame2).grid(row=0,column=1,padx=80)
        Label(frame2,text="Enter dish name: ",font=("Helvatica",15)).grid(row=0,column=0,padx=50,sticky='w')
        Label(frame2).grid(row=0,column=2,sticky='e',ipadx=220)
        dish_name = Entry(frame2)
        dish_name.grid(row=0,column=2,sticky='e',ipadx=80)


        global text, rec
        rec = False
        text = 'Enter Ingredients'
        text_label = Label(frame3, text = text, font =("Helvatica",15)).grid(row=0,column=0)
        widget = Text(frame3, font=("Helvatica",15), borderwidth=6, bg='white', wrap='word', width=80, height=15)

        def done():
            global text, rec, cuisine_var, ing_get
            if rec:
                rec_get = widget.get('1.0','end')
                sq.add(cuisine_var.get(), dish_name.get(), ing_get, rec_get)
                widget.delete('1.0','end')
                x = messagebox.showinfo('Done!', 'Database edited!')
                try:
                    add_window.destroy()
                except:
                    pass
            else:
                ing_get = widget.get('1.0','end')
                text = 'Enter Recipe'
                text_label = Label(frame3, text = text, font =("Helvatica",15)).grid(row=0,column=0,ipadx=25)
                widget.delete('1.0','end')
                rec = True
        def clear():
            widget.delete('1.0','end')
        def Import():
            name = askopenfilename(filetypes=(("Text File","*.txt"),("All Files","*.*")),
                                   title="Choose a file")
            try:
                file = open(name,'r')
                file.seek(0)
                widget.delete('1.0','end')
                widget.insert('1.0', file.read())
            except:
                messagebox.showerror(title='Error',message='File not found!')

        B_done = Button(frame4,text="Done",command=done,font=("Helvatica",15)).grid(row=0,column=0,padx=90)
        B_clear = Button(frame4,text="Clear",command=clear,font=("Helvatica",15)).grid(row=0,column=1,padx=90)
        B_import = Button(frame4,text="Import",command=Import,font=("Helvatica",15)).grid(row=0,column=2,padx=90)

        #frame1.grid(row=0,column=0,columnspan=3,rowspan=2)
        frame1.pack(fill='x',expand=True,padx=10,pady=4)
        frame2.pack(fill='x',expand=True,padx=10,pady=4)
        frame3.pack(fill='x',expand=True,padx=10,pady=4)
        widget.grid(row=1,column=0,padx=10,pady=4)
        frame4.pack(fill='x',expand=True,padx=10,pady=4)

    def edit():
        global cuisine
        cuisines = {'veg','nonveg','seafood','desserts'}

        window_dConfig=Tk()
        window_dConfig.title('FOODIEPEDIA')
        window_dConfig.config(bg='gray')

        titleframe = Frame(window_dConfig)
        titleframe.pack()

        titlelabel = Label(window_dConfig, text='FOODIEPEDIA',font='Gabriola 26')
        titlelabel.pack(fill='x')

        frame1 = Frame(window_dConfig,highlightbackground='black',highlightthickness=3)
        frame2 = Frame(window_dConfig,highlightbackground='black',highlightthickness=3)
        frame3 = Frame(window_dConfig,highlightbackground='black',highlightthickness=3)
        frame4 = Frame(window_dConfig,highlightbackground='black',highlightthickness=3)

        global cuisine_var, dish_var
        x = {'veg':sq.veg(),'nonveg':sq.nonveg(),'seafood':sq.seafood(),'desserts':sq.dessert()}
        cuisine_var = StringVar(window_dConfig)
        cuisine_var.set(cuisine)
        dish_var = x[cuisine]
        cuisine_menu = OptionMenu(frame1,cuisine_var,*cuisines)
        Label(frame1,text="Choose cuisine: ",font=("Helvatica",15)).pack(side='left',padx=50)
        cuisine_menu.pack(side='right',ipadx=30)

        def cuisine_change(*args):
            global dish_var, cuisine_var, dishes
            dish_var = x[cuisine_var.get()]
            dishes = dish_var.split('\n')
            tkvar = StringVar(window_dConfig)
            Label(frame2).grid(row=0,column=2,sticky='e',ipadx=220,ipady=3)
            dish_menu = OptionMenu(frame2,tkvar,*dishes)
            dish_menu.grid(row=0,column=2,sticky='e',ipadx=80)

        cuisine_var.trace('w',cuisine_change)
        #print(dishes)
        global tkvar
        tkvar = StringVar(window_dConfig)
        dishes = dish_var.split('\n')
        Label(frame2).grid(row=0,column=1,padx=80)
        Label(frame2,text="Select Dish: ",font=("Helvatica",15)).grid(row=0,column=0,padx=50,sticky='w')
        Label(frame2).grid(row=0,column=2,sticky='e',ipadx=220)
        dish_menu = OptionMenu(frame2,tkvar,*dishes)
        dish_menu.grid(row=0,column=2,sticky='e',ipadx=80)

        Label(frame3,text="Choose what you want to edit: ",font=("Helvatica",15)).grid(row=0,column=0,padx=20)
        global variable
        variable = IntVar(window_dConfig)
        variable.set(0)
        Label(frame3).grid(row=0,column=1,sticky='e',ipadx=60)
        bullet1 = Radiobutton(frame3,text='Dish Name',variable=variable,value=0).grid(row=0,column=2,sticky='w')
        bullet2 = Radiobutton(frame3,text='Ingredients',variable=variable,value=1).grid(row=1,column=2,sticky='w')
        bullet3 = Radiobutton(frame3,text='Recipe',variable=variable,value=2).grid(row=2,column=2,sticky='w')

        widget = Text(window_dConfig, font=("Helvatica",15), borderwidth=6, bg='white', wrap='word', width=50, height=15)

        '''global text
        text = ''
        global text
        text += widget.get()
        text += ' ### '
        widget.delete('1.0', 'end')'''
        def done():
            global variable, cuisine_var, tkvar
            if tkvar.get() != None:
                sq.edit(variable.get(),cuisine_var.get(),tkvar.get(),widget.get('1.0','end').strip('\n'))
                widget.delete('1.0', 'end')
                x = messagebox.showinfo('Done!', 'Database edited!')
                window_dConfig.destroy()
            else:
                x = messagebox.showerror('ERROR!','Make selection first.')
        def clear():
            widget.delete('1.0', 'end')
        def Import():
            name = askopenfilename(filetypes=(("Text File","*.txt"),("All Files","*.*")),
                                   title="Choose a file")
            try:
                file = open(name,'r')
                file.seek(0)
                widget.delete('1.0','end')
                widget.insert('1.0', file.read())
            except:
                messagebox.showerror(title='Error',message='File not found!')

        B_done = Button(frame4,text="Done",command=done,font=("Helvatica",15)).grid(row=0,column=0,padx=90)
        B_clear = Button(frame4,text="Clear",command=clear,font=("Helvatica",15)).grid(row=0,column=1,padx=90)
        B_import = Button(frame4,text="Import",command=Import,font=("Helvatica",15)).grid(row=0,column=2,padx=90)

        #frame1.grid(row=0,column=0,columnspan=3,rowspan=2)
        frame1.pack(fill='x',expand=True,padx=10,pady=4)
        frame2.pack(fill='x',expand=True,padx=10,pady=4)
        frame3.pack(fill='x',expand=True,padx=10,pady=4)
        widget.pack(fill='x',padx=10,pady=4)
        frame4.pack(fill='x',expand=True,padx=10,pady=4)

    def delete():
        global cuisine
        cuisines = {'veg', 'nonveg', 'seafood', 'desserts'}

        del_window = Tk()
        del_window.title('FOODIEPEDIA')
        del_window.config(bg='gray')

        titleframe = Frame(del_window)
        titleframe.pack()

        titlelabel = Label(del_window, text='FOODIEPEDIA', font='Gabriola 26')
        titlelabel.pack(fill='x')

        frame1 = Frame(del_window, highlightbackground='black', highlightthickness=3)
        frame2 = Frame(del_window, highlightbackground='black', highlightthickness=3)
        frame3 = Frame(del_window, highlightbackground='black', highlightthickness=3)

        global cuisine_var, dish_var
        x = {'veg': sq.veg(), 'nonveg': sq.nonveg(), 'seafood': sq.seafood(), 'desserts': sq.dessert()}
        cuisine_var = StringVar(del_window)
        cuisine_var.set(cuisine)
        dish_var = x[cuisine]
        cuisine_menu = OptionMenu(frame1, cuisine_var, *cuisines)
        Label(frame1, text="Choose cuisine: ", font=("Helvatica", 15)).pack(side='left', padx=50)
        cuisine_menu.pack(side='right', ipadx=30)

        def cuisine_change(*args):
            global dish_var, cuisine_var, dishes, tkvar
            dish_var = x[cuisine_var.get()]
            dishes = dish_var.split('\n')
            tkvar = StringVar(del_window)
            Label(frame2).grid(row=0, column=2, sticky='e', ipadx=100, ipady=3)
            dish_menu = OptionMenu(frame2, tkvar, *dishes)
            dish_menu.grid(row=0, column=2, sticky='e', ipadx=80)

        cuisine_var.trace('w', cuisine_change)
        # print(dishes)
        global tkvar
        tkvar = StringVar(del_window)
        dishes = dish_var.split('\n')
        Label(frame2).grid(row=0, column=1, padx=100)
        Label(frame2, text="Select Dish: ", font=("Helvatica", 15)).grid(row=0, column=0, padx=30, sticky='w')
        Label(frame2).grid(row=0, column=2, sticky='e', ipadx=100)
        dish_menu = OptionMenu(frame2, tkvar, *dishes)
        dish_menu.grid(row=0, column=2, sticky='e', ipadx=40)

        def del_dish():
            global cuisine_var, tkvar
            x = messagebox.askyesno('Confirm deletion','Are you sure you want to delete?')
            if x:
                sq.delete(cuisine_var.get(),tkvar.get())

        B_delete = Button(frame3, text="Delete", command=del_dish, font=("Helvatica", 12)).pack(fill='x')

        frame1.pack(fill='x', expand=True, padx=10, pady=8)
        frame2.pack(fill='x', expand=True, padx=10, pady=8)
        frame3.pack(fill='x', expand=True, padx=10, pady=8)

        del_window.mainloop()

    def HomePage():
        window=Tk()
        window.title('FOODIEPEDIA')
        window.config(bg='gray')

        font_style = Font(family="Gabriola", size=36)

        titleframe=Frame(window)
        titleframe.pack()

        titlelabel=Label(window, text='FOODIEPEDIA')
        #titlelabel.config(bg='cyan')
        titlelabel.pack(fill='x')
        titlelabel['font']=font_style

        b1img=PhotoImage(file=r"veg food.gif")
        #veg
        t1img=b1img.subsample(5,5)

        button1=Button(window,text='VEG', height=70 , width=350 , font='impact',image=t1img,command=vegClick)
        button1.pack(fill='y', padx =60 , pady= 20)

        b2img=PhotoImage(file=r"non-veg food.gif")
        #nonveg
        t2img=b2img.subsample(3,3)

        button2=Button(window,text='NON-VEG', height=70, width=350, font='impact', image=t2img,command=nonvegClick)
        button2.pack(fill='y', padx =60, pady= 20)

        b3img=PhotoImage(file=r"seafood.gif")
        #seafood.gif
        t3img=b3img.subsample(3,3)


        button3=Button(window,text='SEAFOOD', height=70, width=350, font='impact', image=t3img,command=seafoodClick)
        button3.pack(fill='y', padx =60, pady=20)

        b4img=PhotoImage(file=r"dessert.gif" )
        #dessert.gif
        t4img=b4img.subsample(3,3)

        button4=Button(window,text='DESERT', height=70, width=350,image=t4img,command=dessertClick)
        button4.pack(fill='y', padx =60, pady=20)

        '''button5=Button(window, text='Database configuration',command=configClick,font='Gabriola 15')
        button5.pack(padx=60,pady=10,anchor='se')'''

        bottomlabel=Label(window, text='TRUSTED RECIPES OF TOP CHEFS FROM AROUND THE WORLD!!')
        #bottomlabel.config(bg='cyan')
        bottomlabel['font']=font_style
        bottomlabel.pack(fill='both')

        window.mainloop()

    HomePage()


if __name__ == "__main__":
   foodiepedia()
