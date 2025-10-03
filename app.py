import streamlit as st
import matplotlib.pyplot as plt

# --- Traits ---
traits = ["D Ballerz", "Investors Vibe", "Foodie", "Chill Observer"]

# --- Questions with Naija vibez ---
questions = [
    {"question": "How do you like to spend your Friday night?",
     "options": {"D Ballerz": "Clubbing till mama calls 📞💃🏾",
                 "Investors Vibe": "Working on my side hustle, wrapping up the week's task 💼",
                 "Foodie": "Trying that new buka joint 🍲",
                 "Chill Observer": "Netflix and chill, Sleep 🎥"}},
    {"question": "What’s your go-to response when NEPA takes light?",
     "options": {"D Ballerz": "Oya music go continue from phone 🔊",
                 "Investors Vibe": "Back to grinding with laptop + hotspot 💻",
                 "Foodie": "Go buy street food 🍖",
                 "Chill Observer": "Just relax, light go still come, Social Media 📰"}},
    {"question": "What’s your must-have at owambe?",
     "options": {"D Ballerz": "Shayo and vibes 🍾",
                 "Investors Vibe": "Networking with big men 👔",
                 "Foodie": "Party Jollof and chicken 🥘",
                 "Chill Observer": "Sitting at the corner, observing 👀"}},
    {"question": "Which slang do you use the most?",
     "options": {"D Ballerz": "Who deyyyyyy?! 🔥",
                 "Investors Vibe": "No gree for anybody 💪🏾",
                 "Foodie": "If I perish i perish😋",
                 "Chill Observer": "E go be ✌🏾"}},
    {"question": "How do you react when fuel price increases?",
     "options": {"D Ballerz": "Still enter Uber to groove 🚗",
                 "Investors Vibe": "Sharp sharp calculate new budget 📊",
                 "Foodie": "Complain while buying gala in the bus 🍗",
                 "Chill Observer": "Shake head and trek jejely 🚶🏾"}},
    {"question": "What’s your dream vacation?",
     "options": {"D Ballerz": "Chilling at Maldives 🌍",
                 "Investors Vibe": "Silicon Valley for networking 🖥️",
                 "Foodie": "Ghana for waakye and kelewele 🍛",
                 "Chill Observer": "Obudu Ranch for peace and nature 🌿"}},
    {"question": "When it rains heavily, what’s your vibe?",
     "options": {"D Ballerz": "Still step out with umbrella, no dulling ☔",
                 "Investors Vibe": "Answer emails while stuck in traffic 🚦",
                 "Foodie": "Perfect weather for pepper soup 🍲",
                 "Chill Observer": "Sleep off with sweet breeze 😴"}},
    {"question": "What’s your ideal Sunday afternoon?",
     "options": {"D Ballerz": "Beach party with friends 🏖️",
                 "Investors Vibe": "Working on Monday plans 📑",
                 "Foodie": "Eating amala with gbegiri and ewedu 🍵",
                 "Chill Observer": "Laying on the couch, just vibing 🛋️"}},
    {"question": "What’s your most common phrase?",
     "options": {"D Ballerz": "Turn up or nothing 🎶",
                 "Investors Vibe": "Time is money ⏰💰",
                 "Foodie": "Abeg, where food dey? 🍛",
                 "Chill Observer": "We move 🚶🏾"}},
    {"question": "If you win small lottery money, what will you do?",
     "options": {"D Ballerz": "Host one big party 🥳",
                 "Investors Vibe": "Invest it straight 💹",
                 "Foodie": "Chop better buffet with friends 🍱",
                 "Chill Observer": "Save it and chill 😌"}}
]

# --- Session state initialization ---
if "page" not in st.session_state:
    st.session_state.page = 0
if "scores" not in st.session_state:
    st.session_state.scores = {trait: 0 for trait in traits}
if "answers" not in st.session_state:
    st.session_state.answers = {}

# --- Display current question ---
if st.session_state.page < len(questions):
    q = questions[st.session_state.page]
    st.subheader(f"Q{st.session_state.page+1}: {q['question']}")

    choice = st.radio("Pick one:", list(q["options"].values()), index=None, key=f"q{st.session_state.page}")

    # Next button
    if st.button("Next ➡️"):
        if choice:  # save answer only if selected
            st.session_state.answers[st.session_state.page] = choice
            st.session_state.page += 1
        else:
            st.warning("Please select an option before continuing!")

    # Back button (optional)
    if st.session_state.page > 0:
        if st.button("⬅️ Back"):
            st.session_state.page -= 1

# --- Show results at the end ---
else:
    st.header("🎉 Your Naija Personality Results 🎉")

    # Tally scores
    for i, q in enumerate(questions):
        choice = st.session_state.answers.get(i)
        if choice:
            for trait, option in q["options"].items():
                if option == choice:
                    st.session_state.scores[trait] += 1

    total = sum(st.session_state.scores.values())
    percentages = {t: (s/total)*100 for t, s in st.session_state.scores.items()}
    nonzero_percentages = {t: p for t, p in percentages.items() if p > 0}

    # --- Pie chart ---
    fig, ax = plt.subplots()
    ax.pie(
        nonzero_percentages.values(),
        labels=nonzero_percentages.keys(),
        autopct='%1.1f%%',
        startangle=90,
        colors=plt.cm.Set3.colors,
        wedgeprops={'edgecolor': 'white'}
    )
    ax.set_title("Your Naija Personality Mix")
    plt.axis("equal")
    st.pyplot(fig)

    # --- Summary ---
    dominant_trait = max(percentages, key=percentages.get)
    st.subheader("🎭 Your Personality Summary")
    st.write(f"Your dominant vibe is **{dominant_trait}** ({percentages[dominant_trait]:.1f}%)!")

    if st.button("🔄 Restart Quiz"):
        st.session_state.page = 0
        st.session_state.scores = {trait: 0 for trait in traits}
        st.session_state.answers = {}
