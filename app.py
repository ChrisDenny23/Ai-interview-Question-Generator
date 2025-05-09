import streamlit as st
from openai import OpenAI


client = OpenAI(api_key="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")

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