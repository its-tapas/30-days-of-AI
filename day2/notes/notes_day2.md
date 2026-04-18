# Day 2 Notes — Prompt Control (System / Temperature / Max Output)

## Contents List

1. [Prompt Layering (The “2-Layer Sandwich”)](#1--prompt-layering-the-2-layer-sandwich)
2. [System Prompt (The “Boss Rules”)](#2--system-prompt-the-boss-rules)
3. [Temperature (The “Randomness Dial”)](#3--temperature-the-randomness-dial)
4. [Max Output / `num_predict` (The “Length Limit”)](#4--max-output--num_predict-the-length-limit)
5. [Stop Sequences (The “Hard Brake”)](#5--stop-sequences-the-hard-brake)
6. [Prompt Presets / Modes (The “Saved Settings”)](#6--prompt-presets--modes-the-saved-settings)
7. [Input Validation (The “Range Checker”)](#7--input-validation-the-range-checker)
8. [Functions and meanings (Conceptual helpers)](#8--functions-and-meanings-conceptual-helpers)

## 1 — Prompt Layering (The “2-Layer Sandwich”)

Definition: Keeping “behavior rules” separate from “the task” by splitting instructions into a system layer and a user layer.

Example:
- System: “Answer in 3 bullets. Be concise.”
- User: “Explain retries in HTTP clients.”

Why do we need this?
1. Consistency: the same rules apply to many tasks.
2. Safety/guardrails: you can enforce constraints centrally.
3. Clarity: you avoid mixing rules and questions into one confusing blob.

## 2 — System Prompt (The “Boss Rules”)

Definition: High-priority instructions that define how the assistant should behave (tone, format, constraints).

Example:
- System: “If you are unsure, say you are unsure. No invented facts.”

Why do we need this?
1. It’s the most reliable place to enforce format (JSON-only, bullets-only, etc.).
2. It keeps the assistant aligned to your expectations.
3. It reduces “style drift” across multiple questions.

## 3 — Temperature (The “Randomness Dial”)

Definition: A sampling control that changes how varied or predictable outputs are.

Example:
- Temperature 0.2: stable, repeatable-ish answers.
- Temperature 0.9: more variety, more risk of wandering.

Why do we need this?
1. Predictability: coding/checklist tasks usually want lower temperature.
2. Creativity: brainstorming can benefit from higher temperature.
3. Debugging: stable outputs make it easier to spot real issues.

## 4 — Max Output / `num_predict` (The “Length Limit”)

Definition: A cap on how much the model is allowed to generate.

Example:
- You request “3 bullets” and set `num_predict` to something small-ish.
- The model stops before producing a wall of text.

Why do we need this?
1. Prevents rambling.
2. Controls latency (longer outputs often take longer).
3. Helps CLI tools stay readable.

## 5 — Stop Sequences (The “Hard Brake”)

Definition: A list of strings that, if generated, will cause generation to stop.

Example:
- Stop sequence: `"\n\n"` to stop after one paragraph.
- Stop sequence: `"}"` when you want a single JSON object (use carefully).

Why do we need this?
1. Enforces clean boundaries (especially for structured outputs).
2. Prevents the assistant from adding extra commentary.
3. Improves consistency when combined with strict formatting instructions.

## 6 — Prompt Presets / Modes (The “Saved Settings”)

Definition: Named bundles of system prompts + options (temperature, max output, stop sequences).

Example:
- `concise`: “3 bullets, short sentences” + low temperature
- `teacher`: “step-by-step + tiny example” + medium temperature

Why do we need this?
1. Consistent behavior across runs.
2. Easier tuning: change one preset instead of many callers.
3. Faster UX: users pick a mode instead of typing options every time.

## 7 — Input Validation (The “Range Checker”)

Definition: Checking that user-provided controls are valid before calling the model.

Example:
- If temperature is `-1` or `"hot"`, raise a clean error instead of sending nonsense.

Why do we need this?
1. Prevents confusing server errors.
2. Makes bugs obvious and early.
3. Makes your code easier to test.

## 8 — Functions and meanings (Conceptual helpers)

### `normalize_system_prompt(text: str) -> str`

Meaning: Cleans a system prompt (trim whitespace; decide a policy for empty strings).

### `validate_temperature(value: float) -> None`

Meaning: Enforces a valid temperature range (commonly `0.0` to `1.0`).

### `validate_max_output_tokens(value: int) -> None`

Meaning: Ensures max output is a positive integer.

### `build_options(*, temperature: float | None = None, num_predict: int | None = None, stop: list[str] | None = None) -> dict`

Meaning: Builds an `options` dict with only the keys you set (no empty/invalid keys).

### `get_mode_preset(mode: str, presets: dict[str, dict]) -> dict`

Meaning: Fetches the preset for a mode name or raises a clear “unknown mode” error.

### `build_generate_payload(*, model: str, prompt: str, system: str | None, options: dict | None = None, stream: bool = False) -> dict`

Meaning: Builds a clean JSON request body for a generation call.
