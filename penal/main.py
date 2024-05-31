from database import sqlite3, conn, cursor

# usuario relatando o a ação
Crime = input("Qual foi a ação cometida?")

# Buscando no db
conn = sqlite3.connect('penal.db')
cursor = conn.cursor()
cursor.execute('''
        SELECT Crime, Cod_penal 
            FROM penal
            WHERE Crime = ? 
''',(Crime,))
result = cursor.fetchall()
conn.close()

# verificar se encontro
if result is None:
    print("Crime não encontrado")
else:
# Print inf
    Cod_penal = result[:1]
    print(f'Código Penal: {Cod_penal}')

