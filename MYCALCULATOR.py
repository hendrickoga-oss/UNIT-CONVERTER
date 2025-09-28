import tkinter as tk
from tkinter import ttk
window=tk.Tk()


window.config(bg="grey")
window.title("PENDRAGON UNIT CONVERTER VERSION 2.0")
window.geometry("600x1000")

frame=tk.Frame(window, highlightbackground= "blue", highlightthickness=1, highlightcolor="green")
frame.pack(pady=10, padx=10)
frame6=tk.Frame(window, highlightbackground= "yellow", bg="brown")
frame6.pack(pady=10, padx=10)
entry2=tk.Entry(frame6, highlightthickness=8, justify="center", highlightbackground="brown")
entry2.pack(side="right")
label_for_input=tk.Label(frame6,text="INPUT VALUE:", bg="brown", fg="gold", font=("Tahoma", 16,"underline"))
label_for_input.pack(side="left")
frame2=tk.Frame(window, highlightthickness=1, highlightbackground="black", bg="silver")
frame2.pack(pady=10, padx=10)

frame7=tk.Frame(window, highlightbackground= "black", highlightthickness=1, highlightcolor="green", bg="lavender")
frame7.pack(pady=10, padx=10)

label5=tk.Label(frame7,text="TEMPERATURE", fg="gold", bg="black")
label5.pack(side="top")
label6=tk.Label(frame7, text="FROM")
label6.pack(side="left")

combobox3= ttk.Combobox(frame7,width=15, values=["fahrenheit","kelvin","celcius"] )
combobox3.current(0)
combobox3.pack(side="left")

label7=tk.Label(frame7, text="TO")
label7.pack(side="left")

combobox4= ttk.Combobox(frame7,width=15, values=["kelvin","celcius","fahrenheit"] )
combobox4.current(0)
combobox4.pack(side="left")

frame8=tk.Frame(window, bg="silver", highlightthickness=1,highlightbackground="black")
frame8.pack(pady=10, padx=10)
#----------------------------------------------------------
label8=tk.Label(frame8,text="VOLUME", bg="black", fg="gold")
label8.pack(side="top")
label9=tk.Label(frame8, text="FROM")
label9.pack(side="left")

combobox5= ttk.Combobox(frame8,width=15, values=["cubic_meter","cubic_centimeter","liter","milliliter","barrel","pint","fluid_ounce","cubic_foot","gallon"] )
combobox5.current(0)
combobox5.pack(side="left")

label10=tk.Label(frame8, text="TO")
label10.pack(side="left")

combobox6= ttk.Combobox(frame8,width=15, values=["cubic_centimeter","liter","milliliter","barrel","pint","fluid_ounce","cubic_foot","gallon","cubic_meter"] )
combobox6.current(0)
combobox6.pack(side="left")

#--------------------------------------------------------------------------------------
frame3=tk.Frame(window, highlightbackground= "yellow", highlightthickness=1, highlightcolor="yellow", bg="blue")
frame3.pack(pady=10, padx=10)
length=tk.Label(frame2,text="LENGTH", bg="black", fg="gold")
length.pack(side="top")
frame4=tk.Frame(window, highlightbackground= "yellow", highlightthickness=1, highlightcolor="yellow", bg="blue")
frame4.pack(pady=10, padx=10)
frame5=tk.Frame(window, highlightbackground= "yellow", highlightthickness=1, highlightcolor="yellow", bg="blue")
frame5.pack(pady=10, padx=10)


entry=tk.Entry(frame,bg="sky blue", width=30, justify= tk.CENTER,borderwidth=4,fg="black", font=("Seven Segment", 50))
entry.focus()
entry.pack(side="bottom")


entry1=tk.Entry(frame,bg="black", fg="yellow", width=160, justify="center", font=("Tahoma",10))
entry1.pack(side="top")

label2=tk.Label(frame2,text="FROM:")
label2.pack(side="left")

combobox1=ttk.Combobox(frame2, width=15,values=["meter","centimeter","kilometer","millimeter","micrometer","nanometer","miles","yards", "foot","inches"])
combobox1.current( 0)
combobox1.pack( side="left")
label3=tk.Label(frame2,text="TO:")

label3.pack(side="left")
combobox=ttk.Combobox(frame2, width=15,values=["meter","centimeter","kilometer","millimeter","micrometer","nanometer","miles","yards", "foot","inches"])
combobox.current( 0)


combobox.pack( side="left")


a=1
b=2
c=3
d=4
e=5
f=6
g=7
h=8
i=9
j=0





def number_1 ():

    entry.insert(tk.END,a)
button1=tk.Button(frame3,text="      1       ", command=number_1, bg="green", font=20)

def number_2():
    entry.insert(tk.END, b)


    def number_3():
        entry.insert(tk.END, c)

button2=tk.Button(frame3, text="      2       ", command= number_2, bg="green", font=20)


def number_3():
    entry.insert(tk.END, c)
button3=tk.Button(frame3,text="      3       ", command=number_3, bg="green", font=20)

def number_4():
    entry.insert(tk.END, d)
button4=tk.Button(frame3,text="      4       ", command=number_4, bg="green", font=20)

def number_5():
    entry.insert(tk.END, e)

    def number_6():
        entry.insert(tk.END, e)
button1.pack(side="left", padx=2, pady=2)
button2.pack(side="left", padx=2, pady=2)
button3.pack(side="left", padx=2, pady=2)
button4.pack(side="left", padx=2, pady=2)
button5=tk.Button(frame4,text="      5       ", command=number_5, bg="green", font=20)


def number_6():
    entry.insert(tk.END, f)
button6=tk.Button(frame4,text="      6       ", command=number_6, bg="green", font=20)


def number_7():
    entry.insert(tk.END, g)
button7=tk.Button(frame4,text="      7       ", command=number_7, bg="green", font=20)


def number_8():
    entry.insert(tk.END, h)
button8=tk.Button(frame4,text="      8       ", command=number_8, bg="green", font=20)
button5.pack(side="left", padx=2, pady=2)
button6.pack(side="left", padx=2, pady=2)
button7.pack(side="left", padx=2, pady=2)
button8.pack(side="left", padx=2, pady=2)


def number_9():
    entry.insert(tk.END, i)
button9=tk.Button(frame5,text="      9       ", command=number_9, bg="green", font=20)


def number_o():
    entry.insert(tk.END, j)
button0=tk.Button(frame5,text="      0       ", command=number_o, bg="green", font=20)
def clear ():
    entry.delete(0,tk.END)

    entry2.delete(0, tk.END)
    entry.focus()
clear_button= tk.Button(frame5,bg="red",fg="black",text="CLEAR", command=clear, font=20, width=17)
button9.pack(side="left", padx=1, pady=1)
button0.pack(side="left", padx=1, pady=1)
clear_button.pack(side="left", padx=1, pady=1)
clear_button.pack()
def display():
    if combobox1.get()=="meter" and combobox.get()=="centimeter":
        entry1.delete(0,tk.END)
        entry1.insert(0,"METER TO CENTIMETER SCALE")

        val_of_screen =float(entry.get())

        entry.delete(0,tk.END)
        cent=val_of_screen*100,"CM"
        entry.insert(0,cent)

        entry2.delete(0, tk.END)
        entry2.insert(0,val_of_screen)


    elif combobox1.get() == "meter" and combobox.get() == "kilometer":
        entry1.delete(0, tk.END)
        entry1.insert(0, "METER TO KILOMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        kilo = val_of_screen/1000, "KM"
        entry.insert(0, kilo)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get()=="meter" and combobox.get()=="millimeter":
        entry1.delete(0,tk.END)
        entry1.insert(0, "METER TO MILLIMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        milli = val_of_screen * 1000, "MM"
        entry.insert(0, milli)
        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "meter" and combobox.get() == "micrometer":
        entry1.delete(0, tk.END)
        entry1.insert(0, "METER TO MICROMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        micro = val_of_screen * 1000000, "MicroM."
        entry.insert(0, micro)
        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "meter" and combobox.get() == "nanometer":
        entry1.delete(0, tk.END)
        entry1.insert(0, "METER TO NANOMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        nano = val_of_screen * 1000000000, "NanoM."
        entry.insert(0, nano)
        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "meter" and combobox.get() == "miles":
        entry1.delete(0, tk.END)
        entry1.insert(0, "METER TO MILES SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        mile = val_of_screen*0.000621371, "MILE"
        entry.insert(0, mile)
        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "meter" and combobox.get() == "yards":
        entry1.delete(0, tk.END)
        entry1.insert(0, "METER TO YARDS SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        yard = val_of_screen * 1.09361, "YARD"
        entry.insert(0, yard)
        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "meter" and combobox.get() == "foot":
        entry1.delete(0, tk.END)
        entry1.insert(0, "METER TO FOOT SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        foot = val_of_screen * 3.28084, "Feet"
        entry.insert(0, foot)
        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "meter" and combobox.get() == "inches":
        entry1.delete(0, tk.END)
        entry1.insert(0, "METER TO INCHES SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        inch = val_of_screen * 39.3701, "inch"
        entry.insert(0, inch)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "centimeter" and combobox.get() == "meter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "KILOMETER TO METER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        kilotometer = val_of_screen/100, " Meters"
        entry.insert(0, kilotometer)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)


    elif combobox1.get() == "centimeter" and combobox.get() == "kilometer":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CENTIMETER TO KILOMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        KILO = val_of_screen/100000, "KM"
        entry.insert(0, KILO)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "centimeter" and combobox.get() == "millimeter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CENTIMETER TO MILLIMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        MILLI = val_of_screen * 10, "MM"
        entry.insert(0, MILLI)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "centimeter" and combobox.get() == "micrometer":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CENTIMETER TO MICROMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        MICRO = val_of_screen * 10000, "MicroM"
        entry.insert(0, MICRO)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "centimeter" and combobox.get() == "nanometer":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CENTIMETER TO NANOMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        NANO = val_of_screen * 10000000, "Nano-M"
        entry.insert(0, NANO)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "centimeter" and combobox.get() == "miles":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CENTIMETER TO MILE SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        MILE = val_of_screen * 0.00000621371, "Mile"
        entry.insert(0, MILE)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "centimeter" and combobox.get() == "yards":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CENTIMETER TO YARD SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        YARD = val_of_screen * 0.0109361, "YARD"
        entry.insert(0, YARD)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "centimeter" and combobox.get() == "foot":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CENTIMETER TO FEET SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        FEET = val_of_screen * 0.0328084, "Feet"
        entry.insert(0, FEET)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "centimeter" and combobox.get() == "inches":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CENTIMETER TO INCHES SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        INCHES = val_of_screen * 0.393701, " INCHES"
        entry.insert(0, INCHES)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "kilometer" and combobox.get() == "meter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "KILOMETER TO METER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        kilotometer = val_of_screen * 1000, " Meters"
        entry.insert(0, kilotometer)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)


    elif combobox1.get() == "kilometer" and combobox.get() == "centimeter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "KILOMETER TO CENTIMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        kilotocent = val_of_screen * 100000, " CM"
        entry.insert(0, kilotocent)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "kilometer" and combobox.get() == "millimeter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "KILOMETER TO MILLIMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        kilotomilli = val_of_screen * 1000000, " MM"
        entry.insert(0, kilotomilli)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "kilometer" and combobox.get() == "micrometer":
        entry1.delete(0, tk.END)
        entry1.insert(0, "KILOMETER TO MICROMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        kilotomicro = val_of_screen * 1000000000, " Micro_M"
        entry.insert(0, kilotomicro)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "kilometer" and combobox.get() == "nanometer":
        entry1.delete(0, tk.END)
        entry1.insert(0, "KILOMETER TO NANOMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        kilotonano = val_of_screen * 1000000000000, " Nano_M"
        entry.insert(0, kilotonano)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "kilometer" and combobox.get() == "miles":
        entry1.delete(0, tk.END)
        entry1.insert(0, "KILOMETER TO MILE SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        kilotomile = val_of_screen * 0.621371, " Miles"
        entry.insert(0, kilotomile)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "kilometer" and combobox.get() == "yards":
        entry1.delete(0, tk.END)
        entry1.insert(0, "KILOMETER TO YARD SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        kilotoyard = val_of_screen * 1093.61, " Yards"
        entry.insert(0, kilotoyard)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "kilometer" and combobox.get() == "foot":
        entry1.delete(0, tk.END)
        entry1.insert(0, "KILOMETER TO FOOT SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        kilotofoot = val_of_screen * 3280.84, " Foot"
        entry.insert(0, kilotofoot)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "kilometer" and combobox.get() == "inches":
        entry1.delete(0, tk.END)
        entry1.insert(0, "KILOMETER TO INCHES SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        kilotoinch = val_of_screen * 39370.1, " INCHES"
        entry.insert(0, kilotoinch)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "millimeter" and combobox.get() == "meter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MILLIMETER TO METER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        millimetertometer = val_of_screen/1000, " Meters"
        entry.insert(0, millimetertometer)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "millimeter" and combobox.get() == "centimeter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MILLIMETER TO CENTIMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        millimetertocent = val_of_screen/10, " CM"
        entry.insert(0, millimetertocent)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "millimeter" and combobox.get() == "kilometer":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MILLIMETER TO KILOMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        millimetertokilo = val_of_screen/1000000, " KM"
        entry.insert(0, millimetertokilo)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "millimeter" and combobox.get() == "micrometer":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MILLIMETER TO MICROMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        millimetertomicro = val_of_screen * 1000, " Micro_M"
        entry.insert(0, millimetertomicro)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)


    elif combobox1.get() == "millimeter" and combobox.get() == "nanometer":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MILLIMETER TO NANOMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        millimetertonano = val_of_screen * 1000000, " Nano_M"
        entry.insert(0, millimetertonano)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "millimeter" and combobox.get() == "miles":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MILLIMETER TO MILE SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        millimetertomiles = val_of_screen/1609344, " Miles"
        entry.insert(0, millimetertomiles)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "millimeter" and combobox.get() == "foot":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MILLIMETER TO FFOT SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        millimetertofoot = val_of_screen/304.8, " Feet"
        entry.insert(0, millimetertofoot)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "millimeter" and combobox.get() == "inches":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MILLIMETER TO INCHES SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        millimetertoinches = val_of_screen/25.4, " Inches"
        entry.insert(0, millimetertoinches)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "micrometer" and combobox.get() == "meter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MICROMETER TO METER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        microtometer = val_of_screen/1000000, " Meters"
        entry.insert(0, microtometer)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "micrometer" and combobox.get() == "centimeter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MICROMETER TO CENTIMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        microtocent = val_of_screen / 10000, " Cm"
        entry.insert(0, microtocent)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "micrometer" and combobox.get() == "kilometer":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MICROMETER TO KILOMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        microtokilo = val_of_screen / 1000000000, " Km"
        entry.insert(0, microtokilo)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "micrometer" and combobox.get() == "millimeter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MICROMETER TO MILLIMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        microtomilli = val_of_screen / 1000, " Milli_M"
        entry.insert(0, microtomilli)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "micrometer" and combobox.get() == "nanometer":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MICROMETER TO NANOMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        microtonano = val_of_screen * 1000, " Nano_M"
        entry.insert(0, microtonano)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "micrometer" and combobox.get() == "miles":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MICROMETER TO MILE SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        microtomile = val_of_screen / 1609344000000, " Miles"
        entry.insert(0, microtomile)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "micrometer" and combobox.get() == "yards":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MICROMETER TO YARD SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        microtoyard = val_of_screen / 914400, " Yards"
        entry.insert(0, microtoyard)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "micrometer" and combobox.get() == "foot":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MICROMETER TO FEET SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        microtofeet = val_of_screen / 304800, " Feet"
        entry.insert(0, microtofeet)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)


    elif combobox1.get() == "micrometer" and combobox.get() == "inches":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MICROMETER TO INCHES SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        microtoinch = val_of_screen / 25400, " Inches"
        entry.insert(0, microtoinch)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)


    elif combobox1.get() == "nanometer" and combobox.get() == "meter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "NANOMETER TO METER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        nanotometer = val_of_screen / 1000000000, " Meter"
        entry.insert(0, nanotometer)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)


    elif combobox1.get() == "nanometer" and combobox.get() == "centimeter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "NANOMETER TO CENTIMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        nanotocent = val_of_screen / 10000000, " Cm"
        entry.insert(0, nanotocent)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "nanometer" and combobox.get() == "kilometer":
        entry1.delete(0, tk.END)
        entry1.insert(0, "NANOMETER TO KILOMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        nanotokilo = val_of_screen / 1000000000000, " Km"
        entry.insert(0, nanotokilo)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "nanometer" and combobox.get() == "millimeter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "NANOMETER TO MILLIMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        nanotomilli = val_of_screen /1000000, " Milli_M"
        entry.insert(0, nanotomilli)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "nanometer" and combobox.get() == "micrometer":
        entry1.delete(0, tk.END)
        entry1.insert(0, "NANOMETER TO MICROMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        nanotomicro = val_of_screen / 1000, " Micro_M"
        entry.insert(0, nanotomicro)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "nanometer" and combobox.get() == "miles":
        entry1.delete(0, tk.END)
        entry1.insert(0, "NANOMETER TO MILE SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        nanotomile = val_of_screen / 1609344000000, " Miles"
        entry.insert(0, nanotomile)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "nanometer" and combobox.get() == "yards":
        entry1.delete(0, tk.END)
        entry1.insert(0, "NANOMETER TO YARD SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        nanotoyard = val_of_screen / 914400000, " Yards"
        entry.insert(0, nanotoyard)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "nanometer" and combobox.get() == "foot":
        entry1.delete(0, tk.END)
        entry1.insert(0, "NANOMETER TO FOOT SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        nanotofoot = val_of_screen / 304800000, " Feets"
        entry.insert(0, nanotofoot)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "nanometer" and combobox.get() == "inches":
        entry1.delete(0, tk.END)
        entry1.insert(0, "NANOMETER TO INCHES SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        nanotoinch = val_of_screen / 25400000, " Inches"
        entry.insert(0, nanotoinch)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)


    #--------------------------------------------------------------------------------

    elif combobox1.get() == "miles" and combobox.get() == "meter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MILE TO METER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        miletometer = val_of_screen * 1609.34, " Meter"
        entry.insert(0, miletometer)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)


    elif combobox1.get() == "miles" and combobox.get() == "centimeter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MILE TO CENTIMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        miletocent = val_of_screen * 160934, " Cm"
        entry.insert(0, miletocent)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "miles" and combobox.get() == "kilometer":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MILES TO KILOMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        miletokilo = val_of_screen *1.60934, " Km"
        entry.insert(0, miletokilo)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "miles" and combobox.get() == "millimeter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MILE TO MILLIMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        miletomilli = val_of_screen *1609344, " Milli_M"
        entry.insert(0, miletomilli)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "miles" and combobox.get() == "micrometer":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MILE TO MICROMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        miletomicro = val_of_screen *1609344000, " Micro_M"
        entry.insert(0, miletomicro)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "miles" and combobox.get() == "nanometer":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MILE TO NANOMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        miletonano = val_of_screen * 1609344000000, " Nano_M"
        entry.insert(0, miletonano)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "miles" and combobox.get() == "yards":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MILE TO YARD SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        miletoyard = val_of_screen  *1760, " Yards"
        entry.insert(0, miletoyard)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "miles" and combobox.get() == "foot":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MILE TO FOOT SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        miletofoot = val_of_screen *5280, " Feets"
        entry.insert(0, miletofoot)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "miles" and combobox.get() == "inches":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MILES TO INCHES SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        miletoinch = val_of_screen * 63360, " Inches"
        entry.insert(0, miletoinch)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    #_______________________________________________________________________________

    elif combobox1.get() == "yards" and combobox.get() == "meter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "YARD TO METER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        yardtometer = val_of_screen * 0.9144, " Meters"
        entry.insert(0, yardtometer)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "yards" and combobox.get() == "centimeter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "YARD TO CENTIMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        yardtocent = val_of_screen * 91.44, " Cm"
        entry.insert(0, yardtocent)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "yards" and combobox.get() == "kilometer":
        entry1.delete(0, tk.END)
        entry1.insert(0, "YARD TO KILOMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        yardtokilo = val_of_screen * 0.0009144, " Km"
        entry.insert(0, yardtokilo)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "yards" and combobox.get() == "millimeter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "YARD TO MILLIMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        yardtomilli = val_of_screen * 914.4, " Milli_M"
        entry.insert(0, yardtomilli)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "yards" and combobox.get() == "micrometer":
        entry1.delete(0, tk.END)
        entry1.insert(0, "YARD TO MICROMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        yardtomicro = val_of_screen * 914400, " Micro_M"
        entry.insert(0, yardtomicro)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "yards" and combobox.get() == "nanometer":
        entry1.delete(0, tk.END)
        entry1.insert(0, "YARD TO NANOMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        yardtonano = val_of_screen * 914400000, " Nano_M"
        entry.insert(0, yardtonano)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "yards" and combobox.get() == "miles":
        entry1.delete(0, tk.END)
        entry1.insert(0, "YARD TO MILES SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        yardtomiles = val_of_screen/1760, " Miles"
        entry.insert(0, yardtomiles)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "yards" and combobox.get() == "foot":
        entry1.delete(0, tk.END)
        entry1.insert(0, "YARD TO FOOT SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        yardtofeet = val_of_screen * 3, " Feet"
        entry.insert(0, yardtofeet)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "yards" and combobox.get() == "inches":
        entry1.delete(0, tk.END)
        entry1.insert(0, "YARD TO INCHES SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        yardtoinches = val_of_screen * 36, " Inches"
        entry.insert(0, yardtoinches)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    #-------------------------------------------------------------------
    elif combobox1.get() == "foot" and combobox.get() == "meter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "FOOT TO METER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        foottometer = val_of_screen *0.3048, " Meters"
        entry.insert(0, foottometer)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "foot" and combobox.get() == "centimeter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "FOOT TO CENTIMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        foottocent = val_of_screen * 30.48, "Cm"
        entry.insert(0, foottocent)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "foot" and combobox.get() == "kilometer":
        entry1.delete(0, tk.END)
        entry1.insert(0, "FOOT TO KILOMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        foottokilo = val_of_screen * 0.0003048, "Km"
        entry.insert(0, foottokilo)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "foot" and combobox.get() == "millimeter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "FOOT TO MILLIMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        foottomilli = val_of_screen * 304.8, " Milli_M"
        entry.insert(0, foottomilli)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "foot" and combobox.get() == "micrometer":
        entry1.delete(0, tk.END)
        entry1.insert(0, "FOOT TO MICROMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        foottomicro = val_of_screen * 304800, " Micro_M"
        entry.insert(0, foottomicro)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "foot" and combobox.get() == "nanometer":
        entry1.delete(0, tk.END)
        entry1.insert(0, "FOOT TO NANOMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        foottonano = val_of_screen * 304800000, " Nano_M"
        entry.insert(0, foottonano)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "foot" and combobox.get() == "miles":
        entry1.delete(0, tk.END)
        entry1.insert(0, "FOOT TO MILE SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        foottomiles = val_of_screen/5280, " Miles"
        entry.insert(0, foottomiles)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "foot" and combobox.get() == "yards":
        entry1.delete(0, tk.END)
        entry1.insert(0, "FOOT TO YARDS SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        foottoyards = val_of_screen/3, " Yards"
        entry.insert(0, foottoyards)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "foot" and combobox.get() == "inches":
        entry1.delete(0, tk.END)
        entry1.insert(0, "FOOT TO INCHES SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        foottoinches = val_of_screen * 12, " Inches"
        entry.insert(0, foottoinches)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    #--------------------------------------------------------------------------------

    elif combobox1.get() == "inches" and combobox.get() == "meter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "INCHES TO METER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        inchestometer = val_of_screen * 0.0254, " Meter"
        entry.insert(0, inchestometer)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "inches" and combobox.get() == "centimeter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "INCHES TO CENTIMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        inchestocent = val_of_screen * 2.54, " Cm"
        entry.insert(0, inchestocent)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "inches" and combobox.get() == "kilometer":
        entry1.delete(0, tk.END)
        entry1.insert(0, "INCHES TO KILOMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        inchestokilo = val_of_screen * 0.0000254, "Km"
        entry.insert(0, inchestokilo)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "inches" and combobox.get() == "millimeter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "INCHES TO MILLIMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        inchestomilli = val_of_screen * 25.4, " Milli_M"
        entry.insert(0, inchestomilli)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "inches" and combobox.get() == "micrometer":
        entry1.delete(0, tk.END)
        entry1.insert(0, "INCHES TO MICROMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        inchestomicro = val_of_screen * 25400, " Micro_M"
        entry.insert(0, inchestomicro)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "inches" and combobox.get() == "nanometer":
        entry1.delete(0, tk.END)
        entry1.insert(0, "INCHES TO NANOMETER SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        inchestonano = val_of_screen * 25400000, " Nano_N"
        entry.insert(0, inchestonano)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "inches" and combobox.get() == "miles":
        entry1.delete(0, tk.END)
        entry1.insert(0, "INCHES TO MILE SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        inchestomile = val_of_screen/ 63360, " Miles"
        entry.insert(0, inchestomile)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox1.get() == "inches" and combobox.get() == "yards":
        entry1.delete(0, tk.END)
        entry1.insert(0, "INCHES TO YARD SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        inchestoyard = val_of_screen/36, " Yards"
        entry.insert(0, inchestoyard)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox1.get() == "inches" and combobox.get() == "foot":
        entry1.delete(0, tk.END)
        entry1.insert(0, "INCHES TO FOOT SCALE")
        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        inchestofeet = val_of_screen /12, " Feets"
        entry.insert(0, inchestofeet)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
        #____________________________________________________________
    else:
        entry1.delete(0, tk.END)
        entry1.insert(0,"MACHINE ERROR")

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

def display2():
    if combobox3.get()=="fahrenheit" and combobox4.get()=="kelvin":
        entry1.delete(0,tk.END)
        entry1.insert(0,"FAHRENHEIT TO KELVIN SCALE")

        val_of_screen =float(entry.get())

        entry.delete(0,tk.END)
        ftok=(val_of_screen-32)*(5/9) + 273.15,"Kelvin (K)"
        entry.insert(0,ftok)

        entry2.delete(0, tk.END)
        entry2.insert(0,val_of_screen)
    elif combobox3.get()=="fahrenheit" and combobox4.get()=="celcius":
        entry1.delete(0,tk.END)
        entry1.insert(0,"FAHRENHEIT TO CELCIUS SCALE")

        val_of_screen =float(entry.get())

        entry.delete(0,tk.END)
        ftoc=(val_of_screen-32)*(5/9) ," ̊C"
        entry.insert(0,ftoc)

        entry2.delete(0, tk.END)
        entry2.insert(0,val_of_screen)
    elif combobox3.get()=="kelvin" and combobox4.get()=="celcius":
        entry1.delete(0,tk.END)
        entry1.insert(0,"KELVIN TO CELCIUS SCALE")

        val_of_screen =float(entry.get())

        entry.delete(0,tk.END)
        ktoc=val_of_screen-273.15," ̊C"
        entry.insert(0,ktoc)

        entry2.delete(0, tk.END)
        entry2.insert(0,val_of_screen)
    elif combobox3.get()=="kelvin" and combobox4.get()=="fahrenheit":
        entry1.delete(0,tk.END)
        entry1.insert(0,"KELVIN TO FAHRENHEIT SCALE")

        val_of_screen =float(entry.get())

        entry.delete(0,tk.END)
        ktof=(val_of_screen-273.15)*(9/5) + 32," ̊ F"
        entry.insert(0,ktof)

        entry2.delete(0, tk.END)
        entry2.insert(0,val_of_screen)
    elif combobox3.get()=="celcius" and combobox4.get()=="kelvin":
        entry1.delete(0,tk.END)
        entry1.insert(0,"CELCIUS TO KELVIN SCALE")

        val_of_screen =float(entry.get())

        entry.delete(0,tk.END)
        ctok=val_of_screen+273.15," Kelvin(K)"
        entry.insert(0,ctok)

        entry2.delete(0, tk.END)
        entry2.insert(0,val_of_screen)
    elif combobox3.get()=="celcius" and combobox4.get()=="fahrenheit":
        entry1.delete(0,tk.END)
        entry1.insert(0,"CELCIUS TO FAHRENHEIT SCALE")

        val_of_screen =float(entry.get())

        entry.delete(0,tk.END)
        ctof=(val_of_screen*(9/5))+32," ̊ F"
        entry.insert(0,ctof)

        entry2.delete(0, tk.END)
        entry2.insert(0,val_of_screen)
    else:
        entry1.delete(0, tk.END)
        entry1.insert(0,"MACHINE ERROR")

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
def display3():
    if combobox5.get()=="cubic_meter" and combobox6.get()=="cubic_centimeter":
        entry1.delete(0,tk.END)
        entry1.insert(0,"CUBIC METER TO CUBIC CENTIMETER SCALE")

        val_of_screen =float(entry.get())

        entry.delete(0,tk.END)
        cmtocc=val_of_screen*1000000,"Cubic_Cm"
        entry.insert(0,cmtocc)

        entry2.delete(0, tk.END)
        entry2.insert(0,val_of_screen)
    elif combobox5.get() == "cubic_meter" and combobox6.get() == "liter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CUBIC METER TO LITER SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        cmtol = val_of_screen * 1000, "Liters (Ltrs)"
        entry.insert(0, cmtol)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "cubic_meter" and combobox6.get() == "milliliter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CUBIC METER TO MILLILITER SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        cmtoml = val_of_screen * 1000000000, "Milliliters (M_Ltrs)"
        entry.insert(0, cmtoml)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "cubic_meter" and combobox6.get() == "barrel":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CUBIC METER TO BARREL SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        cmtobl = val_of_screen/0.158987, "Barrel (Brl)"
        entry.insert(0, cmtobl)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "cubic_meter" and combobox6.get() == "pint":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CUBIC METER TO PINT SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        cmtop = val_of_screen * 2113.38, "Pints (Pts)"
        entry.insert(0, cmtop)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "cubic_meter" and combobox6.get() == "fluid_ounce":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CUBIC METER TO FLUID OUNCE SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        cmtofo = val_of_screen * 33814.02, "Fluid-Ounce (Fld-O)"
        entry.insert(0, cmtofo)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "cubic_meter" and combobox6.get() == "cubic_foot":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CUBIC METER TO CUBIC FOOT SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        cmtocf = val_of_screen * 35.3147, "Cubic-Feets (CFts)"
        entry.insert(0, cmtocf)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "cubic_meter" and combobox6.get() == "gallon":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CUBIC METER TO GALLON SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        cmtogn = val_of_screen * 264.172, "Gallons (Gn)"
        entry.insert(0, cmtogn)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "cubic_centimeter" and combobox6.get() == "liter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CUBIC CENTIMETER TO LITER SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        ccmtol = val_of_screen/1000, "Liters (Ltrs)"
        entry.insert(0, ccmtol)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "cubic_centimeter" and combobox6.get() == "milliliter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CUBIC CENTIMETER TO MILLILITER SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        ccmtoml = val_of_screen, " M-Ltrs"
        entry.insert(0, ccmtoml)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "cubic_centimeter" and combobox6.get() == "barrel":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CUBIC CENTIMETER TO BARREL SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        ccmtob = val_of_screen/158987, " Barrel (Bl)"
        entry.insert(0, ccmtob)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "cubic_centimeter" and combobox6.get() == "pint":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CUBIC CENTIMETER TO PINT SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        ccmtop = val_of_screen / 473.176, " Pint (Pt)"
        entry.insert(0, ccmtop)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "cubic_centimeter" and combobox6.get() == "fluid_ounce":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CUBIC CENTIMETER TO FLUID OUNCE SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        ccmtofo = val_of_screen /29.5735, " Fluid Ounce(Fl oz)"
        entry.insert(0, ccmtofo)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "cubic_centimeter" and combobox6.get() == "cubic_foot":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CUBIC CENTIMETER TO CUBIC FOOT SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        ccmtocf = val_of_screen / 28316.85, " Cubic Feet"
        entry.insert(0, ccmtocf)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "cubic_centimeter" and combobox6.get() == "gallon":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CUBIC CENTIMETER TO GALLON SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        ccmtog = val_of_screen / 3785.41, " Gallon (Gn)"
        entry.insert(0, ccmtog)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "liter" and combobox6.get() == "cubic_centimeter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CUBIC CENTIMETER TO CUBIC CENTIMETER SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        ltocc = val_of_screen * 1000, " Cubic Cm"
        entry.insert(0, ltocc)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "liter" and combobox6.get() == "milliliter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "LITER TO MILLILITER SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        ltoml = val_of_screen * 1000, " Milli-Ltrs"
        entry.insert(0, ltoml)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "liter" and combobox6.get() == "barrel":
        entry1.delete(0, tk.END)
        entry1.insert(0, "LITERS TO BARREL SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        ltob = val_of_screen/ 158.987, " Barrels"
        entry.insert(0, ltob)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "liter" and combobox6.get() == "pint":
        entry1.delete(0, tk.END)
        entry1.insert(0, "LITERS TO PINT SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        ltop = val_of_screen/0.4732, " Pint"
        entry.insert(0, ltop)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "liter" and combobox6.get() == "fluid_ounce":
        entry1.delete(0, tk.END)
        entry1.insert(0, "LITERS TO FLUID OUNCE SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        ltofo = val_of_screen/0.0296, "Fluid ounce (Fl oz)"
        entry.insert(0, ltofo)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "liter" and combobox6.get() == "cubic_foot":
        entry1.delete(0, tk.END)
        entry1.insert(0, "LITERS TO CUBIC SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        ltocf = val_of_screen*0.0353147, "Cubit Ft"
        entry.insert(0, ltocf)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox5.get() == "liter" and combobox6.get() == "gallon":
        entry1.delete(0, tk.END)
        entry1.insert(0, "LITERS TO GALLON SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        ltog = val_of_screen*0.264172, "Gallon"
        entry.insert(0, ltog)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox5.get() == "liter" and combobox6.get() == "cubic_meter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "LITERS TO CUBIC METER SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        ltocm = val_of_screen/1000, "Cubic Meter"
        entry.insert(0, ltocm)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "milliliter" and combobox6.get() == "cubic_centimeter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MILLILITER TO CUBIC CENTIMETER SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        mltoccm = val_of_screen, "Cubic Cm"
        entry.insert(0, mltoccm)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox5.get() == "milliliter" and combobox6.get() == "liter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MILLILITER TO LITER SCALE ")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        mltol = val_of_screen / 1000, "Ltrs"
        entry.insert(0, mltol)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "milliliter" and combobox6.get() == "barrel":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MILLILITER TO BARREL SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        mltob = val_of_screen / 119240.475, "Barrels"
        entry.insert(0, mltob)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "milliliter" and combobox6.get() == "pint":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MILLILITER TO PINT SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        mltop = val_of_screen / 473.176, "Pints"
        entry.insert(0, mltop)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "milliliter" and combobox6.get() == "fluid_ounce":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MILLILITER TO FLUID OUNCE SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        mltofo = val_of_screen / 29.5735, "Fluid Ounce (Fl oz)"
        entry.insert(0, mltofo)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "milliliter" and combobox6.get() == "cubic_foot":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MILLILITER TO CUBIC FOOT SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        mltocf = val_of_screen / 28316.85, "Cubic Feet"
        entry.insert(0, mltocf)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "milliliter" and combobox6.get() == "cubic_meter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "BARREL TO CUBIC METER")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        mltocm = val_of_screen *0.000001, "Cubic Meter"
        entry.insert(0, mltocm)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)


    elif combobox5.get() == "barrel" and combobox6.get() == "cubic_centimeter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "BARREL TO CUBIC CENTIMETER SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        btoccm = val_of_screen *119240, "Cubic Cm"
        entry.insert(0, btoccm)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox5.get() == "milliliter" and combobox6.get() == "gallon":
        entry1.delete(0, tk.END)
        entry1.insert(0, "MILLILITER TO GALLON SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        mltog = val_of_screen / 3785.41, "Gallon"
        entry.insert(0, mltog)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox5.get() == "barrel" and combobox6.get() == "liter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "BARREL TO LITER")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        btol = val_of_screen *119.24, "Liters"
        entry.insert(0, btol)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "barrel" and combobox6.get() == "milliliter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "BARREL TO MILLILITER SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        btoml = val_of_screen* 119240, "Milli Liters"
        entry.insert(0, btoml)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "barrel" and combobox6.get() == "pint":
        entry1.delete(0, tk.END)
        entry1.insert(0, "BARREL TO PINT SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        btop = val_of_screen*248, "Pint"
        entry.insert(0, btop)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "barrel" and combobox6.get() == "fluid_ounce":
        entry1.delete(0, tk.END)
        entry1.insert(0, "BARREL TO FLUID OUNCE SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        btofo = val_of_screen*3968, "Fluid ounce(Fl oz)"
        entry.insert(0, btofo)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "barrel" and combobox6.get() == "cubic_foot":
        entry1.delete(0, tk.END)
        entry1.insert(0, "BARREL TO CUBIC FOOT")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        btocf = val_of_screen *5.614583, "Cubic Feet"
        entry.insert(0, btocf)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "barrel" and combobox6.get() == "gallon":
        entry1.delete(0, tk.END)
        entry1.insert(0, "BARREL TO GALLON SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        btog = val_of_screen *31, "Gallons"
        entry.insert(0, btog)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "barrel" and combobox6.get() == "cubic_meter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "BARREL TO CUBIC CUBIC METER")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        btocm = val_of_screen *0.158987, "Cubic Meter"
        entry.insert(0, btocm)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox5.get() == "pint" and combobox6.get() == "cubic_centimeter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "PINT TO CUBIC CUBIC CENTIMETER")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        PtocCm = val_of_screen * 473.176, "Cubic  Cm"
        entry.insert(0, PtocCm)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "pint" and combobox6.get() == "liter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "PINT TO LITER SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        ptoL = val_of_screen * 0.473176, "Liters"
        entry.insert(0, ptoL)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "pint" and combobox6.get() == "milliliter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "PINT TO MILLILITER SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        ptoml = val_of_screen * 473.176, "Milli Ltrs"
        entry.insert(0, ptoml)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "pint" and combobox6.get() == "barrel":
        entry1.delete(0, tk.END)
        entry1.insert(0, "PINT TO BARREL SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        ptob = val_of_screen * 0.00396825, "Barrel"
        entry.insert(0, ptob)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "pint" and combobox6.get() == "fluid_ounce":
        entry1.delete(0, tk.END)
        entry1.insert(0, "PINT TO FLUID OUNCE SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        ptofo = val_of_screen *  16, "Fluid Ounce(Fl oz)"
        entry.insert(0, ptofo)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "pint" and combobox6.get() == "cubic_foot":
        entry1.delete(0, tk.END)
        entry1.insert(0, "PINT TO CUBIC FOOT")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        ptocf = val_of_screen * 0.0167101, "Cubic Feet"
        entry.insert(0, ptocf)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox5.get() == "pint" and combobox6.get() == "gallon":
        entry1.delete(0, tk.END)
        entry1.insert(0, "PINT TO GALLON SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        ptog = val_of_screen * 0.125, "Gallons"
        entry.insert(0, ptog)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox5.get() == "pint" and combobox6.get() == "cubic_meter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "PINT TO  CUBIC METER")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        ptocm = val_of_screen * 0.000473176, "Cubic Meter"
        entry.insert(0, ptocm)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "fluid_ounce" and combobox6.get() == "cubic_centimeter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "FLUID OUNCE TO CUBIC CENTIMETER SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        fotoccm = val_of_screen * 29.5735, "Cubic Cm"
        entry.insert(0, fotoccm)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox5.get() == "fluid_ounce" and combobox6.get() == "liter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "FLUID OUNCE TO LITER SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        fotol = val_of_screen * 0.0295735, " Ltrs"
        entry.insert(0, fotol)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)


    elif combobox5.get() == "fluid_ounce" and combobox6.get() == "milliliter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "FLUID OUNCE TO MILLILITER SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        fotoml = val_of_screen * 29.5735, "Milli Ltrs"
        entry.insert(0, fotoml)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox5.get() == "fluid_ounce" and combobox6.get() == "barrel":
        entry1.delete(0, tk.END)
        entry1.insert(0, "FLUID OUNCE TO BARREL SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        fotob = val_of_screen * 0.00003125, "Barrels"
        entry.insert(0, fotob)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox5.get() == "fluid_ounce" and combobox6.get() == "pint":
        entry1.delete(0, tk.END)
        entry1.insert(0, "FLUID OUNCE TO PINT SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        fotop = val_of_screen * 0.0625, "Pint"
        entry.insert(0, fotop)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox5.get() == "fluid_ounce" and combobox6.get() == "cubic_foot":
        entry1.delete(0, tk.END)
        entry1.insert(0, "FLUID OUNCE TO CUBIC FOOT SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        fotocf = val_of_screen * 0.00104438, "Cubic Ft"
        entry.insert(0, fotocf)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox5.get() == "fluid_ounce" and combobox6.get() == "gallon":
        entry1.delete(0, tk.END)
        entry1.insert(0, "FLUID OUNCE TO GALLON SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        fotog = val_of_screen * 0.0078125, "Gallons"
        entry.insert(0, fotog)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox5.get() == "fluid_ounce" and combobox6.get() == "cubic_meter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "FLUID OUNCE TO CUBIC METERSCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        fotocm = val_of_screen * 0.0000295735, "Cubic Meter"
        entry.insert(0, fotocm)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox5.get() == "cubic_foot" and combobox6.get() == "cubic_centimeter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CUBIC FOOT TO CUBIC CENTIMETER SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        cftoccm = val_of_screen * 28316.8466, "Cubic Cm"
        entry.insert(0, cftoccm)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)


    elif combobox5.get() == "cubic_foot" and combobox6.get() == "liter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CUBIC FOOT TO LITER SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        cftol = val_of_screen * 28.3168, "Ltrs"
        entry.insert(0, cftol)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "cubic_foot" and combobox6.get() == "milliliter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CUBIC FOOT TO MILLILITER SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        cftoml = val_of_screen * 28316.8, "Milli Ltrs"
        entry.insert(0, cftoml)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox5.get() == "cubic_foot" and combobox6.get() == "barrel":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CUBIC FOOT TO BARRELSCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        cftob= val_of_screen * 0.17811, "Barrels"
        entry.insert(0, cftob)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox5.get() == "cubic_foot" and combobox6.get() == "pint":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CUBIC FOOT TO PINT SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        cftop = val_of_screen * 59.8442, "Pints"
        entry.insert(0, cftop)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)


    elif combobox5.get() == "cubic_foot" and combobox6.get() == "fluid_ounce":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CUBIC FOOT TO FLUID OUNCESCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        cftofo = val_of_screen * 957.506, "Fl oz"
        entry.insert(0, cftofo)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)


    elif combobox5.get() == "cubic_foot" and combobox6.get() == "gallon":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CUBIC FOOT TO GALLON SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        cftog = val_of_screen * 7.48052, "Gallons"
        entry.insert(0, cftog)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox5.get() == "cubic_foot" and combobox6.get() == "cubic_meter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "CUBIC FOOT TO CUBIC METER SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        cftocm = val_of_screen * 0.0283168, "Cubic M"
        entry.insert(0, cftocm)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "gallon" and combobox6.get() == "cubic_centimeter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "GALLON TO CUBIC CENTIMETER SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        gtoccm = val_of_screen * 3785.41, "Cubic Cm"
        entry.insert(0, gtoccm)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox5.get() == "gallon" and combobox6.get() == "liter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "GALLON TO LITER SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        gtol= val_of_screen * 3.78541, "Ltr"
        entry.insert(0, gtol)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "gallon" and combobox6.get() == "milliliter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "GALLON TO MILLILITER SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        gtoml = val_of_screen * 3785.41, "Milli Ltrs"
        entry.insert(0, gtoml)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "gallon" and combobox6.get() == "barrel":
        entry1.delete(0, tk.END)
        entry1.insert(0, "GALLON TO BARREL SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        gtob = val_of_screen * 0.0238095, "Barrel"
        entry.insert(0, gtob)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "gallon" and combobox6.get() == "pint":
        entry1.delete(0, tk.END)
        entry1.insert(0, "GALLON TO PINT SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        btop = val_of_screen * 8, "Pint"
        entry.insert(0, btop)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)

    elif combobox5.get() == "gallon" and combobox6.get() == "fluid_ounce":
        entry1.delete(0, tk.END)
        entry1.insert(0, "GALLON TO FLUID OUNCE SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        gtofo = val_of_screen *128, "Fl oz"
        entry.insert(0, gtofo)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "gallon" and combobox6.get() == "cubic_foot":
        entry1.delete(0, tk.END)
        entry1.insert(0, "GALLON TO CUBIC FOOT SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        gtocf = val_of_screen * 0.133681, "Cubic Ft"
        entry.insert(0, gtocf)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)
    elif combobox5.get() == "gallon" and combobox6.get() == "cubic_meter":
        entry1.delete(0, tk.END)
        entry1.insert(0, "GALLON TO CUBIC METER SCALE")

        val_of_screen = float(entry.get())

        entry.delete(0, tk.END)
        gtocm = val_of_screen * 0.0378541, "Cubic M"
        entry.insert(0, gtocm)

        entry2.delete(0, tk.END)
        entry2.insert(0, val_of_screen)






    else:
        entry1.delete(0, tk.END)
        entry1.insert(0, "MACHINE ERROR")




tempscale= tk.Button(frame2,bg="blue",text="Convert Length",wraplength=50,command=display, fg="white", width=13)
tempscale.pack()
temperature_button= tk.Button(frame7,text="Convert Temperature",command=display2, wraplength=100, width=14, bg="blue", fg="white")
temperature_button.pack()

volume_scale=tk.Button(frame8,text="Convert Volume",command=display3, wraplength=60, width=15, bg="blue", fg="white")
volume_scale.pack()
window.mainloop()