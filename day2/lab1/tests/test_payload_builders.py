import pytest

from day2.lab1.prompt_playground import (
    DEFAULT_OLLAMA_BASE_URL,
    build_generate_payload,
    normalize_base_url,
    validate_controls,
)


def test_normalize_base_url_strips_and_removes_trailing_slash() -> None:
    assert normalize_base_url("  http://localhost:11434/  ") == "http://localhost:11434"


def test_normalize_base_url_empty_uses_default() -> None:
    assert normalize_base_url("   ") == DEFAULT_OLLAMA_BASE_URL


def test_validate_controls_ok() -> None:
    validate_controls(0.0, 1)
    validate_controls(1.0, 10)


def test_validate_controls_bad_temperature() -> None:
    with pytest.raises(ValueError):
        validate_controls(-0.1, 10)
    with pytest.raises(ValueError):
        validate_controls(1.1, 10)


def test_validate_controls_bad_max_tokens() -> None:
    with pytest.raises(ValueError):
        validate_controls(0.2, 0)


def test_build_generate_payload_has_expected_shape_and_options() -> None:
    payload = build_generate_payload(
        model="gemma2:2b",
        prompt="hi",
        system="Answer in 3 bullets",
        temperature=0.2,
        max_output_tokens=120,
    )

    assert payload["model"] == "gemma2:2b"
    assert payload["prompt"] == "hi"
    assert payload["stream"] is False
    assert payload["system"] == "Answer in 3 bullets"
    assert payload["options"]["temperature"] == 0.2
    assert payload["options"]["num_predict"] == 120


def test_build_generate_payload_omits_empty_system() -> None:
    payload = build_generate_payload(
        model="gemma2:2b",
        prompt="hi",
        system="   ",
        temperature=0.2,
        max_output_tokens=120,
    )
    assert "system" not in payload
