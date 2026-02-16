# TalentScout AI Hiring Assistant

## 📌 Project Overview

TalentScout AI Hiring Assistant is an intelligent chatbot designed to assist recruiters in the initial screening of candidates. The chatbot collects candidate details and generates technical interview questions dynamically based on the candidate's selected technology stack.

This project demonstrates the use of Large Language Models (LLMs), conversational AI design, and prompt engineering to automate early hiring stages.

---

## 🚀 Features

- Candidate Information Collection
- Dynamic Technical Question Generation
- Tech Stack Based Screening
- Interactive Chat Interface
- Input Validation
- Smooth Conversation Flow

---

## 🛠️ Technologies Used

- Python
- Streamlit
- OpenAI / LLM API
- Pandas
- CSV Data Handling

---
TalentScout_AI_Hiring_Assistant/
│
├── app.py # Main chatbot application
├── candidates_data.csv # Stores candidate responses
├── requirements.txt # Project dependencies
└── README.md # Project documentation

---

## ⚙️ Installation & Setup

### Step 1: Clone Repository
git clone <your-github-repo-link>
cd TalentScout_AI_Hiring_Assistant

### Step 2: Create Virtual Environment
venv\Scripts\activate

Mac/Linux:

### Step 4: Install Dependencies
pip install -r requirements.txt

### Step 5: Run Application
streamlit run app.py

---

## 💬 Usage Guide

1. Open chatbot in browser.
2. Enter candidate details:
   - Name
   - Email
   - Phone Number
   - Experience
   - Desired Role
   - Tech Stack
3. Chatbot generates technical questions.
4. Candidate responses are stored for recruiter review.

---

## 🧠 Prompt Design Strategy

The chatbot uses LLM prompts to dynamically generate interview questions based on the candidate's declared tech stack.

### Key Prompt Goals:
- Generate relevant technical questions
- Maintain difficulty balance
- Ensure role-based evaluation
- Provide structured responses

---

## ⚠️ Challenges Faced

- Designing dynamic question generation
- Maintaining natural conversation flow
- Input validation for candidate data
- Handling multiple tech stack inputs

---

## 🔮 Future Improvements

- Resume Parsing Integration
- Database Storage
- Candidate Scoring System
- Multi-Round Interview Automation
- Admin Dashboard

---

## 👨‍💻 Author

Developed as part of AI/ML Internship Assignment.

## 📂 Project Structure

