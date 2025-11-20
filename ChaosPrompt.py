import streamlit as st
import random

st.set_page_config(page_title="Chaos Prompt Generator", layout="wide")

st.title("Chaos Prompt Generator")
st.write("A surreal prompt generator powered by chaos, poetry, and nonsense.")

# 500-word surreal/eldritch/chaotic list
all_words = [
"abyss","aether","aura","arcane","astral","altar","amber","anomaly","apparition","arboreal",
"aurora","ashen","artifact","basilisk","blight","bramble","bloom","banshee","barrow","beacon",
"catacomb","cinder","cavern","cipher","crystal","cobweb","corvus","chaos","chasm","cavernous",
"crypt","crux","catalyst","crevice","crescent","cobble","cavern","drift","dusk","dust","dome",
"drone","echo","ember","eclipse","ether","ethereal","effigy","fracture","fractal","fog","flare",
"frost","gossamer","gloom","glyph","glimmer","hollow","haze","haunt","hive","horizon","hollowed",
"incubus","iris","infernal","illusion","labyrinth","lantern","lattice","lament","loom","lumen",
"maelstrom","mist","mirage","myriad","neon","nether","nocturne","obelisk","obsidian","orb","orbit",
"oasis","omens","ombre","phantom","prism","pulse","pyre","quartz","rift","spire","specter","spectrum",
"shard","signal","solstice","shadow","spire","shroud","sable","tomb","twilight","veil","vortex",
"vein","void","wraith","warp","web","whisper","zenith","zephyr","zoetic","abyssion","alabaster",
"arcology","astrium","bloodmoon","celestia","cimmerian","cognizance","crystalline","darkspire",
"dawnlight","ebon","eclipse","empyrean","fathom","gloaming","grimoire","hallowed","hyperion",
"incubus","ionis","lore","luminesce","lurid","mausoleum","nebulon","nexus","noctis","obelion",
"phantasia","pyxis","reverie","sable","silica","somnium","sorcery","spectra","tenebris","umbrage",
"vellichor","voidborn","wraithborne","xenolith","zenobia","zircon"
]

# Human descriptors for person-centered prompts
human_adj = [
    "mysterious", "ethereal", "surreal", "dreamlike", "eerie",
    "otherworldly", "luminous", "ageless", "enigmatic", "soft-lit",
    "phantasmic", "haunted", "celestial", "gossamer", "arcane",
    "shadowed", "lucid", "ominous", "astral", "haunting"
]

# Random descriptors for endings
random_descriptors = [
    "cinematic lighting", "strange dreamlike atmosphere", "glitching colors",
    "floating objects", "soft shadows", "fractal patterns", "foggy ambiance",
    "overexposed highlights", "vibrant reflections", "twisted perspective",
    "distorted reality", "surreal reflections", "mirrored dimensions", "ethereal glow",
    "phantasmic hues", "floating geometry", "shifting shadows", "liquid light",
    "fractured space", "cosmic distortion"
]

# MidJourney parameters
mj_stylize_values = [50, 100, 250, 500, 625, 750, 1000]
mj_sref_values = [1, 2, 3, 4, 5, 10]

def make_prompt(person_mode=False, add_mj_params=True):
    # Pick 9 random words from expanded list
    fragments = random.sample(all_words, k=9)

    # Assign body, hints, and person words without overlap
    body_words = fragments[:3]
    hints_words = fragments[3:6]

    if person_mode:
        # person_flavour must be unique from body and hints
        available_for_person = fragments[6:]
        person_flavour = random.choice(available_for_person) if available_for_person else random.choice(human_adj)
        prompt_body = (
            f"A {person_flavour} person standing among {', '.join(body_words)}, "
            f"with hints of {', '.join(hints_words)}, "
            f"{random.choice(random_descriptors)}."
        )
    else:
        prompt_body = (
            f"A {body_words[0]} {body_words[1]} emerging from {body_words[2]}, "
            f"surrounded by {', '.join(hints_words)}, "
            f"{random.choice(random_descriptors)}."
        )

    if add_mj_params:
        s_val = random.choice(mj_stylize_values)
        sref_val = random.choice(mj_sref_values)
        prompt_body += f" --s {s_val} --sref {sref_val}"

    return prompt_body

# Initialize session state
if "prompt" not in st.session_state:
    st.session_state.prompt = ""

# Person toggle
person_mode = st.checkbox("Center the prompt around a person", value=False)

# MidJourney toggle
add_mj = st.checkbox("Add random MidJourney --s and --sref parameters", value=True)

# Generate Prompt button
if st.button("Generate Prompt"):
    st.session_state.prompt = make_prompt(person_mode, add_mj_params=add_mj)

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
