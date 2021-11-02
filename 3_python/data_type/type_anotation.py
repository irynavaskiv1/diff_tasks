from typing import Tuple


def get_api_response() -> Tuple[int, int]:  # type annotation
    successes, errors = ...  # Some API call
    return successes, errors
