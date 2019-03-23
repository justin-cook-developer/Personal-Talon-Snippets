def verifyJavascriptExtension(app, win):
    if win.doc.endswith(".js"):
      return True
    elif win.doc.endswith(".ts"):
      return True
    else:
      return False

def verifyFrontEndExtension(app, win):
  if verifyJavascriptExtension(app, win):
    return True
  elif win.doc.endswith(".jsx"):
    return True
  elif "freeCodeCamp" in win.title:
    return True
  else:
    return False
