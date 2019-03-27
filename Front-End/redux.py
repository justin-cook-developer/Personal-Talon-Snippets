from talon.voice import Context, Key
from ...talon_community.utils import parse_words, insert
from ..scopingFunctions import verifyFrontEndExtension

context = Context("redux", func=verifyFrontEndExtension)

def remove_spaces_around_dashes(m):
    words = parse_words(m)
    s = ' '.join(words)
    s = s.replace(' – ', '-')
    insert(s)

def CursorText(s):
    left, right = s.split('{.}', 1)
    return [left + right, Key(' '.join(['left'] * len(right)))]


context.keymap({
  # redux snippets
  'duck import': CursorText('import { createStore, combineReducers, applyMiddleware{.} } from \'redux\';'),
  'duck store': CursorText('createStore({.})'),
  'duck combine': CursorText('combineReducers({.})'),
  'duck patch': CursorText('dispatch({.})'),
  'duck mid': CursorText('applyMiddleware({.})'),
  # react-redux snippets
  'duck import provider': 'import { Provider } from \'react-redux\';',
  'duck import connect': 'import { connect } from \'react-redux\';',
  'duck provider': CursorText('<Provider>{.}</Provider>'),
  'duck map state': 'mapStateToProps',
  'duck map patch': 'mapDispatchToProps',
})

