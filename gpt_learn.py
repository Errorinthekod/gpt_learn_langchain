from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.embeddings import OpenAIEmbeddings
from config import OPENAI_API_KEY

tour_info = [ # данные
    'Тур в Париж - 5000$, отличный вид на Эйфелеву башню',
    'Тур в Турцию - 5000$, отличный вид на Черное море',
    'Тур в Испанию - 5000$, там отличная музыка',
    'Тур в Берлин - 4000$, будет предоставлен танк',


]

embeddings = OpenAIEmbeddings(openai_api_key = OPENAI_API_KEY) # связывание с моделями чат GPT

db = FAISS.from_texts(tour_info, embeddings) # связывание с данными 

chain = RetrievalQA.from_chain_type( # создание цепи чтоб ИИ запоминал всю цепочку сообщений
    llm = OpenAI(temperature = 0, openai_api_key = OPENAI_API_KEY),
retriever=db.as_retriever() # перебор и изучение данных и вывод ответа на их основе
)

query = "Расскажи мне про доступные туры" # запрос

result = chain.run(query) # запуск
print(result) # вывод результата обработки данных ИИ