import pyttsx3
import pdfplumber
from tkinter.filedialog import askopenfilename

book_path = askopenfilename()

with pdfplumber.open(book_path) as pdf:
    player = pyttsx3.init()
    
    for page_num in range(len(pdf.pages)):
        page = pdf.pages[page_num]
        text = page.extract_text()
        
        if text:  # Check if there's text on the page
            player.say(text)
            player.runAndWait()
