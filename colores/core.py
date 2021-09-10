import sys

import colorama

CYAN, RED, YELLOW, BLUE, MAGENTA = (
    colorama.Fore.CYAN,
    colorama.Fore.RED,
    colorama.Fore.YELLOW,
    colorama.Fore.BLUE,
    colorama.Fore.MAGENTA,
)


def setup_colorama() -> None:
    """
    Execute init function of Colorama. This is not necessary in Linux or Darwin.
    """
    if "win" in sys.platform:
        colorama.init()


def colorized_input(text: str, color: str = YELLOW) -> str:
    """
    Same as normal input, but printed with colors.
    """
    return input(f" {color}{text} ")


def colorized_print(
    text: str, color: str = BLUE, brightness: str = colorama.Style.NORMAL, **kwargs
) -> None:
    """
    Print the text with colors.
    """
    print(f"{brightness}{color} {text}{colorama.Style.RESET_ALL}", **kwargs)


def error_no_traceback(
    text: str, color: str = RED, brightness: str = colorama.Style.NORMAL, **kwargs
) -> None:
    """
    Print the text with colors and exit the program without traceback.
    """
    colorized_print(text, color, brightness, **kwargs)
    sys.exit(0)
