**ClairiAI** is an AI-powered tool that summarizes YouTube videos instantly using transformer models. Just paste a YouTube link, and ClairiAI will fetch the transcript (if available) and summarize it in seconds.

![mvp](https://github.com/user-attachments/assets/d6ed8c79-c696-4c1b-8f0f-c9616842d449)

---

## 🚀 Features

- 📎 Paste any YouTube link
- 🎯 Automatically detects captions and summarizes using BART
- 🤖 Powered by Hugging Face Transformers
- 🌐 Clean, beginner-friendly Streamlit web UI

---

## 🧠 How It Works

1. Extracts video ID from a YouTube link
2. Uses `youtube-transcript-api` to fetch the transcript (if available)
3. Summarizes text using `facebook/bart-large-cnn` from Hugging Face
4. Displays the summary in a clean web interface via Streamlit

---

## 🧪 Test It

Try this link: https://www.youtube.com/watch?v=2lAe1cqCOXo

--- Set Up Instructions: 
# 📥 Step 1: Clone the Repo
git clone https://github.com/YOUR_USERNAME/Clairi_Ai.git
cd Clairi_Ai

# 🧪 Step 2: Set Up Virtual Environment
python -m venv venv
.\venv\Scripts\activate       # (Windows)
# OR
source venv/bin/activate      # (Mac/Linux)

# 📥 Step 3: Install Dependencies
pip install -r requirements.txt

# 🚀 Step 4: Run the Web App
python -m streamlit run streamlit_app.py

# 🌐 Step 5: Open in Browser
# Once it runs, go to: http://localhost:8501

