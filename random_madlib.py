import streamlit as st
import random
from sample_madlibs import st1, st2, st3, st4

st.title("🎲 Random Madlib Generator")

madlibs = [st1, st2, st3, st4]
chosen = random.choice(madlibs)

chosen.madlib()
