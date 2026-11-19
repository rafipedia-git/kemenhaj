"""Buat ZIP source code portabel; tanpa konfigurasi akun atau kredensial."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
root = Path(__file__).resolve().parent
out = root / 'dist' / 'source-code.zip'
files = [root / 'README.md', root / 'package-source.py']
files += [p for p in (root / 'dist').rglob('*') if p.is_file() and p != out]
with ZipFile(out, 'w', ZIP_DEFLATED) as z:
    for p in sorted(files):
        z.write(p, 'kemenhaj-salatiga/' + str(p.relative_to(root)))
print(out)
