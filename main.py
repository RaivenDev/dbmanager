import sqlite3
reset = ['quit', 'exit', 'cancel']
setupdb = bool(False)
tabling = []
c = ''
cursor = ''
banco = ''
additem = []


def ask():
    global setupdb
    global cursor
    global banco
    todo = str(input('Me diga o que quer fazer: '))
    if todo == 'setup':
        a = str(input('Me diga o nome da database: '))
        if a in reset:
            ask()
        else:
            print('Fazendo o setup...')    
            banco = sqlite3.connect(a + '.db')
            cursor = banco.cursor()
            setupdb = True
            ask()
    if todo == 'edit':
        if setupdb == True:
            edit = str(input('O que quer editar? '))
            if edit == 'table':
                nome = str(input('Qual vai ser o nome da table?'))
                a = int(input('Quantas camadas?'))
                command = str(tabler(a))
                x='CREATE TABLE '+nome
                final=x+command
                print(final)
                cursor.execute(final)
                ask()
            if edit == 'items':
                print('--- Abrindo Editor de Items ---') 
                nome = str(input('Qual é o nome da table requerida?'))
                a = int(input('Quantos items?'))
                command = item_editor(a)
                x = "INSERT INTO "+nome+" VALUES"
                final = x+str(command)
                print(str(final))
                cursor.execute(str(final))
                banco.commit()
                ask()
                

            else:
                print('Comando invalido...')
                ask()        
        else:
            print('O setup não foi feito...')  
            ask()      
    else:
        print('Comando invalido...')
        ask()        

def tabler(num):
    global c
    while num != 0:
        a = str(input('Qual será o nome dessa camada?'))
        b = str(input('Qual será o tipo dessa camada?'))
        a = a + ' ' + b
        if num == 1:
            c = c + a
        else:
            c = c + a + ', '
        num -= 1     
    finaltable = '(' + c + ')'
    c = ''
    return finaltable

def item_editor(num):
    global c
    global additem
    while num != 0:
        a = input('Qual será esse item?')
        b = str(input('Qual será o tipo desse item?'))
        if b == 'text':
            a = str(a)
            additem.append(str(a))
        elif b == 'integer':
            a = int(a)   
            additem.append(int(a)) 
        num -= 1     
    finaltable = tuple(additem)
    additem = []
    return finaltable



ask()
#banco = sqlite3.connect('primeiro_banco.db')

#cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")

#cursor.execute("INSERT INTO pessoas VALUES('Maria', 40, 'maria_123@gmail.com')")
#banco.commit()
#cursor.execute("SELECT * FROM pessoas")
#print(cursor.fetchall())

#cursor.execute("INSERT INTO pessoas VALUES('Joao', 20, 'joao_123@gmail.com')")
#banco.commit()

#cursor.execute("SELECT * FROM pessoas")
#print(cursor.fetchall())