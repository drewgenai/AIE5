#placeholder# Add PyPDF2 import for PDF handling
from PyPDF2 import PdfReader

# Create a PDFLoader class
class PDFLoader:
    def __init__(self, path):
        self.path = path
        self.documents = []
    
    def load_documents(self):
        reader = PdfReader(self.path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        self.documents.append(text)
        return self.documents
