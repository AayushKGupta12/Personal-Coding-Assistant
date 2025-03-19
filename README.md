# 🎙️ Your Personal Assistant Project

## 👋 Welcome to My Personal Coding Assistant!

This is a Python-based voice assistant that can listen, respond, and execute commands using **Speech Recognition** and **Text-to-Speech (TTS)** synthesis. It is designed to make interaction with your system more intuitive and efficient by enabling voice-based commands for various tasks.

---

## 🛠️ Features

✅ **Speech Recognition**: Converts spoken words into text effortlessly.
✅ **Text-to-Speech (TTS)**: Generates responses in a clear, natural voice.
✅ **Multiple Voice Options**: Choose from different accents and voices to personalize the experience.
✅ **Customizable Speed & Volume**: Modify the speech rate and volume to your preference. ✅ **Error Handling**: Ensures smooth interaction by handling speech errors efficiently.
✅ **Command Execution**: Supports a variety of voice commands to make system interaction easier.
✅ **Real-Time Processing**: Provides instant responses to spoken commands.

---

## 🚀 Installation

To get started, clone this repository and install the required dependencies.

```sh
# Clone the repository
git clone https://github.com/your-username/voice-assistant.git

# Navigate to the directory
cd voice-assistant

# Install dependencies
pip install -r requirements.txt
```

---

## 🔧 How to Use

1. **Run the Python script:**
   ```sh
   python main.py
   ```
2. **Speak a command**, like:
   - "Can You write a program to Print Fibonacci series taking user input"
   - "Java Program to Check if two Arrays are Equal or not"
   - "Can you Please Open Youtube"
   - "Can you Please Open Google"
   - "Write Letter to the publisher ordering books for your store"
   - "MMD School, Nashik, recently organised a science symposium on the topic: ‘Effect of pollution on quality of life’. You are Amit/Amita Raazdan, editor of the school magazine. Write a report on the event for your school magazine. (120 – 150 words)

     (SOURCE- CBSE 2018)"
   -
3. **Get a response instantly!** 🎤 The assistant listens to your command, processes it, and responds accordingly.

---

## 🎛️ Changing Voice Settings

Modify the `pyttsx3` settings in `main.py` to change the voice, speed, and volume:

```python
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speed
engine.setProperty('volume', 0.8)  # Adjust volume
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Select a different voice
```

To find all available voices, use:

```python
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name}")
```

---

## ⚠️ Troubleshooting

🛑 If you face errors while running the assistant, try:

- Ensuring your **microphone is working** 🎤
- Updating your **speech recognition library** to the latest version
- Running the script with **admin privileges**
- Checking **audio drivers** to ensure proper functionality
- Testing different **voice engine settings** in case of compatibility issues
- Verifying **network connectivity** if using online speech services

---

## 🎯 Future Enhancements

🔹 Add support for **Google Assistant & OpenAI API** 🤖
🔹 Enable **multi-language support** 🌍
🔹 Implement **voice-based task automation** 📅
🔹 Enhance **contextual understanding** for smarter responses 🧠
🔹 Integrate with **smart home devices** for voice-based control 🏠
🔹 Develop a **mobile application version** 📱
🔹 Expand **customization options** for user preferences ⚙️

---

## 🤝 Contributing

Want to improve this project? PRs are welcome! 🎉

1. **Fork the repo** 🍴
2. **Create a feature branch** (`git checkout -b feature-name`)
3. **Commit your changes** (`git commit -m 'Added new feature'`)
4. **Push and submit a PR** 🚀
5. **Join discussions and suggest improvements!** 💡

---

## 📝 License

Allowing free usage, modification, and distribution while giving credit to the original author.

---

## 📬 Developer

👨‍💻 **Aayush Kumar Gupta**

Kalinga Institute Of Industrial Technology

---

### ✨ Thanks for visiting! Happy Coding! 🚀 Keep innovating! 🎉

