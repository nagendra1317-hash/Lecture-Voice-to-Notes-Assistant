
import os
import streamlit as st
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

from utils.transcribe import transcribe_audio

from utils.gemini_utils import configure_gemini
from utils.gemini_utils import (
    generate_notes,
    generate_quiz,
    generate_flashcards,
    ask_question
)

st.set_page_config(
    page_title=" Lecture Voice to Notes Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

.block-container{
    padding-top:1rem;
}

/* HERO */
.hero{
    padding:35px;
    border-radius:25px;
    background:linear-gradient(135deg,#667eea,#764ba2,#f093fb);
    color:white;
    text-align:center;
    margin-bottom:20px;
    box-shadow:0 10px 30px rgba(118,75,162,0.4);
}

/* SIDEBAR */
section[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#0f172a,#1e293b);
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* BUTTON */
.stButton > button{
    width:100%;
    border-radius:10px;
    background:#2563eb;
    color:white;
    border:none;
}

/* METRICS */
[data-testid="metric-container"]{
    border:1px solid #e5e7eb;
    border-radius:12px;
    padding:10px;
}

/* CARDS */
.card{
    padding:15px;
    border-radius:15px;
    background:#f8fafc;
    border:1px solid #e5e7eb;
}

</style>
""", unsafe_allow_html=True)

def create_pdf(text, title):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    story = [Paragraph(title, styles["Title"]), Spacer(1, 12)]
    for line in text.split("\n"):
        if line.strip():
            story.append(Paragraph(line, styles["BodyText"]))
    doc.build(story)
    buffer.seek(0)
    return buffer

# HERO
st.markdown("""
<div class="hero">
<h1>🎓 Lecture Voice to Notes Assistant </h1>
<h3>AI-Powered Lecture Learning Assistant</h3>
<p>Upload Audio → Transcript → Notes → Quiz → Flashcards → AI Tutor</p>
</div>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.title("⚙️ Control Panel")

    api_key = st.text_input("🔑 Gemini API Key", type="password")

    st.caption("Get your Gemini API Key from Google AI Studio")
    st.link_button(
        "🔗 Get Gemini API Key",
        "https://aistudio.google.com/apikey"
    )

    st.markdown("---")

    st.subheader("🎯 Generation Settings")
    quiz_questions = st.slider("Quiz Questions", 5, 30, 10)
    flashcard_count = st.slider("Flashcards", 5, 50, 20)

    st.markdown("---")

    st.subheader("🚀 Features")
    st.markdown("""
- ✅ Speech To Text
- ✅ Smart Notes
- ✅ MCQ Generator
- ✅ Flashcards
- ✅ AI Tutor
- ✅ PDF Export
- ✅ Transcript Analytics
""")

    st.markdown("---")

    st.subheader("📖 About")
    st.info(
        "Lecture Voice-to-Notes Assistant is an AI-powered learning tool designed to transform lecture recordings into structured study materials. The application automatically transcribes audio, generates concise notes, creates summaries, and prepares quizzes to help students review and retain concepts more effectively. By reducing manual note-taking effort, it enables learners to focus on understanding and engaging with the lecture content."
    )

    st.markdown("---")

    st.link_button("🌐 GitHub", "https://github.com/NagendraSahani/Lecture-Voice-to-Notes-Assistant")
    st.link_button("💼 LinkedIn", "https://www.linkedin.com/in/nagendra-sahani-293503188/")





model = None

if api_key:
    try:
        model = configure_gemini(api_key)
        st.sidebar.success("✅ API Key Connected")
    except Exception as e:
        st.sidebar.error(f"❌ {e}")

# Upload
audio_file = st.file_uploader(
    "🎤 Upload Lecture Audio",
    type=["mp3", "wav", "m4a"]
)

if audio_file:

    with open("lecture.wav", "wb") as f:
        f.write(audio_file.read())

    st.success("✅ Audio Uploaded Successfully")

    if st.button("📝 Generate Transcript"):

        with st.spinner("Transcribing Audio..."):
            st.session_state["transcript"] = transcribe_audio("lecture.wav")

    if "transcript" in st.session_state:

        transcript = st.session_state["transcript"]

        words = len(transcript.split())
        read_time = max(1, words // 200)

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("📝 Words", words)
        c2.metric("⏱ Read Time", f"{read_time} min")
        c3.metric("🎯 Quiz Count", quiz_questions)
        c4.metric("🎴 Flashcards", flashcard_count)

        st.subheader("📝 Transcript")

        st.text_area(
            "Transcript Output",
            transcript,
            height=250
        )

        tab1, tab2, tab3, tab4 = st.tabs(
            ["📚 Notes", "📝 Quiz", "🎴 Flashcards", "🤖 AI Tutor"]
        )

        # NOTES
        with tab1:

            if st.button("📚 Generate Notes"):
                

                if model is None:
                    st.error("⚠️ Please enter a valid Gemini API Key first.")
                    st.stop()

                with st.spinner("Generating Notes..."):
                    st.session_state["notes"] = generate_notes(
                        model,
                        transcript
                    )

                with st.spinner("Generating Notes..."):
                    st.session_state["notes"] = generate_notes(model,transcript)

            if "notes" in st.session_state:

                st.markdown(st.session_state["notes"])

                st.download_button(
                    "⬇ Download Notes TXT",
                    st.session_state["notes"],
                    file_name="notes.txt"
                )

                st.download_button(
                    "📄 Download Notes PDF",
                    create_pdf(st.session_state["notes"], "Lecture Notes"),
                    file_name="notes.pdf"
                )

        # QUIZ
        with tab2:

            if st.button("📝 Generate Quiz"):
                if model is None:
                    st.error("⚠️ Please enter a valid Gemini API Key first.")
                    st.stop()

                with st.spinner("Generating Quiz..."):
                    st.session_state["quiz"] = generate_quiz(
                        model,
                        transcript,
                        quiz_questions
                    )

                with st.spinner("Generating Quiz..."):
                    st.session_state["quiz"] = generate_quiz(
                        model,
                        transcript,
                        quiz_questions
                    )

            if "quiz" in st.session_state:

                st.markdown(st.session_state["quiz"])

                st.download_button(
                    "⬇ Download Quiz",
                    st.session_state["quiz"],
                    file_name="quiz.txt"
                )

        # FLASHCARDS
        with tab3:

            if st.button("🎴 Generate Flashcards"):
                
                if model is None:
                    st.error("⚠️ Please enter a valid Gemini API Key first.")
                    st.stop()

                with st.spinner("Generating Flashcards..."):
                    st.session_state["flashcards"] = generate_flashcards(
                    model,
                    transcript,
                    flashcard_count
                    )

                with st.spinner("Generating Flashcards..."):
                    st.session_state["flashcards"] = generate_flashcards(
                        model,
                        transcript,
                        flashcard_count
                    )

            if "flashcards" in st.session_state:

                st.markdown(st.session_state["flashcards"])

                st.download_button(
                    "⬇ Download Flashcards",
                    st.session_state["flashcards"],
                    file_name="flashcards.txt"
                )

        # AI TUTOR
        with tab4:

            if "chat_history" not in st.session_state:
                st.session_state["chat_history"] = []

            for role, msg in st.session_state["chat_history"]:
                with st.chat_message(role):
                    st.write(msg)

            question = st.chat_input(
                "Ask anything from the lecture..."
            )

            if question:

                st.session_state["chat_history"].append(
                    ("user", question)
                )

                answer = ask_question(
                    model,
                    transcript,
                    question
                )

                st.session_state["chat_history"].append(
                    ("assistant", answer)
                )

                st.rerun()

st.markdown("---")
st.caption("🚀 Lecture Voice to Notes Assistant| Built with Streamlit + Gemini")
