import streamlit as st
import requests
import random

st.set_page_config(page_title="Chaos Prompt Generator", layout="wide")

# Custom CSS to recolor the checkbox to match the theme
st.markdown("""
<style>
/* checkbox outline */
div[data-testid="stCheckbox"] input + div:before {
    border: 2px solid #FDBAFC !important;
}

/* checkbox checked background */
div[data-testid="stCheckbox"] input:checked + div:before {
    background-color: #FDBAFC !important;
    border-color: #FDBAFC !important;
}

/* checkbox checkmark */
div[data-testid="stCheckbox"] input:checked + div:after {
    color: #260C34 !important;
}
</style>
""", unsafe_allow_html=True)

st.title("Chaos Prompt Generator")
st.write("A surreal prompt generator powered by chaos, poetry, and nonsense.")

# Random Word API URL
RANDOM_WORD_URL = "https://random-word-api.herokuapp.com/word?number=3"

# Datamuse API
DATAMUSE_URL = "https://api.datamuse.com/words?ml="

def get_random_words():
    try:
        r = requests.get(RANDOM_WORD_URL, timeout=5)
        if r.status_code == 200:
            return r.json()
        return ["ghost", "signal", "static"]
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

# Expanded human descriptors
person_adj = [
    "mysterious", "ethereal", "surreal", "dreamlike", "eerie",
    "otherworldly", "luminous", "ageless", "enigmatic", "soft-lit",
    "somber", "vivid-eyed", "shadow-faced", "hollow-gazed",
    "storm-touched", "glow-lined", "ashen-skinned", "feral-looking",
    "moon-kissed", "spectral-looking", "dusk-veiled", "fog-framed",
    "starlit", "ember-eyed", "gleaming", "worn", "fragmented",
    "untethered", "wandering", "electric"
]

# Word pool
all_words = [
    "spire","hollow","mango","cerulean","raven","paper","static","ember","ivory","signal",
    "copper","marble","velvet","python","orbit","iron","fracture","forest","neon","lattice",
    "canyon","memory","shadow","solstice","engine","gutter","aperture","glimmer","cog",
    "horizon","tangle","quartz","bubble","plasma","wax","maple","vortex","harbor","dust",
    "chrome","temple","spool","lantern","root","relic","silence","pattern","spectrum",
    "harvest","flame","pillar","glyph","thread","bloom","feather","drift","riddle","pulse",
    "mirrorless","coda","tremor","circuit","carpet","dawn","dusk","pearl","fragment",
    "crown","lumen","bow","storm","marrow","crystal","tower","spire","lilac","void",
] * 20  # approx 1000 words

random_descriptors = [
    "overexposed contours", "soft roaring haze", "fractured ambience",
    "drifting particles", "geometric fog", "ambient static",
    "holographic shimmer", "cold depth", "twisted reflections",
    "shifting negative space", "echoing silhouettes",
    "slow-burning glow", "mist-locked textures", "cosmic debris",
    "flickering shapes", "ashen atmosphere", "surreal distortion",
    "cinematic grain", "dreamlike heat haze"
]

def make_prompt(person_mode=False, include_sref=False):
    # choose 4–6 random words
    words = random.sample(all_words, k=6)
    w1, w2, w3, w4, w5, w6 = words

    descriptor = random.choice(random_descriptors)

    if person_mode:
        person_word = random.choice(person_adj)
        prompt = (
            f"A {person_word} person standing among {w1}, {w2}, and {w3}, "
            f"with hints of {w4}, {w5}, {w6}, {descriptor}."
        )
    else:
        prompt = (
            f"A {w1} {w2} emerging from {w3}, surrounded by {w4}, {w5}, {w6}, {descriptor}."
        )

    if include_sref:
        random_sref = str(random.randint(1000000000, 9999999999))
        prompt += f" --sref {random_sref}"

    return prompt

# Session state
if "prompt" not in st.session_state:
    st.session_state.prompt = ""

# UI widgets
person_mode = st.checkbox("Center prompt around a person", value=False)
include_sref = st.checkbox("Add random Midjourney --sref", value=False)

if st.button("Generate Prompt"):
    st.session_state.prompt = make_prompt(person_mode, include_sref)

# Output
if st.session_state.prompt:
    st.text_area("Your Generated Prompt:", value=st.session_state.prompt, height=140)

# Footer
st.markdown(
    "Created by [@Farah_ai_](https://x.com/Farah_ai_)",
    unsafe_allow_html=True
)
st.markdown(
    "Use of this generator is free but if you find it useful please consider donating; [Donate via Kofi](https://ko-fi.com/farahai)",
    unsafe_allow_html=True
)
