import streamlit as st
import csv
import os
import re

# ---------------- Page Config ----------------
st.set_page_config(page_title="TalentScout AI Hiring Assistant")

st.title("🤖 TalentScout AI Hiring Assistant")
st.write("👋 Welcome to TalentScout Hiring Assistant")
st.write("I will help you with initial screening. Please fill your details below.")

# ---------------- Validation Functions ----------------
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) >= 10

# ---------------- AI Evaluation Function ----------------
def evaluate_answer(answer):
    score = 0
    feedback = []

    word_count = len(answer.split())

    if word_count > 30:
        score += 5
        feedback.append("Excellent detailed answer")
    elif word_count > 15:
        score += 3
        feedback.append("Good answer")
    else:
        feedback.append("Answer is too short")

    return score, ", ".join(feedback)

# ---------------- Dynamic Question Generator ----------------
def generate_questions(stack):

    tech_questions = {
        "Python": "Explain OOP concepts in Python.",
        "React": "Explain React Hooks and their usage.",
        "Machine Learning": "Explain overfitting and how to prevent it.",
        "AWS": "Explain EC2 and S3 services.",
        "Docker": "What is containerization?",
        "JavaScript": "Explain closures in JavaScript.",
        "Django": "Explain Django MVT architecture.",
        "Flask": "Difference between Flask and Django."
    }

    questions = []

    for tech in stack:
        if tech in tech_questions:
            questions.append(tech_questions[tech])
        else:
            questions.append(f"Explain fundamentals of {tech}.")

    questions.append("Describe a project where you used your tech stack.")
    questions.append("What challenges did you face?")
    questions.append("How do you optimize performance?")

    return questions

# ---------------- CSV Save Function ----------------
def save_to_csv(name, email, phone, experience, role, location, tech_stack, answers):

    file_exists = os.path.isfile("candidates_data.csv")

    with open("candidates_data.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Name","Email","Phone","Experience","Role",
                "Location","Tech Stack","Answers"
            ])

        writer.writerow([
            name, email, phone, experience, role,
            location, ", ".join(tech_stack), " | ".join(answers)
        ])

# ---------------- Candidate Details ----------------
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
experience = st.number_input("Years of Experience", 0, 50)

role = st.selectbox(
    "Desired Role",
    [
        "Python Developer","Frontend Developer","Backend Developer",
        "Full Stack Developer","Data Scientist","Machine Learning Engineer",
        "DevOps Engineer","UI/UX Designer","QA Engineer","Mobile App Developer"
    ]
)

location = st.text_input("Current Location")

tech_stack = st.multiselect(
    "Select Your Tech Stack",
    [
        "Python","JavaScript","Java","C++","React","Angular","Node.js",
        "Django","Flask","Spring Boot","MongoDB","MySQL","PostgreSQL",
        "Machine Learning","Deep Learning","TensorFlow","PyTorch",
        "AWS","Docker","Kubernetes","Git"
    ]
)

# ---------------- Session State ----------------
if "q_index" not in st.session_state:
    st.session_state.q_index = 0

if "answers" not in st.session_state:
    st.session_state.answers = []

# ---------------- Question Flow ----------------
if tech_stack:

    questions = generate_questions(tech_stack)

    st.subheader("Technical Screening Questions")

    # Progress Bar
    st.progress(st.session_state.q_index / len(questions))

    if st.session_state.q_index < len(questions):

        current_q = questions[st.session_state.q_index]
        st.write(current_q)

        answer = st.text_area("Your Answer", key=f"ans_{st.session_state.q_index}")

        if st.button("Submit Answer"):

            if answer.strip() == "":
                st.warning("Please enter your answer")
            else:
                st.session_state.answers.append(answer)
                st.session_state.q_index += 1
                st.rerun()

    # ---------------- After All Questions ----------------
    else:

        if not name or not is_valid_email(email):
            st.warning("Enter valid Name and Email")

        elif not is_valid_phone(phone):
            st.warning("Enter valid phone number")

        else:
            save_to_csv(name, email, phone, experience, role, location, tech_stack, st.session_state.answers)

            st.success("Thanks for applying to TalentScout 🎉")
            st.info("Our HR team will review your profile and contact you soon.")

            st.write("### Your Submitted Answers")

            for i, ans in enumerate(st.session_state.answers):
                score, feedback = evaluate_answer(ans)

                st.write(f"Q{i+1}: {questions[i]}")
                st.write(f"Answer: {ans}")
                st.write(f"Score: {score}")
                st.write(f"Feedback: {feedback}")
                st.write("---")

# ---------------- Buttons ----------------
col1, col2 = st.columns(2)

with col1:
    if st.button("Reset Conversation"):
        st.session_state.q_index = 0
        st.session_state.answers = []
        st.rerun()

with col2:
    if st.button("Exit Chat"):
        st.success("Conversation Ended. Thank You!")
        st.stop()
