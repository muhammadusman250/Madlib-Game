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
        On a cloudy morning, **{name}** packed their backpack, grabbed a map,  
        and jumped into their trusty **{vehicle}**. This wasn't just any trip —  
        it was a mission to find the legendary land of **{place}**.  

        After hours of travel through wild forests and bumpy roads,  
        **{name}** finally reached the entrance to **{place}**. The air was thick with mystery,  
        and strange sounds echoed all around. But **{name}** was brave.  

        Deep inside the place, hidden behind a giant waterfall,  
        was a shining **{obj}** floating in the air. It sparkled like a thousand stars!  

        As soon as **{name}** touched the **{obj}**, the ground shook,  
        and ancient symbols lit up around them. Suddenly, a voice whispered:  
        *"Only the true adventurer may continue..."*

        Without fear, **{name}** began **{action}**, moving deeper into the magical place.  
        New doors opened, secrets were revealed, and the real journey had only just begun.  

        Who knows what adventures **{name}** will face next?  
        One thing is sure — with courage and curiosity, anything is possible!
        """
        st.markdown(story)
    else:
        st.info("👈 Fill in all the fields to see your full adventure!")
