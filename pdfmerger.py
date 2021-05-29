from PyPDF2 import PdfFileMerger
import os
import glob

from tkinter import filedialog
from tkinter import *

def browse_button1():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    global first_folder
    filename = filedialog.askdirectory()
    first_folder = filename+'/'
    if filename!='':
        show_folder2_button()


def browse_button2():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    global second_folder
    filename = filedialog.askdirectory()
    second_folder = filename+'/'
    if filename!='':
        show_res_btn()

def browse_res_btn():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    global result_folder
    filename = filedialog.askdirectory()
    result_folder = filename+'/'
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
        l.insert(ctr,msg)
        pdfs = [pdf,second_pdf]
        merger = PdfFileMerger()
        for pdf in pdfs:
            merger.append(pdf)
        
        merger.write(result)
        merger.close()
        show_mergeall_button()

def mergeall():
    os.chdir(result_folder)
    pdfs = [p for p in glob.glob("*.pdf")]

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write("result.pdf")
    merger.close()

def show_folder2_button():
    button2 = Button(text="Browse Folder 2", command=browse_button2)
    button2.configure(background='#007d0f', foreground='white',font=('arial',15,'bold'))
    button2.pack()
    button2.place(x=250,y=550)

def show_res_btn():
    res_btn = Button(text="Browse Result Folder", command=browse_res_btn)
    res_btn.configure(background='#007d0f', foreground='white',font=('arial',15,'bold'))
    res_btn.pack()
    res_btn.place(x=450,y=550)

def show_merge_button():
    merge_b=Button(root,text="Merge PDF",command=merge)
    merge_b.configure(background='#007d0f', foreground='white',font=('arial',15,'bold'))
    merge_b.place(x=750,y=550)

def show_mergeall_button():
    merge_b=Button(root,text="Merge All in 1 PDF",command=mergeall)
    merge_b.configure(background='#007d0f', foreground='white',font=('arial',15,'bold'))
    merge_b.place(x=900,y=550)

root = Tk()
root.geometry('1200x600')
root.title('PDF Merger (Serialized)')
root.configure(background='#CDCDCD')

button1 = Button(text="Browse Folder 1", command=browse_button1)
button1.configure(background='#007d0f', foreground='white',font=('arial',15,'bold'))
button1.pack()
button1.place(x=50,y=550)
var = StringVar()
label = Label( root, textvariable=var,background='#CDCDCD')
label.place(x=15,y=15)
var.set("Merged Pdfs")
label.pack()  
f = Frame(root)
f.place(x=50, y=35)

scrollbar = Scrollbar(f)
l = Listbox(f, height=30, width=180, yscrollcommand=scrollbar.set)
scrollbar.config(command=l.yview)
scrollbar.pack(side=RIGHT, fill=Y)
l.pack(side="left")

mainloop()



