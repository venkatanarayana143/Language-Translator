#import library
from tkinter import*
from translate import Translator
from tkinter import ttk
#translation
def translate():
 #get input from user
 ip=engVariable.get()
 #get selected langauge
 langauge=lang.get()
 #creating variable of Translator
 translator = Translator(to_lang=langauge)
 #Translation
 translation = translator.translate(ip)
 #set translated message into Label
 transVariable.set(translation)

#creating GUI for Transator
root =Tk()
#setting window height and width
root.geometry("600x200")
#setting window background color
root["bg"]="#20325B"
#setting title of window
root.title("GUI:Language Translator")
#creating variable for messages
global engVariable
global transVariable
global lang;
engVariable=StringVar()
transVariable=StringVar()
lang=StringVar()
#Entry/Textbox for message/Sentence
Entry(root,text="Hello",textvariable=engVariable,font="Arial 12",fg="black",width=42).place(x=80,y=30)
#combox for language
fontExample = ("Courier", 12, "bold")
comboExample = ttk.Combobox(root,textvariable=lang,
                            values=[
                                    "Hindi",
                                    "German",
                                    "Chinese",
                                    "Telugu",
                                    "Estonian",
                                    "Japanese",
                                    "Marathi",
                                    "Spanish",
                                    "French",
                                    "Arabic",
                                    "Bengali",
                                    "Russian",
                                    "Portuguese",
                                    "Urdu",
                                    "Swahili",
                                    "Turkish",
                                    "Tamil",
                                    "Kannada",
                                    "Malayalam",
                                    "Punjabi",
                                    "Korean",
                                    "Czech",
                                    "Bulgarian", "Manipuri","Mongolian","Nepali","Oriya","Rajasthani",
                                    "Serbian", "Bihari","Esperanto", "Gujarati", "Kashmiri","Korean",
                                    "Danish", "Achinese","Abkhazian","Assamese","Asturian","Bhojpuri",
                                    "Finnish", "Dutch", "Romanian", "Latin","Ukrainian","Swedish",
                                    "Greek","Hungarian","Italian","Latvian","Lithuanian","Polish"
                                    ],
                            #here you can add many more languages
                            font = fontExample)

root.option_add('*TCombobox*Listbox.font', fontExample)
comboExample.place(x=80,y=70)

#button for translate
Button(root,text="Translate",font="Arial 12 bold",width="10",command=translate,bg="orange").place(x=350,y=70)
#label for generated/success message
Label(root,text="Hello",textvariable=transVariable,font="Arial 12",bg="#20325B",fg="white").place(x=80,y=120)
root.mainloop()
