def remove_indentation(text):
    lines = text.split("\n")
    return "\n".join(line.lstrip() for line in lines)

print("Enter multi-line text (end with empty line):")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

text = "\n".join(lines)
print(remove_indentation(text))
