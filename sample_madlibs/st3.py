import streamlit as st

def madlib():
    st.header("🧭 Adventurous Journey")

    name = st.text_input("Adventurer's name:")
    vehicle = st.text_input("Type of vehicle:")
    place = st.text_input("Mysterious place:")
    obj = st.text_input("Magical object:")
    action = st.text_input("An action ending with -ing:")

    if name and vehicle and place and obj and action:
        st.markdown("---")
        st.subheader("📖 Here's your story:")
        story = f"""
        **{name}** hopped into a **{vehicle}** and sped toward **{place}**.  
        There, they discovered a glowing **{obj}**.  
        Without hesitation, **{name}** started **{action}**, ready for the next adventure!
        """
        st.markdown(story)
    else:
        st.info("👈 Fill in all the fields to see your story!")
