from talon.voice import Context, Key
from ...talon_community.utils import parse_words, insert

def verifyExtension(app, win):
    return win.doc.endswith(".js") or win.doc.endswith(".jsx")

context = Context("ReactRouter")

def remove_spaces_around_dashes(m):
    words = parse_words(m)
    s = ' '.join(words)
    s = s.replace(' – ', '-')
    insert(s)

def CursorText(s):
    left, right = s.split('{.}', 1)
    return [left + right, Key(' '.join(['left'] * len(right)))]


context.keymap({
  # IMPORTS
  'router import hash': CursorText("import { HashRouter as Router, Router, Link, NavLink }{.} from 'react-router-dom';"),
  'router import browser':CursorText("import { BrowserRouter as Router, Route, Link, NavLink, Switch }{.} from 'react-router-dom';"),
  'router import navigation': CursorText("import { NavLink }{.} from 'react-router-dom';"),
  'router import link': CursorText("import { Link }{.} from 'react-router-dom';"),
  # TAGS
  'router link': CursorText('<Link to= >{.}</Link>'),
  'router navigation': CursorText('<NavLink to="" >{.}</NavLink>'),
  'router switch': CursorText('<Switch>{.}</Switch>'),
  # ATTRIBUTES
  'router path': ['path=""', Key('left')],
  'router exact': 'exact={true}',
  'router render': CursorText('render={() => {.}}'),
})
