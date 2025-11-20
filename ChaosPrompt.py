import streamlit as st
import random

st.set_page_config(page_title="Chaos Prompt Generator", layout="wide")

st.title("Chaos Prompt Generator")
st.write("A surreal prompt generator powered by chaos, poetry, and nonsense.")

# Local word list for fully random prompts
all_words = [
    "ghost","signal","shadow","orbit","mist","void","pulse","echo","aura",
    "fractal","glitch","neon","crystal","smoke","flare","vortex","ripple",
    "haze","flare","cinder","lumen","rift","spiral","ember","drift","cobweb",
    "gloom","spark","shard","lattice","hollow","veil","frost","bloom","drone"
]

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

def make_prompt(person_mode=False):
    # Pick 8 random words from local list
    fragments = random.sample(all_words, k=8)

    # Separate body and hints words
    body_words = fragments[:3]
    hints_words = fragments[3:6]

    # Pick random descriptor for ending
    ending_descriptor = random.choice(random_descriptors)

    if person_mode:
        person_flavour = random.choice(all_words) if all_words else random.choice(human_adj)
        prompt = (
            f"A {person_flavour} person standing among {', '.join(body_words)}, "
            f"with hints of {', '.join(hints_words)}, "
            f"{ending_descriptor}."
        )
    else:
        prompt = (
            f"A {body_words[0]} {body_words[1]} emerging from {body_words[2]}, "
            f"surrounded by {', '.join(hints_words)}, "
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
