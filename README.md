# jpXCode Optimizer 🤖⚡  
**Windows System Optimizer with AI Recommendation Engine (DeepSeek)**

jpXCode Optimizer adalah aplikasi **Windows system monitoring & optimization tool** dengan **AI Assistant** berbasis **DeepSeek API**.  
Dibuat untuk penggunaan **real-world**, fokus pada **stabilitas, keamanan, dan performa**, bukan gimmick.

---

## ✨ Features

### 📊 Realtime System Monitor
- CPU usage
- RAM usage
- Disk usage (C:\)
- Status indicator (OK / WARN / HIGH)
- Non-blocking UI (thread-safe)

### ⚙ Mini Task Manager
- Running processes
- CPU usage per process
- RAM usage per process
- Auto refresh (2s)
- Lightweight (psutil based)

### 🤖 AI Assistant (DeepSeek)
- Analyze real system snapshot
- Detect performance bottlenecks
- Recommend **SAFE** optimizations
- Startup optimization advice
- Hardware upgrade suggestions
- No dangerous auto-tweaks

### 🔐 Safety First
- ❌ No auto registry edits
- ❌ No forced service disable
- ✅ Recommendation only
- ✅ User in full control

---

## 🧠 AI Engine

Powered by **DeepSeek Chat API (Free Tier)**  
AI hanya bekerja berdasarkan **real snapshot data**, bukan asumsi.

AI Tasks:
- Bottleneck detection
- Safe optimization advice
- Startup program insights
- Hardware upgrade recommendations

---

## 📁 Project Structure

jpXCode-Optimizer/
│
├── main.py # Application entry point
├── ai_engine.py # DeepSeek AI Recommendation Engine
├── requirements.txt # Dependencies
└── README.md # Documentation

---

## 🖥 Requirements

- Windows 10 / 11
- Python **3.9+**
- Internet connection (for AI Assistant)
- DeepSeek API Key 

---

## 📦 Installation

### 1️⃣ Clone Repository
```bash
git clone https://github.com/yourusername/jpXCode-Optimizer.git
cd jpXCode-Optimizer

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Set DeepSeek API Key (Windows)
set DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxxxxx


🔐 Never hardcode your API key

▶ Run Application
python main.py

🧪 Tested On

Windows 10 Pro

Windows 11

SSD & NVMe systems

8GB / 16GB RAM

📦 Compile to EXE (Optional)
pip install pyinstaller
pyinstaller --onefile --noconsole main.py


Output:

/dist/main.exe

⚠ Disclaimer

This software:

Does NOT modify critical system settings automatically

Does NOT disable services without user consent

Does NOT guarantee performance increase on all systems

Use recommendations responsibly.

🚀 Roadmap

 AI Auto-Apply (Optional & Safe Mode)

 Optimization Profiles (Gaming / Work / Battery)

 Startup Manager with Toggle UI

 System Health Score

 Tray Background Monitor

 Hardened EXE Release

🧑‍💻 Author

jpX project
Built for real-world personal system optimization.

📜 License

MIT License
Feel free to fork, modify, and improve.

⚡ “Optimize responsibly. Measure everything. Trust data, not myths.”
