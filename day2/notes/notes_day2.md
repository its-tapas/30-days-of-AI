# Day 2 Notes — Prompt Control (system / temperature / max output)

## Abbreviations / technical terms

| Term | Meaning |
|---|---|
| System prompt | High-priority instruction that sets rules/style/constraints. |
| User prompt | The task/question the user asks. |
| Temperature | Randomness control (lower = more consistent). |
| Sampling | How the model chooses next tokens (temperature/top_p/seed/etc.). |
| `num_predict` | Ollama option that limits output length (similar to max output tokens). |
| Stop sequence | A string that tells generation to stop when produced. |
| Deterministic | Same input → same output (not always guaranteed, but closer at low temperature). |
| Guardrails | Constraints you enforce (format, allowed actions, safety rules). |
| Preset / mode | A named bundle of system prompt + settings (example: “teacher”). |

## Topics (1-liners)

| Topic | One-liner |
|---|---|
| Prompt layering | System sets rules; user sets task; keep them separate. |
| Output predictability | Lower temperature + clear constraints → more reliable outputs. |
| Output length control | Use `num_predict` to avoid overly long or cut-off outputs. |
| Prompt presets | Store reusable “modes” as a dict so behavior is consistent. |
| Input validation | Fail fast on invalid controls (range/type checks). |
| Format control | Ask for bullets/JSON and add stop sequences if needed. |

## Prompt layering (the practical mental model)

You typically have (at least) two instruction layers:

1) **System prompt** (rules, style, boundaries)
2) **User prompt** (the task)

Good practice:
- System prompt: short and constraint-based
- User prompt: specific task + required output format

Example system prompt:

- “Answer in 3 bullets. No fluff. If unsure, say you’re unsure.”

Example user prompt:

- “Explain retries in HTTP clients.”

## Temperature (what it really changes)

Temperature changes how “random” the token sampling is.

Practical guidance:
- `0.0–0.3`: stable, good for coding steps and checklists
- `0.4–0.7`: balanced
- `0.8+`: creative/varied, but less consistent

Important:
- Low temperature does not magically make outputs correct.
- It mainly makes outputs **more consistent**.

## Output length (`num_predict` / max output tokens)

Why you need it:
- Too high: long, rambling answers
- Too low: truncated answers

Practical starting point:
- 80–250 for short explanations
- 300–800 for longer reasoning (still depends on model)

## Prompt presets (“modes”)

A mode is a named preset that controls behavior.

Example mode registry (conceptual):

- `concise`: short bullets
- `teacher`: step-by-step with a tiny example
- `reviewer`: critique + risks + edge cases

Why modes help:
- Consistent behavior
- Less repetition
- Easier to test and tune

## Reusable helper functions (generic)

### `validate_temperature(value: float) -> None`

Meaning:
- Ensures temperature is in an allowed range (commonly `[0.0, 1.0]`).

Why:
- Prevents accidental “garbage in” values.

### `validate_max_output_tokens(value: int) -> None`

Meaning:
- Ensures output limit is positive.

Why:
- A zero/negative value is always a bug.

### `normalize_system_prompt(text: str) -> str`

Meaning:
- Cleans whitespace and returns a normalized string.

Typical rule:
- `text.strip()`

### `build_options(*, temperature: float | None = None, num_predict: int | None = None, stop: list[str] | None = None) -> dict`

Meaning:
- Builds a clean `options` dict with only the keys you actually set.

Why:
- Avoid sending empty/invalid keys.

### `build_generate_payload(*, model: str, prompt: str, system: str | None, options: dict, stream: bool = False) -> dict`

Meaning:
- Builds the request JSON for generation.

Key behaviors:
- Validate `model` non-empty
- Include `system` only if non-empty
- Include `options` only if non-empty

### `get_mode_preset(mode: str, presets: dict[str, dict]) -> dict`

Meaning:
- Returns preset config for a mode name.

Rules:
- Strip + lowercase mode
- Raise a clear error if unknown

## Example payload (conceptual)

```json
{
  "model": "gemma2:2b",
  "prompt": "Explain retries",
  "system": "Answer in 3 bullets. Be concise.",
  "stream": false,
  "options": {
    "temperature": 0.2,
    "num_predict": 160
  }
}
```

## Common pitfalls (and fixes)

- Overlong system prompts: keep them short and constraint-based.
- Mixing task + rules in one string: separate system (rules) from user (task).
- Temperature too high for “reliable” tasks: lower it.
- Truncation: increase `num_predict` or tighten the requested format.
- Empty system prompt key: omit it instead of sending `"system": ""`.
