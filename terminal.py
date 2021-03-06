from talon.voice import Context

from ..talon_community.utils import text, is_in_bundles
from ..talon_community.bundle_groups import TERMINAL_BUNDLES

context = Context("myTerminal", func=is_in_bundles(TERMINAL_BUNDLES))

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
  "node root": "npm root [-g]\n",
  "node install [<dgndictation>]": ["npm install ", text],
  "node install dev [<dgndictation>]": ["npm install --save-dev ", text],
  "node remove [<dgndictation>]": ["npm uninstall ", text],
  "node remove dev [<dgndictation>]": ["npm uninstall --save-dev ", text],
  "node start": "npm start\n",
  "node run": "npm run ",
  "node run develop": "npm run start-dev",
  "node init": "npm init -y",
  "node react app": "npx create-react-app ",
  # prettier
  "node prettier": "prettier --write ",
})
