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

jd_file="job_description.txt"
try:
    with open(jd_file,"r",encoding="utf-8") as f:
        jd_text=f.read()
except FileNotFoundError:
    print("job description was not found")
    jd_text=""
jd_keywords=extract_keywords_from_jd(jd_text,top_n=10)
print("top jd keywords ",jd_keywords)

matched_keywords=[word for word,freq in jd_keywords 
                if word in extracted_text.lower()]
score=len(matched_keywords)/len(jd_keywords) *100
print("matched keywords : ",matched_keywords)
print("resume score : ",round(score,2),"% match with JD ")