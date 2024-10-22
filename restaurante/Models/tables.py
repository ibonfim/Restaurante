import sqlite3

banco = sqlite3.connect('restaurante_banco.db')

cursor=banco.cursor()
 
cursor.execute("""
                    CREATE TABLE IF NOT EXISTS user (
                        nome string , 
                        id integer PRIMARY KEY autoincrement,
                        senha string,
                        endereco string,
                        CPF integer UNIQUE,
                        telefone integer,
                        usertype TEXT CHECK( usertype IN ('ADMIN','USER') )   NOT NULL DEFAULT 'USER'
                         )
                        
                      
            """)


cursor.execute("""
                    CREATE TABLE IF NOT EXISTS pedido (
                        descricao text, 
                        id_user INTEGER,
                        id integer PRIMARY KEY autoincrement,
                        FOREIGN KEY (id_user) REFERENCES user(id)  ON DELETE CASCADE ON UPDATE CASCADE
                        )
            """)

cursor.execute("""
            
                CREATE TABLE IF NOT EXISTS cardapio (
                        nome string UNIQUE, 
                        id integer PRIMARY KEY autoincrement,
                        valor DECIMAL 
                        )
                        
            """)

    
 
# cursor.execute("PRAGMA foreign_keys=ON;") 
# cursor.execute("INSERT INTO user (nome,cpf,endereco,telefone,senha) VALUES ('Darap','127456789','rua abc',71987200798695, 'senha1234')")
# cursor.execute("INSERT INTO cardapio (nome,valor) VALUES ('Pizza Calabresa com catupiry','23,50'),('Pizza palmito com catupiry','29,50'),('Piza Lombinho com catupiry','22,30')")
# cursor.execute("INSERT INTO pedido (descricao, id_user) VALUES ('pizza de calabresa',1)")





banco.commit()

# consulta=cursor.execute("SELECT * FROM user").fetchall()
# print(consulta)