code = 'code = \'?\'\nfor i in range(len(code)):\n\tif ord(code[i]) == 63:\n\t\tfor j in range(len(code)):\n\t\t\tif code[j] == \'\"\':\n\t\t\t\tprint(\'\\\\\"\', end=\"\")\n\t\t\telif code[j] == \"\'\":\n\t\t\t\tprint(\"\\\\\'\", end=\"\")\n\t\t\telif code[j] == \'\\\\\':\n\t\t\t\tprint(\'\\\\\\\\\', end=\"\")\n\t\t\telif code[j] == \'\\n\':\n\t\t\t\tprint(\'\\\\n\', end=\"\")\n\t\t\telif code[j] == \'\\t\':\n\t\t\t\tprint(\'\\\\t\', end=\"\")\n\t\t\telse:\n\t\t\t\tprint(code[j], end=\"\")\n\telse:\n\t\tprint(code[i], end=\"\")'
for i in range(len(code)):
    if ord(code[i]) == 63:
        for j in range(len(code)):
            if code[j] == '"':
                print('\\"', end="")
            elif code[j] == "'":
                print("\\'", end="")
            elif code[j] == '\\':
                print('\\\\', end="")
            elif code[j] == '\n':
                print('\\n', end="")
            elif code[j] == '\t':
                print('\\t', end="")
            else:
                print(code[j], end="")
    else:
        print(code[i], end="")