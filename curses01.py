#!/usr/bin/python3
# -*- coding: utf-8 -*-

import curses, time

def menu(stdscr):
    # no blinking cursor
    curses.curs_set(False)    
    
    stdscr.clear()
    stdscr.refresh()
    
    c = 0
    
    # window size
    height, width = stdscr.getmaxyx()
    
    # center horizontal
    #start_title = int((width // 2) - (len(title) // 2) - len(titile) % 2)
    # center vertical
    #first_row = int((hegiht //2) - (len(rows) // 2) - len(rows) % 2)
    
    window = stdscr.subwin(10, 10, 2, 2)
    waddstr(window, "ablak")
    box(window)
    key = wgetch(window)
    
    while c != ord('q'):
        # Store the key value in the variable `c`
        c = stdscr.getch()
        # Clear the terminal
        stdscr.clear()
        if c == ord('a'):
            stdscr.addstr("You pressed the 'a' key.")
        elif c == curses.KEY_UP:
            stdscr.addstr("You pressed the up arrow.", curses.A_REVERSE)
        elif c == ord('q'):
            curses.endwin()
        else:
            stdscr.addstr("This program doesn't know that key.....", curses.A_BOLD)

def main():
    curses.wrapper(menu)

if __name__ == "__main__":
    main()
