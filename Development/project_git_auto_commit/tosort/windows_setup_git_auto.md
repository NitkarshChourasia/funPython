# 🤖 Automate Git Commits with Task Scheduler

## Overview
This guide will walk you through setting up automated Git commits on a Windows system using Task Scheduler. Follow these precise steps to schedule regular commits to your Git repository, ensuring your project is always up to date.

### Prerequisites
- Git installed on your system.
- A batch script (`run.bat`) with Git commit commands. Ensure the script is easily accessible.

## Step-by-Step Instructions

1. 🕵️‍♂️ **Open Task Scheduler**
   - Click the Windows search bar, type "Task Scheduler," and open the app.

2. 🚀 **Create a New Task**
   - In Task Scheduler, click "Create Task..." in the right panel.

3. 📝 **Name the Task**
   - In the General tab, name your task "Git Auto Commit" for easy identification.

4. ⚙️ **Configure Task Settings**
   - In the General tab, ensure the following options are selected:
     - ✔️ "Run with highest privileges" to avoid permission issues.
     - ✔️ "Run whether the user is logged on or not" to run the task even when your PC is logged out.

5. 📅 **Set Triggers**
   - Go to the "Triggers" tab, click "New," and configure the trigger to your desired schedule (e.g., daily). Ensure the trigger's "Status" is "Enabled."

6. 🚨 **Define Actions**
   - In the "Actions" tab, specify the program to run.
   - Click "Browse," navigate to your `run.bat` script, and double-click it as the action. No additional arguments are needed.

7. ⚙️ **Additional Settings**
   - In the "Settings" tab, configure additional options, such as:
     - 🔄 Restart the task if it fails (you can set a delay between retries).
     - ⏱️ Set the task to run as soon as possible after a missed schedule.

## Conclusion
By following these accurate and straightforward steps, you've configured Task Scheduler to automate Git commits. Your project will stay up to date without manual intervention. 🚀😎💻