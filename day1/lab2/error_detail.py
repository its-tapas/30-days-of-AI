from __future__ import annotations

from typing import Any


def extract_error_detail(*, response_text: str, response_json: dict[str, Any] | None) -> str:
    """Extract a helpful error message from an HTTP error response.

    TODO (Practical): write your code here.

    Rules:
    - If response_json contains a non-empty string in key 'error', return it.
    - Else if response_json contains a non-empty string in key 'message', return it.
    - Else return stripped response_text (can be empty).
    """

    raise NotImplementedError
