# WhatsApp Chat Analyzer 📊💬

A Python-based tool to analyze exported WhatsApp chat files and generate visual and statistical insights.

---

## 📌 Features

- 📈 Chat activity over time (daily, monthly)
- 👤 Most active users (in group chats)
- 🔤 Most commonly used words
- 😂 Emoji usage analysis
- 🕐 Hourly activity distribution
- ☁️ Word cloud generation
- 🔍 Supports both individual and group chats

---

## 📂 Folder Structure

whatsapp-chat-analyzer/
├── app/ # Main app logic
├── helper/ # Utility functions
├── preprocessor/ # Data cleaning and preprocessing
├── stop_hinglish.txt # Custom stopword list
├── qodana/ # Code quality tools
├── .venv/ # Virtual environment (not pushed)
├── qodana.yaml
├── qodana.sarif.json
├── requirements.txt
└── main.py # Entry point


---

## 🛠️ Requirements

- Python 3.7+
- `pandas`
- `matplotlib`
- `seaborn`
- `wordcloud`
- `emoji`

Install all dependencies using:

```bash
pip install -r requirements.txt

---

## 🚀 How to Use

1. Export your WhatsApp chat as a `.txt` file (text only, no media).
2. Run the main script:

```bash
python main.py
