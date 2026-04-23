def remove_indentation(text):
    lines = text.split("\n")
    result = []

    for line in lines:
        result.append(line.lstrip())

    return "\n".join(result)


print("Enter multi-line text (end with empty line):")
lines = []

while True:
    line = input()
    if line == "":
        break
    lines.append(line)

text = "\n".join(lines)

print(remove_indentation(text))