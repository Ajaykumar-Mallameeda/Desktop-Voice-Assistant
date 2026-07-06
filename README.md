# Desktop Voice Assistant

![Status](https://img.shields.io/badge/Status-Active-059669?style=flat)
![License](https://img.shields.io/badge/License-MIT-2563EB?style=flat)
![Last Updated](https://img.shields.io/badge/Last%20Updated-2026--07-6B7280?style=flat)

![Python](https://img.shields.io/badge/Python-0D9488?style=flat&logo=python&logoColor=white)

A Python-based desktop voice assistant for hands-free system interaction, application automation, and voice-driven desktop workflows.

---

## Overview

**The problem:** Desktop automation typically requires manual input — clicking, typing, navigating menus. Voice-driven interaction can streamline common tasks, but most voice assistants are cloud-dependent or tied to specific ecosystems.

**The approach:** A lightweight, offline-capable desktop assistant that combines speech recognition, natural language command parsing, and system automation. The assistant listens for voice commands, interprets intent through keyword matching, and executes actions — from launching applications to controlling browser workflows.

**Architecture:** Four-module pipeline — speech recognition (`speech_to_text.py`), command routing (`action.py`), speech synthesis (`text_to_speech.py`), and the main orchestration layer (`Allen.py`) with a Tkinter GUI.

---

## Features

- **Voice command processing** — Real-time microphone input with speech-to-text conversion
- **Application launching** — Open Chrome, YouTube, Google Maps, and other tools by voice
- **Browser automation** — Navigate to Spotify, WhatsApp, Gmail, Google Calendar, Zoom, and more
- **System information** — Voice-query current time
- **Text-based input** — Alternative keyboard input mode alongside voice
- **Conversation history** — Scrollable chat interface showing user and assistant messages

---

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Core language |
| SpeechRecognition | Speech-to-text via Google Web Speech API |
| pyttsx3 | Offline text-to-speech engine |
| Tkinter | Desktop GUI framework |
| Webbrowser | System browser integration |

---

## Getting Started

### Prerequisites

- Python 3.7 or later
- Microphone (for voice input)

### Installation

```bash
# Clone the repository
git clone https://github.com/Ajaykumar-Mallameeda/Desktop-Voice-Assistant.git
cd Desktop-Voice-Assistant

# Install dependencies
pip install -r requirements.txt

# Run the assistant
python Allen.py
```

### Dependencies

See [requirements.txt](./requirements.txt) for the full list:

- `speechrecognition` — microphone input and speech-to-text
- `pyttsx3` — text-to-speech synthesis
- `pyaudio` — audio I/O for microphone access
- `Pillow` — image handling for GUI
- `pipwin` — Windows audio dependency helper (Windows only)

---

## Project Structure

```
Desktop-Voice-Assistant/
├── Allen.py                 # Main entry point and GUI
├── action.py                # Command routing and execution
├── speech_to_text.py        # Speech recognition module
├── text_to_speech.py        # Speech synthesis module
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## Usage

Run the assistant:

```bash
python Desktop\ voice\ assistant/Allen.py
```

The GUI window opens with an ASK button (voice input), a SEND button (text input), and a DELETE button (clear chat).

**Example commands:**
- "What is your name"
- "What is the time"
- "Open YouTube"
- "Play music allen"
- "Open Google"
- "Open WhatsApp"
- "Shutdown"

---

## Known Limitations

- Hardcoded image path in the GUI — currently points to a local file that doesn't exist on other machines
- Module-level function calls in `speech_to_text.py` and `text_to_speech.py` execute on import
- Single-threaded — voice recognition blocks the UI during processing
- Keyword-based command matching (no NLP/LLM integration)

These are documented as areas for future improvement.

---

## Lessons Learned

- **Separation of concerns** — Splitting STT, TTS, and action routing into separate modules made the system testable and extensible. Adding new commands requires only editing `action.py`.
- **Offline vs. cloud trade-offs** — Using `pyttsx3` for offline TTS (no internet required) meant lower voice quality but higher reliability. The `speech_recognition` library uses Google's cloud API, introducing a network dependency for input.
- **GUI frameworks matter** — Tkinter is built-in and lightweight but limited in modern UI capabilities. A web-based interface would enable richer interactions.

---

## License & Author

**License:** This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.

**Author:** [Ajaykumar Mallameeda](https://github.com/Ajaykumar-Mallameeda) · Indian Institute of Technology Palakkad

---

*Built at IIT Palakkad as part of a continuous learning journey in AI and Backend Engineering.*
