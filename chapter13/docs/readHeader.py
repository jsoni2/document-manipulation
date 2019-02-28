import docx

def getHeaders(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        print(para.style)
        if "Heading" in para.style.name:
            fullText.append(para.text)
        
    return '\n'.join(fullText)