
from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import random

typ=0
if typ==0:

    import first.father as father
    import first.Database as database
    import first.cardServent as S
    import first.cardMagic as M
    import first.cardGround as G
    import first.cardShelter as J
    import first.cardMoreServent as moreS
    
else:
    import father as father
    import Database as database
    import cardServent as S
    import cardMagic as M
    import cardGround as G
    import cardShelter as J
    import cardMoreServent as moreS


import numpy as np
import pandas as pd
import re
import threading
test=False
room=[]
smallroom=[]#max 2people
servicePath='/testdjangoproject/django/sco/first/'
def newcomer():
    a=''
    
    for i in range(4):
        a += "/SDoctor"
    return a
def encodeCard(text):#/Catagory+Name
    inde = ['S', 'M', 'G', 'J']
    catagoryCard = []
    fileName = ["ServantCsv", "MagicCsv", "GroundCsv", "ShelterCsv"]

    for i in fileName:
        csv = pd.read_csv(((servicePath) if test==True else'/Users/chenxuanpei/PycharmProjects/CardGame/first/')+i + ".csv")
        catagoryCard.append(csv)
    eac=text.split("/")
    eac.remove("")
    print(eac[0][1:])
    encode=[]
    for ii in eac:
        encode.append(foundCard(ii,inde,catagoryCard))
    encodeText=''
    for iii in decomposs(encode):
        encodeText+="/"+iii
    return encodeText
def decomposs(arr,num=0):
    print(arr)
    count=1
    get=arr
    delete=[]
    if num!=len(arr):
        for i in range(num+1,len(get)):
            #print(i,len(get))
            if get[num]==get[i]:
                count+=1
                delete.append(i)
        for ii in delete[::-1]:
            get.pop(ii)
        get[num]=str(count)+get[num]
        return decomposs(get,num+1)
    else:
        return get

def foundCard(name,inde,catagoryCard):
    for col in [chr(i) for i in range(97,123)]:
        for row in range(len(catagoryCard[inde.index(name[0])][col])):
            if name[1:]==catagoryCard[inde.index(name[0])][col][row]:
                return name[0]+str(row)+col
    return None
def getCardList(encode):#/Number+Catagory+Number+(a~z) 个数 种类 第几行 第几列
    inde=['S','M','G','J']
    catagoryCard=[]
    fileName = ["ServantCsv", "MagicCsv", "GroundCsv", "ShelterCsv"]
    CardList=[]
    for i in fileName:
        csv = pd.read_csv(((servicePath) if test==True else'/Users/chenxuanpei/PycharmProjects/CardGame/first/')+i + ".csv")
        catagoryCard.append(csv)
    encode1=encode.split("/")
    encode1.remove('')
    for iii in encode1:

        ree=re.compile(r'\d+')
        splitStr=ree.findall(iii)[0]
        ii=iii[len(splitStr):]
        print(ii)
        #ii.remove(splitStr)
        for encode2 in range(int(splitStr)):

            CardList.append(eval(ii[0]+'.'+catagoryCard[inde.index(ii[0])][ii[2]][int(ii[1])]+'()'))
    return CardList
def decode(tex):
    inde=['S','M','G','J']
    catagoryCard=[]
    string=''
    fileName = ["ServantCsv", "MagicCsv", "GroundCsv", "ShelterCsv"]
    CardList=[]
    for i in fileName:
        csv = pd.read_csv(((servicePath) if test==True else'/Users/chenxuanpei/PycharmProjects/CardGame/first/')+i + ".csv")
        catagoryCard.append(csv)
    encode1=tex.split("/")
    encode1.remove('')
    for iii in encode1:
        ree=re.compile(r'\d+')
        splitStr=ree.findall(iii)[0]
        ii=iii[len(splitStr):]
        print(ii)
        #ii.remove(splitStr)
        for encode2 in range(int(splitStr)):
            string+='/'+ii[0]+catagoryCard[inde.index(ii[0])][ii[2]][int(ii[1])]
    return string
def reSetCsvFile():#将所有卡牌类型的名字写在csv文件里
    createCsv()
    getNC=re.compile(r"\.\w+'")
    AllCards=[father.servent.__subclasses__(),father.magic.__subclasses__(),father.ground.__subclasses__(),father.shelter.__subclasses__()]
    fileName=["ServantCsv","MagicCsv","GroundCsv","ShelterCsv"]
    for category in AllCards:
        #print(category)
        for i in range(len(category)):
            #print(i)
            addCardNameIntoCsv(getNC.findall(str(category[i]))[0].replace(".","").replace("'",""),fileName[AllCards.index(category)])
def createCsv():
    df=pd.DataFrame(columns=[chr(i) for i in range(97,123)])
    for i in ["ServantCsv","MagicCsv","GroundCsv","ShelterCsv"]:
        df.to_csv(((servicePath) if test==True else'/Users/chenxuanpei/PycharmProjects/CardGame/first/')+i+".csv")
def judgeIndex(csv,num=97):
    ch=chr(num)
    if True in list(pd.isnull(csv[ch])):
        #csv=csv.append([{'a':np.nan}],ignore_index=True)
        return csv,(ch)
    elif ch=='z':
        csv=csv.append([{'a':np.nan}],ignore_index=False)
        return csv,'a'
    else:
        return judgeIndex(csv,num+1)

def addCardNameIntoCsv(name,fileName):
    csv = pd.read_csv(((servicePath) if test==True else'/Users/chenxuanpei/PycharmProjects/CardGame/first/')+fileName+".csv")

    csv, index = judgeIndex(csv)
    #print(csv)
    csv[index]=csv[index].replace(np.NAN,name)
    csv.to_csv(((servicePath) if test==True else'/Users/chenxuanpei/PycharmProjects/CardGame/first/')+fileName+".csv",index=False)
def addPlayerOnce(name,password):
    newcomerCard=encodeCard(newcomer())

    #print(csv)
    database.addPlayer(name,password,"0")
    database.addCard(name,"newcomerCard",newcomerCard)
    #print(csv["b"][0]==csv["b"][0])
    #print(True in list(pd.isnull(csv["b"])))

def fondMaster(selfname):
    for i in room:
        for ii in range(2):
            print(i[ii][1])
            if i[ii][1]==selfname:
                return i[ii][0]
    print(selfname)
    return False
def fondReferee(self):
    for i in room:
        for ii in range(2):
            if i[ii][0].client==self:
                return i[2]
def fondMastersBySelf(self):
    for i in room:
        for ii in range(2):
            if i[ii][0].client==self:
                return i[ii][0],i[int(not(ii))][0]
def getCardNarrate(card):
    na=[card.typeCard,card.narrate,str(len(card.cost))+'@']+([card.live,card.power]) if card.typeCard=='servent' else []
    return na
def fondRoomByMaster(Master):
    for i in room:
        for ii in range(2):
            if i[ii][0]==Master:
                print(i)
                return room.index(i)

def sendAllDataToPage(MyMaster,OpMaster):
    #thread=threading.Thread(target=threadSend,args=(MyMaster,OpMaster))
    #thread.start()
    threadSend(MyMaster,OpMaster)
def threadSend(MyMaster,OpMaster):

    for ckeckM in MyMaster.cardGround.copy():
        ckeckM.whenSendData(MyMaster,OpMaster)
        ckeckM.CheckLive(MyMaster,OpMaster)
    for ckeckO in OpMaster.cardGround.copy():
        ckeckO.whenSendData(OpMaster,MyMaster)
        ckeckO.CheckLive(OpMaster,MyMaster)
    if len(MyMaster.cardGround)>9:
        for i in range(len(MyMaster.cardGround)-9):
            MyMaster.client.send("s随从被吞噬："+MyMaster.cardGround[len(MyMaster.cardGround)-1].name)
            OpMaster.client.send("s敌方随从被吞噬："+MyMaster.cardGround[len(MyMaster.cardGround)-1].name)
            MyMaster.cardGround.pop()
            
    if len(OpMaster.cardGround)>9:
        for i in range(len(OpMaster.cardGround)-9):
            MyMaster.client.send("s敌方随从被吞噬："+MyMaster.cardGround[len(MyMaster.cardGround)-1-i].name)
            OpMaster.client.send("s随从被吞噬："+MyMaster.cardGround[len(MyMaster.cardGround)-1-i].name)
            OpMaster.cardGround.pop()
    
    
    
    myCardHand='Mh'
    myCardGround='Mg'
    myLive='Mm'
    myFee='Mf'
    myTomb='Mt'
    myStorage='Ms'
    myProtect=MyMaster.ifProtect

    OpCardHand='Oh'
    OpCardGround='Og'
    OpLive='Om'
    OpFee='Of'
    OpTomb='Ot'
    OpStorage='Os'
    
    CanIDo='Mc'#T|F

    
    for mh in MyMaster.cardHand:
        text=''
        for tex in range(len(mh.Rcost(MyMaster,OpMaster))):
            text+=str(mh.Rcost(MyMaster,OpMaster)[tex])+('-' if tex!=len(mh.Rcost(MyMaster,OpMaster))-1 else '')
        myCardHand+=mh.typeCard+(('_'+mh.name+'_'+mh.narrate+'_'+str(mh.Rpower(MyMaster,OpMaster))+'_'+str(mh.Rlive(MyMaster,OpMaster))+'_'+text+'_'+str(mh.allCost)+'/') if mh.typeCard=='servent' else ('_'+mh.name+'_'+mh.narrate+'_'+'_'+'_'+text+'_'+str(mh.allCost)+'/'))
    for mg in MyMaster.cardGround:
        text=''
        for tex in range(len(mg.Rcost(MyMaster,OpMaster))):
            text+=str(mg.Rcost(MyMaster,OpMaster)[tex])+('-' if tex!=len(mg.Rcost(MyMaster,OpMaster))-1 else '')
        buff=''
        for buf in mg.buff:
            buff+=((str(buf.Name)+'+'+str(buf.buffType[0][1])+'+'+str(buf.buffType[1][1])) if buf.buffName=='body' else buf.buffType)+('~' if buf!=mg.buff[len(mg.buff)-1] else '')
        myCardGround+=mg.typeCard+(('_'+mg.name+'_'+mg.narrate+'_'+str(mg.Rpower(MyMaster,OpMaster))+'_'+str(mg.Rlive(MyMaster,OpMaster))+'_'+text+'_'+str(mg.allCost)+'_'+buff+'/') if mg.typeCard=='servent' else ('_'+mg.name+'_'+mg.narrate+'_'+'_'+'_'+text+'_'+str(mh.allCost)+'/'))
    myLive+=str(MyMaster.live)
    for mfee in range(len(MyMaster.termGround)):
        myFee+=str(MyMaster.termGround[mfee])+(("-") if mfee!=len(MyMaster.termGround)-1 else'')
    for mtomb in MyMaster.tomb:
        myTomb+=mtomb.name
    myStorage+=str(len(MyMaster.cardStorage))

    OpCardHand+=str(len(OpMaster.cardHand))
    for og in OpMaster.cardGround:
        text=''
        for tex in range(len(og.Rcost(MyMaster,OpMaster))):
            text+=str(og.Rcost(MyMaster,OpMaster)[tex])+('-' if tex!=len(og.Rcost(MyMaster,OpMaster))-1 else '')
        buff=''
        for buf in og.buff:
            buff+=((str(buf.Name)+'+'+str(buf.buffType[0][1])+'+'+str(buf.buffType[1][1])) if buf.buffName=='body' else buf.buffType)+('~' if buf!=og.buff[len(og.buff)-1] else '')
        OpCardGround+=og.typeCard+(('_'+og.name+'_'+og.narrate+'_'+str(og.Rpower(MyMaster,OpMaster))+'_'+str(og.Rlive(MyMaster,OpMaster))+'_'+text+'_'+str(og.allCost)+'_'+buff+'/') if og.typeCard=='servent' else '/')
    for ofee in range(len(OpMaster.termGround)):
        OpFee+=str(OpMaster.termGround[ofee])+(("-") if ofee!=len(OpMaster.termGround)-1 else'')
    OpLive+=str(OpMaster.live)
    for otomb in OpMaster.tomb:
        OpTomb+=otomb.name
    OpStorage+=str(len(OpMaster.cardStorage))

    CanIDo+='F' if MyMaster.MyTerm==False else'T'
    sendAll=[CanIDo,myFee,myCardHand,myCardGround,myLive,myTomb,myStorage,OpFee,OpCardHand,OpCardGround,OpLive,OpTomb,myProtect]
    for send in sendAll:
        MyMaster.client.send(send)
    MyMaster.client.send(MyMaster.selectMode)
    if MyMaster.live<=0:#lose game
        MyMaster.client.send('gl')
        OpMaster.client.send('gw')
        try:
            room.pop(fondRoomByMaster(MyMaster))
            database.successfulGame(OpMaster.clientName)
            database.failGame(MyMaster.clientName)
        except:
            pass
    '''
    if OpMaster.live<=0:
        MyMaster.client.send('gw')
        OpMaster.client.send('gl')
        room.pop(fondRoomByMaster(MyMaster))
    '''
def furtherSend(self):
    Master1,Master2=fondMastersBySelf(self)
    sendAllDataToPage(Master1,Master2)
def furfurSend(self):
    Master1,Master2=fondMastersBySelf(self)
    sendAllDataToPage(Master1,Master2)
    sendAllDataToPage(Master2,Master1)
def threadReceive(self,message):
    global smallroom,room
        
    self.send("response")
    #print(message)
    if message['text'][0]=='p':
        print(type(self))
        name=message['text'][1:].split('_')
        peivacy=['4742bsxgv','zhouchen','leol229','zouchunxi','AnyingMAO','caesar','TangYa','201794228']#cards designed by classmate
        #cards=[moreS.jakey(),moreS.raymond(),moreS.leo(),moreS.eli(),moreS.javas()]
        if len(smallroom)!=0 and name[0] == smallroom[0][1]:
            smallroom=[]
        
        checkMaster=fondMaster(name[0])
        if checkMaster==False:
            getMaster=father.Master(self,name[0])
            #print(database.getCardListByNameADCN(name[0],name[1]))
            getMaster.cardStorage=getCardList(name[1])#database.getCardListByNameADCN(name[0],name[1])[0])
            if name[0] in peivacy:
                cards=[moreS.jakey(),moreS.raymond(),moreS.leo(),moreS.eli(),moreS.javas(),moreS.Caesar(),moreS.lily(),moreS.rain()]
                getMaster.cardStorage.append(cards[peivacy.index(name[0])])
            #test
            getMaster.getCard(4)
            #database.successfulGame(name[0])
            #
            smallroom.append([getMaster,name[0]])
            if len(smallroom)==2:
                smallroom.append(father.referee(smallroom[0][0],smallroom[1][0]))
                room.append(smallroom)
                room[len(room)-1][2].firstStar(room[len(room)-1][2].Master1,room[len(room)-1][2].Master2)
                sendAllDataToPage(smallroom[0][0],smallroom[1][0])
                sendAllDataToPage(smallroom[1][0],smallroom[0][0])
                smallroom=[]
            #print(getMaster.cardStorage)
        else:
            print('change')
            checkMaster.client=self
            furtherSend(self)


    elif message['text'][0]=='a':
        if (fondMastersBySelf(self)[0].MyTerm==True):
            refer=fondReferee(self)
            if refer.serventRegister==None:
                MyMaster,OpMaster=fondMastersBySelf(self)
                index=int(message['text'][1:])
                if MyMaster.cardGround[index].haveAttack!=True and MyMaster.cardGround[index].sleep==False:
                    refer.checkAttack(MyMaster.cardGround[index],MyMaster,OpMaster,index)
                    if (len(OpMaster.cardGround)==0):
                        refer.checkAttack(None,OpMaster,MyMaster,'F')
        


    elif message['text'][0]=='s':
        MYMaster,OPMaster=fondMastersBySelf(self)
        if message['text'][1]=='S' and MYMaster.OptionCard!=None:
            if message['text'][2]=='O':
                print(message['text'][3:])
                MYMaster,OPMaster=fondMastersBySelf(self)
                MYMaster.OptionCard.ability(MYMaster,OPMaster,OPMaster.cardGround[int(message['text'][3:])])
                MYMaster.selectMode=''
                MYMaster.client.send("s选择："+OPMaster.cardGround[int(message['text'][3:])].name)
                OPMaster.client.send("s对手选择："+OPMaster.cardGround[int(message['text'][3:])].name)
                
            elif message['text'][2]=='M':
                MYMaster,OPMaster=fondMastersBySelf(self)
                MYMaster.OptionCard.ability(MYMaster,OPMaster,MYMaster.cardGround[int(message['text'][3:])])
                MYMaster.selectMode=''
                MYMaster.client.send("s选择："+MYMaster.cardGround[int(message['text'][3:])].name)
                OPMaster.client.send("s对手选择："+MYMaster.cardGround[int(message['text'][3:])].name)
        

        elif message['text'][1]=='M' and MYMaster.OptionCard!=None:
            if message['text'][2]=='O':
                print(message['text'][3:])
                MYMaster,OPMaster=fondMastersBySelf(self)
                MYMaster.OptionCard.ability(MYMaster,OPMaster,OPMaster)
                MYMaster.selectMode=''
                MYMaster.client.send("s选择：敌方英雄")
                OPMaster.client.send("s对手选择：我方英雄")
                
            elif message['text'][2]=='M':
                MYMaster,OPMaster=fondMastersBySelf(self)
                MYMaster.OptionCard.ability(MYMaster,OPMaster,MYMaster)
                MYMaster.selectMode=''
                MYMaster.client.send("s选择：我方英雄")
                OPMaster.client.send("s对手选择：敌方英雄")
        MYMaster.OptionCard=None
        furfurSend(self)
    elif message['text'][0]=='d':
        if (fondMastersBySelf(self)[0].MyTerm==False):
            refer=fondReferee(self)
            if refer.serventRegister!=None:
                MyMaster,OpMaster=fondMastersBySelf(self)
                index=message['text'][1:]
                refer.checkAttack(None,MyMaster,OpMaster,index)
        

    elif message['text'][0]=='f':
        if (fondMastersBySelf(self)[0].MyTerm==True):
            refer=fondReferee(self)
            MyMaster,OpMaster=fondMastersBySelf(self)
            cardWhenUse=MyMaster.cardHand[int(message['text'][1:])]
            if cardWhenUse.whenCheck(MyMaster,OpMaster)==True:
                print('startuse')
                cardWhenUse.whenUse(MyMaster,OpMaster)
                text=''
                for tex in range(len(cardWhenUse.Rcost(MyMaster,OpMaster))):
                    text+=str(cardWhenUse.Rcost(MyMaster,OpMaster)[tex])+('-' if tex!=len(cardWhenUse.Rcost(MyMaster,OpMaster))-1 else '')


                MyMaster.client.send("u"+cardWhenUse.typeCard+(('_'+cardWhenUse.name+'_'+cardWhenUse.narrate+'_'+str(cardWhenUse.Rpower(MyMaster,OpMaster))+'_'+str(cardWhenUse.Rlive(MyMaster,OpMaster))+'_'+text+'_'+str(cardWhenUse.allCost)+'/') if cardWhenUse.typeCard=='servent' else ('_'+cardWhenUse.name+'_'+cardWhenUse.narrate+'_'+'_'+'_'+text+'_'+str(cardWhenUse.allCost))))
                OpMaster.client.send("u"+cardWhenUse.typeCard+(('_'+cardWhenUse.name+'_'+cardWhenUse.narrate+'_'+str(cardWhenUse.Rpower(MyMaster,OpMaster))+'_'+str(cardWhenUse.Rlive(MyMaster,OpMaster))+'_'+text+'_'+str(cardWhenUse.allCost)+'/') if cardWhenUse.typeCard=='servent' else ('_'+cardWhenUse.name+'_'+cardWhenUse.narrate+'_'+'_'+'_'+text+'_'+str(cardWhenUse.allCost))))
                MyMaster.client.send("s打出："+cardWhenUse.name)
                OpMaster.client.send("s对手打出："+cardWhenUse.name)
            else:
                MyMaster.client.send("s没有足够的法力值")
            furfurSend(self)
    elif message['text'][0]=='e':
        if (fondMastersBySelf(self)[0].MyTerm==True):
            refer=fondReferee(self)
            if refer.serventRegister==None:
                refer.whenPlayerFinsh(refer.Master1,refer.Master2)
    elif message['text'][0]=='c':
        MyMaster,OpMaster=fondMastersBySelf(self)
        MyMaster.client.send('gl')
        OpMaster.client.send('gw')
        room.pop(fondRoomByMaster(MyMaster))
        database.successfulGame(OpMaster.clientName)
        database.failGame(MyMaster.clientName)
class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self,message):
        global smallroom
        self.accept()

        #self.send("first")
    '''
    开头字母
    p:player名字，
    a：攻击+索引，
    s:选择+ (位置+索引)[哪个随从发起的]+（M|S)[自己或随从]+(M|O)[敌人或自己]+索引，
    f:召唤+索引[手牌]，
    d:防御+T|F+索引
    e:end
    r(response):T|F
    c:投降capitulate
    '''
    def websocket_receive(self,message):
        receive=threading.Thread(target=(threadReceive),args=(self,message))
        receive.start()
    def websocket_disconnect(self,message):
        
        raise StopConsumer()


reSetCsvFile()
