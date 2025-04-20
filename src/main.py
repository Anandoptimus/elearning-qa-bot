from langchain.document_loaders import CSVLoader
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.document_loaders.csv_loader import CSVLoader


# llm = OpenAI(model_name="gpt-3.5-turbo", temperature = 0.6)
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature = 0.6)

from langchain.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="codebasics_faqs.csv",
    source_column="prompt",
    encoding="ISO-8859-1" 
)

data = loader.load()

embeddings = OpenAIEmbeddings()

vectorstore = FAISS.from_documents(documents = data, embedding = embeddings)

retriever = vectorstore.as_retriever()

# retriever.get_relevant_documents("for how long is this course valid")

prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""

PROMPT = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])

qa = RetrievalQA.from_chain_type(retriever = retriever,
                                llm=llm,
                                chain_type = "stuff",
                                input_key = "query",
                                return_source_documents = True,
                                chain_type_kwargs = {"prompt": PROMPT}
                                )

qa("DO YOU HAVE A JAVASCRIPT COURSE")

# sample questions
# Do you guys provide internship and also do you offer EMI payments?
# Do you have javascript course?
# Should I learn power bi or tableau?
# I've a MAC computer. Can I use powerbi on it?
# I don't see power pivot. how can I enable it?
