# 🎙️ Intelligent Desktop Voice Assistant

A Python-based AI-powered desktop voice assistant designed for hands-free system interaction, application automation, intelligent query handling, and voice-driven desktop workflows.

---

# 📌 Overview

The **Intelligent Desktop Voice Assistant** is a lightweight desktop automation platform that combines speech recognition, natural language processing, and command orchestration to enable seamless voice-controlled interaction with a computer system.

The assistant supports:

* Voice-driven desktop interaction
* Application automation
* Speech-to-text processing
* Text-to-speech responses
* Browser and utility control
* Intelligent command execution
* Modular command routing

The project demonstrates practical integration of NLP workflows, real-time audio processing, and desktop automation pipelines.

---

# 🏗️ System Architecture

## High-Level Workflow

```text
User Voice Input
        ↓
Speech Recognition Engine
        ↓
Speech-to-Text Processing
        ↓
Command Interpretation
        ↓
Action Routing Engine
        ↓
Desktop/System Automation
        ↓
Text-to-Speech Response
```

---

# ⚙️ Core Features

## 🎤 Voice Interaction

* Real-time voice command processing
* Speech-to-text conversion
* Hands-free desktop control
* Interactive assistant responses

## 🧠 Intelligent Command Handling

* Natural language command interpretation
* Modular action execution
* Utility and browser automation
* Dynamic task routing

## 🖥️ Desktop Automation

* Application launching
* System interaction workflows
* Browser-based operations
* User productivity automation

## 🔊 Audio Processing

* Text-to-speech synthesis
* Voice feedback generation
* Conversational interaction workflow

---

# 🧩 Repository Structure

```text
Desktop-Voice-Assistant/
│
├── Allen.py                 # Main assistant entry point
├── action.py                # Command execution engine
├── speech_to_text.py        # Voice recognition pipeline
├── text_to_speech.py        # Speech synthesis module
└── README.md
```

---

# 🧠 Processing Pipeline

## 1. Speech Recognition

The assistant captures microphone input and converts speech into text using a speech-recognition workflow.

---

## 2. Command Interpretation

The recognized command is processed and routed through the action engine to determine the required system operation.

Supported workflows include:

* Opening applications
* Browser interaction
* Utility commands
* System operations
* Information retrieval

---

## 3. Response Generation

The assistant generates voice-based responses using text-to-speech synthesis.

---

# 🧪 Technologies Used

## Programming

* Python

## NLP & Audio

* Speech Recognition
* Text-to-Speech (TTS)
* Natural Language Processing

## Automation

* Desktop Automation
* Command Routing
* Browser Interaction

---

# 📂 Important Modules

## `Allen.py`

Main execution file responsible for initializing the assistant and coordinating workflows.

## `speech_to_text.py`

Handles microphone input and speech recognition processing.

## `text_to_speech.py`

Generates voice-based assistant responses.

## `action.py`

Processes interpreted commands and executes automation tasks.

---

# 🚀 Setup & Installation

## Clone Repository

```bash
git clone https://github.com/112301021/Desktop-Voice-Assistant.git
cd Desktop-Voice-Assistant
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements are unavailable, install manually:

```bash
pip install speechrecognition pyttsx3 pyaudio
```

---

## Run the Assistant

```bash
python Allen.py
```

---

# 📊 Example Workflow

## Example Commands

* “Open Chrome”
* “Search the web”
* “Tell me the time”
* “Launch application”
* “Play music”

The assistant processes the command and executes the associated desktop operation.

---

# 📈 Engineering Focus

This project explores:

* Real-time speech processing
* Voice-driven system interaction
* NLP-based command interpretation
* Desktop automation workflows
* Human-computer interaction systems
* Lightweight AI assistants

---

# 🛠️ Future Improvements

Potential future enhancements:

* Wake-word detection
* LLM-powered conversational AI
* Context-aware memory
* Multi-language support
* GUI dashboard integration
* Cloud-based speech inference
* Async voice processing pipeline
* Smart task scheduling

---

# 👨‍💻 Author

Ajay Kumar Mallameeda
Indian Institute of Technology Palakkad

---

# 📜 License

This project is intended for academic and personal learning purposes.
