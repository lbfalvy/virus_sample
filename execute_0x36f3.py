import re
import json
txt = open("before._0x36f3.precomputed.js", "r").read()
myjson = json.load(open("_0x36f3.json", "r"))
def replacement(match:re.Match):
    return json.dumps(myjson[int(match.group(1), base=0)])
final = re.sub(r'_0x36f3\("(0x[0-9a-f]+)"\)', replacement, txt)
open("precomputed._0x36f3.js", "w").write(final)