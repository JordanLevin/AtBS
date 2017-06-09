#!/usr/bin/env python3
# multiclipboard.pyw Saves and loads text to clipboard
# Usage: multiclipboard.pyw save <word> saves clipboard to word
#        multiclipboard.pyw <word> load word to clipboard
#        multiclipboard.pyw list - loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb') #opens file to save words to

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    #check if the arg is list or if it should load word
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
