import requests
import re
from datetime import datetime
import psycopg2

url = "https://monitordolarvenezuela.com/historico/bcv-banco-central-de-venezuela"

response = requests.get(url)

if response.status_code == 200:
    content = response.text
    regex = """<div id="Costo">
(.+?) Bs
</div>"""

    for precio in re.findall(regex, content):
        dolar = float(precio.replace(',','.'))

hoy = datetime.today()

conexion = psycopg2.connect(
    database="",
    user="",
    password=""
)

cursor1=conexion.cursor()

sql = "insert into factura_dolar(created,modified,valor) values (%s,%s,%s)"
datos = (hoy,hoy,dolar)
cursor1.execute(sql,datos)
conexion.commit()
conexion.close()
