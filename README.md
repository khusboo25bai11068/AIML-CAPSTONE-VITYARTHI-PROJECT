# 🎙️ Voice to Voice Multilingual Translator 🚀
### *Bridging Language Barriers with Neural Machine Translation*

---

## 📝 Project Overview
This is a Smart **NLP Agent** that listens to your voice and instantly speaks it back in another language. It is built to solve real-world communication gaps by using **Natural Language Processing (NLP)** and **Neural Machine Translation (NMT)** to understand the actual meaning of your words across 14 global and regional languages.

---

## 🏗️ Technical Architecture (The NLP Pipeline)
The system functions as a sophisticated **Three-Stage NLP Pipeline**:

1.  **👂 Stage 1: Speech Recognition (ASR)** Converts raw acoustic signals into normalized text tokens. It uses probabilistic modeling to filter out environmental noise and improve accuracy in stochastic environments.

2.  **🧠 Stage 2: Neural Machine Translation (NMT)** The "Brain" of the project. It maps the meaning (semantics) from English to a target language using a **Transformer-based Deep Learning model** rather than simple word-to-word substitution.

3.  **🗣️ Stage 3: Speech Synthesis (TTS)** A generative application that synthesizes the final processed text into a high-fidelity, human-like voice output.

---

## ✨ Features at a Glance
* **⚡ One-Shot Logic:** No messy loops or repetitive prompts. Run, speak, translate, and exit automatically.
* **🌍 14 Verified Languages:** Supports a robust mix of Indian and Global languages:
    * *Indian:* Hindi, Marathi, Bengali, Tamil, Telugu, Kannada, Malayalam, Gujarati.
    * *Global:* French, Japanese, Spanish, German, Korean, English.
* **🎤 Intelligent Noise Filter:** Clears background noise for better voice pickup.
* **🧹 Auto-Cleanup:** Auto-removes temporary audio files to keep the folder clean.
---

## 🛠️ Tech Stack & Requirements
To get this agent running, you need the following Python libraries:

| Library | What it does? |
| :--- | :--- |
| `SpeechRecognition` | **Hears** your voice and turns it into text.**(Sensors)** |
| `deep-translator` | **Translates** the text into another language. |
| `gTTS` | **Converts** the translated text into a voice file. |
| `pygame` | **Plays** the voice file through your speakers. **(Audio Actuators)**|
---
## ⚙️ How to Set Up (Installation)?
### 1. Download the project files**
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

### 2.Install Required Libraries:**
```bash
pip install speechrecognition deep-translator gTTS pygame
```

## 🚦How to Use?
1.  **Run the Script:** Execute the following command in your terminal: "AIML CAPSTONE PROJECT.py"
2.  **Voice Input:** Wait for the "Listening..." prompt and speak your sentence clearly.
3.  **Select Language:** Say the name of your target language (e.g., "Hindi" or "French") to hear the translation instantly🎬





