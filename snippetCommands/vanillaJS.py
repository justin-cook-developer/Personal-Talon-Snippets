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
  # should not be here
  'script come': [',', Key('space')],
  # UTILITY
  'script assign': ' = ',
  'script (rest | spread)': '...',
  'script structure': CursorText('{ {.} }'),
  'script require': CursorText('require({.})'),
  'script log': CursorText('console.log({.})'),
  'script log error': CursorText('console.error({.})'),
  'script type': 'typeof',
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
  # ES6 AND ES-NEXT FEATURES
  'script import': 'importJS',
  'script arrow': CursorText('({.}) => {}'),
  'script class': 'vanillaClass',
  'script class extends': 'vanillaClassExtends',
  'script sync': 'async',
  'script weight': 'await',
  # METHODS
  'script length': '.length',
  'script parse integer': CursorText('parseInt({.})'),
  # STRING PROTOTYPE METHODS
  'script uppercase': '.toUpperCase()',
  'script lowercase': '.toLowerCase()',
  # ARRAY PROTOTYPE METHODS
  'script pop': '.pop()',
  'script push': CursorText('.push({.})'),
  'script shift': '.shift()',
  'script on shift': CursorText('.unshift({.})'),
  'script index': CursorText('.indexOf({.})'),
  'script splice': CursorText('.splice({.})'),
  'script slice': CursorText('.slice({.})'),
  'script cat': CursorText('.concat({.})'),
  'script filter': CursorText('.filter({.})'),
  'script map': CursorText('.map({.})'),
  'script reduce': CursorText('.reduce({.})'),
  'script for each': CursorText('.forEach({.})'),
  'script split': CursorText('.split(\'{.}\')'),
  'script reverse': '.reverse()',
  'script joint': CursorText('.join(\'{.}\')'),
  'script sort': CursorText('.sort({.})'),
  'script find': CursorText('.find({.})'),
  # OBJECT CLASS METHODS
  'script keys': CursorText('Object.keys({.})'),
})
