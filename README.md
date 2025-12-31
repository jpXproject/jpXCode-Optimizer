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

<img width="2752" height="1536" alt="Realtime System Monitor" src="https://github.com/user-attachments/assets/581f6446-5387-4cd8-8d8c-35a23ed27b5a" />

### ⚙ Optimizing
- Daftar proses aktif
- CPU % per proses
- RAM % per proses
- Auto refresh
  
<img width="2816" height="1536" alt="wmremove-transformed (7)" src="https://github.com/user-attachments/assets/9df44c8c-8e79-4d1a-ae38-cab9c26028d7" />

<img width="2816" height="1536" alt="Optimizing" src="https://github.com/user-attachments/assets/df06723a-59ea-4787-b95f-70cb428e49bc" />

### 🤖 AI Assistant  
- Analisis kondisi PC berdasarkan data nyata
- Deteksi bottleneck performa
- Rekomendasi optimasi **AMAN**
- Saran startup & hardware upgrade
- Tidak ada auto-tweak berbahaya

<img width="2752" height="1536" alt="AI Assistant" src="https://github.com/user-attachments/assets/33d290db-2672-481c-af95-86808a743a49" />

---

## 📁 Struktur Project

```text
jpXCode-Optimizer/
├── main.py
├── ai_engine.py
├── requirements.txt
└── README.md
```
🖥️ Kebutuhan Sistem

Windows 10 / 11

Python 3.9+

Internet (untuk AI Assistant)

DeepSeek API Key  

Tentang DeepSeek API
DeepSeek API adalah antarmuka pemrograman aplikasi yang memungkinkan pengembang mengintegrasikan kemampuan AI DeepSeek ke dalam aplikasi mereka sendiri.

Cara Mendapatkan DeepSeek API
1. Akses Platform DeepSeek
Kunjungi website resmi DeepSeek: platform.deepseek.com

Atau melalui halaman utama: deepseek.com

2. Proses Registrasi
   
- Klik tombol "Sign Up" atau "Register"
- Anda bisa mendaftar menggunakan email atau akun Google
- Lengkapi proses verifikasi email

3. Mengelola API Key:
   
- Setelah login, buka dashboard pengembang
- Navigasi ke bagian "API Keys" atau "API Management"
- Klik "Create new API key" untuk membuat kunci baru
- Simpan API key dengan aman - ini hanya akan ditampilkan sekali!

4. Dokumentasi API
- Akses dokumentasi lengkap di: api-docs.deepseek.com
- okumentasi berisi contoh kode, parameter, dan best practices

Contoh Penggunaan API
```python
import requests

api_key = "your-api-key-here"
url = "https://api.deepseek.com/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "user", "content": "Halo, bisa bantu saya?"}
    ]
}

response = requests.post(url, json=data, headers=headers)
print(response.json())
```

📦 Instalasi
1️⃣ Clone Repository
```python
git clone https://github.com/jpXproject/jpXCode-Optimizer.git
cd jpXCode-Optimizer
``` 
2️⃣ Install Dependencies
```python
pip install -r requirements.txt
```
3️⃣ Set DeepSeek API Key (Windows)
```python
set DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxxxxx
```

⚠️ Jangan hardcode API key ke dalam source code.

▶ Menjalankan Aplikasi
```python
python main.py
```
📦 Compile ke EXE (Opsional)
```python
pip install pyinstaller

pyinstaller --onefile --noconsole main.py
```

Hasil build:
```
/dist/main.exe
```
⚠️ Disclaimer

Aplikasi ini:
- Tidak mengubah registry secara otomatis
- Tidak mematikan service tanpa persetujuan user
- Memberikan rekomendasi, bukan eksekusi paksa
- Gunakan dengan bijak.


🚀 Roadmap

- AI Auto-Apply (Safe Mode)
- Optimization Profile (Gaming / Work)
- Startup Manager (Enable / Disable)
- System Health Score
- Background Tray Monitor

  
👤 Author
```
jpX project
```
```
📜 License

MIT License
```
