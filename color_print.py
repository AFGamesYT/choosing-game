def txt(text, color=None, bold=False, italic=False, underline=False):
    """
    Returns formatted text with colors and decorations.
    """
    color_codes = {
        "black": "30",
        "red": "31",
        "green": "32",
        "yellow": "33",
        "blue": "34",
        "magenta": "35",
        "cyan": "36",
        "white": "37",
        "gray": "90",
        "reset": "0"
    }

    styles = []

    if bold:
        styles.append("1")
    if italic:
        styles.append("3")
    if underline:
        styles.append("4")
    if color in color_codes:
        styles.append(color_codes[color])

    start = "\033[" + ";".join(styles) + "m" if styles else ""
    end = "\033[0m" if styles else ""

    return f"{start}{text}{end}"

def format_print(*parts):
    """
    Prints multiple txt() objects in an order
    """
    print("".join(str(part) for part in parts))
