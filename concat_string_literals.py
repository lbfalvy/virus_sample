import re
txt = open("before.strcat.js", "r").read()
final = re.sub(r'"\s*\+\s*"', "", txt)
open("strcats.done.js", "w").write(final)