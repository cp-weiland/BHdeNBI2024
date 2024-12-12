import os, sys, re

import psycopg2 as pg
import pandas as pd


from ontogpt.clients import LLMClient


def getData():
    selec = "SELECT habitat FROM habitats WHERE habitat IS nOT null ORDER BY LENGTH (habitat) DESC LIMIT 1"
    con = pg.connect("dbname=collection user=ontogpt")
    cr = con.cursor()
    cr.execute(selec)
    result = cr.fetchall()
    return result

if __name__ == '__main__':

    dat = getData()

    with open("habitat.dat", "w") as outfile:
        outfile.write("\n".join(str(item) for item in dat))

    command = "ontogpt extract -i habitat.dat -t ./habitats.yaml -m ollama/llama3"
    print(command)
    print(os.popen(command).read())
