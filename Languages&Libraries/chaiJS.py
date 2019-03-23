from talon.voice import Context, Key
from ...talon_community.utils import parse_words, insert

context = Context("chai")

def remove_spaces_around_dashes(m):
    words = parse_words(m)
    s = ' '.join(words)
    s = s.replace(' – ', '-')
    insert(s)

def CursorText(s):
    left, right = s.split('{.}', 1)
    return [left + right, Key(' '.join(['left'] * len(right)))]


context.keymap({
  'assert no': CursorText('assert.isNull({.})'),
  'assert not no': CursorText('assert.isNotNull({.})'),
  'assert equal': CursorText('assert.strictEqual({.})'),
  'assert not equal': CursorText('assert.notStrictEqual({.})'),
  'assert include': CursorText('assert.include({.})'),
  'assert type': CursorText('assert.typeOf({.})'),
  'assert property': CursorText('assert.property({.})'),
  'assert not property': CursorText('assert.notProperty({.})'),
  'assert property value': CursorText('assert.propertyVal({.})'),
  'assert not property value': CursorText('asserty.notPropertyVal({.})'),
  'assert length': CursorText('assert.lengthOf({.})'),
})
