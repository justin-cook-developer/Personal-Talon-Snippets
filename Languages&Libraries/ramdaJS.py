from talon.voice import Context, Key
from ...talon_community.utils import text, parse_words, insert
from ..scopingFunctions import verifyFrontEndExtension

context = Context("ramda", func=verifyFrontEndExtension)

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
