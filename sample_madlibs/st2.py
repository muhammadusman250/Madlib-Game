import streamlit as st

def madlib():
    st.header("💡 The Power of Gratitude")

    boy = st.text_input("Name of the boy:")
    old_man = st.text_input("Name of the wise old man:")
    complaint = st.text_input("What the boy complained about:")

    if boy and old_man and complaint:
        st.markdown("---")
        st.subheader("📖 Here's your story:")
        story = f"""
        Once, a boy named **{boy}** lived in a small city. He always complained about **{complaint}**,  
        wishing for a different life.  

        One day, he met a wise man named **{old_man}**, who said,  
        *"Instead of complaining about what you don’t have, be grateful for what you do.  
        Gratitude is the key to true happiness."*  

        **{boy}** realized his mistake and learned to appreciate the present.
        """
        st.markdown(story)
    else:
        st.info("👈 Fill in all the fields to see your story!")
