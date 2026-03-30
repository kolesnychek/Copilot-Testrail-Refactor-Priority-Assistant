import importlib.util
import os
from pathlib import Path

from llm.llm_client import LLMClient


def _load_module():
    os.environ.setdefault("TESTRAIL_URL", "https://example.testrail.io")
    os.environ.setdefault("TESTRAIL_EMAIL", "test@example.com")
    os.environ.setdefault("TESTRAIL_API_KEY", "key")
    os.environ.setdefault("TESTRAIL_SECTION_ID", "1")
    module_path = Path(__file__).resolve().parents[1] / "Copilot-AI-TestRail.py"
    spec = importlib.util.spec_from_file_location("copilot_testrail", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


class _StubLLMClient:
    def __init__(self, response_text: str):
        self.response_text = response_text
        self.called = 0

    async def complete(self, prompt: str) -> str:
        self.called += 1
        return self.response_text


def test_llm_client_uses_supported_backend():
    prev = {
        "LLM_BACKEND": os.getenv("LLM_BACKEND"),
        "GITHUB_MODELS_TOKEN": os.getenv("GITHUB_MODELS_TOKEN"),
        "GITHUB_MODELS_MODEL": os.getenv("GITHUB_MODELS_MODEL"),
    }
    try:
        os.environ["LLM_BACKEND"] = "github_models"
        os.environ["GITHUB_MODELS_TOKEN"] = "token"
        os.environ["GITHUB_MODELS_MODEL"] = "model"
        client = LLMClient()
        assert client.model == "model"
    finally:
        for key, value in prev.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value


def test_refactor_case_with_agent_routes_through_llm_client():
    mod = _load_module()
    stub = _StubLLMClient(
        '{"title":"T","preconditions":"P","steps":[{"action":"A","expected_result":"E"}],"global_expected_result":"","violations":[],"priority_id":2,"priority_reason":""}'
    )
    mod._llm_client = stub

    import asyncio

    raw_case = {
        "title": "old",
        "custom_preconds": "p",
        "custom_steps": "1. a",
        "custom_expected": "1. e",
        "custom_steps_separated": None,
    }
    out = asyncio.run(mod.refactor_case_with_agent(raw_case))
    assert stub.called == 1
    assert out["title"] == "T"
