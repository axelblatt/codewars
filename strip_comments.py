def strip_comments(strng, markers):
    lines = strng.split("\n")
    for i in range(len(lines)):
        for j in markers:
            try:
                lines[i] = lines[i][:lines[i].index(j)]
                while lines[i][-1] == " ":
                    lines[i] = lines[i][:-1]
            except:
                pass
    lines = "\n".join(lines)
    while "\t\n" in lines:
        lines = lines.replace("\t\n", "\n")
    return lines