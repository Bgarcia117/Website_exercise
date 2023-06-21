import streamlit as st
from send import send_email
import pandas

st.header("Contact Me") 

df = pandas.read_csv("files/topics.csv")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    topic = st.selectbox(
        "What topic do you want to discuss?",
        options=(df["topic"])
    )
    raw_message = st.text_area("Your message")
    # Allows us to enter multiple lines of text 
    message = f"""
Subject: New email from {user_email}

From: {user_email}
Topic: {topic}
{raw_message}
    """
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully")