#!/data/data/com.termux/files/usr/bin/env

import yaml
import glob
import sqlite3

cocktails = glob.glob("recipes/*.yml")

for cocktail in cocktails:
    f = open(cocktail)

    # use safe_load instead load
    cocktail = yaml.safe_load(f)

    f.close()

    print(cocktail)
