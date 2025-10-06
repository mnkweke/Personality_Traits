import streamlit as st
from collections import Counter

# Page setup
st.set_page_config(page_title="Naija Personality Quiz", layout="centered")

# --- QUESTIONS ---
questions = [
    {
        "question": "Which landmark feels like home? Pick the spot that calls your name:",
        "options": {
            "Kano City Walls": "Hausa",
            "Sukur Cultural Landscape": "Hausa",
            "Zuma Rock": "North Central",
            "Olumo Rock": "Yoruba",
            "Onitsha Niger Bridge": "Igbo",
            "Oloibiri Oil Well": "South South"
        }
    },
    {
        "question": "What language do you love to sprinkle into conversations?",
        "options": {
            "Yoruba": "Yoruba",
            "Hausa": "Hausa",
            "Igbo": "Igbo",
            "Pidgin": "South South",
            "Ibibio/Efik": "South South"
        }
    },
    {
        "question": "Pick your comfort food for a rainy day.",
        "options": {
            "Jollof Rice": "South South",
            "Tuwo Shinkafa & Miyan Kuka": "Hausa",
            "Afang Or Edikang Ikong Soup": "South South",
            "Amala & Ewedu": "Yoruba",
            "Nkwobi Or Isi Ewu": "Igbo"
        }
    },
    {
        "question": "Your ideal street snack is...",
        "options": {
            "Boli - Roasted Plantain": "South South",
            "Akara & Bread": "Yoruba",
            "Masa": "Hausa",
            "Roasted Corn & Ube": "Igbo"
        }
    },
    {
        "question": "What gets you dancing fastest?",
        "options": {
            "Afrobeat": "Yoruba",
            "Highlife": "Igbo",
            "Fuji/Apala": "Yoruba",
            "Afro-Highlife": "South South",
            "Hausa/Fulani Folk Tunes": "Hausa"
        }
    },
    {
        "question": "What's your go-to expression?",
        "options": {
            "Ahhh!": "South South",
            "Nna Men!": "Igbo",
            "Kai!": "Hausa",
            "Omo!": "Yoruba",
            "Area!": "South South",
            "Walahi!": "Hausa"
        }
    },
    {
        "question": "December vibe?",
        "options": {
            "Beach & Palm Wine": "South South",
            "King The Hills / Nature Trails": "Hausa",
            "Lagos Nightlife": "Yoruba",
            "Village Visit & Family Time": "Igbo"
        }
    },
    {
        "question": "If you had a Nigerian superpower, you'd be...",
        "options": {
            "The Hustler": "Hausa",
            "The Innovator": "Yoruba",
            "The Party Starter": "South South",
            "The Connector": "Igbo"
        }
    },
    {
        "question": "Pick the proverb that speaks to you most:",
        "options": {
            "A Child Who Washes His Hands Dines With Elders": "Igbo",
            "When Spider Webs Unite, They Can Tie A Lion.": "South South",
            "No Matter How Long The Night, The Day Will Break.": "Hausa",
            "The Person Who Fetches Firewood Should Expect The Lizard's Visit.": "Yoruba"
        }
    },
    {
        "question": "If your friends described your vibe in one word, it'd be:",
        "options": {
            "Bold": "Hausa",
            "Warm": "South South",
            "Resilient": "Yoruba",
            "Spirited": "Igbo"
        }
    },
]

# --- SESSION STATE ---
if "index" not in st.session_state:
    st.session_state.index = 0
if "answers" not in st.session_state:
    st.session_state.answers = []

# --- CUSTOM STYLING ---
st.markdown("""
    <style>
        body {
            background-color: #004d40;
            color: white;
        }
        .stApp {
            background-color: #004d40;
        }
        .main {
            background-color: #004d40;
            color: #ffffff;
            font-family: 'Poppins', sans-serif;
        }
        h1, h2, h3, h4, h5 {
            text-align: center;
            color: #ffffff;
        }
        .stButton>button {
            width: 100%;
            background-color: #007a5e;
            color: white;
            font-weight: 600;
            border-radius: 12px;
            padding: 12px;
            margin-top: 8px;
            transition: 0.3s;
            border: none;
            box-shadow: 0 3px 10px rgba(0,0,0,0.2);
        }
        .stButton>button:hover {
            background-color: #00a676;
            transform: scale(1.03);
        }
        .stProgress > div > div > div > div {
            background-color: #00a676;
        }
    </style>
""", unsafe_allow_html=True)

# --- APP HEADER ---
st.title("🇳🇬 Naija Personality Quiz")
st.caption("Find out which region your vibe truly belongs to 💚🤍💚")

# --- QUIZ LOGIC ---
index = st.session_state.index

# Progress bar
progress = (index / len(questions))
st.progress(progress)

if index < len(questions):
    q = questions[index]
    st.markdown(f"### {index + 1}. {q['question']}")

    # Display each option as a button
    for opt, region in q["options"].items():
        if st.button(opt, key=f"{index}_{opt}"):
            st.session_state.answers.append(region)
            st.session_state.index += 1
            st.rerun()

    st.markdown(f"<p style='text-align:center; opacity:0.7;'>Question {index+1} of {len(questions)}</p>", unsafe_allow_html=True)

else:
    st.success("🎉 Quiz Complete! Let’s see your Naija vibe:")
    counts = Counter(st.session_state.answers)
    total = sum(counts.values())

    st.markdown("### You are:")
    for region, count in counts.items():
        percent = (count / total) * 100
        st.markdown(f"**{percent:.0f}% {region}**")

    st.balloons()

    if st.button("Restart 🔁"):
        st.session_state.index = 0
        st.session_state.answers = []
        st.rerun()
