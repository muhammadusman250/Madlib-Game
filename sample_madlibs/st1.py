import streamlit as st

def madlib():
    st.header("😂 The Restaurant Trick")

    friend1 = st.text_input("Name of friend 1:")
    friend2 = st.text_input("Name of friend 2:")
    profession = st.text_input("A profession (e.g., chef, artist):")
    food = st.text_input("A favorite food:")
    drink = st.text_input("Favorite cold drink:")

    if friend1 and friend2 and profession and food and drink:
        st.markdown("---")
        st.subheader("📖 Here's your story:")
        story = f"""
        Two friends, **{friend1}** and **{friend2}**, who are both **{profession}**, went to a restaurant and ordered **{drink}**.  
        After ordering, they took out their own **{food}** and started eating.  
        The waiter came over and said, “You are not allowed to eat your own food here”  
        They looked at each other, smiled, and swapped their **{food}** instead!
        """
        st.markdown(story)
    else:
        st.info("👈 Fill in all the fields to see your story!")
