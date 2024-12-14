import google.generativeai as genai
from langchain_community.document_loaders import PyPDFLoader

GOOGLE_API_KEY = "AIzaSyDI297Sjfbeq2ShC8m0nzjcSIUFBLDQvoY"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

loader = PyPDFLoader('/Users/jjummi/Desktop/WinterAcademicConfernece2025/LangChain.pdf')
data = loader.load()

history = [
    {
        "role":"assistant",
        "parts":[
            {"text": data[i].page_content} for i in range(3,10)
        ]    
    },
]

chat = model.start_chat(history=history)
response = model.generate_content("LayoutParser의 핵심 구성 요소를 'history'에 기록된 내용을 기반으로 알려줘.")


for part in response.parts:
    if hasattr(part, "text"):
        print(part.text)