import PyPDF2
import nltk
nltk.download('punkt')
nltk.download('stopwords')


def extract_text_from_pdf(pdf_path):
    text=""
    with open(pdf_path,'rb') as file:
        reader=PyPDF2.PdfReader(file)
        for page in reader.pages:
            text+=page.extract_text()
    return text

resume_file="sample_resume.pdf"
try:
    extracted_text=extract_text_from_pdf(resume_file)
    print("Extracted_text:\n")
    print(extracted_text[:1000])
except FileNotFoundError:
    print("File not found")


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

def extract_keywords_from_jd(jd_text,top_n=10):
    stop_words=set(stopwords.words('english'))
    words=word_tokenize(jd.text.lower())
    filtered=[word for word in words
              if word not in stop_words and word not in string.punctuation]
    freq={}
    for word in filtered:
        freq[word]=freq.get(word,0)+1
        sorted_keywords=sorted(freq.items())
        key=lambda x:x[1],reverse=True
    return sorted_keywords[:top_n]