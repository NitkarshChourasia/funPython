import numpy as np
from numba import cuda, jit
import string

# Precompute the list of digits as a Numpy array of bytes on the CPU
digits = np.array(list(string.digits.encode()), dtype=np.uint8)

@cuda.jit(device=True)
def generate_password_combinations(length, password, target_password, output):
    # Recursive function to generate password combinations
    index = cuda.threadIdx.x + cuda.blockDim.x * cuda.blockIdx.x

    if index >= length:
        return

    for d in digits:
        password[index] = d

        # Check if the generated password matches the target password
        if cuda.grid(1) == 0 and np.all(password[:length] == target_password):
            output[0] = 1  # Set output flag to 1
            for i in range(length):
                output[i+1] = password[i]  # Copy the cracked password to the output

        generate_password_combinations(length, password, target_password, output)

def password_cracker(target_password, max_length, output):
    password_length = 1  # Start with password length 1

    # Initialize an array on the CPU to hold the password
    password = np.zeros(max_length, dtype=np.uint8)

    while password_length <= max_length:
        # Launch the CUDA kernel (one block with 256 threads)
        threads_per_block = 256
        blocks_per_grid = 1
        generate_password_combinations[blocks_per_grid, threads_per_block](password_length, password, target_password, output)

        password_length += threads_per_block * blocks_per_grid

if __name__ == "__main__":
    # Target numeric password (change this to the password you want to crack)
    target_password = np.array(list("1234"), dtype=np.uint8)

    # Set the maximum password length to try
    max_length = 6

    # Initialize output array (used to store the result)
    output = np.zeros(max_length + 1, dtype=np.uint8)

    # Launch the password_cracker function
    password_cracker(target_password, max_length, output)

    # Check if the password was cracked
    if output[0] == 1:
        cracked_password = "".join(map(str, output[1:]))
        print(f"Password successfully cracked! The password is: {cracked_password}")
    else:
        print("Password not found. Try increasing the max_length or target a different password.")
