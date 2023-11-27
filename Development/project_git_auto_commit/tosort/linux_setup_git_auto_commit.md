# 🚀 Automate Git Commits on Linux using `crontab`

## Overview
This guide will help you automate Git commits on a Linux-based operating system using `crontab`. By following these accurate and straightforward steps, you can schedule regular commits to your Git repository. Ensure your project is always up to date with minimal effort.

### Prerequisites
- A Linux-based operating system.
- Git installed on your system.
- A Python script (`main.py`) for performing Git commits. Ensure this script is in an easily accessible location.

## Step-by-Step Instructions

1. 🕵️‍♂️ **Open `crontab`**
   - Open a terminal and run the following command to open `crontab` with root privileges:
     ```shell
     sudo crontab -e
     ```

2. 📝 **Add a `crontab` Entry**
   - In the `crontab` file, add the following line to schedule your Git commits at a specific time (e.g., 11:59 PM):
     ```shell
     59 23 * * * cd /path/to/script/folder/ ; /usr/bin/env /usr/local/bin/python3.8 /path/to/script/main.py
     ```
     - Replace `/path/to/script/folder/` with the actual path to the folder containing your Python script.
     - Ensure that the Python interpreter path (`/usr/local/bin/python3.8`) is correct. You can check your Python interpreter location with `which python3.8` and adjust the path accordingly.

3. 💾 **Save and Exit**
   - Save the `crontab` file and exit the text editor.

4. 🛠️ **Git Configuration**
   - Note that you may encounter Git configuration issues. To resolve this, generate a GitHub token in your GitHub developer settings. Then, use the generated token as a login for Git. Make sure Git is configured correctly on your system.

## Additional Information
- You can explore more about `crontab` scheduling at [crontab.guru](https://crontab.guru). 

By following these steps, you'll have automated Git commits running on your Linux system. Your project will stay up to date with the scheduled commits. 🚀😎💻
