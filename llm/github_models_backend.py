from __future__ import annotations

import os

import aiohttp


class GitHubModelsBackend:
    def __init__(self):
        self.token = os.getenv("GITHUB_MODELS_TOKEN", "").strip()
        self.model = os.getenv("GITHUB_MODELS_MODEL", "").strip()
        if not self.token or not self.model:
            raise EnvironmentError("GITHUB_MODELS_TOKEN and GITHUB_MODELS_MODEL must be set.")

    async def complete(self, prompt: str) -> str:
        url = "https://api.githubcopilot.com/v1/completions"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": self.model,
            "prompt": prompt,
            "temperature": 0.1,
            "max_tokens": 4096,
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, headers=headers) as resp:
                resp.raise_for_status()
                data = await resp.json()
        choices = data.get("choices") or []
        if not choices:
            raise ValueError("GitHub Models backend returned no choices.")
        text = (choices[0].get("text") or "").strip()
        if not text:
            raise ValueError("GitHub Models backend returned empty completion.")
        return text
