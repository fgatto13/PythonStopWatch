# 🐍 PythonStopWatch ⏱️
## 🖼 App Preview
Here you can see what the app looks like:

![Screen1](assets/Screenshot%202025-07-31%20alle%2017.24.14.png)

And here are a couple of screenshots to show how the app behaves based on the operation performed:

<p float="left">
    <img src="assets/Screenshot%202025-07-31%20alle%2017.24.14.png" width="135"/>
    <img src="assets/Screenshot%202025-07-31%20alle%2017.24.28.png" width="135"/>
    <img src="assets/Screenshot%202025-07-31%20alle%2017.24.38.png" width="135"/>
</p>

This project is a stopwatch application built with **PyQt5**, combining a real-time digital clock with a start/stop/reset timer. It features a custom 7-segment-style font, dynamic styling, and a clean, interactive interface.

---

## 🚀 Features

- ✅ Stopwatch with Start / Stop / Reset functionality
- ✅ Real-time digital clock displayed at the top
- ✅ Updates every 10 milliseconds
- ✅ Custom font (`DS-DIGIT.TTF`) loaded safely with fallback
- ✅ Clean UI with bold styling and hover effects
- ✅ Custom cursor for buttons
- ✅ Button states change dynamically (e.g., disable Start after press)
- ✅ Designed for modularity and clarity using multiple classes

---

## 🗂 Project Structure

```
PythonStopwatch/
├── main.py              # Entry point – initializes and runs the app
├── stopwatch.py         # Main widget – stopwatch UI and logic
├── digitalClock.py      # Reused digital clock widget with real-time display
├── fonts/
│   └── ds_digital/
│       └── DS-DIGIT.TTF # Custom digital-style font
```

---

## 🎨 Styling

The app uses Qt Style Sheets (QSS) within Python to style:

- Labels and buttons with rounded borders
- Button hover states
- Font sizes and background colors

Buttons are enhanced with a **pointing hand cursor** to signal interactivity.

---

## 🧠 How It Works

- The stopwatch uses `QTime` and `QTimer` to track elapsed time in 10ms intervals.
- The digital clock updates every second using its own `QTimer`.
- Time is formatted consistently using `f"{val:02}"` specifiers to ensure fixed-width layout.
- The custom font is loaded using `QFontDatabase.addApplicationFont(...)` with safe fallbacks and exception handling.
- Font path detection adapts for PyInstaller or `.app` bundle usage.

---

## ▶️ Running the App

```bash
pip install PyQt5
python main.py
```

---

## 💾 Font Loading

The stopwatch uses a custom font stored at:

```
fonts/ds_digital/DS-DIGIT.TTF
```

It is loaded programmatically and safely handled in case the file is missing or fails to register.

---

## 🧑‍💻 Author

Built by @fgatto13  
This project reflects applied concepts of custom font handling, 
time management, event-driven programming, and clean UI design in PyQt5.

## 🙏 Credits & Acknowledgments

This project is based on a PyQt5 digital stopwatch tutorial originally created by [BroCode](https://www.youtube.com/watch?v=ix9cRaBkVe0&t=17196s).

The original tutorial served as a foundation for building a simple stopwatch GUI. 

This version adds:
- event handling of the various buttons (enabled/disabled dynamically)
- dynamic changes based on events for the text
- a custom font
- reuse of another custom widget (digital clock)