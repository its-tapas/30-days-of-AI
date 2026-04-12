from __future__ import annotations

PROMPT_MODES: dict[str, str] = {
    "concise": "Answer in 3–5 bullets. No fluff.",
    "teacher": "Explain step-by-step. Use a tiny example.",
    "reviewer": "Critique the approach. Call out risks and edge cases.",
}


def get_system_prompt(mode: str) -> str:
    key = (mode or "").strip().lower()
    if key not in PROMPT_MODES:
        raise ValueError(f"Unknown mode: {mode!r}")
    return PROMPT_MODES[key]
