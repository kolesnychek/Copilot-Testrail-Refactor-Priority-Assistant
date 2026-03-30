from __future__ import annotations

import logging
import os

from llm.github_models_backend import GitHubModelsBackend


class LLMClient:
    def __init__(self):
        backend = os.getenv("LLM_BACKEND", "github_models").strip().lower()
        if backend != "github_models":
            raise ValueError("Only 'github_models' backend is supported.")

        self.provider = GitHubModelsBackend()
        self.model = os.getenv("GITHUB_MODELS_MODEL", "").strip()
        if not self.model:
            raise EnvironmentError("GITHUB_MODELS_MODEL must be set.")

    def log_provider(self, logger: logging.Logger | None = None):
        target = logger if logger is not None else logging.getLogger(__name__)
        target.info("LLM provider: GitHub Copilot | Model: %s", self.model)

    async def complete(self, prompt: str) -> str:
        return await self.provider.complete(prompt)
