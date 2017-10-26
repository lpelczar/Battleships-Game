import sys
import tty
import termios


def getch():
    """Get key which user has entered and return it
    Args:
        none
    Returns:
        ch: key user has enetered
    """
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
