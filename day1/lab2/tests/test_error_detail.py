from day1.lab2.error_detail import extract_error_detail


def test_extract_error_detail_prefers_error_key() -> None:
    assert (
        extract_error_detail(
            response_text="raw text",
            response_json={"error": "Model not found"},
        )
        == "Model not found"
    )


def test_extract_error_detail_uses_message_key() -> None:
    assert (
        extract_error_detail(
            response_text="raw text",
            response_json={"message": "Something went wrong"},
        )
        == "Something went wrong"
    )


def test_extract_error_detail_falls_back_to_text() -> None:
    assert (
        extract_error_detail(
            response_text="  plain body  ",
            response_json=None,
        )
        == "plain body"
    )


def test_extract_error_detail_ignores_empty_json_values() -> None:
    assert (
        extract_error_detail(
            response_text="fallback",
            response_json={"error": "   ", "message": ""},
        )
        == "fallback"
    )
