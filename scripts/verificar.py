"""Confere integridade das fontes e dos artefatos de distribuição."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote
from zipfile import ZipFile

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'origem/inventario-wolf.json').read_text())
assert len(manifest['documentos']) == 11, 'Inventário WOLF incompleto'
for item in manifest['documentos']:
    data = (root / item['arquivo']).read_bytes()
    assert hashlib.sha256(data).hexdigest() == item['sha256'], item['arquivo']
    assert len(data) == item['bytes'], item['arquivo']
authored = [root / 'README.md', root / 'NOTICE.md', root / 'skills/ze-marreta-vendedor/SKILL.md']
authored += [p for p in (root / 'docs').glob('*.md') if not p.name.startswith('._')]
authored += [root / 'skills/ze-marreta-vendedor/references/indice.md',
             root / 'skills/ze-marreta-vendedor/references/framework-comercial-7-etapas.md']
for path in authored:
    for link in re.findall(r'\]\(([^)]+)\)', path.read_text()):
        if '://' not in link and not link.startswith('#'):
            assert (path.parent / unquote(link.split('#')[0])).exists(), (path, link)
bundle = (root / 'dist/ZE-MARRETA-COMPLETO.md').read_text()
for path in [root / 'prompts/INSTRUCOES.md'] + [p for p in (root / 'skills/ze-marreta-vendedor/references').glob('*.md') if not p.name.startswith('._')]:
    assert path.read_text() in bundle, f'Conteúdo ausente do pacote: {path}'
skill = root / 'skills/ze-marreta-vendedor'
expected = {p.relative_to(skill.parent).as_posix(): p.read_bytes()
            for p in skill.rglob('*') if p.is_file() and not p.name.startswith('._')}
with ZipFile(root / 'dist/ze-marreta-vendedor-skill.zip') as archive:
    assert set(archive.namelist()) == set(expected), 'Inventário do ZIP divergente'
    for name, data in expected.items():
        assert archive.read(name) == data, name
print('OK: 11 fontes WOLF íntegras; links locais, pacote completo e ZIP conferidos.')
