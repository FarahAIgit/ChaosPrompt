import streamlit as st
import random

st.set_page_config(page_title="Chaos Prompt Generator", layout="wide")

st.title("Chaos Prompt Generator")
st.write("A surreal prompt generator powered by chaos, poetry, and nonsense.")

# Expanded local word list
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
"vein","void","wraith","warp","web","whisper","zenith","zephyr","zeal","arcadia","ascent","blooming",
"bastion","blaze","brimstone","cavernous","cinder","cortex","corruption","crimson","cryptic","cusp",
"dawn","drizzle","driftwood","dread","echoes","eerie","emberlight","entropic","ephemeral","equinox",
"ethos","evermore","exile","fallow","fen","feral","fissure","flare","foggy","forlorn","fringe","gale",
"gloomy","grimoire","grove","harrow","haze","hollowed","horizon","hymn","icebound","incense","infinity",
"iris","labyrinthine","lurk","luminous","maelstrom","marrow","miasma","misty","moonglow","murk",
"mythos","nebulous","nightfall","nocturnal","omen","opal","orbital","otherworldly","palace","paradox",
"penumbra","phantasm","pinnacle","plume","portal","prismatic","pulse","pyre","quagmire","quartz","radiance",
"rift","roost","ruin","sable","scepter","shadowed","shimmer","shrouded","silhouette","spire","spectral",
"spiral","starlit","stasis","stygian","sublime","summit","temple","tenebrous","thicket","thrall","tombstone",
"tranquil","twilight","umbra","undergrowth","veil","verdant","void","vortex","waning","wraith","zephyr",
"aberration","abyssal","acolyte","alchemy","altar","apparition","arcadia","auric","bastion","blight",
"blaze","bramble","brooding","cataclysm","catacomb","chasm","coven","cursed","crag","crevasse",
"cryptic","cynosure","darkling","decay","descent","divination","draconian","dread","echoic","eldritch",
"empyreal","enigma","entropic","ephemeral","ethereal","fallow","fissure","forlorn","fractured","gleam",
"graven","grim","haunted","hallowed","haze","helix","hex","hollow","illusory","immortal","incantation",
"incense","infinity","labyrinth","lament","luminous","lurking","maelstrom","marrow","mire","mirage",
"myriad","necrotic","nether","nocturne","obelisk","occult","omniscient","ominous","oracular","orbital",
"otherworldly","palimpsest","penumbra","phantasm","phosphorescent","plume","portal","prismatic","pulse",
"pyre","quagmire","quartz","raven","relic","rift","runic","sanctum","scepter","shadowed","shard","shroud",
"spectral","spiral","starlit","stasis","stygian","sublime","summit","temple","tenebrous","thicket","thrall",
"tomb","tranquil","twilight","umbra","undergrowth","veil","verdant","vortex","waning","whisper","wraith",
"zenith","zephyr","zoetic","abyssion","alabaster","arcology","astrium","bloodmoon","celestia","cimmerian",
"cognizance","crystalline","darkspire","dawnlight","ebon","eclipse","empyrean","fathom","gloaming","grimoire",
"hallowed","hyperion","incubus","ionis","lore","luminesce","lurid","mausoleum","nebulon","nexus","noctis",
"obelion","phantasia","pyxis","reverie","sable","silica","somnium","sorcery","spectra","tenebris","umbrage",
"vellichor","voidborn","wraithborne","xenolith","zenobia","zircon"
]


# Expanded human descriptors
human_adj = [
    "mysterious", "ethereal", "surreal", "dreamlike", "eerie",
    "otherworldly", "luminous", "ageless", "enigmatic", "soft-lit",
    "phantasmic", "haunted", "celestial", "gossamer", "arcane",
    "shadowed", "enigmatic", "lucid", "ominous", "astral"
]

# Expanded random descriptors
random_descriptors = [
    "cinematic lighting", "strange dreamlike atmosphere", "glitching colors",
    "floating objects", "soft shadows", "fractal patterns", "foggy ambiance",
    "overexposed highlights", "vibrant reflections", "twisted perspective",
    "distorted reality", "surreal reflections", "mirrored dimensions", "ethereal glow",
    "phantasmic hues", "floating geometry", "shifting shadows", "liquid light",
    "fractured space", "cosmic distortion"
]

def make_prompt(person_mode=False):
    # Pick 8 random words from expanded list
    fragments = random.sample(all_words, k=8)

    # Separate body and hints words
    body_words = fragments[:3]
    hints_words = fragments[3:6]

    # Pick random descriptor for ending
    ending_descriptor = random.choice(random_descriptors)

    if person_mode:
        person_flavour = random.choice(fragments) if fragments else random.choice(human_adj)
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

