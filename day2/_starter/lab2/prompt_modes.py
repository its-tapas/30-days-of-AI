from __future__ import annotations

PROMPT_MODES: dict[str, str] = {
    "concise": "Answer in 3–5 bullets. No fluff.",
    "teacher": "Explain step-by-step. Use a tiny example.",
    "reviewer": "Critique the approach. Call out risks and edge cases.",
}


def get_system_prompt(mode: str) -> str:
    """Return the system prompt for a given mode.

    TODO (Practical): write your code here.

    Rules:
    - mode lookup is case-insensitive
    - strip whitespace
    - raise ValueError if mode is unknown
    """

    raise NotImplementedError
