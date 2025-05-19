import streamlit as st
from sample_madlibs import st1, st2, st3, st4

st.set_page_config(page_title="Madlib Stories", layout="centered")
st.title("🎉 Welcome to Madlib World!")

st.write("Choose a story from below and fill in the blanks to create your own fun version.")

story_option = st.selectbox(
    "📚 Choose a Madlib Story",
    (
        "A Memorable Day (Default)",
        "😂 Funny Restaurant Trick",
        "💡 The Power of Gratitude",
        "🧭 Adventurous Journey",
        "📚 Student's Dream Adventure",
        "🎲 Surprise Me!",
    )
)

# Default story from your original madlib.py
def default_story():
    name = st.text_input("Enter a name:")
    friend_name = st.text_input("Enter your friend's name:")
    food = st.text_input("Enter a type of food:")
    place = st.text_input("Enter a place:")
    hobby = st.text_input("Enter a hobby or activity:")

    if name and friend_name and food and place and hobby:
        st.markdown("---")
        st.subheader("📖 Here's your story:")
        story = f"""
        One golden morning, **{name}** packed a box of **{food}** and called up **{friend_name}**.  
        “Let’s vanish to **{place}** for the day,” they said, smiling.

        They spent hours **{hobby}**, talking about themselves.  
        There was no rush, no noise — just the comfort of being with someone who truly gets you.  
        They laughed at old memories, made new ones, and soaked in the quiet magic of the moment.  
        As the sky turned soft and golden, they sat side by side, watching the light fade.  
        “Same time next week?” **{friend_name}** asked.  
        **{name}** smiled, “Always.”
        """
        st.markdown(story)
    else:
        st.info("👈 Fill in all the fields to see your story!")

# Route to the correct story
if story_option == "A Memorable Day (Default)":
    default_story()
elif story_option == "😂 Funny Restaurant Trick":
    st1.madlib()
elif story_option == "💡 The Power of Gratitude":
    st2.madlib()
elif story_option == "🧭 Adventurous Journey":
    st3.madlib()
elif story_option == "📚 Student's Dream Adventure":
    st4.madlib()
elif story_option == "🎲 Surprise Me!":
    import random
    random.choice([st1, st2, st3, st4]).madlib()
