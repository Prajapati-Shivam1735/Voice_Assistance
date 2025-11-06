# 🧠 Voice Assistant 

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Ubuntu-lightgrey?logo=ubuntu)](https://ubuntu.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen)]()
[![Offline](https://img.shields.io/badge/Works-Offline-success)]()

A simple, offline **Voice Assistant** written in Python 🐍.  
It greets you, tells the time and date, performs web searches, and speaks aloud using **Festival** (Linux TTS).  
Perfect for beginners learning **Python automation** and **speech synthesis**.

---

## 📚 Table of Contents
- [✨ Features](#-features)
- [🧰 Tech Stack](#-tech-stack)
- [⚙️ Prerequisites](#️-prerequisites)
- [🧩 Installation Guide](#-installation-guide)
- [📁 Project Structure](#-project-structure)
- [▶️ How to Run](#️-how-to-run)
- [💬 Available Commands](#-available-commands)
- [🧠 How It Works](#-how-it-works)
- [🚧 Troubleshooting](#-troubleshooting)
- [🚀 Future Improvements](#-future-improvements)
- [👨‍💻 Author](#-author)

---

## ✨ Features
✅ Responds to greetings  
✅ Speaks using **Festival** TTS  
✅ Tells the current **time** and **date**  
✅ Opens Google search results  
✅ Works fully **offline**  
✅ Lightweight and extendable  

---

## 🧰 Tech Stack
| Component | Description |
|------------|-------------|
| **Language** | Python 3.10 + |
| **TTS Engine** | Festival (Linux built-in) |
| **Web Search** | `webbrowser` module |
| **Date & Time** | `datetime` |
| **System Control** | `os` |
| **Platform** | Ubuntu / Linux |

---

## ⚙️ Prerequisites
Before running, make sure you have:

1. **Python 3.10 +**
   ```bash
   python3 --version
   sudo apt install python3 python3-pip -y

2. **Festival TTS**
   ```bash
   sudo apt install festival -y

3. **(Optional) PulseAudio**
   ```bash
   sudo apt install pulseaudio pavucontrol -y
   pulseaudio --start

5. **Git**
   ```bash
   sudo apt install git -y

## 🧩 Installation Guide
  ```bash
  # 1. Clone Repository
  git clone https://github.com/<your-username>/Voice_Assistance.git
  cd Voice_Assistance

  # 2. (Optional) Create virtual environment
  python3 -m venv voiceenv
  source voiceenv/bin/activate
  
  # 3. Verify Festival works
  echo "Festival test voice" | festival --tts

  # 4. Run the assistant
  python3 voice_assistant.py
  ```
## 📁 Project Structure
```bash
  Voice_Assistance/
  ├── voice_assistant.py     # Main Python script
  ├── README.md              # Project documentation
  ├── requirements.txt       # Dependency list (optional)
  └── voiceenv/              # Virtual environment (optional)
```
## ▶️ How to Run
Run:
```bash
  python3 voice_assistant.py
```
Example interaction:
``` bash
  Assistant: Voice assistant activated. Type your commands below!
  You: hello
  Assistant: Hello! How can I help you today?
  You: time
  Assistant: The current time is 07:45 PM
  You: search python basics
  Assistant: Searching the web for python basics
```
## 💬 Available Commands
|Command|Description|
|:---:|:---:|
|`hello , hi`| `Greet the assistant`|
|`time`| `Get the current time`|
|`date`|`Get today's date`|
|`search <query>`|`Search the web`|
|`exit, quit, bye`|`Close the program`|

## 🧠 How It Works

1. Starts a continuous command loop.
2. Reads your input and matches it to keywords.
3. Uses os.system('echo "text" | festival --tts') for speech output.
4. Uses webbrowser.open() for searches.
5. Runs entirely offline.

## 🚧 Troubleshooting

|Problem|   Possible Fix|
|:---:|:---:|
|`aplay: not found`|Install audio playback utility -> `sudo apt install alsa-utils -y`|
|`Festival voice not clear`| Try installing `pulseaudio` or different Festival voice packages|
|`Permission denied`| Run command with `sudo` or check file permissions|
|`Command not responding`| Restart terminal or re-run virtual environment|

## 🚀 Future Improvements

- Add speech recognition (using speech_recognition or vosk)
- Integrate OpenWeather API for weather updates
- Add custom wake word (like “Hey Python”)
- GUI version using Tkinter or PyQt
- Add text-based chat log feature

## 👨‍💻 Author
Shivam Prajapati

💼 GitHub:[ prajapati-shivam1735](https://github.com/prajapati-shivam1735)

📧 Email: shivamprajapati1942@gmail.com

🌐 Project Link:[ Voice Assistant on GitHub](https://github.com/Prajapati-Shivam1735/Voice_Assistance)






