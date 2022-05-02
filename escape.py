with open('main.py', 'r') as f:
    c = f.read()
    print(c.replace('\\', '\\\\').replace('\n', '\\n').replace('    ', '\\t').replace("'", "\\'").replace('"', '\\"'))