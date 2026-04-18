# Day 3 Notes — Chat Memory + Session Save/Load + Trimming

## Contents List

1. [Multi-Turn History (The “Long Memory”)](#1--multi-turn-history-the-long-memory)
2. [Message Roles (The “Script Labels”)](#2--message-roles-the-script-labels)
3. [Context Window (The “Attention Limit”)](#3--context-window-the-attention-limit)
4. [Context Trimming (The “Memory Eraser”)](#4--context-trimming-the-memory-eraser)
5. [Session Persistence (The “Save Game”)](#5--session-persistence-the-save-game)
6. [Schema Validation (The “Seatbelt”)](#6--schema-validation-the-seatbelt)
7. [Summarization (The “Compression”)](#7--summarization-the-compression)
8. [Functions and meanings (Conceptual helpers)](#8--functions-and-meanings-conceptual-helpers)

## 1 — Multi-Turn History (The “Long Memory”)

Definition: Sending the full list of prior chat messages to the model every time you ask a new question.

Example:
- Message 1 (user): “I like blue.”
- Message 2 (user): “What is my favorite color?”
- To answer Message 2, the request must include both Message 1 and Message 2.

Why do we need this?
1. Models are stateless (they don’t remember between requests).
2. The “history list” creates the illusion of a continuous conversation.
3. It enables follow-ups, references, and corrections.

## 2 — Message Roles (The “Script Labels”)

Definition: A label on each message that tells the model what that message represents.

The roles:
- System: “Boss” instructions (how to behave)
- User: the human asking questions
- Assistant: the model’s prior answers

Example:
- system: “You are a math teacher.”
- user: “What is 2+2?”
- assistant: “It is 4.”

Why do we need this?
1. The model must distinguish rules from questions from prior answers.
2. System rules should stay stable and high priority.
3. Role labeling reduces prompt confusion and “instruction leakage”.

## 3 — Context Window (The “Attention Limit”)

Definition: The maximum amount of text (tokens) the model can consider at once.

Example:
- If the model can only consider N tokens, messages beyond that limit effectively can’t be used.

Why do we need this?
1. You cannot grow history forever.
2. Performance and cost scale with how much you send.
3. You must choose what information is most important to keep.

## 4 — Context Trimming (The “Memory Eraser”)

Definition: Setting a limit on how much old history you include in each request.

Example:
- You decide to keep only the last 3 turns.
- When you send the 4th turn, the oldest turn is dropped from the list.

Why do we need this?
1. Space: you must fit within the context window.
2. Speed: less history usually means faster responses.
3. Focus: old topics can become noise when the conversation shifts.

## 5 — Session Persistence (The “Save Game”)

Definition: Saving the message list to disk and loading it later so a conversation can resume.

Example:
- Save: write `{ "messages": [...] }` to a JSON file.
- Load: read JSON back into memory and continue appending messages.

Why do we need this?
1. You can resume after closing your terminal/editor.
2. You can share a session file or archive it.
3. It enables debugging (you can replay a session deterministically-ish).

## 6 — Schema Validation (The “Seatbelt”)

Definition: Verifying loaded/supplied data has the expected structure before using it.

Example:
- Ensure `messages` is a list.
- Ensure each message is a dict with string `role` and string `content`.

Why do we need this?
1. Files can be corrupted or edited manually.
2. Validation prevents confusing runtime errors later.
3. It improves security hygiene by treating disk input as untrusted.

## 7 — Summarization (The “Compression”)

Definition: Replacing older message history with a short summary message that preserves key facts.

Example:
- Replace 30 old messages with 1 summary: “Summary: user prefers blue; goal is to build a CLI chatbot; avoid web APIs.”

Why do we need this?
1. Keeps important context without blowing the window.
2. Retains long-term “facts” even when trimming aggressively.
3. Helps the model stay on-topic across long conversations.

## 8 — Functions and meanings (Conceptual helpers)

### `build_chat_payload(*, model: str, messages: list[dict], stream: bool = False, options: dict | None = None) -> dict`

Meaning: Builds the JSON body for a chat request.

### `trim_messages_by_turns(messages: list[dict], max_turns: int) -> list[dict]`

Meaning: Keeps system messages and only the last N turns.

### `trim_messages_by_budget(messages: list[dict], budget: int) -> list[dict]`

Meaning: Keeps as many recent messages as possible under a size limit (tokens/characters).

### `summarize_old_history(messages: list[dict]) -> dict`

Meaning: Produces one summary message to replace older history.

### `save_session(path, messages: list[dict], version: int = 1) -> None`

Meaning: Writes the session to disk as UTF-8 JSON (often with an atomic write).

### `load_session(path) -> list[dict]`

Meaning: Loads a session from disk, validates it, and returns a message list.
