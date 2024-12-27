# Hardware Information

A simple Python script.

Purpose is to allow users to check their hardware information with ease.

Easily access your computers hardware information essentials using this program.

---

## 📋 Features

1. **System Information**  
   Displays basic system details such as OS, manufacturer, and more.

2. **CPU Information**  
   Shows details about your processor.

3. **Memory Information**  
   Provides information on RAM capacity, speed.

4. **Storage Information**  
   Lists all storage drives and their size.

5. **GPU Information**  
   Displays details about your graphics card(s).

6. **Network Information**  
   Offers details on active network interfaces.

---

## ❓ How to Use

### Method 1: Run the Python Script
1. **Download**  
   Clone or download the repository as a ZIP file from the latest release:
   
   [![Download Latest Release Hardware_Information.zip](https://img.shields.io/badge/▼%20Download_Latest_Release%20▼-Source_Code.zip%20-blue?style=for-the-badge)](https://github.com/Justagwas/Hardware-Information/archive/refs/tags/v1.0.0.zip)

3. **Install Dependencies**  
   Ensure Python is installed on your system. Then, install the required libraries using the following command:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Script**  
   Execute the Python script using:
   ```bash
   python Hardware_Information.py
   ```

5. **Navigate the Menu**  
   Use the numeric input (1-7) to explore various system details or exit the program.

---

### Method 2: Download and Run the Executable
1. **Download Executable**  
   Head to the [Latest Release](https://github.com/Justagwas/Hardware-Information/releases/latest) page and download the precompiled executable file (`Hardware_Information.exe`).  

   [![Download Hardware_Information.exe](https://img.shields.io/badge/▼%20Download%20▼-Hardware_Information.exe%20-blue?style=for-the-badge)](https://github.com/Justagwas/Hardware-Information/releases/latest/download/Hardware_Information.exe)


2. **Run the Executable**  
   Simply double-click the `Hardware_Information.exe` file to launch the program. No additional setup or dependencies are required.

3. **Navigate the Menu**  
   Use the numeric input (1-7) to explore various system details or exit the program.

---
## 📦 Packaging Instructions

Follow these steps to package/build the Python script into an executable using **PyInstaller**:

1. **Extract ZIP**  
   Extract the downloaded ZIP file into a directory of your choice.

2. **Install PyInstaller**  
   Open a terminal/command prompt and install PyInstaller (if not already installed):
   ```bash
   pip install pyinstaller
   ```

3. **Build Using the `.spec` File**
   (skip this if you want to do it manually)
   
   Use the provided `.spec` file to replicate the exact settings used during development, run:
   ```bash
   pyinstaller Hardware_Information.spec
   ```
   
   This will generate the executable in the `dist/` folder, using the configurations from the `.spec` file.

4. **Build Without the `.spec` File** -#
   If you prefer to compile manually, run:
   ```bash
   pyinstaller --onefile Hardware_Information.py
   ```
   - `--onefile`: Combines all dependencies into a single executable.  

5. **Locate the Executable**  
   After packaging, the executable (`Hardware_Information.exe`) will be located in the `dist/` directory.


- **Why** should I build it by using the provided `.spec` file?

- `.spec` is a file that stores all the settings used during development packaging, meaning this is how the executable in releases was built, however, as the user, you are free to do whatever.
   
---

## 📷 Preview

![image](https://github.com/user-attachments/assets/3871bb5a-0c07-4f66-b838-d3c1436f5bbf)

---

## 🔗 Links & Statistics

[![Latest Release](https://img.shields.io/badge/🔖%20Latest%20Release-blue?style=for-the-badge)](https://github.com/Justagwas/Hardware-Information/releases/latest)  
[![Issues](https://img.shields.io/badge/🐛%20Issues-orange?style=for-the-badge)](https://github.com/Justagwas/Hardware-Information/issues)  
[![Contributors](https://img.shields.io/github/contributors/Justagwas/Hardware-Information?label=👥%20Contributors&style=for-the-badge)](https://github.com/Justagwas/Hardware-Information/graphs/contributors)  
[![Download Count](https://img.shields.io/github/downloads/Justagwas/Hardware-Information/total?label=⬇️%20Total%20Downloads&style=for-the-badge&color=blue)](https://github.com/Justagwas/Hardware-Information/releases)  
[![Open Issues](https://img.shields.io/github/issues/Justagwas/Hardware-Information?label=🐛%20Open%20Issues&style=for-the-badge)](https://github.com/Justagwas/Hardware-Information/issues)  
[![Last Commit](https://img.shields.io/github/last-commit/Justagwas/Hardware-Information?label=🕒%20Last%20Commit&style=for-the-badge)](https://github.com/Justagwas/Hardware-Information/commits)  

---

## 📜 License

[![License](https://img.shields.io/github/license/Justagwas/Hardware-Information?label=📝%20License&style=for-the-badge)](LICENSE.txt)
