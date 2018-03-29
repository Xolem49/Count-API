#!C:\Users\Laptop-R\Desktop\Mes_Documents\IMIE\Cours\DEV3\Docker\tp3\serviceShowCount\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==9.0.1','console_scripts','pip3'
__requires__ = 'pip==9.0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pip==9.0.1', 'console_scripts', 'pip3')()
    )
