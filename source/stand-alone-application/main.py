import tkinter
from tkinter import *
import webbrowser
import AES
import tkinter.constants 
import tkinter.filedialog
import os
import pdfcreate2 as pc
import tkinter as tk
from PyPDF2 import PdfFileWriter, PdfFileReader
import getpass

def openfileEnc():
	filename = tkinter.filedialog.askopenfilename(initialdir = "C:/Users/Kirtan/Desktop",title = "Select file",filetypes = (("text files","*.txt"),("word files","*.docx"),("all files","*.*")))
	fileToEncrptyEntryUpdate(filename)
    
def openfileEnc2():
	filename = tkinter.filedialog.askopenfilename(initialdir = "C:/Users/Kirtan/Desktop",title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
	fileToEncrptyEntryUpdate(filename)

def opendirectoryEnc():
	directory = tkinter.filedialog.askdirectory(initialdir = "C:/Users/Kirtan/Desktop",title = "Select directory")
	destinationFolderEncEntryUpdate(directory)

def openfileDec():
	filename = tkinter.filedialog.askopenfilename(initialdir = "C:/Users/Kirtan/Desktop",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
	fileToDecryptEntryUpdate(filename)	
def opendirectoryDec():
	directory = tkinter.filedialog.askdirectory(initialdir = "C:/Users/Kirtan/Desktop",title = "Select directory")
	destinationFolderDecEntryUpdate(directory)

def sendfilepage():
	webbrowser.open_new(r"http://127.0.0.1:5000/upload-file")

def recievefilepage():
	webbrowser.open_new(r"http://127.0.0.1:5000/file-directory")

def fileToEncrptyEntryUpdate(filename):
	inputEncFileEntry.delete(0,tkinter.END)
	inputEncFileEntry.insert(0,filename)
    
def destinationFolderEncEntryUpdate(directory):
	inputEncDirEntry.delete(0,tkinter.END)
	inputEncDirEntry.insert(0,directory)
    
def fileToDecryptEntryUpdate(filename):
	outputDecFileEntry.delete(0,tkinter.END)
	outputDecFileEntry.insert(0,filename)
    
def destinationFolderDecEntryUpdate(directory):
	outputDecDirEntry.delete(0,tkinter.END)
	outputDecDirEntry.insert(0,directory)

def encryptor():
	EncryptBTN.config(state="disabled")
	public_key = publicKeyOfRecieverEntry.get()
	private_key = privateKeyOfSenderEntry.get()
	directory = inputEncDirEntry.get()
	filename = inputEncFileEntry.get()
	AES.encrypt(filename,directory,public_key,private_key)

def decryptor():
	DecryptBTN.config(state="disabled")
	public_key = publicKeyOfSenderEntry.get()
	private_key = privateKeyOfRecieverEntry.get()
	directory = outputDecDirEntry.get()
	filename = outputDecFileEntry.get()
	AES.decrypt(filename,directory,public_key,private_key)

def main():
    global PDF
    global filename
    global directory
    
    filename = ""
    directory = ""
    global form
    form = tkinter.Tk()
    form.wm_title('ProGuard')
    form.wm_iconbitmap('Security.ico')
    EncryptStep = tkinter.LabelFrame(form, text=" Encryption ")
    EncryptStep.grid(row=0, columnspan=7, sticky='W', \
		padx=5, pady=5, ipadx=5, ipady=5)	
    DecryptStep = tkinter.LabelFrame(form, text=" Decryption ")
    DecryptStep.grid(row=2, columnspan=7, sticky='W', \
    	             padx=5, pady=5, ipadx=5, ipady=5)
    
    
    global inputEncFileEntry
    global inputEncDirEntry
    global publicKeyOfRecieverEntry
    global privateKeyOfSenderEntry
    global EncryptBTN
    
    inputEncFile = tkinter.Label(EncryptStep, text="Select the File:")
    inputEncFile.grid(row=0, column=0, sticky='E', padx=5, pady=2)
    
    inputEncFileEntry = tkinter.Entry(EncryptStep)
    inputEncFileEntry.grid(row=0, column=1, columnspan=7, sticky="WE", pady=3)
    
    inputEncBtn = tkinter.Button(EncryptStep, text="Browse ...", command = openfileEnc)
    inputEncBtn.grid(row=0, column=8, sticky='W', padx=5, pady=2)
    inputEncDir = tkinter.Label(EncryptStep, text="Save File to:")
    inputEncDir.grid(row=1, column=0, sticky='E', padx=5, pady=2)
    
    inputEncDirEntry = tkinter.Entry(EncryptStep)
    inputEncDirEntry.grid(row=1, column=1, columnspan=7, sticky="WE", pady=2)
    
    inputEncDirBtn = tkinter.Button(EncryptStep, text="Browse ...", command = opendirectoryEnc)
    inputEncDirBtn.grid(row=1, column=8, sticky='W', padx=5, pady=2)
    publicKeyOfReciever = tkinter.Label(EncryptStep, text="Pass-Key :")
    publicKeyOfReciever.grid(row=2, column=0, sticky='E', padx=5, pady=2)
    
    publicKeyOfRecieverEntry = tkinter.Entry(EncryptStep)
    publicKeyOfRecieverEntry.grid(row=2, column=1, sticky='E', pady=2)
    
    privateKeyOfSender = tkinter.Label(EncryptStep, text="Secret-Key :")
    privateKeyOfSender.grid(row=2, column=5, padx=5, pady=2)
    
    privateKeyOfSenderEntry = tkinter.Entry(EncryptStep)
    privateKeyOfSenderEntry.grid(row=2, column=7, pady=2)
    
    EncryptBTN = tkinter.Button(EncryptStep, text="Encrypt   ", command=encryptor)
    EncryptBTN.grid(row=2, column=8, sticky='W', padx=5, pady=2)
    
    PDFbtn= tkinter.Button(EncryptStep, text="Make PDF  ",command=Pdf_maker)
    PDFbtn.grid(row=3,column=5,sticky='W',padx=5,pady=2)
    
    #SPDFbtn= tkinter.Button(EncryptStep, text="Secure PDF  ",command=Pdf_maker)
    #SPDFbtn.grid(row=3,column=5,sticky='W',padx=5,pady=2)
    
    
    global outputDecFileEntry
    global outputDecDirEntry
    global publicKeyOfSenderEntry
    global privateKeyOfRecieverEntry
    
    global DecryptBTN
    
    outputDecFile = tkinter.Label(DecryptStep, text="Select the File:")
    outputDecFile.grid(row=0, column=0, sticky='E', padx=5, pady=2)
    
    outputDecFileEntry = tkinter.Entry(DecryptStep)
    outputDecFileEntry.grid(row=0, column=1, columnspan=7, sticky="WE", pady=3)
    
    outputDecBtn = tkinter.Button(DecryptStep, text="Browse ...", command = openfileDec)
    outputDecBtn.grid(row=0, column=8, sticky='W', padx=5, pady=2)
    outputDecDir = tkinter.Label(DecryptStep, text="Save File to:")
    outputDecDir.grid(row=1, column=0, sticky='E', padx=5, pady=2)
    
    outputDecDirEntry = tkinter.Entry(DecryptStep)
    outputDecDirEntry.grid(row=1, column=1, columnspan=7, sticky="WE", pady=2)
    
    outputDecDirBtn = tkinter.Button(DecryptStep, text="Browse ...", command = opendirectoryDec)
    outputDecDirBtn.grid(row=1, column=8, sticky='W', padx=5, pady=2)
    publicKeyOfSender = tkinter.Label(DecryptStep, text="Pass-Key :")
    publicKeyOfSender.grid(row=2, column=0, sticky='E', padx=5, pady=2)
    
    publicKeyOfSenderEntry = tkinter.Entry(DecryptStep)
    publicKeyOfSenderEntry.grid(row=2, column=1, sticky='E', pady=2)
    privateKeyOfReciever = tkinter.Label(DecryptStep, text="Secret-Key :")
    privateKeyOfReciever.grid(row=2, column=5, padx=5, pady=2)
    
    privateKeyOfRecieverEntry = tkinter.Entry(DecryptStep)
    privateKeyOfRecieverEntry.grid(row=2, column=7, pady=2)
    DecryptBTN = tkinter.Button(DecryptStep, text="Decrypt   ", command = decryptor)
    DecryptBTN.grid(row=2, column=8, sticky='W', padx=5, pady=2)
    
    
    form.mainloop()
    

def Pdf_maker():
    root = tkinter.Tk()
    root.wm_title('ProGuard') 
    root.wm_iconbitmap('Security.ico')
    label = tk.Label(root, text="File name: ")
    label.pack()
    var = tkinter.StringVar()
    entry = tkinter.Entry(root, textvariable=var)
    entry.pack()
     
    content = tk.Text(root)
    content.pack()
    content.insert("0.0", pc.text)
    
     
    def create_pdf():
        
        if entry.get() == "":
           entry.set("KEY")
        if ".pdf" not in var.get():
            name, doc = pc.make_doc(entry.get() + ".pdf")
        else:
            name, doc = pc.make_doc(var.get())
        pc.show(content.get("0.0", tk.END))
        os.startfile(name)
        
    button = tk.Button(root,text="Create PDF",command = create_pdf) 
    button.pack() 
   
    def protect_pdf():
        global PDF
        global filename
        global directory
        
        filename = ""
        directory = ""
    
        global sec
        sec = tkinter.Tk()
        sec.wm_title('ProGuard')
        sec.wm_iconbitmap('Security.ico')
        EncryptStep = tkinter.LabelFrame(sec, text=" 1. PDF Encryption: ")
        EncryptStep.grid(row=0, columnspan=7, sticky='W', \
    		padx=5, pady=5, ipadx=5, ipady=5)	
    
        
        global inputEncFileEntry
        global inputEncDirEntry
        global publicKeyOfRecieverEntry
        global privateKeyOfSenderEntry
        global EncryptBTN
        
        inputEncFile = tkinter.Label(EncryptStep, text="Select the File:")
        inputEncFile.grid(row=0, column=0, sticky='E', padx=5, pady=2)
        
        inputEncFileEntry = tkinter.Entry(EncryptStep)
        inputEncFileEntry.grid(row=0, column=1, columnspan=7, sticky="WE", pady=3)
        
        inputEncBtn = tkinter.Button(EncryptStep, text="Browse ...", command = openfileEnc2)
        inputEncBtn.grid(row=0, column=8, sticky='W', padx=5, pady=2)
        
        publicKeyOfReciever = tkinter.Label(EncryptStep, text="Pass-Key :")
        publicKeyOfReciever.grid(row=2, column=0, sticky='E', padx=5, pady=2)
        
        privateKeyOfSenderEntry = tkinter.Entry(EncryptStep)
        privateKeyOfSenderEntry.grid(row=2, column=1,columnspan=7, pady=2)
        
        def Pdf_protector():
            pdfwriter=PdfFileWriter()
            
            filename=inputEncFileEntry.get()
            pdf=PdfFileReader(filename)
            for page_num in range(pdf.numPages):
              pdfwriter.addPage(pdf.getPage(page_num))
            pswd=privateKeyOfSenderEntry.get()
            pdfwriter.encrypt(pswd)
            with open('ENCRYPTED_KEY.pdf','wb') as f:
              pdfwriter.write(f)
              f.close()
              
        SPDFbtn= tkinter.Button(EncryptStep, text="Secure PDF",command=Pdf_protector)
        SPDFbtn.grid(row=3,column=5,sticky='W',padx=5,pady=2)
        sec.mainloop()   
     
    
    button2= tk.Button(root,text="Secure PDF",command = protect_pdf)
    button2.pack() 
if __name__ == "__main__":
	main()

    