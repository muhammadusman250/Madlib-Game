import streamlit as st

def madlib():
    st.header("😊 A Funny Lesson About Gratitude")

    boy = st.text_input("What's the boy's name?")
    old_man = st.text_input("What's the old man's name?")
    complaint = st.text_input("What's something silly your annoying friend always does?")

    if boy and old_man and complaint:
        st.markdown("---")
        st.subheader("📖 Your Story:")
        story = f"""
        There was a boy named **{boy}** who always complained.  
        The thing that made him super mad? His friend always **{complaint}**!  
        
        One day, **{boy}** was walking in the park and met a funny old man named **{old_man}**.  
        The old man was feeding popcorn to squirrels wearing hats. 🐿️🎩  

        **{old_man}** looked at **{boy}** and said,  
        *"You know, life is more fun when you stop complaining and start being thankful!"*  

        **{boy}** thought about it, and started to smile.  
        He realized maybe life wasn’t so bad — even if his friend was annoying sometimes.  

        From that day on, **{boy}** tried to laugh instead of complain.  
        And guess what? He felt a lot happier!
        """
        st.markdown(story)
    else:
        st.info("👈 Fill in all the boxes to see your silly story!")
