import streamlit as st
import requests
import random

st.title("Chaos Prompt Generator")
st.write("A surreal prompt generator powered by chaos, poetry, nonsense.")

# Random Word API URL
RANDOM_WORD_URL = "https://random-word-api.herokuapp.com/word?number=3"

# Datamuse API
DATAMUSE_URL = "https://api.datamuse.com/words?ml="

def get_random_words():
    try:
        r = requests.get(RANDOM_WORD_URL, timeout=5)
        if r.status_code == 200:
            return r.json()
        return ["ghost", "signal", "static"]  # fallback
    except:
        return ["shadow", "glass", "orbit"]

def get_related_words(word):
    try:
        r = requests.get(DATAMUSE_URL + word, timeout=5)
        if r.status_code == 200:
            words = [item["word"] for item in r.json()]
            return words[:10] if words else []
        return []
    except:
        return []

# Human descriptors for fallback or flavor
human_adj = [
    "mysterious", "ethereal", "surreal", "dreamlike", "eerie",
    "otherworldly", "luminous", "ageless", "enigmatic", "soft-lit"
]

def make_prompt(person_mode=False):
    base_words = get_random_words()
    trig
