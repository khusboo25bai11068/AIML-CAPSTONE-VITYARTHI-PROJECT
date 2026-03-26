# 🎙️ Voice to Voice Multilingual Translator 🚀
### *Bridging Language Barriers with Neural Machine Translation*

---

## 📝 Project Overview
This is an **Intelligent NLP Agent** designed for seamless, real-time voice-to-voice translation. By integrating advanced **Natural Language Processing (NLP)** techniques, the agent captures human speech, understands its semantic intent, and translates it into a target language with natural-sounding audio output.

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

### 🚀 Quick Install:
```bash
pip install speechrecognition deep-translator gTTS pygame
