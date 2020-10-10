import tkinter as tk
from datetime import datetime
from tkinter import ttk
from ttkthemes import ThemedTk
from pytz import timezone
from tkinter import colorchooser

curr_design=open("./objects(Do_not_delete)/theme.thm","r").read()
curr_design=curr_design.split("_")
curr_desno=curr_design[0]
curr_design=curr_design[1]

fontcolor = open('./objects(Do_not_delete)/fontcolor.fnt', "r").read()
fontcolor = str(fontcolor)

fonttype=open('./objects(Do_not_delete)/fonttype.fnt', "r").read()
fonttype=str(fonttype)
fonttype=fonttype.split("_")
fontno=fonttype[0]
fonttype=fonttype[1]

root = ThemedTk()
root.get_themes()
root.set_theme(curr_design)
root.title("G World clock")
root.iconbitmap('./objects(Do_not_delete)/icon.ico')
root.resizable(False, False)
root.geometry("300x300")
root.config(themebg=curr_design)

systime = True
dubai_time=False
india_time = False
kuwait_time = False
newyork_time = False
los_time=False
mexico_time=False
tokyo_time=False

def settings():
    curr_design = open("./objects(Do_not_delete)/theme.thm", "r").read()
    curr_design = curr_design.split("_")
    curr_desno = curr_design[0]
    curr_design = curr_design[1]

    setting_win = ThemedTk()
    setting_win.get_themes()
    setting_win.set_theme(curr_design)
    setting_win.title("Settings")
    setting_win.iconbitmap('./objects(Do_not_delete)/icon2.ico')
    setting_win.config(themebg=curr_design)
    setting_win.geometry("500x500")

    type = ttk.Notebook(setting_win, width=500, height=500)
    type.grid(row=1, column=1)

    frame_col = ttk.Frame(setting_win)
    frame_col.place(relheight=1, relwidth=1)

    frame_fnt = ttk.Frame(setting_win)
    frame_fnt.place(relheight=1, relwidth=1)

    type.add(frame_col, text="Design")
    type.add(frame_fnt, text="Time font")

    def design_widgets():
        info1=ttk.Label(frame_col,text="Theme:")
        info1.place(relx=0.1,rely=0.1)

        def apply():
            theme_ch=theme_now.get().lower()

            if theme_ch=='black':
                curr_design = open("./objects(Do_not_delete)/theme.thm", "w").write('1_black')
                curr_design = open("./objects(Do_not_delete)/theme.thm", "r").read()
                curr_design = curr_design.split("_")
                curr_desno = curr_design[0]
                curr_design = curr_design[1]
                theme_now.set(theme_av[int(curr_desno)])
                root.get_themes()
                root.set_theme(curr_design)
                root.config(themebg=curr_design)
                setting_win.get_themes()
                setting_win.set_theme(curr_design)
                setting_win.config(themebg=curr_design)

            elif theme_ch=='light':
                curr_design = open("./objects(Do_not_delete)/theme.thm", "w").write('2_plastik')
                curr_design = open("./objects(Do_not_delete)/theme.thm", "r").read()
                curr_design = curr_design.split("_")
                curr_desno = curr_design[0]
                curr_design = curr_design[1]
                theme_now.set(theme_av[int(curr_desno)])
                root.get_themes()
                root.set_theme(curr_design)
                root.config(themebg=curr_design)
                setting_win.get_themes()
                setting_win.set_theme(curr_design)
                setting_win.config(themebg=curr_design)

            elif theme_ch=='kroc':
                curr_design = open("./objects(Do_not_delete)/theme.thm", "w").write('3_kroc')
                curr_design = open("./objects(Do_not_delete)/theme.thm", "r").read()
                curr_design = curr_design.split("_")
                curr_desno = curr_design[0]
                curr_design = curr_design[1]
                theme_now.set(theme_av[int(curr_desno)])
                root.get_themes()
                root.set_theme(curr_design)
                root.config(themebg=curr_design)
                setting_win.get_themes()
                setting_win.set_theme(curr_design)
                setting_win.config(themebg=curr_design)

            elif theme_ch=='equilux':
                curr_design = open("./objects(Do_not_delete)/theme.thm", "w").write('4_equilux')
                curr_design = open("./objects(Do_not_delete)/theme.thm", "r").read()
                curr_design = curr_design.split("_")
                curr_desno = curr_design[0]
                curr_design = curr_design[1]
                theme_now.set(theme_av[int(curr_desno)])
                root.get_themes()
                root.set_theme(curr_design)
                root.config(themebg=curr_design)
                setting_win.get_themes()
                setting_win.set_theme(curr_design)
                setting_win.config(themebg=curr_design)


        theme_av=['','Black', 'Light', 'Kroc','Equilux']
        theme_now=tk.StringVar(frame_col)
        theme=ttk.OptionMenu(frame_col,theme_now,*theme_av)
        theme.place(relx=0.3,rely=0.1)
        theme_now.set(theme_av[int(curr_desno)])

        apply_btn=ttk.Button(frame_col,text="Apply Change",command=apply)
        apply_btn.place(relx=0.1,rely=0.3)

    design_widgets()

    def font_add():
        color_select=""

        def colorpie():
            global color_select
            color_select = colorchooser.askcolor()[1]

        def apply2(type_now):
            global color_select
            type_now=type_now.split(".")
            typen_now=type_now[0]
            type_now=type_now[1]

            fonttype = open('./objects(Do_not_delete)/fonttype.fnt', "w").write(typen_now+"_"+type_now+" "+"40")
            fontcolor = open('./objects(Do_not_delete)/fontcolor.fnt', "w").write(color_select)

            fontcolor = open('./objects(Do_not_delete)/fontcolor.fnt', "r").read()
            fontcolor = str(fontcolor)

            fonttype = open('./objects(Do_not_delete)/fonttype.fnt', "r").read()
            fonttype = str(fonttype)
            fonttype = fonttype.split("_")
            fontno = fonttype[0]
            fonttype = fonttype[1]

            prev.configure(font=fonttype,foreground=fontcolor)
            clock.configure(font=fonttype, foreground=fontcolor)

        prev=ttk.Label(frame_fnt, text='Text preview', font=fonttype, foreground=fontcolor)
        prev.place(relx=0.1,rely=0.1)

        info_color=ttk.Label(frame_fnt,text="Font Color:")
        info_color.place(relx=0.1,rely=0.3)
        chose=ttk.Button(frame_fnt,text="Choose a color",command=colorpie)
        chose.place(relx=0.3,rely=0.3)

        types=['','1.Ariel','2.Verdana','3.Times']
        type_now=tk.StringVar(frame_fnt)
        info_type=ttk.Label(frame_fnt,text="Font type:")
        info_type.place(relx=0.1,rely=0.5)
        chose_type= ttk.OptionMenu(frame_fnt,type_now,*types)
        chose_type.place(relx=0.3, rely=0.5)
        type_now.set(types[int(fontno)])

        apply_btn=ttk.Button(frame_fnt,text='Apply changes',command=lambda:apply2(type_now.get().lower()))
        apply_btn.place(relx=0.1,rely=0.7)

    font_add()


def tick():
    if systime:
        time = datetime.now().strftime("%H:%M:%S")
        clock.config(text=time)
        clock.after(200, tick)

def dubai():
    if dubai_time:
        time = datetime.now(timezone('Asia/Dubai')).strftime("%H:%M:%S")
        clock.config(text=time)
        clock.after(200, dubai)

def india():
    if india_time:
        time = datetime.now(timezone('Asia/Calcutta')).strftime("%H:%M:%S")
        clock.config(text=time)
        clock.after(200, india)


def kuwait():
    if kuwait_time:
        time = datetime.now(timezone('Asia/Kuwait')).strftime("%H:%M:%S")
        clock.config(text=time)
        clock.after(200, kuwait)


def newyork():
    if newyork_time:
        time = datetime.now(timezone('America/New_York')).strftime("%H:%M:%S")
        clock.config(text=time)
        clock.after(200, newyork)

def losangeles():
    if los_time:
        time = datetime.now(timezone('America/Los_Angeles')).strftime("%H:%M:%S")
        clock.config(text=time)
        clock.after(200, losangeles)

def mexico():
    if mexico_time:
        time = datetime.now(timezone('America/Mexico_city')).strftime("%H:%M:%S")
        clock.config(text=time)
        clock.after(200, mexico)

def tokyo():
    if tokyo_time:
        time = datetime.now(timezone('Asia/Tokyo')).strftime("%H:%M:%S")
        clock.config(text=time)
        clock.after(200, tokyo)

def settime():
    global systime
    global dubai_time
    global india_time
    global kuwait_time
    global newyork_time
    global los_time
    global mexico_time
    global tokyo_time

    time_list = now.get().lower()
    if time_list == 'system time':
        systime = True
        india_time = False
        kuwait_time = False
        newyork_time = False
        los_time=False
        mexico_time=False
        tokyo_time=False
        dubai_time=False
        tick()
    if time_list == 'india':
        systime = False
        india_time = True
        kuwait_time = False
        newyork_time = False
        los_time = False
        mexico_time = False
        tokyo_time = False
        dubai_time=False
        india()
    if time_list == 'kuwait':
        systime = False
        india_time = False
        kuwait_time = True
        newyork_time = False
        los_time = False
        mexico_time = False
        tokyo_time = False
        dubai_time=False
        kuwait()
    if time_list == 'new york':
        systime = False
        india_time = False
        kuwait_time = False
        newyork_time = True
        los_time = False
        mexico_time = False
        tokyo_time = False
        dubai_time=False
        newyork()
    if time_list=='los angeles':
        systime = False
        india_time = False
        kuwait_time = False
        newyork_time = False
        los_time = True
        mexico_time = False
        tokyo_time = False
        dubai_time=False
        losangeles()

    if time_list=='mexico':
        systime = False
        india_time = False
        kuwait_time = False
        newyork_time = False
        los_time = False
        mexico_time = True
        tokyo_time = False
        dubai_time=False
        mexico()

    if time_list=='tokyo':
        systime = False
        india_time = False
        kuwait_time = False
        newyork_time = False
        los_time = False
        mexico_time = False
        tokyo_time = True
        dubai_time=False
        tokyo()

    if time_list=='dubai':
        systime = False
        india_time = False
        kuwait_time = False
        newyork_time = False
        los_time = False
        mexico_time = False
        tokyo_time = False
        dubai_time=True
        dubai()

clock = ttk.Label(root, font=fonttype, foreground=fontcolor)
clock.place(relx=0.1, rely=0.1)

help = ttk.Label(root, text="Select a time from the list and click on Set time")
help.place(relx=0.1, rely=0.5)

now = tk.StringVar(root)
values = ['System time', 'System time', 'India', 'Kuwait', 'New York','Los Angeles','Mexico','Tokyo','Dubai']
now.set(values[0])

times = ttk.OptionMenu(root, now, *values)
times.place(relx=0.1, rely=0.7)

time_set = ttk.Button(root, text="Set time", command=settime)
time_set.place(relx=0.5, rely=0.7)

settings_btn = ttk.Button(root, text="Settings", command=settings)
settings_btn.place(relx=0.1, rely=0.8)

tick()

root.mainloop()
