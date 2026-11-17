"""Copia a skill para um diretório escolhido, sem sobrescrever versões existentes."""
import argparse
import shutil
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--destino', required=True, type=Path, help='Diretório de skills do agente')
args = parser.parse_args()
source = Path(__file__).resolve().parents[1] / 'skills' / 'ze-marreta-vendedor'
target = args.destino.expanduser().resolve() / source.name
if target.exists():
    parser.exit(1, f'Já existe: {target}. Preserve ou renomeie a instalação anterior antes de atualizar.\n')
shutil.copytree(source, target, ignore=shutil.ignore_patterns('._*', '.DS_Store'))
print(f'Skill instalada em {target}. Abra uma nova sessão no seu agente.')
