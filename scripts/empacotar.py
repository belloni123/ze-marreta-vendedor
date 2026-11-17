"""Gera distribuição Markdown e ZIP, sem dependências externas."""
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

root = Path(__file__).resolve().parents[1]
skill = root / 'skills/ze-marreta-vendedor'
dist = root / 'dist'
dist.mkdir(exist_ok=True)
files = [root / 'prompts/INSTRUCOES.md'] + sorted(p for p in (skill / 'references').glob('*.md') if not p.name.startswith('._'))
parts = ['# ZE MARRETA - VENDEDOR — pacote completo\n\n'
         'Instruções e documentos de consulta. Os blocos históricos são fontes; '
         'aplique as instruções atuais na interpretação. Créditos e direitos em NOTICE.md.\n',
         (root / 'NOTICE.md').read_text()]
for path in files:
    parts.append(f'\n---\n\n<!-- ARQUIVO: {path.relative_to(root).as_posix()} -->\n\n' + path.read_text())
(dist / 'ZE-MARRETA-COMPLETO.md').write_text('\n'.join(parts), encoding='utf-8')
with ZipFile(dist / 'ze-marreta-vendedor-skill.zip', 'w', compression=ZIP_DEFLATED) as archive:
    for path in sorted(skill.rglob('*')):
        if path.is_file() and not path.name.startswith('._'):
            info = ZipInfo(path.relative_to(skill.parent).as_posix(), date_time=(2026, 11, 17, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
print('Distribuições geradas em dist/.')
