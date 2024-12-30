from re import finditer, MULTILINE

if __name__ ==   '__main__':
    with open('geo-datadome.js', 'r') as f:
        data = f.read()
        matches = finditer(r"'(?P<name>(\\x[0-9A-Fa-f]{2})+)'", data, MULTILINE)
        actualNames = {}
        for match in matches:
            actualNames[match.group('name')] = match.group('name').encode().decode('unicode_escape').replace("'", "\\'")

        sortNames = sorted(actualNames.keys(), key=len, reverse=True)
        for name in sortNames:
            data = data.replace(name, actualNames[name])

        with open('geo-datadome-resolved.js', 'w') as w:
            w.write(data)