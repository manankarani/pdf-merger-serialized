from PyPDF2 import PdfFileMerger
import os
import glob

from tkinter import filedialog
from tkinter import *
from tkinter import ttk

def browse_button1():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    global first_folder
    filename = filedialog.askdirectory()
    first_folder = filename+'/'
    print(first_folder)
    if filename!='':
        show_folder2_button()

def browse_button2():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    global second_folder
    filename = filedialog.askdirectory()
    second_folder = filename+'/'
    print(second_folder)
    if filename!='':
        show_res_btn()

def browse_res_btn():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    global result_folder
    filename = filedialog.askdirectory()
    result_folder = filename+'/'
    print(result_folder)
    if filename!='':
        show_merge_button()

def merge():
    os.chdir(first_folder)
    ctr=0
    for pdf in glob.glob("*.pdf"):
        ctr+=1
        
        second_pdf=second_folder+os.path.splitext(pdf)[0]+'_A'+os.path.splitext(pdf)[1]
        result = result_folder+os.path.splitext(pdf)[0]+'_M.pdf'
        
        msg = '['+str(ctr)+'] Merged '+pdf+' and '+second_pdf+' to '+result  
        treev.insert("", 'end', text ="L1", 
                values =(ctr, pdf, os.path.splitext(pdf)[0]+'_A.pdf', os.path.splitext(pdf)[0]+'_M.pdf'))
        pdf = first_folder + os.path.splitext(pdf)[0]+os.path.splitext(pdf)[1]
        pdfs = [pdf,second_pdf]
        merger = PdfFileMerger()
        for pdf in pdfs:
            merger.append(pdf)        
        merger.write(result)
        merger.close()
        mergeall()

def mergeall():
    os.chdir(result_folder)
    pdfs = [p for p in glob.glob("*.pdf")]

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write("result.pdf")
    merger.close()
#================================================================#
window = Tk()
window.geometry("1152x700")
window.configure(bg = "#323232")
canvas = Canvas(
    window,
    bg = "#323232",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

f = Frame(window)
f.place(x=40, y=166)
style = ttk.Style()

style.configure("Treeview",
                background="#8a8a8a",
                foreground="#000000",
                rowheight=25,
                fieldbackground="#8a8a8a")
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
style.map('Treeview', background=[('selected', '#323232')])
scrollbar = Scrollbar(f)
# Using treeview widget
treev = ttk.Treeview(f, selectmode ='browse',height=15, style="mystyle.Treeview")
  
# Calling pack method w.r.to treeview
treev.place(x=40,y=166)
treev.pack()

# Constructing vertical scrollbar
# with treeview
treev.configure(xscrollcommand = scrollbar.set)

# Defining number of columns
treev["columns"] = ("1", "2", "3","4")
  
# Defining heading
treev['show'] = 'headings'
  
# Assigning the width and anchor to  the
# respective columns
treev.column("1", width = 90, anchor ='c')
treev.column("2", width = 330, anchor ='c')
treev.column("3", width = 330, anchor ='c')
treev.column("4", width = 330, anchor ='c')
# Assigning the heading names to the 
# respective columns
treev.heading("1", text ="Sr No")
treev.heading("2", text ="File 1")
treev.heading("3", text ="File 2")
treev.heading("4", text ="Result File")

img0 = PhotoImage(file = f"imgs/heading.png")
canvas.create_image(35,49, anchor=NW, image=img0)     


# canvas.create_rectangle(
#     40, 166, 40+1074, 166+332,
#     fill = "#8a8a8a",
#     outline = "")

resultfol = PhotoImage(file = f"imgs/resultfol.png")
second = PhotoImage(file = f"imgs/second.png")
merge_img = PhotoImage(file = f"imgs/merge.png") 
first = PhotoImage(file = f"imgs/first.png")

#=========================================================================#
def show_folder1_button():
    b1 = Button(
        image = first,
        borderwidth = 0,
        highlightthickness = 0,
        command = browse_button1,
        relief = "flat")

    b1.place(
        x = 40, y = 585,
        width = 240,
        height = 60)

def show_folder2_button():

    b4 = Button(
        image = second,
        borderwidth = 0,
        highlightthickness = 0,
        command = browse_button2,
        relief = "flat")

    b4.place(
        x = 310, y = 585,
        width = 240,
        height = 60)

def show_res_btn():

    b3 = Button(
        image = resultfol,
        borderwidth = 0,
        highlightthickness = 0,
        command = browse_res_btn,
        relief = "flat")

    b3.place(
        x = 580, y = 585,
        width = 240,
        height = 60)

def show_merge_button():
    
    b2 = Button(
        image = merge_img,
        borderwidth = 0,
        highlightthickness = 0,
        command = merge,
        relief = "flat")

    b2.place(
        x = 894, y = 585,
        width = 220,
        height = 60)

show_folder1_button()
window.resizable(False, False)
window.mainloop()
