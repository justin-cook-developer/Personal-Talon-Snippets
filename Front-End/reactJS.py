from talon.voice import Context, Key
from ...talon_community.utils import parse_words, insert
from ..scopingFunctions import verifyFrontEndExtension

context = Context("ReactJS", func=verifyFrontEndExtension)

def remove_spaces_around_dashes(m):
    words = parse_words(m)
    s = ' '.join(words)
    s = s.replace(' – ', '-')
    insert(s)

def CursorText(s):
    left, right = s.split('{.}', 1)
    return [left + right, Key(' '.join(['left'] * len(right)))]


context.keymap({
  'react import': CursorText('import React{.} from \'react\';'),
  'react import prop types': 'import PropTypes from \'prop-types\';',
  'react component class': 'StatefulComponent',
  'react tag': CursorText('<{.} />'),
  'react fragment': CursorText('<React.Fragment>{.}</React.Fragment>'),
  'react state': CursorText('this.setState({.})'),
  'react prop types': CursorText("{.}.propTypes = { _: PropTypes.func.isRequired }"),
  # ATTRIBUTES
  'react clack': ['onClick={}', Key('left')],
  'react class': ['className=""', Key('left')],
  'react for': ['htmlFor=""', Key('left')],
  'react defaults': CursorText('{.}.defaultProps = {  };'),
  # LIFECYCLE
  'react will mount': CursorText('componentWillMount() {{.}}'),
  'react did mount': CursorText('componentDidMount() {{.}}'),
  'react unmount': CursorText('componentWillUnmount() {{.}}'),
  'react should update': CursorText('shouldComponentUpdate(nextProps, nextState) {{.}}'),
})
