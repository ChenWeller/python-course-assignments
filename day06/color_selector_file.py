#!/usr/bin/env python3
"""
color_selector_file.py

Reads a list of colors from a file and allows user to select a color
either by number or by name.

Usage:
    python color_selector_file.py <colors_file> [selection]

    - <colors_file> is the path to the file containing colors (one per line).
    - [selection] is optional and can be:
        - An integer (1-based index of the color)
        - A color name (case-insensitive)

If no selection is provided, the script displays a menu and prompts the user.

Example:
    python color_selector_file.py examples/files/colors.txt
    python color_selector_file.py examples/files/colors.txt 3
    python color_selector_file.py examples/files/colors.txt yellow
"""

import sys
import os

def load_colors(filepath):
    """
    Reads colors from the given file, stripping whitespace and ignoring empty lines.

    Args:
        filepath (str): Path to the colors file.

    Returns:
        list of str: List of color names.
    """
    colors = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                color = line.strip()
                if color:
                    colors.append(color)
    except Exception as e:
        print(f"Error reading colors file: {e}")
        sys.exit(1)

    if not colors:
        print("Error: No colors found in the file.")
        sys.exit(1)

    return colors

def print_menu(colors):
    """
    Prints a numbered menu of colors.

    Args:
        colors (list of str): List of colors to display.
    """
    print("Available colors:")
    for i, color in enumerate(colors, start=1):
        print(f"{i}. {color}")

def select_color_by_index(colors, index):
    """
    Select a color by 1-based index.

    Args:
        colors (list of str)
        index (int)

    Returns:
        str: Selected color if valid, else None
    """
    if 1 <= index <= len(colors):
        return colors[index - 1]
    return None

def select_color_by_name(colors, name):
    """
    Select a color by name (case-insensitive).

    Args:
        colors (list of str)
        name (str)

    Returns:
        str: Selected color if found, else None
    """
    name_lower = name.lower()
    for color in colors:
        if color.lower() == name_lower:
            return color
    return None

def prompt_user_selection(colors):
    """
    Prompt the user repeatedly until a valid selection is made.

    The user can enter either a number or a color name.

    Args:
        colors (list of str)

    Returns:
        str: Selected color
    """
    while True:
        choice = input("Please select a color by number or name: ").strip()
        # Try number first
        if choice.isdigit():
            idx = int(choice)
            color = select_color_by_index(colors, idx)
            if color:
                return color
            else:
                print(f"Invalid number. Please enter a number between 1 and {len(colors)}.")
        else:
            # Try by name
            color = select_color_by_name(colors, choice)
            if color:
                return color
            else:
                print(f"'{choice}' is not a valid color. Please try again.")

def main():
    # Check for at least one argument (colors file)
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python color_selector_file.py <colors_file> [selection]")
        sys.exit(1)

    colors_file = sys.argv[1]

    if not os.path.isfile(colors_file):
        print(f"Error: File '{colors_file}' does not exist.")
        sys.exit(1)

    colors = load_colors(colors_file)

    # If selection provided as argument
    if len(sys.argv) == 3:
        selection = sys.argv[2]
        # Try as number
        if selection.isdigit():
            selected_color = select_color_by_index(colors, int(selection))
            if not selected_color:
                print(f"Error: Number {selection} is out of range. Valid range is 1 to {len(colors)}.")
                sys.exit(1)
        else:
            selected_color = select_color_by_name(colors, selection)
            if not selected_color:
                print(f"Error: Color '{selection}' not found in list.")
                sys.exit(1)
    else:
        # No selection argument, show menu and prompt user
        print_menu(colors)
        selected_color = prompt_user_selection(colors)

    print(f"You selected: {selected_color}")

if __name__ == "__main__":
    main()
