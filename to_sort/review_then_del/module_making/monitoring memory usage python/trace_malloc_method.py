# importing the module
import tracemalloc


# code or function for which memory
# has to be monitored
def app():
    lt = []
    for i in range(0, 1000):
        lt.append(i)


# starting the monitoring
tracemalloc.start()

# function call
app()

# displaying the memory
print(tracemalloc.get_traced_memory())

# stopping the library
tracemalloc.stop()


# First iteration of python.
import tracemalloc


def app():
    lt = []
    for i in range(0, 100000):
        lt.append(i)


def format_memory(memory_bytes):
    if memory_bytes < 10000:
        return f"{memory_bytes} KB"
    else:
        return f"{memory_bytes / 1024:.2f} MB"


tracemalloc.start()

app()

current_memory, peak_memory = tracemalloc.get_traced_memory()
print("Current memory usage:", format_memory(current_memory))
print("Peak memory usage:", format_memory(peak_memory))

tracemalloc.stop()


# Second iteration of python.
import tracemalloc


def app():
    lt = [i for i in range(100000)]


def format_memory(memory_bytes):
    if memory_bytes < 1024:
        return f"{memory_bytes} bytes"
    elif memory_bytes < 1024 * 1024:
        return f"{memory_bytes / 1024:.2f} KB"
    else:
        return f"{memory_bytes / (1024 * 1024):.2f} MB"


def main():
    tracemalloc.start()

    app()

    current_memory, peak_memory = tracemalloc.get_traced_memory()
    print("Current memory usage:", format_memory(current_memory))
    print("Peak memory usage:", format_memory(peak_memory))

    tracemalloc.stop()


if __name__ == "__main__":
    main()
