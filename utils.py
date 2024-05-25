from difflib import SequenceMatcher

color_delete = "#FF0000"
color_insert = "#008000"
color_replace = "#FF8000"
f_str = '<span style="color: {};">{}</span>'


def getFormattedDiff(a, b):
    s = SequenceMatcher(None, a, b)

    formatted_a = []
    formatted_b = []

    for tag, i1, i2, j1, j2 in s.get_opcodes():
        if tag == "equal":
            formatted_a.append(a[i1:i2])
            formatted_b.append(b[j1:j2])
        elif tag == "delete":
            formatted_a.append(f_str.format(color_delete, a[i1:i2]))
        elif tag == "insert":
            formatted_b.append(f_str.format(color_insert, b[j1:j2]))
        elif tag == "replace":
            formatted_a.append(f_str.format(color_replace, a[i1:i2]))
            formatted_b.append(f_str.format(color_replace, b[j1:j2]))

    return "".join(formatted_a), "".join(formatted_b)
