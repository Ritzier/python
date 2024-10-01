import curses
from curses import window


def keyboard_handler(stdscr: window) -> None:
    stdscr.clear()
    stdscr.addstr("Press 'q' to exit...\n")

    while True:
        key = stdscr.getch()
        if key == ord("q"):
            break
        stdscr.addstr(f"You pressed: {chr(key)}\n")
        stdscr.refresh()


def main():
    curses.wrapper(keyboard_handler)
