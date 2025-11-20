import streamlit as st
import random

st.set_page_config(page_title="Chaos Prompt Generator", layout="wide")

# --- CSS Styling ---
st.markdown(
    """
    <style>
    body {
        background-color: #121212;
        color: #e0e0e0;
        font-family: 'Courier New', monospace;
        background-image: url('https://i.imgur.com/3vXl8U8.jpg');  /* subtle eldritch background */
        background-size: cover;
        background-attachment: fixed;
    }
    h1, h2, h3 {
        color: #ff8c00;
        font-family: 'Courier New', monospace;
    }
    .stTextArea textarea {
        background: rgba(0,0,0,0.6);
        border: 2px solid #444;
        box-shadow: 0 0 10px #ff8c00;
        color: #e0e0e0;
        font-family: 'Courier New', monospace;
        font-size: 16px;
    }
    .stButton>button {
        background-color: #2b2b2b;
        color: #f5f5f5;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
        font-family: 'Courier New', monospace;
        cursor: pointer;
    }
    .stCheckbox>div {
        color: #f5f5f5;
        font-family: 'Courier New', monospace;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Headings ---
st.markdown("### 🔮 Chaos Prompt Generator 🔮")
st.markdown("*A surreal, eldritch prompt engine for MidJourney and beyond*")
st.markdown("---")

# --- Word Pools ---
all_words = ["abyss","aether","aura","arcane","astral","altar","amber","anomaly","apparition","arboreal",
"aurora","ashen","artifact","basilisk","blight","bramble","bloom","banshee","barrow","beacon",
"catacomb","cinder","cavern","cipher","crystal","cobweb","corvus","chaos","chasm","cavernous",
"crypt","crux","catalyst","crevice","crescent","cobble","cavern","drift","dusk","dust","dome",
"drone","echo","ember","eclipse","ether","ethereal","effigy","fracture","fractal","fog","flare",
"frost","gossamer","gloom","glyph","glimmer","hollow","haze","haunt","hive","horizon","hollowed",
"incubus","iris","infernal","illusion","labyrinth","lantern","lattice","lament","loom","lumen",
"maelstrom","mist","mirage","myriad","neon","nether","nocturne","obelisk","obsidian","orb","orbit",
"oasis","omens","ombre","phantom","prism","pulse","pyre","quartz","rift","spire","specter","spectrum",
"shard","signal","solstice","shadow","spire","shroud","sable","tomb","twilight","veil","vortex",
"vein","void","wraith","warp","web","whisper","zenith","zephyr","zoetic"]

human_adj = ["mysterious", "ethereal", "surreal", "dreamlike", "eerie","otherworldly",
"luminous", "ageless", "enigmatic", "soft-lit","phantasmic","haunted","celestial","gossamer",
"arcane","shadowed","lucid","ominous","astral","haunting"]

random_descriptors = ["cinematic lighting", "strange dreamlike atmosphere", "glitching colors",
"floating objects", "soft shadows", "fractal patterns", "foggy ambiance", "overexposed highlights",
"vibrant reflections", "twisted perspective","distorted reality", "surreal reflections",
"mirrored dimensions", "ethereal glow","phantasmic hues","floating geometry","shifting shadows",
"liquid light","fractured space","cosmic distortion"]

mj_stylize_values = [50, 100, 250, 500, 625, 750, 1000]

def make_prompt(person_mode=False, add_mj_params=True):
    fragments = random.sample(all_words, k=9)
    body_words = fragments[:3]
    hints_words = fragments[3:6]

    if person_mode:
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
        sref_val = random.randint(1000000000, 9999999999)
        prompt_body += f" --s {s_val} --sref {sref_val}"

    return prompt_body

# --- Session state ---
if "prompt" not in st.session_state:
    st.session_state.prompt = ""

# --- Layout columns ---
col1, col2 = st.columns([1,2])

with col1:
    person_mode = st.checkbox("Center the prompt around a person", value=False)
    add_mj = st.checkbox("Add random MidJourney --s and --sref parameters", value=True)
    if st.button("Generate Prompt"):
        st.session_state.prompt = make_prompt(person_mode, add_mj_params=add_mj)

with col2:
    if st.session_state.prompt:
        st.text_area("Your Generated Prompt:", value=st.session_state.prompt, height=150)

# --- Footer ---
st.markdown("---")
st.markdown(
    "Created by [@Farah_ai_](https://x.com/Farah_ai_)", unsafe_allow_html=True
)
st.markdown(
    "*~ Let the chaos guide your creations ~*", unsafe_allow_html=True
)
