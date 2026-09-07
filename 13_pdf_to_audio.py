import pyttsx3
from pypdf import PdfReader
from tkinter.filedialog import askopenfilename

book_path = askopenfilename(title="Select a pdf file", filetypes=[("PDF files", "*.pdf")])

if book_path:
    reader = PdfReader(book_path)
    player = pyttsx3.init()
    voices = player.getProperty('voices')
    for voice in voices:
        if "ja" in voice.id.lower() or "japanese" in voice.name.lower():
            player.setProperty('voice', voice.id)
            break

    for num, page in enumerate(reader.pages):
        text = page.extract_text()
        if text.strip():
            player.say(text)
            player.runAndWait()