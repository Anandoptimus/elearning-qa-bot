# 📚 E-Learning FAQ Bot using LangChain & OpenAI

This project is a smart **Question & Answer chatbot** built for an **E-Learning company**. It uses **LangChain**, **OpenAI’s GPT-3.5**, and **FAISS** to answer natural language questions from a CSV file of course FAQs. It’s perfect for companies that want to offer an intelligent, automated support experience to learners.

---

## 🚀 Features

- 🔍 Semantic search on CSV-based FAQs
- 🤖 Natural language Q&A with GPT-3.5-Turbo
- 📎 Accurate source-backed answers
- 🧠 Custom prompt template to avoid hallucinations
- 💻 (Optional) Streamlit UI for user-friendly interaction

---

## 📂 Folder Structure
elearning-qa-bot/ 
├── data/ 
    └── codebasics_faqs.csv 
├── src/ 
    └── main.py 
├── streamlit_app.py 
├── requirements.txt 
├── README.md 
├── .gitignore


---

## 🛠️ Tech Stack

- **LangChain**
- **OpenAI GPT**
- **FAISS**
- **Streamlit**

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/elearning-qa-bot.git
cd elearning-qa-bot
```

### 2. Install Requirements
pip install -r requirements.txt

### 3. Set OpenAI API Key
export OPENAI_API_KEY=your-key

### 4. Run from Terminal (Backend Only)
python src/main.py


## 🧪 Example Questions
- Do you offer EMI payment options?
- Is there a JavaScript course?
- Should I learn Power BI or Tableau?
- I use a Mac. Can I run Power BI on it?





