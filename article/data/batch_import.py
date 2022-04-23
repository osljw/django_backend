import os
import glob
from pathlib import Path

from ..models import Article

base_dir='E:\\workspace\\vue_work\\django_backend\\osljw_docs\\docs'
#base_dir='E:/workspace/vue_work/django_backend/osljw_docs/docs'

for path in Path(base_dir).rglob('*.md'):
    print(path.relative_to(base_dir))
