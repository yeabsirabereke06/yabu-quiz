import streamlit as st

# የገጹ ዲዛይን እና ከለር ማስተካከያ (CSS Styling)
st.set_page_config(page_title="Ultimate Quiz Game", page_icon="🌟", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        background: linear-gradient(45deg, #FF4B4B, #FF914D);
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        padding: 12px 24px;
        width: 100%;
        border: none;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.2);
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #FF914D, #FF4B4B);
        color: #fff;
    }
    h1 {
        color: #00ADB5;
        text-align: center;
        font-family: 'Helvetica Neue', sans-serif;
    }
    h3 {
        color: #EEEEEE;
    }
    .stRadio label {
        font-size: 16px;
        color: #DDDDDD;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌟 የዕውቀት ፈተና መድረክ / Ultimate Quiz Game 🌟")
st.markdown("---")

# ቋንቋ መምረጫ
lang = st.radio("እባክዎ ቋንቋ ይምረጡ / Choose Language:", ("አማርኛ", "English"))

if lang == "አማርኛ":
    st.subheader("🇪🇹 እንኳን ወደ አማርኛ የዕውቀት ፈተና በደህና መጡ!")
    
    questions = [
        {"q": "1. የፓይቶን ቋንቋ መቼ ተፈጠረ?", "options": ["ሀ) 1991", "ለ) 2000", "ሐ) 1985"], "answer": "ሀ) 1991"},
        {"q": "2. የኢትዮጵያ ዋና ከተማ አዲስ አበባ መቼ ተመሰረተች?", "options": ["ሀ) 1886", "ለ) 1900", "ሐ) 1930"], "answer": "ሀ) 1886"},
        {"q": "3. ከአለም ትልቁ ውቅያኖስ ማን ይባላል?", "options": ["ሀ) አትላንቲክ ውቅያኖስ", "ለ) ፓስፊክ ውቅያኖስ", "ሐ) ህንድ ውቅያኖስ"], "answer": "ለ) ፓስፊክ ውቅያኖስ"},
    ]
    
    user_answers = []
    for i, item in enumerate(questions):
        st.markdown(f"**{item['q']}**")
        ans = st.radio("", item["options"], key=f"am_{i}", label_visibility="collapsed")
        user_answers.append((ans, item["answer"]))
        st.markdown("---")
        
    if st.button("መልሶችን ላክ (Submit)", key="btn_am"):
        score = 0
        for user_ans, correct_ans in user_answers:
            if user_ans == correct_ans:
                score += 1
        
        st.success(f"🎉 ጨዋታው አልቋል! ያገኙት ጠቅላላ ነጥብ: {score} ከ {len(questions)}")
        if score == len(questions):
            st.balloons()

else:
    st.subheader("🇬🇧 Welcome to the Ultimate Quiz Game!")
    
    questions_en = [
        {"q": "1. When was the Python programming language created?", "options": ["a) 1991", "b) 2000", "c) 1985"], "answer": "a) 1991"},
        {"q": "2. Which planet is known as the Red Planet?", "options": ["a) Venus", "b) Mars", "c) Jupiter"], "answer": "b) Mars"},
        {"q": "3. What is the capital city of France?", "options": ["a) London", "b) Berlin", "c) Paris"], "answer": "c) Paris"},
    ]
    
    user_answers_en = []
    for i, item in enumerate(questions_en):
        st.markdown(f"**{item['q']}**")
        ans = st.radio("", item["options"], key=f"en_{i}", label_visibility="collapsed")
        user_answers_en.append((ans, item["answer"]))
        st.markdown("---")
        
    if st.button("Submit Answers", key="btn_en"):
        score = 0
        for user_ans, correct_ans in user_answers_en:
            if user_ans == correct_ans:
                score += 1
        
        st.success(f"🎉 Game Over! Your total score: {score} out of {len(questions_en)}")
        if score == len(questions_en):
            st.balloons()

# የገጹ ዲዛይን እና ከለር ማስተካከያ (CSS Styling)
st.set_page_config(page_title="Ultimate Quiz Game", page_icon="🌟", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        background: linear-gradient(45deg, #FF4B4B, #FF914D);
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        padding: 12px 24px;
        width: 100%;
        border: none;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.2);
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #FF914D, #FF4B4B);
        color: #fff;
    }
    h1 {
        color: #00ADB5;
        text-align: center;
        font-family: 'Helvetica Neue', sans-serif;
    }
    h3 {
        color: #EEEEEE;
    }
    .stRadio label {
        font-size: 16px;
        color: #DDDDDD;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌟 የዕውቀት ፈተና መድረክ / Ultimate Quiz Game 🌟")
st.markdown("---")

# ቋንቋ መምረጫ
lang = st.radio("እባክዎ ቋንቋ ይምረጡ / Choose Language:", ("አማርኛ", "English"))

if lang == "አማርኛ":
    st.subheader("🇪🇹 እንኳን ወደ አማርኛ የዕውቀት ፈተና በደህና መጡ!")
    
    questions = [
        {"q": "1. የፓይቶን ቋንቋ መቼ ተፈጠረ?", "options": ["ሀ) 1991", "ለ) 2000", "ሐ) 1985"], "answer": "ሀ) 1991"},
        {"q": "2. የኢትዮጵያ ዋና ከተማ አዲስ አበባ መቼ ተመሰረተች?", "options": ["ሀ) 1886", "ለ) 1900", "ሐ) 1930"], "answer": "ሀ) 1886"},
        {"q": "3. ከአለም ትልቁ ውቅያኖስ ማን ይባላል?", "options": ["ሀ) አትላንቲክ ውቅያኖስ", "ለ) ፓስፊክ ውቅያኖስ", "ሐ) ህንድ ውቅያኖስ"], "answer": "ለ) ፓስፊክ ውቅያኖስ"},
    ]
    
    user_answers = []
    for i, item in enumerate(questions):
        st.markdown(f"**{item['q']}**")
        ans = st.radio("", item["options"], key=f"am_{i}", label_visibility="collapsed")
        user_answers.append((ans, item["answer"]))
        st.markdown("---")
        
    if st.button("መልሶችን ላክ (Submit)", key="btn_am"):
        score = 0
        for user_ans, correct_ans in user_answers:
            if user_ans == correct_ans:
                score += 1
        
        st.success(f"🎉 ጨዋታው አልቋል! ያገኙት ጠቅላላ ነጥብ: {score} ከ {len(questions)}")
        if score == len(questions):
            st.balloons()

else:
    st.subheader("🇬🇧 Welcome to the Ultimate Quiz Game!")
    
    questions_en = [
        {"q": "1. When was the Python programming language created?", "options": ["a) 1991", "b) 2000", "c) 1985"], "answer": "a) 1991"},
        {"q": "2. Which planet is known as the Red Planet?", "options": ["a) Venus", "b) Mars", "c) Jupiter"], "answer": "b) Mars"},
        {"q": "3. What is the capital city of France?", "options": ["a) London", "b) Berlin", "c) Paris"], "answer": "c) Paris"},
    ]
    
    user_answers_en = []
    for i, item in enumerate(questions_en):
        st.markdown(f"**{item['q']}**")
        ans = st.radio("", item["options"], key=f"en_{i}", label_visibility="collapsed")
        user_answers_en.append((ans, item["answer"]))
        st.markdown("---")
        
    if st.button("Submit Answers", key="btn_en"):
        score = 0
        for user_ans, correct_ans in user_answers_en:
            if user_ans == correct_ans:
                score += 1
        
        st.success(f"🎉 Game Over! Your total score: {score} out of {len(questions_en)}")
        if score == len (quation_en):

# የገጹ ዲዛይን እና ከለር ማስተካከያ (CSS Styling)
st.set_page_config(page_title="Ultimate Quiz Game", page_icon="🌟", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        background: linear-gradient(45deg, #FF4B4B, #FF914D);
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        padding: 12px 24px;
        width: 100%;
        border: none;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.2);
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #FF914D, #FF4B4B);
        color: #fff;
    }
    h1 {
        color: #00ADB5;
        text-align: center;
        font-family: 'Helvetica Neue', sans-serif;
    }
    h3 {
        color: #EEEEEE;
    }
    .stRadio label {
        font-size: 16px;
        color: #DDDDDD;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌟 የዕውቀት ፈተና መድረክ / Ultimate Quiz Game 🌟")
st.markdown("---")

# ቋንቋ መምረጫ
lang = st.radio("እባክዎ ቋንቋ ይምረጡ / Choose Language:", ("አማርኛ", "English"))

if lang == "አማርኛ":
    st.subheader("🇪🇹 እንኳን ወደ አማርኛ የዕውቀት ፈተና በደህና መጡ!")
    
    questions = [
        {"q": "1. የፓይቶን ቋንቋ መቼ ተፈጠረ?", "options": ["ሀ) 1991", "ለ) 2000", "ሐ) 1985"], "answer": "ሀ) 1991"},
        {"q": "2. የኢትዮጵያ ዋና ከተማ አዲስ አበባ መቼ ተመሰረተች?", "options": ["ሀ) 1886", "ለ) 1900", "ሐ) 1930"], "answer": "ሀ) 1886"},
        {"q": "3. ከአለም ትልቁ ውቅያኖስ ማን ይባላል?", "options": ["ሀ) አትላንቲክ ውቅያኖስ", "ለ) ፓስፊክ ውቅያኖስ", "ሐ) ህንድ ውቅያኖስ"], "answer": "ለ) ፓስፊክ ውቅያኖስ"},
    ]
    
    user_answers = []
    for i, item in enumerate(questions):
        st.markdown(f"**{item['q']}**")
        ans = st.radio("", item["options"], key=f"am_{i}", label_visibility="collapsed")
        user_answers.append((ans, item["answer"]))
        st.markdown("---")
        
    if st.button("መልሶችን ላክ (Submit)", key="btn_am"):
        score = 0
        for user_ans, correct_ans in user_answers:
            if user_ans == correct_ans:
                score += 1
        
        st.success(f"🎉 ጨዋታው አልቋል! ያገኙት ጠቅላላ ነጥብ: {score} ከ {len(questions)}")
        if score == len(questions):
            st.balloons()

else:
    st.subheader("🇬🇧 Welcome to the Ultimate Quiz Game!")
    
    questions_en = [
        {"q": "1. When was the Python programming language created?", "options": ["a) 1991", "b) 2000", "c) 1985"], "answer": "a) 1991"},
        {"q": "2. Which planet is known as the Red Planet?", "options": ["a) Venus", "b) Mars", "c) Jupiter"], "answer": "b) Mars"},
        {"q": "3. What is the capital city of France?", "options": ["a) London", "b) Berlin", "c) Paris"], "answer": "c) Paris"},
    ]
    
    user_answers_en = []
    for i, item in enumerate(questions_en):
        st.markdown(f"**{item['q']}**")
        ans = st.radio("", item["options"], key=f"en_{i}", label_visibility="collapsed")
        user_answers_en.append((ans, item["answer"]))
        st.markdown("---")
        
    if st.button("Submit Answers", key="btn_en"):
        score = 0
        for user_ans, correct_ans in user_answers_en:
            if user_ans == correct_ans:
                score += 1
        
        st.success(f"🎉 Game Over! Your total score: {score} out of {len(questions_en)}")
        if score == len(questions_en):
            st.balloons()import streamlit as st

# የገጹ ዲዛይን እና ከለር ማስተካከያ (CSS Styling)
st.set_page_config(page_title="Ultimate Quiz Game", page_icon="🌟", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        background: linear-gradient(45deg, #FF4B4B, #FF914D);
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        padding: 12px 24px;
        width: 100%;
        border: none;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.2);
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #FF914D, #FF4B4B);
        color: #fff;
    }
    h1 {
        color: #00ADB5;
        text-align: center;
        font-family: 'Helvetica Neue', sans-serif;
    }
    h3 {
        color: #EEEEEE;
    }
    .stRadio label {
        font-size: 16px;
        color: #DDDDDD;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌟 የዕውቀት ፈተና መድረክ / Ultimate Quiz Game 🌟")
st.markdown("---")

# ቋንቋ መምረጫ
lang = st.radio("እባክዎ ቋንቋ ይምረጡ / Choose Language:", ("አማርኛ", "English"))

if lang == "አማርኛ":
    st.subheader("🇪🇹 እንኳን ወደ አማርኛ የዕውቀት ፈተና በደህና መጡ!")
    
    questions = [
        {"q": "1. የፓይቶን ቋንቋ መቼ ተፈጠረ?", "options": ["ሀ) 1991", "ለ) 2000", "ሐ) 1985"], "answer": "ሀ) 1991"},
        {"q": "2. የኢትዮጵያ ዋና ከተማ አዲስ አበባ መቼ ተመሰረተች?", "options": ["ሀ) 1886", "ለ) 1900", "ሐ) 1930"], "answer": "ሀ) 1886"},
        {"q": "3. ከአለም ትልቁ ውቅያኖስ ማን ይባላል?", "options": ["ሀ) አትላንቲክ ውቅያኖስ", "ለ) ፓስፊክ ውቅያኖስ", "ሐ) ህንድ ውቅያኖስ"], "answer": "ለ) ፓስፊክ ውቅያኖስ"},
    ]
    
    user_answers = []
    for i, item in enumerate(questions):
        st.markdown(f"**{item['q']}**")
        ans = st.radio("", item["options"], key=f"am_{i}", label_visibility="collapsed")
        user_answers.append((ans, item["answer"]))
        st.markdown("---")
        
    if st.button("መልሶችን ላክ (Submit)", key="btn_am"):
        score = 0
        for user_ans, correct_ans in user_answers:
            if user_ans == correct_ans:
                score += 1
        
        st.success(f"🎉 ጨዋታው አልቋል! ያገኙት ጠቅላላ ነጥብ: {score} ከ {len(questions)}")
        if score == len(questions):
            st.balloons()

else:
    st.subheader("🇬🇧 Welcome to the Ultimate Quiz Game!")
    
    questions_en = [
        {"q": "1. When was the Python programming language created?", "options": ["a) 1991", "b) 2000", "c) 1985"], "answer": "a) 1991"},
        {"q": "2. Which planet is known as the Red Planet?", "options": ["a) Venus", "b) Mars", "c) Jupiter"], "answer": "b) Mars"},
        {"q": "3. What is the capital city of France?", "options": ["a) London", "b) Berlin", "c) Paris"], "answer": "c) Paris"},
    ]
    
    user_answers_en = []
    for i, item in enumerate(questions_en):
        st.markdown(f"**{item['q']}**")
        ans = st.radio("", item["options"], key=f"en_{i}", label_visibility="collapsed")
        user_answers_en.append((ans, item["answer"]))
        st.markdown("---")
        
    if st.button("Submit Answers", key="btn_en"):
        score = 0
        for user_ans, correct_ans in user_answers_en:
            if user_ans == correct_ans:
                score += 1
        
        st.success(f"🎉 Game Over! Your total score: {score} out of {len(questions_en)}")
        if score == len(questions_en):
            st.balloons()import streamlit as st

# የገጹ ዲዛይን እና ከለር ማስተካከያ (CSS Styling)
st.set_page_config(page_title="Ultimate Quiz Game", page_icon="🌟", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        background: linear-gradient(45deg, #FF4B4B, #FF914D);
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        padding: 12px 24px;
        width: 100%;
        border: none;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.2);
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #FF914D, #FF4B4B);
        color: #fff;
    }
    h1 {
        color: #00ADB5;
        text-align: center;
        font-family: 'Helvetica Neue', sans-serif;
    }
    h3 {
        color: #EEEEEE;
    }
    .stRadio label {
        font-size: 16px;
        color: #DDDDDD;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌟 የዕውቀት ፈተና መድረክ / Ultimate Quiz Game 🌟")
st.markdown("---")

# ቋንቋ መምረጫ
lang = st.radio("እባክዎ ቋንቋ ይምረጡ / Choose Language:", ("አማርኛ", "English"))

if lang == "አማርኛ":
    st.subheader("🇪🇹 እንኳን ወደ አማርኛ የዕውቀት ፈተና በደህና መጡ!")
    
    questions = [
        {"q": "1. የፓይቶን ቋንቋ መቼ ተፈጠረ?", "options": ["ሀ) 1991", "ለ) 2000", "ሐ) 1985"], "answer": "ሀ) 1991"},
        {"q": "2. የኢትዮጵያ ዋና ከተማ አዲስ አበባ መቼ ተመሰረተች?", "options": ["ሀ) 1886", "ለ) 1900", "ሐ) 1930"], "answer": "ሀ) 1886"},
        {"q": "3. ከአለም ትልቁ ውቅያኖስ ማን ይባላል?", "options": ["ሀ) አትላንቲክ ውቅያኖስ", "ለ) ፓስፊክ ውቅያኖስ", "ሐ) ህንድ ውቅያኖስ"], "answer": "ለ) ፓስፊክ ውቅያኖስ"},
    ]
    
    user_answers = []
    for i, item in enumerate(questions):
        st.markdown(f"**{item['q']}**")
        ans = st.radio("", item["options"], key=f"am_{i}", label_visibility="collapsed")
        user_answers.append((ans, item["answer"]))
        st.markdown("---")
        
    if st.button("መልሶችን ላክ (Submit)", key="btn_am"):
        score = 0
        for user_ans, correct_ans in user_answers:
            if user_ans == correct_ans:
                score += 1
        
        st.success(f"🎉 ጨዋታው አልቋል! ያገኙት ጠቅላላ ነጥብ: {score} ከ {len(questions)}")
        if score == len(questions):
            st.balloons()

else:
    st.subheader("🇬🇧 Welcome to the Ultimate Quiz Game!")
    
    questions_en = [
        {"q": "1. When was the Python programming language created?", "options": ["a) 1991", "b) 2000", "c) 1985"], "answer": "a) 1991"},
        {"q": "2. Which planet is known as the Red Planet?", "options": ["a) Venus", "b) Mars", "c) Jupiter"], "answer": "b) Mars"},
        {"q": "3. What is the capital city of France?", "options": ["a) London", "b) Berlin", "c) Paris"], "answer": "c) Paris"},
    ]
    
    user_answers_en = []
    for i, item in enumerate(questions_en):
        st.markdown(f"**{item['q']}**")
        ans = st.radio("", item["options"], key=f"en_{i}", label_visibility="collapsed")
        user_answers_en.append((ans, item["answer"]))
        st.markdown("---")
        
    if st.button("Submit Answers", key="btn_en"):
        score = 0
        for user_ans, correct_ans in user_answers_en:
            if user_ans == correct_ans:
                score += 1
        
        st.success(f"🎉 Game Over! Your total score: {score} out of {len(questions_en)}")
        if score == len(questions_en):
            st.balloons()import streamlit as st

# የገጹ ዲዛይን እና ከለር ማስተካከያ (CSS Styling)
st.set_page_config(page_title="Ultimate Quiz Game", page_icon="🌟", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        background: linear-gradient(45deg, #FF4B4B, #FF914D);
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        padding: 12px 24px;
        width: 100%;
        border: none;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.2);
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #FF914D, #FF4B4B);
        color: #fff;
    }
    h1 {
        color: #00ADB5;
        text-align: center;
        font-family: 'Helvetica Neue', sans-serif;
    }
    h3 {
        color: #EEEEEE;
    }
    .stRadio label {
        font-size: 16px;
        color: #DDDDDD;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌟 የዕውቀት ፈተና መድረክ / Ultimate Quiz Game 🌟")
st.markdown("---")

# ቋንቋ መምረጫ
lang = st.radio("እባክዎ ቋንቋ ይምረጡ / Choose Language:", ("አማርኛ", "English"))

if lang == "አማርኛ":
    st.subheader("🇪🇹 እንኳን ወደ አማርኛ የዕውቀት ፈተና በደህና መጡ!")
    
    questions = [
        {"q": "1. የፓይቶን ቋንቋ መቼ ተፈጠረ?", "options": ["ሀ) 1991", "ለ) 2000", "ሐ) 1985"], "answer": "ሀ) 1991"},
        {"q": "2. የኢትዮጵያ ዋና ከተማ አዲስ አበባ መቼ ተመሰረተች?", "options": ["ሀ) 1886", "ለ) 1900", "ሐ) 1930"], "answer": "ሀ) 1886"},
        {"q": "3. ከአለም ትልቁ ውቅያኖስ ማን ይባላል?", "options": ["ሀ) አትላንቲክ ውቅያኖስ", "ለ) ፓስፊክ ውቅያኖስ", "ሐ) ህንድ ውቅያኖስ"], "answer": "ለ) ፓስፊክ ውቅያኖስ"},
    ]
    
    user_answers = []
    for i, item in enumerate(questions):
        st.markdown(f"**{item['q']}**")
        ans = st.radio("", item["options"], key=f"am_{i}", label_visibility="collapsed")
        user_answers.append((ans, item["answer"]))
        st.markdown("---")
        
    if st.button("መልሶችን ላክ (Submit)", key="btn_am"):
        score = 0
        for user_ans, correct_ans in user_answers:
            if user_ans == correct_ans:
                score += 1
        
        st.success(f"🎉 ጨዋታው አልቋል! ያገኙት ጠቅላላ ነጥብ: {score} ከ {len(questions)}")
        if score == len(questions):
            st.balloons()

else:
    st.subheader("🇬🇧 Welcome to the Ultimate Quiz Game!")
    
    questions_en = [
        {"q": "1. When was the Python programming language created?", "options": ["a) 1991", "b) 2000", "c) 1985"], "answer": "a) 1991"},
        {"q": "2. Which planet is known as the Red Planet?", "options": ["a) Venus", "b) Mars", "c) Jupiter"], "answer": "b) Mars"},
        {"q": "3. What is the capital city of France?", "options": ["a) London", "b) Berlin", "c) Paris"], "answer": "c) Paris"},
    ]
    
    user_answers_en = []
    for i, item in enumerate(questions_en):
        st.markdown(f"**{item['q']}**")
        ans = st.radio("", item["options"], key=f"en_{i}", label_visibility="collapsed")
        user_answers_en.append((ans, item["answer"]))
        st.markdown("---")
        
    if st.button("Submit Answers", key="btn_en"):
        score = 0
        for user_ans, correct_ans in user_answers_en:
            if user_ans == correct_ans:
                score += 1
        
        st.success(f"🎉 Game Over! Your total score: {score} out of {len(questions_en)}")
        if score == len(questions_en):
            st.balloons()
