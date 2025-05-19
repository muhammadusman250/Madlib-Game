import streamlit as st

def madlib():
    st.header("📚 Student Dream Adventure")

    student = st.text_input("Student's name:")
    subject = st.text_input("Subject:")
    chocolate = st.text_input("Favorite chocolate:")
    item = st.text_input("Favorite book or item:")
    feeling = st.text_input("Emotion (e.g., excited, amazed):")

    if student and subject and chocolate and item and feeling:
        st.markdown("---")
        st.subheader("📖 Here's your story:")
        story = f"""
        While studying **{subject}**, **{student}** dozed off.  
        In a dream, they found a magical box of **{chocolate}**.  
        Inside was their **{item}**, glowing like treasure.  

        Suddenly awake, they saw both the **{chocolate}** and **{item}** beside them!  
        **{student}** felt **{feeling}** — as if the dream had become real.
        """
        st.markdown(story)
    else:
        st.info("👈 Fill in all the fields to see your story!")
