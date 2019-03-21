from talon.voice import Context, Key, press
import talon.clip as clip
from ....talon_community.utils import text, parse_words, parse_words_as_integer, insert, word, join_words

def verifyExtension(app, win):
    return win.doc.endswith(".js") or win.doc.endswith(".jsx")

context = Context("axios")

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
  'axe create': CursorText('axios.all({.})'),
})
