import tracemalloc

def format_memory(memory_bytes, unit='bytes'):
    if unit == 'bytes':
        return f"{memory_bytes} bytes"
    elif unit == 'kilobytes':
        return f"{memory_bytes / 1024:.2f} KB"
    elif unit == 'megabytes':
        return f"{memory_bytes / (1024 * 1024):.2f} MB"
    elif unit == 'gigabytes':
        return f"{memory_bytes / (1024 * 1024 * 1024):.2f} GB"
    else:
        raise ValueError("Invalid unit. Use 'bytes', 'kilobytes', 'megabytes', or 'gigabytes'.")

def trace_memory_usage(unit='bytes'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            tracemalloc.start()

            result = func(*args, **kwargs)

            current_memory, peak_memory = tracemalloc.get_traced_memory()

            print("Current memory usage:", format_memory(current_memory, unit=unit))
            print("Peak memory usage:", format_memory(peak_memory, unit=unit))

            tracemalloc.stop()

            return result

        return wrapper

    return decorator


# Another program here to import the profiler showcase.
from memory_tracer import trace_memory_usage

@trace_memory_usage(unit='megabytes')
def app():
    lt = [i for i in range(100000)]

def main():
    app()

if __name__ == "__main__":
    main()
