import tracemalloc


def format_memory(memory_bytes):
    if memory_bytes < 1024:
        return f"{memory_bytes} bytes"
    elif memory_bytes < 1024 * 1024:
        return f"{memory_bytes / 1024:.2f} KB"
    else:
        return f"{memory_bytes / (1024 * 1024):.2f} MB"


def trace_memory_usage(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()

        result = func(*args, **kwargs)

        current_memory, peak_memory = tracemalloc.get_traced_memory()

        print("Current memory usage:", format_memory(current_memory))
        print("Peak memory usage:", format_memory(peak_memory))

        tracemalloc.stop()

        return result

    return wrapper


# It is a another program showcasing importing.

from memory_tracer import trace_memory_usage


@trace_memory_usage
def app():
    lt = [i for i in range(100000)]


def main():
    app()


if __name__ == "__main__":
    main()
