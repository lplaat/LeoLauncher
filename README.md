# LeoLauncher - A Minecraft Launcher in Python

## Overview

LeoLauncher is a Python-based Minecraft launcher that simplifies the process of running Minecraft on your system.

## How to Run LeoLauncher

Follow these steps to run LeoLauncher on your system:

1. **Install Python:**
   - Ensure that Python is installed on your system. It is recommended to use version 3.8.9. You can download Python from [python.org](https://www.python.org/).

2. **Clone the Project:**
   - Clone the LeoLauncher project to your local machine using a version control system like Git.

     ```bash
     git clone https://github.com/lplaat/LeoLauncher.git
     ```

3. **Install Requirements:**
   - Navigate to the project directory and install the required dependencies using the following command:

     ```bash
     pip install -r requirements.txt
     ```

4. **Edit .env File:**
   - Open the `.env` file in the project directory and set your Minecraft username UUID and you're minecraft version.

     ```env
     MINECRAFT_USERNAME=YourUsername
     MINECRAFT_UUID=YourUUID
     MINECRAFT_VERSION=YourMinecraftVersion
     ```

5. **Set Java in PATH:**
   - Ensure that your Java version is added to your system's PATH environment variable. This is necessary for LeoLauncher to locate and use Java.

6. **Run LeoLauncher:**
   - Execute the main.py script to launch LeoLauncher:

     ```bash
     python main.py
     ```

   This command will start LeoLauncher, providing you with an easy and efficient way to launch Minecraft.

## Notes
- If you encounter any issues, double-check that your Python version is 3.8.9, and the required dependencies are installed.
- Ensure that your Java version is accessible from the command line.
- LeoLauncher has been tested and confirmed to work with Minecraft versions 1.13 up to 1.20.1 on Windows! Versions under 1.13 may not launch successfully.
- There are currently no possible ways to connect a Mojang account or Microsoft account to LeoLauncher.
- Please note that this code is old and considered to be in an early and less refined state. Consider it as a basic example rather than a production-ready application.

Enjoy playing Minecraft with LeoLauncher!
