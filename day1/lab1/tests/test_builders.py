from day1.lab1.ollama_one_shot import (
    DEFAULT_OLLAMA_BASE_URL,
    build_generate_url,
    build_stream_payload,
    normalize_base_url,
)


def test_normalize_base_url_strips_and_removes_trailing_slash() -> None:
    assert normalize_base_url("  http://localhost:11434/  ") == "http://localhost:11434"


def test_normalize_base_url_empty_uses_default() -> None:
    assert normalize_base_url("   ") == DEFAULT_OLLAMA_BASE_URL


def test_build_generate_url() -> None:
    assert build_generate_url("http://example:11434/") == "http://example:11434/api/generate"


def test_build_stream_payload() -> None:
    payload = build_stream_payload("gemma2:2b", "hello")
    assert payload["model"] == "gemma2:2b"
    assert payload["prompt"] == "hello"
    assert payload["stream"] is True
