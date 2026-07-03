import streamlit as st
import requests

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="Career AI Assistant",
    page_icon="🤖",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000"

# ==========================
# SESSION STATE
# ==========================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "resume_uploaded" not in st.session_state:
    st.session_state.resume_uploaded = False

if "mode" not in st.session_state:
    st.session_state.mode = "Resume AI"

# ==========================
# CUSTOM CSS
# (theme base/colors come from .streamlit/config.toml —
#  this only adds the bespoke bits on top)
# ==========================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&display=swap');

* {
    font-family:'Inter', sans-serif;
}

h1, h2, h3, h4 {
    font-family:'Space Grotesk', sans-serif !important;
}

/* ---------- Sidebar text contrast ---------- */
section[data-testid="stSidebar"] * {
    color:#f0f0f0 !important;
}

section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
    color:#b0b0b0 !important;
}

section[data-testid="stSidebar"] hr {
    border-color:#2a2a2a !important;
}

/* radio option labels */
div[role="radiogroup"] label {
    background:#161616;
    border:1px solid #2a2a2a;
    border-radius:8px;
    padding:8px 12px;
    margin-bottom:6px;
    width:100%;
}

div[role="radiogroup"] label:hover {
    border-color:#ff6a00;
}

div[role="radiogroup"] label p {
    color:#f0f0f0 !important;
    font-size:14px;
}

/* file uploader — dark card instead of white */
div[data-testid="stFileUploaderDropzone"] {
    background:#161616 !important;
    border:1px dashed #333 !important;
}

div[data-testid="stFileUploaderDropzone"] * {
    color:#d0d0d0 !important;
}

/* ---------- Header ---------- */
.header-box {
    padding:26px 32px;
    background:#111111;
    border:1px solid #262626;
    border-radius:16px;
    position:relative;
    overflow:hidden;
}

.header-box::before {
    content:"";
    position:absolute;
    top:0; left:0; right:0;
    height:4px;
    background:linear-gradient(90deg, #ff6a00, #ffb066, #ff6a00);
}

.header-title {
    font-size:30px;
    font-weight:700;
    color:#f5f5f5;
    margin:0;
}

.header-title span {
    color:#ff6a00;
}

.header-sub {
    color:#9a9a9a;
    font-size:14px;
    margin-top:6px;
}

/* ---------- Info cards ---------- */
.info-card {
    background:#111111;
    border:1px solid #262626;
    border-left:3px solid #444;
    border-radius:10px;
    padding:14px 16px;
    height:100%;
}

.info-card.active {
    border-left:3px solid #ff6a00;
    background:#1a1210;
}

.info-card-title {
    font-weight:600;
    font-size:14px;
    color:#f5f5f5;
    margin-bottom:4px;
}

.info-card-desc {
    font-size:12px;
    color:#9a9a9a;
}

/* ---------- Metric cards (fix oversized/truncated values) ---------- */
.metric-card {
    background:#111111;
    border:1px solid #262626;
    border-radius:10px;
    padding:12px 16px;
}

.metric-label {
    font-size:12px;
    color:#9a9a9a;
    margin-bottom:2px;
}

.metric-value {
    font-size:20px;
    font-weight:600;
    color:#ff6a00;
    font-family:'Space Grotesk', sans-serif;
    white-space:normal;
    word-break:break-word;
}

/* ---------- Chat container ---------- */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background:#0d0d0d !important;
    border:1px solid #262626 !important;
    border-radius:12px !important;
}

/* ---------- Chat bubbles ---------- */
.msg-row {
    display:flex;
    margin:10px 4px;
}

.msg-row.user { justify-content:flex-end; }
.msg-row.bot { justify-content:flex-start; }

.bubble {
    max-width:70%;
    padding:12px 16px;
    border-radius:14px;
    font-size:14px;
    line-height:1.5;
}

.bubble.user {
    background:#ff6a00;
    color:#0a0a0a;
    font-weight:500;
    border-radius:14px 14px 2px 14px;
}

.bubble.bot {
    background:#161616;
    border:1px solid #2a2a2a;
    border-left:3px solid #ff6a00;
    color:#f0f0f0;
    border-radius:14px 14px 14px 2px;
}

.bubble-tag {
    font-size:10px;
    font-weight:600;
    letter-spacing:0.5px;
    color:#ff6a00;
    margin-bottom:4px;
    display:block;
}

/* ---------- Buttons ---------- */
.stButton>button {
    background:#ff6a00;
    color:#0a0a0a;
    border:none;
    font-weight:600;
    border-radius:8px;
}

.stButton>button:hover {
    background:#ffb066;
    color:#0a0a0a;
}

/* ---------- Chat input ---------- */
div[data-testid="stChatInput"] {
    background:#111111 !important;
    border:1px solid #2a2a2a !important;
    border-radius:10px !important;
}

div[data-testid="stChatInput"] textarea {
    background:transparent !important;
    color:#f0f0f0 !important;
}

div[data-testid="stChatInput"] textarea::placeholder {
    color:#777 !important;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# SIDEBAR
# ==========================

with st.sidebar:

    st.markdown("## 🤖 Career AI")
    st.caption("Multi-turn Conversational AI")
    st.divider()

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx"]
    )

    if uploaded_file is not None:
        if st.button("Upload Resume", use_container_width=True):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue()
                )
            }

            with st.spinner("Uploading..."):
                try:
                    response = requests.post(
                        API_URL + "/upload",
                        files=files
                    )

                    if response.status_code == 200:
                        st.success("Resume Uploaded")
                        st.session_state.resume_uploaded = True
                    else:
                        st.error("Upload Failed")

                except Exception as e:
                    st.error(str(e))

    st.divider()

    st.markdown("### AI Mode")

    mode = st.radio(
        "Select mode",
        [
            "Resume AI",
            "Career Advisor",
            "Learning Planner",
            "Multi-turn AI"
        ],
        label_visibility="collapsed"
    )

    st.session_state.mode = mode

    st.divider()

    if st.session_state.resume_uploaded:
        st.success("Resume Loaded")
    else:
        st.warning("No Resume Uploaded")

# ==========================
# MAIN HEADER
# ==========================

st.markdown("""
<div class="header-box">
    <p class="header-title">🤖 Career <span>AI</span> Assistant</p>
    <p class="header-sub">Multi-turn Conversational AI powered by Gemini + RAG</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# ==========================
# INFO CARDS
# ==========================

cards = [
    ("Resume AI", "📄", "Ask anything from your resume."),
    ("Career Advisor", "🎯", "Personalized career guidance."),
    ("Learning Planner", "📚", "Generate complete learning roadmaps."),
    ("Multi-turn AI", "💬", "Persistent conversation memory."),
]

cols = st.columns(4)

for col, (title, icon, desc) in zip(cols, cards):
    active_class = "active" if st.session_state.mode == title else ""
    with col:
        st.markdown(
            f"""
            <div class="info-card {active_class}">
                <div class="info-card-title">{icon} {title}</div>
                <div class="info-card-desc">{desc}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.write("")

# ==========================
# METRICS (custom cards — avoids Streamlit's oversized/truncated metric value)
# ==========================

metric_data = [
    ("Resume", "Uploaded" if st.session_state.resume_uploaded else "Not Uploaded"),
    ("Mode", st.session_state.mode),
    ("Messages", str(len(st.session_state.messages))),
    ("LLM", "Gemini"),
]

m_cols = st.columns(4)

for col, (label, value) in zip(m_cols, metric_data):
    with col:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.write("")

# ==========================
# CHAT HISTORY
# ==========================

chat_container = st.container(height=500, border=True)

with chat_container:
    if not st.session_state.messages:
        st.markdown(
            "<p style='color:#7a7a7a; text-align:center; margin-top:200px;'>"
            "Start the conversation — ask a question below.</p>",
            unsafe_allow_html=True
        )

    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(
                f'''
                <div class="msg-row user">
                    <div class="bubble user">{message["content"]}</div>
                </div>
                ''',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'''
                <div class="msg-row bot">
                    <div class="bubble bot">
                        <span class="bubble-tag">AI</span>{message["content"]}
                    </div>
                </div>
                ''',
                unsafe_allow_html=True
            )

# ==========================
# INPUT AREA
# ==========================

question = st.chat_input("Ask anything...")

if question:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    try:
        with st.spinner("Thinking..."):

            # ==============================
            # Resume AI
            # ==============================
            if st.session_state.mode == "Resume AI":

                response = requests.post(
                    API_URL + "/ask_resume",
                    json={"question": question}
                )

                reply = response.json()["answer"]

            # ==============================
            # Career Advisor
            # ==============================
            elif st.session_state.mode == "Career Advisor":

                response = requests.post(
                    API_URL + "/career",
                    json={
                        "type": "career",
                        "goal": question,
                        "current_skills": "Python, Machine Learning, Deep Learning",
                        "duration": "8 weeks"
                    }
                )

                reply = response.json()["response"]

            # ==============================
            # Learning Planner
            # ==============================
            elif st.session_state.mode == "Learning Planner":

                response = requests.post(
                    API_URL + "/career",
                    json={
                        "type": "learning",
                        "goal": question,
                        "current_skills": "Python, Machine Learning, Deep Learning",
                        "duration": "8 weeks"
                    }
                )

                reply = response.json()["response"]

            # ==============================
            # Multi-turn AI
            # ==============================
            else:

                response = requests.post(
                    API_URL + "/chat",
                    json={
                        "session_id": "yamini_session",
                        "message": question
                    }
                )

                reply = response.json()["response"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": reply
            }
        )

    except Exception as e:
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": str(e)
            }
        )

    st.rerun()

