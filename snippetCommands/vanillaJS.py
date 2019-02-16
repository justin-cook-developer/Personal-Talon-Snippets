from talon.voice import Context, Key, press
import talon.clip as clip
from ...talon_community.utils import text, parse_words, parse_words_as_integer, insert, word, join_words

def verifyExtension(app, win):
    return win.doc.endswith(".js") or win.doc.endswith(".jsx")

context = Context("javascript")

def remove_spaces_around_dashes(m):
    words = parse_words(m)
    s = ' '.join(words)
    s = s.replace(' – ', '-')
    insert(s)

def CursorText(s):
    left, right = s.split('{.}', 1)
    return [left + right, Key(' '.join(['left'] * len(right)))]


# namespace snippets
context.keymap({
  # UTILITY
  'script assign': ' = ',
  'script require': CursorText('require({.})'),
  'script log': CursorText('console.log({.})'),
  'script log error': CursorText('console.error({.})'),
  # MAIN LANGUAGE FEATURES
  'script funk': 'vanillaFunction',
  'script if': 'ifStatement',
  'script else': 'elseStatement',
  'script elif': 'ifElseStatement',
  'script switch': 'switchStatement',
  'script case': 'caseStatement',
  'script while': 'whileLoop',
  'script for': 'forLoop',
  'script terneary': 'ternary',
  # METHODS
  'script length': '.length',
  'script parse integer': CursorText('parseInt({.})'),
  # STRING METHODS
  'script uppercase': '.toUpperCase()',
  'script lowercase': '.toLowerCase()',
  # ARRAY METHODS
  'script pop': '.pop()',
  'script push': CursorText('.push({.})'),
  'script shift': '.shift()',
  'script on shift': CursorText('.unshift({.})'),
})
