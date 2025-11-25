import streamlit as st
import random
import itertools

st.set_page_config(page_title="Chaos Prompt Generator", layout="wide")

# ---------------------------
# Minimal dark styling
# ---------------------------
st.markdown(
    """
    <style>
    body { background-color: #0d0d0f; color: #e8e6e3; font-family: 'Courier New', monospace; }
    .stApp { min-height: 100vh; }
    .stTextArea textarea { background: rgba(10,10,12,0.7); color: #e8e6e3; border: 1px solid #2f2f31; }
    .stButton>button { background-color:#252427; color:#f2f0ef; border-radius:8px; padding:8px 14px; }
    .block-container { padding: 1rem 2rem; }
    h1,h2,h3 { color: #ff8c00; font-family: 'Courier New', monospace; }
    .footer { color:#a8a6a3; font-size:12px; margin-top:8px; }

    /* Style the code block to match the theme */
    .stCodeBlock { background: rgba(10,10,12,0.7); }

    /* Make code block text wrap instead of scroll */
    .stCodeBlock code { 
        white-space: pre-wrap !important; 
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
    }
    .stCodeBlock pre {
        white-space: pre-wrap !important;
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
        overflow-x: auto !important;
    }
    [data-testid="stCode"] {
        white-space: pre-wrap !important;
    }
    [data-testid="stCode"] code {
        white-space: pre-wrap !important;
        word-wrap: break-word !important;
    }

    /* ----------------------------------------- */
    /* ADDED: Checkbox styling to match theme    */
    /* ----------------------------------------- */
    [data-baseweb="checkbox"] > div:first-child {
        border-color: #ff8c00 !important;
    }
    [data-baseweb="checkbox"] svg {
        fill: #ff8c00 !important;
    }
    /* ----------------------------------------- */

    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div style="text-align:center;">
        <img src="https://raw.githubusercontent.com/FarahAIgit/ChaosPrompt/e6cfefad007a1e2c6bff3a717638961bfb49d771/ChaosPrompt_Logo.png" style="width:100%; max-width:600px; margin-bottom:20px;">
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("### 🔮 Chaos Prompt Generator 🔮", unsafe_allow_html=True)
st.markdown("*A surreal prompt engine*")
st.markdown("---")

# Add CSS to center the title and tagline
st.markdown(
    """
    <style>
    /* Center the first h3 (title) and the first paragraph (tagline) */
    .block-container > div > div > div:first-child h3 {
        text-align: center;
    }
    .block-container > div > div > div:first-child p {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# Clean person descriptor pool
# ---------------------------
PERSON_BASE_DESCRIPTORS = [
    "ethereal figure", "lone wanderer", "cloaked silhouette", "veiled stranger",
    "spectral woman", "shadow-touched figure", "war-torn survivor",
    "cosmic pilgrim", "star-marked traveler", "quiet nomad", "wandering oracle",
    "dusk-skinned silhouette", "pale drifter", "dusk-haired mystic",
    "nocturnal figure", "storm-eyed visionary", "scar-lined wanderer",
    "obsidian-haired stranger", "porcelain-skinned figure", "freckled phantom",
    "raven-haired traveler", "luminous-faced wanderer", "forgotten outcast",
    "haunted dreamer",
    "the seeker", "the observer", "the initiate", "the wayfarer",
    "the revenant", "the pilgrim", "the apostate", "the wanderer",
    "the keeper", "the dream-carrier", "the archivist",
    "the outlier", "the gatewatcher"
]

PERSON_STYLE_MODIFIERS = [
    "draped in tattered fabrics", "wrapped in celestial cloth",
    "wearing layered darkwear", "armored in fractured metal",
    "clad in flowing noir robes", "marked by arcane sigils",
    "wearing worn leather", "dressed in dust-coated linens",
    "adorned with subtle jewelry", "wrapped in weathered cloaks",
    "marked by glowing threads"
]

# ---------------------------
# Programmatic generation of 1000 mixed words
# ---------------------------
base_nouns = [...]
mods = [...]
extras = [...]

def build_word_pool(target=1000):
    pool = []
    pool.extend(base_nouns)
    pool.extend(extras)
    for a, b in itertools.product(mods, base_nouns):
        pool.append(f"{a} {b}")
        if len(pool) >= target:
            break
    if len(pool) < target:
        for a, b in itertools.product(mods, extras):
            pool.append(f"{a} {b}")
            if len(pool) >= target:
                break
    uniq = []
    for w in pool:
        if w not in uniq:
            uniq.append(w)
        if len(uniq) >= target:
            break
    return uniq

ATMOSPHERIC_WORDS = build_word_pool(1000)

# Chaos word generator (intact)
def generate_chaos_word():
    ...
def mix_chaos_words(word_list, chaos_percentage=0.4):
    ...

VISUAL_DESCRIPTORS = [...]
MJ_STYLIZE_VALUES = [...]

def make_prompt(...):
    ...

# ---------------------------
# Streamlit UI
# ---------------------------
if "prompt" not in st.session_state:
    st.session_state.prompt = ""

col1, col2 = st.columns([1, 2])

with col1:
    st.header("Options")
    person_mode = st.checkbox("Center the prompt around a person", value=False)
    add_mj = st.checkbox("Add random MidJourney --s and --sref", value=True)
    pure_chaos = st.checkbox("🌀 Pure Chaos Mode (generate invented words)", value=False)
    if st.button("Generate Prompt"):
        st.session_state.prompt = make_prompt(person_mode, add_mj_params=add_mj, pure_chaos_mode=pure_chaos)
    st.markdown("---")
    st.markdown("Created by [@Farah_ai_](https://x.com/Farah_ai_)", unsafe_allow_html=True)

with col2:
    st.header("Output")
    if st.session_state.prompt:
        st.markdown("**Your Generated Prompt** _(click the copy icon in the top-right corner):_")
        st.code(st.session_state.prompt, language=None)

st.markdown("Tip: Click the copy icon (top right of the prompt box) to copy your prompt.", unsafe_allow_html=True)
st.markdown("---")
st.markdown(
    "Use of this generator is free but if you find it useful please consider donating a little; [Donate via Kofi](https://ko-fi.com/farahai)",
    unsafe_allow_html=True
)
st.markdown("*~ Let the chaos bloom ~*", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .block-container {
        backdrop-filter: blur(6px);
        background: rgba(0, 0, 0, 0.55);
        border-radius: 12px;
        padding: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
