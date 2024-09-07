# **Random Password Generator**

This project provides a Python-based **Random Password Generator** that can be used via both a **Command-Line Interface (CLI)** and a **Graphical User Interface (GUI)**. It helps users generate secure and customizable passwords.

## **Features**
- Generate random, secure passwords.
- Customize password length and options for:
  - Uppercase letters
  - Numbers
  - Special characters
- Easy to use via both CLI and GUI.
- Copy passwords to the clipboard in the GUI version.

## **Requirements**
- Python 3.x installed on your machine.
- No external libraries are needed. The project uses built-in Python modules like `secrets`, `string`, and `tkinter`.

## **How to Use**

### **Command-Line Version (CLI)**
1. Save the script as `password_generator.py`.
2. Run the script from the terminal:
   ```bash
   python password_generator.py
   ```
3. You will be prompted to:
   - Enter the desired password length.
   - Specify whether to include uppercase letters, digits, and special characters.
4. The generated password will be displayed in the terminal.

### **Graphical User Interface (GUI) Version**
1. Save the GUI version as `gui_password_generator.py`.
2. Run the script from the terminal:
   ```bash
   python gui_password_generator.py
   ```
3. A window will appear where you can:
   - Enter the desired password length.
   - Select options for including uppercase letters, digits, and special characters.
4. Click "Generate Password" to see the generated password, and "Copy to Clipboard" to copy the password for easy use.

## **Example**

### **CLI Example**
```bash
$ python password_generator.py
Enter the desired password length: 12
Include uppercase letters? (y/n): y
Include digits? (y/n): y
Include special characters? (y/n): y
Generated Password: rA9#vW2$B1!
```

### **GUI Example**
- Simply run the GUI script and input the desired options through the window. Click on the buttons to generate and copy the password.

---
