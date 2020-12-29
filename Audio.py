import pyttsx3
import PyPDF2

book = open('Magic of Thinking Big - David Schwartz.pdf', 'rb')
PDFreader = PyPDF2.PdfFileReader(book)
pages = PDFreader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(6, pages):       # 'For loop' for continues reading
    page = PDFreader.getPage(6)   # To were it starts reading the book
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

