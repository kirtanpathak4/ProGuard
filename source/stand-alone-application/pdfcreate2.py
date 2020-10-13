import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import os
  
def make_doc(name):
    
    global doc
    doc = SimpleDocTemplate(
        name,
        pagesize=letter,
        rightMargin=72,leftMargin=72,
        topMargin=72,bottomMargin=18)
    return name, doc
 
 
def add_image(img, w=200, h=100, align="LEFT"):
    "Add an image to page"
    im = Image(img, w, h, hAlign=align)

    page.append(im)
 
 
def add_space():
    "Add a space to page"
    page.append(Spacer(1, 12))
 
 
def add_text(text, space=0):
    "Add a text to page followed by a space"
    if type(text)==list:
        for f in text:
            add_text(f)
    else:
        ptext = f'<font size="12">{text}</font>'
        page.append(Paragraph(ptext, styles["Normal"]))
        if space==1:
            add_space()
        add_space()
 
 
def show(text):
    "Adds images and text for each line in 'text' multiline string"
 
    global doc
    
    text = text.splitlines()
    for line in text:
        if ".png" in line:
            if len(line.split()) == 4:
                l, w, h, align = line.split()
                add_image(l, int(w), int(h), align)
            else:
                add_image(line)
 
        elif "ctime()" in line:
            add_text(time.ctime())
        else:
            add_text(line)
    doc.build(page)
 
 
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
page=[]
 
 
text = """
Pass Key:
Secret Key:
 
Hello,
This a key file to decrypt the encrypted message.

"""
 
if __name__ == "__main__":
    name, doc = make_doc("myform.pdf")
    show(text)
 
    os.startfile(name)