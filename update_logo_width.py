from pathlib import Path

root = Path('www.bechtel.com')
pattern = 'width="64" height="48"'
replacement = 'width="80" height="48"'
files = list(root.rglob('*.html'))
updated = 0
for path in files:
    text = path.read_text(encoding='utf-8')
    if pattern in text:
        new_text = text.replace(pattern, replacement)
        if new_text != text:
            path.write_text(new_text, encoding='utf-8')
            updated += 1
            print(f'Updated {path}')
print(f'Files updated: {updated}')
