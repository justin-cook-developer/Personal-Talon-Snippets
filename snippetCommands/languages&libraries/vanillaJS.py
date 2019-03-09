from talon.voice import Context, Key, press
import talon.clip as clip
from ....talon_community.utils import text, parse_words, parse_words_as_integer, insert, word, join_words

def verifyExtension(app, win):
    return win.doc.endswith(".js") or win.doc.endswith(".jsx")

context = Context("javascriptPersonal")

def remove_spaces_around_dashes(m):
    words = parse_words(m)
    s = ' '.join(words)
    s = s.replace(' – ', '-')
    insert(s)

def CursorText(s):
    left, right = s.split('{.}', 1)
    return [left + right, Key(' '.join(['left'] * len(right)))]


# namespace snippets for language features, namespace document for DOM features
context.keymap({
  # should not be here
  'script come': [',', Key('space')],
  'my block': [Key('space'), '{}', Key('left'), Key('enter')],
  # UTILITY
  'script (rest | spread)': '...',
  'script structure': CursorText('{ {.} }'),
  'script require': CursorText('require({.})'),
  'script log': CursorText('console.log({.})'),
  'script log air': CursorText('console.error({.})'),
  'script type': 'typeof ',
  'script instance': 'instanceof',
  # MAIN LANGUAGE FEATURES
  'script funk': 'vanillaFunction',
  'script switch': 'switchStatement',
  'script case': CursorText('case {.}:'),
  'script while': 'whileLoop',
  'script for': 'forLoop',
  'script terneary': 'ternary',
  # ES6 AND ES-NEXT FEATURES
  'script import': 'importJS',
  'script arrow': CursorText('({.}) => {}'),
  'script class': 'vanillaClass',
  'script class extends': 'vanillaClassExtends',
  'script promise': CursorText('new Promise((resolve, reject) => {({.})});'),
  'script promise all': CursorText('Promise.all({.})'),
  'script fetch': CursorText('fetch({.})'),
  # METHODS
  'script length': '.length',
  'script parse integer': CursorText('parseInt({.})'),
  # STRING PROTOTYPE METHODS
  'script uppercase': '.toUpperCase()',
  'script lowercase': '.toLowerCase()',
  'script starts with': CursorText('.startsWith({.})'),
  # ARRAY PROTOTYPE METHODS
  'script pop': '.pop()',
  'script push': CursorText('.push({.})'),
  'script shift': '.shift()',
  'script on shift': CursorText('.unshift({.})'),
  'script index': CursorText('.indexOf({.})'),
  'script splice': CursorText('.splice({.})'),
  'script slice': CursorText('.slice({.})'),
  'script cat': CursorText('.concat({.})'),
  'script includes': CursorText('.includes({.})'),
  'script filter': CursorText('.filter({.})'),
  'script map': CursorText('.map({.})'),
  'script reduce': CursorText('.reduce({.})'),
  'script for each': CursorText('.forEach({.})'),
  'script split': CursorText('.split(\'{.}\')'),
  'script every': CursorText('.every({.})'),
  'script some': CursorText('.some({.})'),
  'script reverse': '.reverse()',
  'script joint': CursorText('.join(\'{.}\')'),
  'script sort': CursorText('.sort({.})'),
  'script find': CursorText('.find({.})'),
  'script then': CursorText('.then({.})'),
  'script catch': CursorText('.catch({.})'),
  # ARRAY CLASS METHODS
  'script from': CursorText('Array.from({.})'),
  # OBJECT CLASS METHODS
  'script keys': CursorText('Object.keys({.})'),
  'script entries': CursorText('Object.entries({.})'),
  'script values': CursorText('Object.values({.})'),
  'script create': CursorText('Object.create({.})'),
  # JSONMETHODS
  'script jason': CursorText('JSON.parse({.})'),
  'script jason string': CursorText('JSON.stringify({.})'),
})

