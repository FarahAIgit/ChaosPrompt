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
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("### 🔮 Chaos Prompt Generator 🔮")
st.markdown("*A surreal prompt engine*")
st.markdown("---")

# ---------------------------
# Clean person descriptor pool
# ---------------------------
PERSON_DESCRIPTORS = [
    # Physical / Appearance
    "ethereal figure", "lone wanderer", "cloaked silhouette", "veiled stranger",
    "spectral woman", "shadow-touched figure", "war-torn survivor",
    "cosmic pilgrim", "star-marked traveler", "quiet nomad", "wandering oracle",
    "dusk-skinned silhouette", "pale drifter", "dusk-haired mystic",
    "nocturnal figure", "storm-eyed visionary", "scar-lined wanderer",
    "obsidian-haired stranger", "porcelain-skinned figure", "freckled phantom",
    "raven-haired traveler", "luminous-faced wanderer", "forgotten outcast",
    "haunted dreamer",

    # Fashion / Style
    "draped in tattered fabrics", "wrapped in celestial cloth",
    "wearing layered darkwear", "armored in fractured metal",
    "clad in flowing noir robes", "marked by arcane sigils",
    "wearing worn leather", "dressed in dust-coated linens",
    "adorned with subtle jewelry", "wrapped in weathered cloaks",
    "marked by glowing threads",

    # Roles / Archetypes
    "the seeker", "the observer", "the initiate", "the wayfarer",
    "the revenant", "the pilgrim", "the apostate", "the wanderer",
    "the keeper", "the dream-carrier", "the archivist",
    "the outlier", "the gatewatcher"
]

# ---------------------------
# Programmatic generation of 1000 mixed words
# (so we don't paste 1000 strings verbatim)
# ---------------------------
base_nouns = [
    "abyss","aether","aura","altar","anomaly","apparition","astral","amber","arcane","atlas","ashen",
    "animal","apple","artifact","autumn","bloom","bramble","barrow","beacon","brick","bridge",
    "bubble","building","butterfly","breeze","boulder","bottle","cinder","cavern","cipher","crystal",
    "cobweb","corvus","chaos","chasm","cloud","copper","candle","city","circle","cliff","clock",
    "cloth","clover","cluster","cobalt","crown","drift","dusk","dust","dome","drone","dream",
    "delta","diamond","dandelion","ember","eclipse","ether","effigy","energy","echo","engine","earth",
    "elm","element","emotion","feather","field","forest","flare","foam","frost","fog","fabric",
    "flower","flame","fawn","flux","gossamer","gloom","glyph","glimmer","garden","glass","ghost",
    "gate","galaxy","granite","grain","hollow","haze","horizon","hive","harbor","harp","harmony",
    "heat","helix","honey","hum","hunger","iris","illusion","ink","iron","ice","image","industry",
    "island","idol","interval","idea","ivory","labyrinth","lantern","lattice","lament","lake","leaf",
    "linen","light","lumen","logic","lily","mist","mirage","myriad","neon","nether","nocturne","noise",
    "night","nature","needle","nest","notion","obelisk","obsidian","orchid","orbit","oasis","oak",
    "opal","omen","oxide","object","origin","prism","pulse","pyre","pearl","petal","pattern","planet",
    "plate","paper","path","pond","quartz","quiet","quest","quill","quasar","quilt","quartzite","quiver",
    "rift","spire","specter","spectrum","shard","signal","solstice","shadow","shroud","sable","sand",
    "salt","steam","stone","spring","star","smoke","silver","scarlet","structure","shore","shape",
    "tomb","twilight","veil","vortex","vein","void","vessel","vine","vapor","valley","vector","vista",
    "vintage","wraith","warp","web","whisper","water","wind","wood","wax","wave","wildflower","willow",
    "wool","woven","zenith","zephyr","zone","zinnia","zircon"
]

# adjectives / modifiers
mods = [
    "ancient","broken","burned","crystalline","damp","drifting","echoing","faint","fractured","frozen",
    "gilded","glowing","hollow","iridescent","jagged","looming","mottled","muted","noisy","odd",
    "polished","prismatic","quiet","rusted","sere","soft","spattered","stained","textured","torn",
    "weathered","wet","worn","woven","grainy","gleaming","foggy","silken","matte","glossy"
]

# textures, materials, tech, emotions, places
extras = [
    "marble","chrome","velvet","leather","copper","steel","plastic","paper","glass","lace",
    "circuitry","neon","analog","digital","signal","static","magnet","wire","node","server",
    "memory","echoes","currents","driftwood","shore","lighthouse","market","terrace","balcony",
    "root","stem","trunk","branch","orchid","lumen","magnet","particle","quantum","gravity","solar",
    "tidal","volcanic","ember","ink","canvas","texture","threshold","liminal","subliminal","clockwork",
    "dustcloud","flash","spark","voltage","current","magnetism","transmission","reflection","horizon",
    "skyline","flightpath","birdsong","footfall","heartbeat","breath","vision","memory","chromatic",
    "monochrome","gradient","contrast","exposure","focus","blur","depth","dimension","form","mass",
    "energy","spirit","attic","cellar","chimney","window","gardenpath","alleyway","arch","column",
    "keystone","pillar","monument","talisman","key","compass","map","journal","shardglass","bark","soil",
    "puddle","dustmote","wireframe"
]

# Build a larger mixed pool programmatically to reach ~1000 unique-ish items
def build_word_pool(target=1000):
    pool = []
    # start with base nouns and extras first
    pool.extend(base_nouns)
    pool.extend(extras)
    # combine basic modifiers with base nouns to make more varied words
    for a, b in itertools.product(mods, base_nouns):
        pool.append(f"{a} {b}")
        if len(pool) >= target:
            break
    # if still short, combine modifiers with extras
    if len(pool) < target:
        for a, b in itertools.product(mods, extras):
            pool.append(f"{a} {b}")
            if len(pool) >= target:
                break
    # ensure unique and trim to target
    uniq = []
    for w in pool:
        if w not in uniq:
            uniq.append(w)
        if len(uniq) >= target:
            break
    return uniq

ATMOSPHERIC_WORDS = build_word_pool(1000)

# ---------------------------
# Visual descriptor pool and MJ values
# ---------------------------
VISUAL_DESCRIPTORS = [
    "glitching colors","drifting light bloom","floating architecture","fractured reflections",
    "shifting geometry","soft neon haze","overexposed contours","cosmic distortion",
    "fog layers moving like breath","shimmering gradients","broken light scatter",
    "deep chromatic shadows","mirrored echo forms","vibrating outlines","pulsing soft glow",
    "ghostlike motion blur","flickering perspective","liquid reflections","surreal dimensional fold",
    "negative-space highlights"
]

MJ_STYLIZE_VALUES = [50, 100, 250, 500, 625, 750, 1000]

# ---------------------------
# Prompt builder with full de-duplication
# ---------------------------
def make_prompt(person_mode=False, add_mj_params=True):
    # sample 9 unique words from ATMOSPHERIC_WORDS
    fragments = random.sample(ATMOSPHERIC_WORDS, k=9)

    # body words (3), hints (3), person-source (3)
    body_words = fragments[0:3]
    hint_words = fragments[3:6]
    person_candidates = fragments[6:9]  # guaranteed not to overlap with body/hints

    # choose a clean person descriptor (phrase) from pool,
    # but if you prefer a single-word person-flavour, use person_candidates
    person_phrase = random.choice(PERSON_DESCRIPTORS)
    # If we want to sometimes use a single-word adjective/noun as "person-flavour",
    # we can mix in a candidate occasionally. For now person_phrase is coherent.

    # Build prompt depending on mode
    if person_mode:
        prompt_body = (
            f"A {person_phrase} standing among {body_words[0]}, {body_words[1]}, {body_words[2]}, "
            f"with hints of {hint_words[0]}, {hint_words[1]}, {hint_words[2]}, "
            f"{random.choice(VISUAL_DESCRIPTORS)}"
        )
    else:
        # use two words as compound for subject so it reads okay
        prompt_body = (
            f"A {body_words[0]} {body_words[1]} emerging from {body_words[2]}, "
            f"surrounded by {hint_words[0]}, {hint_words[1]}, {hint_words[2]}, "
            f"{random.choice(VISUAL_DESCRIPTORS)}"
        )

    # optionally add MidJourney params
    if add_mj_params:
        s_val = random.choice(MJ_STYLIZE_VALUES)
        sref_val = random.randint(10**9, 10**10 - 1)  # 10-digit
        prompt_body += f" --s {s_val} --sref {sref_val}"

    return prompt_body

# ---------------------------
# Streamlit UI
# ---------------------------
if "prompt" not in st.session_state:
    st.session_state.prompt = ""

col1, col2 = st.columns([1, 2])

with col1:
    st.header("Controls")
    person_mode = st.checkbox("Center the prompt around a person", value=False)
    add_mj = st.checkbox("Add random MidJourney --s and --sref", value=True)
    if st.button("Generate Prompt"):
        st.session_state.prompt = make_prompt(person_mode, add_mj_params=add_mj)
    st.markdown("---")
    st.markdown("Tip: use the prompt directly in MidJourney or Flux. Manually copy from the box on the right.", unsafe_allow_html=True)
    st.markdown(
    "Created by [@Farah_ai_](https://x.com/Farah_ai_)", unsafe_allow_html=True)

with col2:
    st.header("Output")
    if st.session_state.prompt:
        st.text_area("Your Generated Prompt:", value=st.session_state.prompt, height=180)

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

