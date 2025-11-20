import streamlit as st
import random
from random_word import RandomWords

st.set_page_config(page_title="Chaos Prompt Generator", layout="wide")

st.title("Chaos Prompt Generator")
st.write("A surreal prompt generator powered by chaos, poetry, and nonsense.")

# Initialize RandomWords
r = RandomWords()

# Human descriptors and random ending descriptors
human_adj = [
    "mysterious", "ethereal", "surreal", "dreamlike", "eerie",
    "otherworldly", "luminous", "ageless", "enigmatic", "soft-lit"
]

random_descriptors = [
    "cinematic lighting", "strange dreamlike atmosphere", "glitching colors",
    "floating objects", "soft shadows", "fractal patterns", "foggy ambiance",
    "overexposed highlights", "vibrant reflections", "twisted perspective"
]

# Extra filler words for chaos
filler_words = ["shadow", "glass", "orbit", "echo", "signal", "mist", "void", "fractal", "pulse", "aura"]

def make_prompt(person_mode=False):
    # Generate 8 random words
    try:
        base_words = [r.get_random_word() for _ in range(8)]
    except:
        # Fallback if API fails
        base_words = ["ghost", "signal", "shadow", "orbit", "mist", "void", "pulse", "echo"]

    # Add a few filler words for extra randomness
    fragments = list(set(base_words + random.sample(filler_words, k=3)))
    random.shuffle(fragments)

    # Pick body and hints words
    body_words = fragments[:3]
    hints_words = fragments[3:6] if len(fragments) > 3 else []

    ending_descriptor = random.choice(random_descriptors)

    if person_mode:
        person_flavour = random.choice(fragments) if fragments else random.choice(human_adj)
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
