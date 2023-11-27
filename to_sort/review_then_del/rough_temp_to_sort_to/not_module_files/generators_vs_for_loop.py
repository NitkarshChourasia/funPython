import psutil


# Function using a generator to generate 10 million integers
def generate_numbers_with_generator(n):
    for i in range(n):
        print(i + i)
        yield i


# Function using a normal for loop to generate 10 million integers
def generate_numbers_with_for_loop(n):
    numbers = []
    for i in range(n):
        numbers.append(i)
    return numbers


def measure_ram_usage(function, *args):
    process = psutil.Process()
    before_ram = process.memory_info().rss / (
        1024 * 1024
    )  # RAM usage before function call (in MB)
    result = function(*args)
    after_ram = process.memory_info().rss / (
        1024 * 1024
    )  # RAM usage after function call (in MB)
    ram_usage = after_ram - before_ram
    return result, ram_usage


if __name__ == "__main__":
    total_numbers = 10000000  # 10 million integers

    # Using generator
    generator_result, generator_ram_usage = measure_ram_usage(
        generate_numbers_with_generator, total_numbers
    )
    print(f"Generator RAM Usage: {generator_ram_usage} MB")
    # Uncomment the line below to see the generated numbers when using the generator
    # print(list(generator_result))

    # Using normal for loop
    for_loop_result, for_loop_ram_usage = measure_ram_usage(
        generate_numbers_with_for_loop, total_numbers
    )
    print(f"For Loop RAM Usage: {for_loop_ram_usage} MB")
    # Uncomment the line below to see the generated numbers when using the for loop
    # print(for_loop_result)


# Slowly Slowly, understand it.
