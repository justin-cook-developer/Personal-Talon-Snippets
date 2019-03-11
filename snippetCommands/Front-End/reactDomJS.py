from talon.voice import Context, Key, press
import talon.clip as clip
from ....talon_community.utils import text, parse_words, parse_words_as_integer, insert, word, join_words

def verifyExtension(app, win):
    return win.doc.endswith(".js") or win.doc.endswith(".jsx")

context = Context("ReactDomJS")

def remove_spaces_around_dashes(m):
    words = parse_words(m)
    s = ' '.join(words)
    s = s.replace(' – ', '-')
    insert(s)

def CursorText(s):
    left, right = s.split('{.}', 1)
    return [left + right, Key(' '.join(['left'] * len(right)))]


context.keymap({
  'react document import': ["import ReactDOM from 'react-dom';", Key('enter')],

  'react document import hash': ["import {HashRouter as Router, Router, Link, NavLink} from 'react-router-dom';", Key('enter')],

  'react document import browser': ["import {BrowserRouter as Router, Route, Link, NavLink, Switch} from 'react-router-dom';", Key('enter')],

  'react document render': ['ReactDOM.render()', Key('left')],
})
