# Color-to-hex-
```markdown
A simple Python program to convert color names to their corresponding hex codes using the `webcolors` library. This program takes a color name as input and returns the hex code for that color.

## Features

- Converts standard HTML color names to hex codes
- Easy to use in the terminal, including Termux

## Requirements

- Python 3.x
- `webcolors` library

## Installation

### Installing on Termux

To install and run the program on Termux, follow these steps:

1. **Update and Upgrade Packages**:

   Open Termux and run the following commands to update and upgrade existing packages:

   ```sh
   pkg update
   pkg upgrade
   ```

2. **Install Python**:

   Install Python by running:

   ```sh
   pkg install python
   ```

3. **Install `webcolors` Library**:

   Use `pip` (Python package installer) to install the `webcolors` library:

   ```sh
   pip install webcolors
   ```

4. **Clone the Repository**:

   Clone this repository to your local machine using `git`. If you don't have `git` installed, you can install it with:

   ```sh
   pkg install git
   ```

   Then clone the repository:

   ```sh
   git clone https://github.com/yourusername/color-to-hex-converter.git
   ```

5. **Navigate to the Project Directory**:

   Change to the project directory:

   ```sh
   cd color-to-hex-converter
   ```

6. **Run the Program**:

   Run the Python program:

   ```sh
   python color_to_hex_full.py
   ```

7. **Enter a Color Name**:

   After running the program, you will be prompted to enter a color name. Type the name of the color and press Enter.

   ```sh
   Enter the color name: red
   The hex code for red is: #FF0000
   ```

### Installing on Other Terminals

To install and run the program on other terminals (Linux, macOS), follow these steps:

1. **Ensure Python is Installed**:

   Make sure Python 3.x is installed. You can check this by running:

   ```sh
   python3 --version
   ```

   If Python is not installed, download and install it from [python.org](https://www.python.org/downloads/).

2. **Install `webcolors` Library**:

   Use `pip` (Python package installer) to install the `webcolors` library:

   ```sh
   pip install webcolors
   ```

3. **Clone the Repository**:

   Clone this repository to your local machine using `git`:

   ```sh
   git clone https://github.com/yourusername/color-to-hex-converter.git
   ```

4. **Navigate to the Project Directory**:

   Change to the project directory:

   ```sh
   cd color-to-hex-converter
   ```

5. **Run the Program**:

   Run the Python program:

   ```sh
   python color_to_hex_full.py
   ```

6. **Enter a Color Name**:

   After running the program, you will be prompted to enter a color name. Type the name of the color and press Enter.

   ```sh
   Enter the color name: red
   The hex code for red is: #FF0000
   ```

## Example

```sh
$ python color_to_hex_full.py
Enter the color name: aquamarine
The hex code for aquamarine is: #7FFFD4
```
