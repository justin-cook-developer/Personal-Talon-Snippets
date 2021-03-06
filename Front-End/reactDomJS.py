from talon.voice import Context, Key
from ...talon_community.utils import parse_words, insert
from ..scopingFunctions import verifyFrontEndExtension

context = Context("ReactDomJS", func=verifyFrontEndExtension)

def remove_spaces_around_dashes(m):
    words = parse_words(m)
    s = ' '.join(words)
    s = s.replace(' – ', '-')
    insert(s)

def CursorText(s):
    left, right = s.split('{.}', 1)
    return [left + right, Key(' '.join(['left'] * len(right)))]


context.keymap({
  'react document import': CursorText("import ReactDOM{.} from 'react-dom';"),
  'react document render': ['ReactDOM.render()', Key('left')],
})
