import time
from functools import wraps

def flaky_retry(max_retries: int = 2, delay_sec: float = 0.5):
    """
    Decorator to retry a flaky function/test a few times.
    Raises the last exception if all attempts fail.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, max_retries + 2):  # e.g., 2 retries -> up to 3 attempts
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    last_exc = exc
                    if attempt <= max_retries:
                        time.sleep(delay_sec)
                    else:
                        raise last_exc
        return wrapper
    return decorator
