# jpXCode Optimizer 🤖⚡
Windows System Optimizer dengan **AI Recommendation Engine (DeepSeek API)**.

Tool ini dibuat untuk **penggunaan nyata di PC pribadi**, fokus pada **monitoring realtime, analisis proses, dan rekomendasi optimasi yang aman**.

---

## ✨ Fitur Utama

### 📊 Realtime System Monitor
- CPU Usage
- RAM Usage
- Disk Usage (C:\)
- Status: OK / WARN / HIGH
- Non-blocking UI

### ⚙ Mini Task Manager
- Daftar proses aktif
- CPU % per proses
- RAM % per proses
- Auto refresh

### 🤖 AI Assistant (DeepSeek)
- Analisis kondisi PC berdasarkan data nyata
- Deteksi bottleneck performa
- Rekomendasi optimasi **AMAN**
- Saran startup & hardware upgrade
- Tidak ada auto-tweak berbahaya

---

## 📁 Struktur Project

```text
jpXCode-Optimizer/
├── main.py
├── ai_engine.py
├── requirements.txt
└── README.md

🖥️ Kebutuhan Sistem

Windows 10 / 11

Python 3.9+

Internet (untuk AI Assistant)

DeepSeek API Key (Free)

📦 Instalasi
1️⃣ Clone Repository
git clone https://github.com/jpXproject/jpXCode-Optimizer.git
cd jpXCode-Optimizer

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Set DeepSeek API Key (Windows)
set DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxxxxx


⚠️ Jangan hardcode API key ke dalam source code.

▶ Menjalankan Aplikasi
python main.py

📦 Compile ke EXE (Opsional)
pip install pyinstaller

pyinstaller --onefile --noconsole main.py


Hasil build:

/dist/main.exe

⚠️ Disclaimer

Aplikasi ini:

Tidak mengubah registry secara otomatis

Tidak mematikan service tanpa persetujuan user

Memberikan rekomendasi, bukan eksekusi paksa

Gunakan dengan bijak.

🚀 Roadmap

AI Auto-Apply (Safe Mode)

Optimization Profile (Gaming / Work)

Startup Manager (Enable / Disable)

System Health Score

Background Tray Monitor

👤 Author

jpX project

📜 License

MIT License
