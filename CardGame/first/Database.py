import mysql.connector


pw='20040723caesar'
conect = mysql.connector.connect(user='root', password=pw, host='localhost', database='CardGame',auth_plugin='mysql_native_password')


def createDatabase():
    conect=mysql.connector.connect(user='root',password=pw,host='localhost')
    con=conect.cursor()
    con.execute('CREATE DATABASE CardGame')
    print("ok")
def createPasswordTable():

    con = conect.cursor()
    con.execute('CREATE TABLE PlayerPassword(ID int AUTO_INCREMENT PRIMARY KEY,Name VARCHAR(255),Password VARCHAR(255),CardsNameList VARCHAR(255))')
def creatCardTable():

    con = conect.cursor()
    con.execute(
        'CREATE TABLE CardStore(ID int AUTO_INCREMENT PRIMARY KEY,Name VARCHAR(255),CardsName VARCHAR(255),Cards VARCHAR(255))')
def addCard(name,CardsName,Cards):
    con = conect.cursor()
    check=[i[0] for i in CardListName(name)]
    if CardsName in check:
        con.execute('UPDATE CardStore SET Cards="%s" WHERE CardsName="%s" AND Name="%s"'%(str(Cards),str(CardsName),name))#UPDATE CardStore SET Cards='/39G0a/11S0c/15S0a/11S0d/11S0e/11S0f/11S0g/11S0h/11S0i/11S0j' WHERE id=1;
    else:
        con.execute('INSERT INTO CardStore(Name,CardsName,Cards) VALUES ("%s","%s","%s")'%(str(name),str(CardsName),str(Cards)))
    conect.commit()
def addPlayer(Name,Password,CardsNameList):

    con = conect.cursor()
    con.execute('INSERT INTO PlayerPassword(Name,Password,CardsNameList) VALUES ("%s","%s","%s")'%(str(Name),str(Password),str(CardsNameList)))
    conect.commit()
def getCardListByName(name):#[('/39G0a/11S0c/15S0a/11S0d/11S0e/11S0f/11S0g/11S0h/11S0i/11S0j', 'newcomerCard')]
    con = conect.cursor()
    con.execute('SELECT Cards,CardsName FROM CardStore WHERE Name="%s"' %(name))
    get = con.fetchall()
    return get
def CardListName(name):#[('newcomerCard',)]
    con = conect.cursor()
    con.execute('SELECT CardsName FROM CardStore WHERE Name="%s"' %(name))
    get = con.fetchall()
    return get
def getCardListByNameADCN(name,cardN):
    con = conect.cursor()
    con.execute('SELECT Cards FROM CardStore WHERE Name="%s" AND CardsName="%s"' %(name,cardN))
    get = con.fetchone()
    return get
def deleteCardList(name,cardname):
    con = conect.cursor()
    con.execute('DELETE FROM CardStore WHERE Name="%s" AND CardsName="%s"'%(str(name),str(cardname)))
    conect.commit()
def successfulGame(name):
    con = conect.cursor()
    con.execute('SELECT CardsNameList FROM PlayerPassword WHERE Name="%s"' %(name))
    
    get = int(con.fetchall()[0][0])
    print(get)
    get+=3
    con.execute('UPDATE PlayerPassword SET CardsNameList="%s" WHERE Name="%s"'%(str(get),name))#UPDATE CardStore SET Cards='/39G0a/11S0c/15S0a/11S0d/11S0e/11S0f/11S0g/11S0h/11S0i/11S0j' WHERE id=1;
    conect.commit()
def failGame(name):
    con = conect.cursor()
    con.execute('SELECT CardsNameList FROM PlayerPassword WHERE Name="%s"' %(name))
    
    get = int(con.fetchall()[0][0])
    print(get)
    get-=1
    con.execute('UPDATE PlayerPassword SET CardsNameList="%s" WHERE Name="%s"'%(str(get),name))#UPDATE CardStore SET Cards='/39G0a/11S0c/15S0a/11S0d/11S0e/11S0f/11S0g/11S0h/11S0i/11S0j' WHERE id=1;
    conect.commit()
def GetScore(name):
    con = conect.cursor()
    con.execute('SELECT CardsNameList FROM PlayerPassword WHERE Name="%s"' %(name))
    get = str(con.fetchall()[0][0])
    return get