import random
from typing import Optional

# Simulated content generator. Replace with OpenAI calls later.
def generate_post(topic: str, tone: Optional[str] = "professional") -> str:
    templates = [
        f"[{tone}] Quick insights on {topic}: 1) Keep learning 2) Build projects 3) Share knowledge.",
        f"[{tone}] Why {topic} matters in 2025 — short thread-style: ...",
        f"[{tone}] 3 practical tips to improve your {topic} skills today."
    ]
    return random.choice(templates)
