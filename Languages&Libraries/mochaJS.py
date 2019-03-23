from talon.voice import Context, Key
from ...talon_community.utils import parse_words, insert
from ..scopingFunctions import verifyJavascriptExtension

context = Context("mocha", func=verifyJavascriptExtension)

def remove_spaces_around_dashes(m):
    words = parse_words(m)
    s = ' '.join(words)
    s = s.replace(' – ', '-')
    insert(s)

def CursorText(s):
    left, right = s.split('{.}', 1)
    return [left + right, Key(' '.join(['left'] * len(right)))]


context.keymap({
  'desribe block': 'describeBlock',
  'it block': CursorText('it(\'{.}\', function(){})'),
})
