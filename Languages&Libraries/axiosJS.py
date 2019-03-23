from talon.voice import Context, Key
from ...talon_community.utils import parse_words, insert
from ..scopingFunctions import verifyFrontEndExtension

context = Context("axios", func=verifyFrontEndExtension)

def remove_spaces_around_dashes(m):
    words = parse_words(m)
    s = ' '.join(words)
    s = s.replace(' – ', '-')
    insert(s)

def CursorText(s):
    left, right = s.split('{.}', 1)
    return [left + right, Key(' '.join(['left'] * len(right)))]


context.keymap({
  'axe import': "import axios from 'axios';",
  'axe get': CursorText('axios.get({.})'),
  'axe post': CursorText('axios.post({.})'),
  'axe put': CursorText('axios.put({.})'),
  'axe delete': CursorText('axios.delete({.})'),
  'axe all': CursorText('axios.all([{.}])'),
  'axe create': CursorText('axios.create({.})'),
})
