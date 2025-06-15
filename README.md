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

---

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.12 (recommended) - The project is not compatible with Python 3.13
- Git
- pip (Python package installer)

### 📥 Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Clairi_Ai.git
cd Clairi_Ai
```

### 🧪 Step 2: Set Up Python Virtual Environment

```bash
# Create a virtual environment with Python 3.12
python3.12 -m venv venv

# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 📦 Step 3: Install Dependencies

```bash
# Upgrade pip first
pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt
```

> **Note:** If you encounter dependency conflicts, try installing with:
> ```bash
> pip install --no-deps -r requirements.txt
> pip install numpy>=1.24.0,<2.0.0
> pip install transformers>=4.0.0,<5.0.0
> ```

### 🚀 Step 4: Run the Application

#### Option 1: Run the Streamlit Web App (Recommended)

```bash
# Start the Streamlit web interface
python -m streamlit run streamlit_app.py
```

The app will be available at: http://localhost:8501

#### Option 2: Run from Command Line

```bash
# Edit the YouTube URL in main.py first
python main.py
```

The summary will be displayed in the terminal and saved to `outputs/summary.txt`.

### 📋 Troubleshooting

- **PyTorch Issues**: If you encounter PyTorch-related errors, ensure you're using Python 3.12 (not 3.13)
- **NumPy Errors**: If you see NumPy compatibility errors, downgrade to NumPy 1.x with: `pip install numpy>=1.24.0,<2.0.0`
- **Transcript Errors**: If transcript fetching fails for a specific video, try another video as some videos may have restricted or unavailable captions
- **Missing Directories**: If you get file not found errors, ensure the `outputs` directory exists: `mkdir -p outputs`

