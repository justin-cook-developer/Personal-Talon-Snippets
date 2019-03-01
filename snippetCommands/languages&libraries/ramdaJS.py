from talon.voice import Context, Key, press
import talon.clip as clip
from ....talon_community.utils import text, parse_words, parse_words_as_integer, insert, word, join_words

def verifyExtension(app, win):
    return win.doc.endswith(".js") or win.doc.endswith(".jsx..")

context = Context("ramda")

def remove_spaces_around_dashes(m):
    words = parse_words(m)
    s = ' '.join(words)
    s = s.replace(' – ', '-')
    insert(s)

def CursorText(s):
    left, right = s.split('{.}', 1)
    return [left + right, Key(' '.join(['left'] * len(right)))]


context.keymap({
  'raw placeholder': 'R.__',
  'raw curry': CursorText('R.curry({.})'),
  'raw pipe': CursorText('R.pipe({.})'),
  'raw find': CursorText('R.find({.})'),
  'raw default two': CursorText('R.defaultTo({.})'),
  'raw some': CursorText('R.sum({.})'),
  'raw append': CursorText('R.append({.})'),
  'raw [<dgndictation>]': ['R.', text, '()', Key('left')],
})
