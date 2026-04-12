import pytest

from day2.lab2.prompt_modes import PROMPT_MODES, get_system_prompt


def test_get_system_prompt_known_modes() -> None:
    assert get_system_prompt("concise") == PROMPT_MODES["concise"]
    assert get_system_prompt("Teacher") == PROMPT_MODES["teacher"]
    assert get_system_prompt("  reviewer ") == PROMPT_MODES["reviewer"]


def test_get_system_prompt_unknown_mode_raises() -> None:
    with pytest.raises(ValueError):
        get_system_prompt("unknown")
