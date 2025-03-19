#!/usr/bin/env python3
"""
A simple Hello World program demonstrating basic Python functionality.
"""

def greet(name: str = "World") -> str:
    """
    Returns a personalized greeting message.
    
    Args:
        name (str): Name to include in greeting. Defaults to "World".
    
    Returns:
        str: Formatted greeting message
    """
    return f"Hello, {name}!"

def main():
    """Main function that runs when the script is executed directly."""
    print(greet())
    # Example of personalized greeting
    print(greet("Python Developer"))

if __name__ == "__main__":
    main()