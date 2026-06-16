[README.md](https://github.com/user-attachments/files/29014680/README.md)
# 🎓Lecture Voice to Notes Assistant

Turn lecture recordings into smart study companions with AI-generated transcripts, notes, quizzes, flashcards, and interactive Q&A.

## 📌 Overview

LectureMind AI is an AI-powered learning assistant designed to help students make the most of their lecture recordings. Instead of spending hours manually creating notes, users can upload an audio lecture and instantly generate a transcript, study notes, quizzes, flashcards, and ask questions about the lecture content.

The project combines Speech-to-Text technology with Generative AI to create a more efficient and interactive learning experience.

---

## ✨ Features

### 🎤 Lecture Transcription

* Upload lecture recordings in MP3, WAV, or M4A format.
* Convert speech into text using OpenAI Whisper.

### 📚 Smart Study Notes

* Generate concise and structured notes from lecture transcripts.
* Quickly review key concepts and important points.

### 📝 Quiz Generation

* Automatically create quizzes from lecture content.
* Useful for revision and self-assessment.

### 🎴 Flashcard Generation

* Generate flashcards for active recall and quick revision.
* Helps improve retention of important concepts.

### 💬 Interactive Q&A

* Ask questions related to the lecture.
* Get AI-generated answers based on the lecture transcript.

### 🎨 User-Friendly Interface

* Built with Streamlit.
* Simple and interactive interface for students.

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **OpenAI Whisper**
* **Google Gemini API**
* **FFmpeg**

---

## 📂 Project Structure

```text
Lecture Voice to Notes Assistant/
│
├── app.py
│
├── utils/
│   ├── transcribe.py
│   └── gemini_utils.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Lecture Voice to Notes Assistant.git
cd Lecture Voice to Notes Assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Gemini API Key

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Get your API key from Google AI Studio.

### 6. Run the Application

```bash
streamlit run app.py
```

---

## 🚀 How It Works

```text
Lecture Audio
      │
      ▼
OpenAI Whisper
(Speech-to-Text)
      │
      ▼
Transcript
      │
      ▼
Google Gemini AI
      │
 ┌────┼────┬─────┐
 ▼    ▼    ▼     ▼
Notes Quiz Flashcards Q&A
```

---

## 🎯 Use Cases

* Students preparing for exams
* Online learning platforms
* Educational institutions
* Lecture revision and note-taking
* Self-learning and knowledge retention

---

## 📸 Workflow

1. Upload lecture audio.
2. Generate transcript.
3. Create study notes.
4. Generate quizzes.
5. Create flashcards.
6. Ask questions related to the lecture.

---

## 🔮 Future Improvements

* PDF export for notes
* Downloadable flashcards
* Multi-lecture support
* RAG-based question answering
* FAISS vector database integration
* Learning analytics dashboard

---

## 👩‍💻 Author

**Nagendra Sahani**
M.Sc. Maths & Computing
IIT ISM DHANBAD

---

## ⭐ Acknowledgements

* OpenAI Whisper
* Google Gemini API
* Streamlit

If you found this project useful, consider giving it a ⭐ on GitHub!
