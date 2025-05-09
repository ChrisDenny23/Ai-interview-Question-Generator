import streamlit as st
from openai import OpenAI


client = OpenAI(api_key=YOUR-OPEN-API-KEY")

st.title("AI Interview Question Generator")

# User input
topic = st.text_input("Enter a topic (e.g., Data Structures, DBMS, etc.):")
difficulty = st.selectbox("Select difficulty level:", ["Easy", "Medium", "Hard"])
num_questions = st.slider("Number of questions:", 1, 10, 3)

# Generate prompt
def generate_questions(topic, difficulty, num_questions):
    prompt = (
        f"Generate {num_questions} interview questions on the topic '{topic}' "
        f"with '{difficulty}' difficulty. Do not provide answers."
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()

# Generate button
if st.button("Generate Questions"):
    if topic:
        questions = generate_questions(topic, difficulty, num_questions)
        st.markdown("### Generated Questions:")
        st.text(questions)
    else:
        st.warning("Please enter a topic.")