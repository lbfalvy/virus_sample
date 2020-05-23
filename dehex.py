text = open("load.js", "r").read()
outtext = ""
jumpnum = 0
for i in range(0, len(text)-2):
    if jumpnum > 0:
        jumpnum -= 1
        continue
    if text[i:i+2] == '\\x':
        num = int(text[i+2:i+4], 16)
        newtext = chr(num)
        if newtext == '"':
            newtext = '\"'
        if newtext == "'":
            newtext = "\'"
        if newtext == "\\":
            newtext = "\\\\"
        outtext += newtext
        jumpnum = 3
    else: 
        outtext += text[i]
open("load-dehexed.js", "w").write(outtext)