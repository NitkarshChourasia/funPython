Sure, I can modify the `memory_tracer` module to include an option to choose the unit of memory usage. We'll add a new parameter to the `trace_memory_usage` decorator, allowing the user to specify the desired unit. Here's the updated version of the `memory_tracer.py` module:

```python
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
```

Now, you can use the `trace_memory_usage` decorator with an optional unit argument when tracing memory usage in other programs. Here's an example of how to use it:

```python
from memory_tracer import trace_memory_usage

@trace_memory_usage(unit='megabytes')
def app():
    lt = [i for i in range(100000)]

def main():
    app()

if __name__ == "__main__":
    main()
```

In this example, the `trace_memory_usage` decorator is applied to the `app()` function, and we specify the unit as `'megabytes'`. You can choose from `'bytes'`, `'kilobytes'`, `'megabytes'`, or `'gigabytes'` as per your requirement.