from talon.voice import Context, Key, press
import talon.clip as clip
from ...talon_community.utils import text, parse_words, parse_words_as_integer, insert, word, join_words

def verifyExtension(app, win):
    return win.doc.endswith(".js")

context = Context("javascript")

def remove_spaces_around_dashes(m):
    words = parse_words(m)
    s = ' '.join(words)
    s = s.replace(' – ', '-')
    insert(s)

def CursorText(s):
    left, right = s.split('{.}', 1)
    return [left + right, Key(' '.join(['left'] * len(right)))]


context.keymap({
  # DOM PROPERTIES
  'document inner': '.innerHTML',
  'document text': '.textContent',
  'document eye text': '.innerText',
  # DOM ATTACHERS
  'document append': CursorText('.appendChild({.})'),
  # DOM CREATORS
  'document create element': CursorText('document.createElement({.})'),
  'document create text': CursorText('document.createTextNode({.})'),
  # DOM RETRIEVERS
  'document idea jen': CursorText('document.getElementById({.})'),
  'document idea': CursorText('.getElementById({.})'),
  'document class jen': CursorText('document.getElementsByClassName({.})'),
  'document class': CursorText('.getElementsByClassName({.})'),
  'document query all jen': CursorText('document.querySelectorAll({.})'),
  'document query all': CursorText('.querySelectorAll({.})'),
  'document query jen': CursorText('document.querySelector({.})'),
  'document query': CursorText('.querySe9lector({.})'),
  'document tag jen': CursorText('document.getElementsByTagName({.})'),
  'document tag': CursorText('.getElementsByTagName({.})'),
  # EVENT LISTENER
  'document listen': CursorText('.addEventListener({.})'),
})
