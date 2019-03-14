import time

from talon.voice import Word, Key, Context, Str, press
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
from talon import ctrl, ui
import string

from ...talon_community.utils import numerals, parse_words, text, is_in_bundles, insert
from ...talon_community.bundle_groups import TERMINAL_BUNDLES

# TODO: move application specific commands into their own files: apt-get, etc

context = Context("myTerminal", func=is_in_bundles(TERMINAL_BUNDLES))

mapping = {"semicolon": ";", r"new-line": "\n", r"new-paragraph": "\n\n"}


def parse_word(word):
    word = word.lstrip("\\").split("\\", 1)[0]
    word = mapping.get(word, word)
    return word


def dash(m):
    words = parse_words(m)
    press(" ")
    if len(words) == 1 and len(words[0]) == 1:
        press("-")
        Str(words[0])(None)
    else:
        press("-")
        press("-")
        Str("-".join(words))(None)


context.keymap({
  # make basic front-end files
  "shell make script": "touch index.js",
  "shell make mark": "touch index.html",
  "shelll make style": "touch style.css",
  # seqeulize
  'new migration': 'sequelize migration:generate --name ',
  'new model': 'sequelize model:generate --name ',
  'model attributes': ' --attributes ',
  'run migration': 'sequelize db:migrate ',
  'undo migration': 'sequelize db:migrate:undo ',
  'new seed': 'sequelize seed:generate --name ',
  'run all seeds': 'sequelize db:seed:all ',
  'undo all seeds': 'sequelize db:seed:undo:all ',
  'run seed': 'sequelize db:seed --seed ',
  'undo seed': 'sequelize db:seed:undo ',
  # npm commands
  "note install [<dgndictation>]": ["npm install ", text],
  "note develop [<dgndictation>]": ["npm install --save-dev ", text],
  "note remove [<dgndictation>]": ["npm remove ", text],
  "note run": "npm start\n",
  "note run develop": "npm run start-dev",
})
