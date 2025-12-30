import os
import requests

DEEPSEEK_API = "https://api.deepseek.com/v1/chat/completions"

class AIRecommendationEngine:
    def __init__(self):
        self.api_key = os.getenv("DEEPSEEK_API_KEY")
        if not self.api_key:
            raise RuntimeError("DEEPSEEK_API_KEY not set")

    def analyze(self, snapshot: dict) -> str:
        prompt = self._build_prompt(snapshot)
        return self._call_api(prompt)

    def _build_prompt(self, s):
        return f"""
You are a professional Windows optimization AI.

SYSTEM SNAPSHOT:
CPU Usage: {s['cpu']} %
RAM Usage: {s['ram']} %
Disk Usage: {s['disk']} %
Startup Programs: {s['startup']}
Top Processes:
{s['processes']}

TASK:
- Detect performance bottlenecks
- Recommend SAFE optimizations
- Recommend startup tweaks
- Suggest hardware upgrades if useful

Rules:
- Do NOT suggest dangerous registry edits
- Be concise
- Bullet points only
"""

    def _call_api(self, prompt):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "You are a Windows performance AI."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.2
        }

        r = requests.post(DEEPSEEK_API, headers=headers, json=payload, timeout=30)
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]
