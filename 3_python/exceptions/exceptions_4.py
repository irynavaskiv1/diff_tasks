import logging


def some_func():
    pass


def main():
    try:
        some_func()
    except TypeError as e:
        logging.error(f"Catch TypeError! {e}")
        raise


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error("Catch Exception!", e)
