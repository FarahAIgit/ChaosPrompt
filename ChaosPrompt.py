import streamlit as st
import requests
import random

st.set_page_config(page_title="Chaos Prompt Generator", layout="wide")

st.title("Chaos Prompt Generator")
st.write("A surreal prompt generator powered by chaos, poetry, and nonsense.")

# Random Word API URL
RANDOM_WORD_URL = "https://random-word-api.herokuapp.com/word?number=5"

# Datamuse API
DATAMUSE_URL = "https://api.datamuse.com/words?ml="

def get_random_words():
    try:
        r = requests.get(RANDOM_WORD_URL, timeout=5)
        if r.status_code == 200:
            return r.json()
        return ["ghost", "signal", "static", "shadow", "orbit"]
    except:
        return ["shadow", "glass", "orbit", "echo", "pulse"]

def get_related_words(word):
    try:
        r = requests.get(DATAMUSE_URL + word, timeout=5)
        if r.status_code == 200:
            words = [item["word"] for item in r.json()]
            return words[:10] if words else []
        return []
    except:
        return []

human_adj = [
    "mysterious", "ethereal", "surreal", "dreamlike", "eerie",
    "otherworldly", "luminous", "ageless", "enigmatic", "soft-lit"
]

random_descriptors = [
    "cinematic lighting", "strange dreamlike atmosphere", "glitching colors",
    "floating objects", "soft shadows", "fractal patterns", "foggy ambiance",
    "overexposed highlights", "vibrant reflections", "twisted perspective"
]

def make_prompt(person_mode=False):
    # Get more base words for variety
    base_words = get_random_words() + get_random_words()  # 10 words total
    base_words = list(set(base_words))  # remove duplicates

    trigger_word = random.choice(base_words)
    related = get_related_words(trigger_word)

    # Sample 2-3 related words
    flavour = random.sample(related, k=min(len(related), random.randint(2, 3))) if related else []

    # Extra random filler words to add variety
    filler = random.sample(["shadow", "glass", "orbit", "echo", "signal", "mist", "void", "fractal", "pulse", "aura"], k=3)

    # Combine all fragments and remove duplicates
    fragments = list(set(base_words + flavour + filler))
    random.shuffle(fragments)

    # Pick separate words for "body" and "hints of"
    body_words = fragments[:3]
    hints_words = fragments[3:6] if len(fragments) > 3 else []

    # Random descriptor for the ending
    ending_descriptor = random.choice(random_descriptors)

    if person_mode:
        person_flavour = random.choice(flavour) if flavour else random.choice(human_adj)
        prompt = (
            f"A {person_flavour} person standing among {', '.join(body_words)}, "
            f"with hints of {', '.join(hints_words) if hints_words else 'ambient chaos'}, "
            f"{ending_descriptor}."
        )
    else:
        prompt = (
            f"A {body_words[0]} {body_words[1]} emerging from {body_words[2]}, "
            f"surrounded by {', '.join(hints_words) if hints_words else 'ambient chaos'}, "
            f"{ending_descriptor}."
        )

    return prompt

# Initialize session state
if "prompt" not in st.session_state:
    st.session_state.prompt = ""

person_mode = st.checkbox("Center the prompt around a person", value=False)

# Generate Prompt button
if st.button("Generate Prompt"):
    st.session_state.prompt = make_prompt(person_mode)

# Display prompt
if st.session_state.prompt:
    st.text_area("Your Generated Prompt:", value=st.session_state.prompt, height=120)

# Footer
st.markdown(
    "Created by [@Farah_ai_](https://x.com/Farah_ai_)",
    unsafe_allow_html=True
)
st.markdown(
    "Use of this generator is free but if you find it useful please consider donating a little; [Donate via Kofi](https://ko-fi.com/farahai)",
    unsafe_allow_html=True
)
