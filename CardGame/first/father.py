import numpy as np
import random
import math
import threading
import time
type=0
if type==0:
    import first.consumers as consumers
else:
    pass
#buff +?/+? -?/-? suckblood
typeGround=['w','bl','bk','r','g']

def getAllcost(cost):
    typegro=['w','bl','bk','r','g']
    arr=[0,0,0,0,0]
    for i in cost:
        arr[typegro.index(i)]+=1
    return np.array(arr)



class card:
    
    typeCard=''
    selectMode='' #[o[s[a,m,o],a[a,m,o]]]
    #def wantUse():
        #pass
    buffNar=None
    def __init__(self) -> None:
        self.cost=[]
        self.allCost=0
    def whenCheck(self,Master,OpMaster=None):#when card is used use this function
        arrM=np.array(Master.termGround)
        print(arrM)
        arrC=getAllcost(self.Rcost(Master,OpMaster))
        arrD=arrM-arrC
        print(arrD)
        for i in arrD:
            if i<0: 
                return False
        lenA=self.allCost
        if lenA>0:
            for ii in range(len(arrD)):
                lenA-=arrD[ii]###
                if lenA>=0:
                    arrD[ii]=0
                else:
                    arrD[ii]=-lenA
                    Master.termGround=list(arrD)
                    return True
                if ii==len(arrD)-1 and lenA>0:
                    return False
        Master.termGround=list(arrD)
        return True

        
    def whenUse(self,MyMaster,Master):
        pass
    def select(self,MyMaster,mode,OpMaster):
        if (mode=='osm' and len(MyMaster.cardGround)!=0):
            MyMaster.OptionCard=self
            MyMaster.client.send(mode)
            MyMaster.selectMode=mode
        elif (mode=='oso' and len(OpMaster.cardGround)!=0):
            MyMaster.OptionCard=self
            MyMaster.client.send(mode)
            MyMaster.selectMode=mode
        elif (mode=='osa' and (len(OpMaster.cardGround)!=0 or len(MyMaster.cardGround)!=0)):
            MyMaster.OptionCard=self
            MyMaster.client.send(mode)
            MyMaster.selectMode=mode
        elif(mode!='osm' and mode!='oso' and mode!='osa'):
            MyMaster.OptionCard=self
            MyMaster.client.send(mode)
            MyMaster.selectMode=mode
    def Rcost(self,MyMaster=None,Master=None):
        return self.cost

def getServentClass():
    class servent(card):
        live=0
        power=0 #0/0
        sleep=True
        haveAttack=False#这个回合有没有攻击过

        wantAttack=False #if it want attack

        name=''
        narrate=''
        typeCard='servent'

        

        funBackUp=None#store function
        def __init__(self) -> None:
            super().__init__()
            self.buff=[]#[a,b]a: p(power)|L(live)  b:number
            self.iniLive=self.live
            self.iniPower=self.power#initinal live and power
        
        def Rlive(self,MyMaster=None,Master=None):
            record=int(self.live)
            for i in self.buff:
                if i.buffName=='body':
                    for buf in i.buffType:

                        record+=buf[1] if buf[0]=='l' else 0
            return record
        def Rpower(self,MyMaster=None,Master=None):
            record=int(self.power)
            for i in self.buff:
                if i.buffName=='body':
                    for buf in i.buffType:

                        record+=buf[1] if buf[0]=='p' else 0
            return record 


        def whenUse(self,MyMaster,Master):
            for buf in MyMaster.ring:
                self.buff.append(buf)
            if self.selectMode!='':
                self.select(MyMaster,self.selectMode,Master)
            else:
                self.ZhanHong(MyMaster,Master)
            MyMaster.cardGround.append(self)
            MyMaster.cardHand.pop(MyMaster.cardHand.index(self))
            ###  
            
            
        def ability(self,MyMaster,Master,selectIndex):
            self.ZhanHong(MyMaster,Master,selectIndex)
        def ZhanHong(self,MyMaster,Master,selectIndex=None):# when use servent the function is used
            pass
        def WangYu(self,MyMaster,Master): # when servent is die function is uesd
            pass
        def WhenBeAttack(self,MyMaster,Master,otherServent):# when serveny be attack use thus function 
            pass
        def WhenAttack(self,MyMaster,Master):
            pass
        def attackServent(self,MyMaster,Servent,Master):# when servent attack Master and other Servent is protect ,use this function
            Servent.WhenBeAttack(MyMaster,Master,self)
            self.CheckLive(MyMaster,Master)
            Servent.CheckLive(Master,MyMaster)
            if self in MyMaster.cardGround:
                Servent.live-=self.Rpower(MyMaster,Master)
                self.live-=Servent.Rpower(MyMaster,Master)
                
                if Servent.live<0:
                    Master.live+=Servent.Rlive(MyMaster,Master)
                if findBuff('toxic',Servent):
                    self.live=-99999
                if findBuff('toxic',self):
                    Servent.live=-99999
                print(findBuff('toxic',Servent),findBuff('toxic',self))
                
                self.CheckLive(MyMaster,Master)
                Servent.CheckLive(Master,MyMaster)
        def attackMaster(self,MyMaster,Master):# when servent attack Master and no Servent not protect , use this function
            Master.live-=self.Rpower(MyMaster,Master)
        #def protectMaster():
            #pass
        def CheckLive(self,MyMaster,Master): # when it is attacked  or attact use this function
            if self.live>self.iniLive:
                self.live=self.iniLive
            if self.power>self.iniPower:
                self.power=self.iniPower
            if self.Rlive(MyMaster,Master)<=0:
                self.WangYu(MyMaster,Master)
                MyMaster.cardGround.remove(self)
                MyMaster.tomb.append(self)
        def dieth(self,MyMaster,Master):
            MyMaster.cardGround.remove(self)
            MyMaster.tomb.append(self)
            self.whenSendData(MyMaster,Master)
            self.WangYu(MyMaster,Master)
        def whenSendData(self,MyMaster,Master):
            pass
        def whenTermFinish(self,MyMaster,Master):
            pass
    return servent

servent=getServentClass()

class magic(card):
    typeCard='magic'
    narrate=''
    def whenUse(self,MyMaster,Master):
        MyMaster.cardHand.pop(MyMaster.cardHand.index(self))
        if self.selectMode!='':
            self.select(MyMaster,self.selectMode,Master)
        else:
            self.ability(MyMaster,Master)

    def ability(self,MyMaster,Master,selectIndex=None):# when card is use ,use this function
        pass
'''  
class immediateMagic(card):
    typeCard='immediateMagic'
    narrate=''
    def whenUse(self,MyMaster,Master,object=None):
        MyMaster.cardHand.pop(MyMaster.cardHand.index(self))
        self.ability(MyMaster,Master,object=None)

    def ability(self,MyMaster,Master,object=None):# when card is use ,use this function
        pass
    '''  
class ground(card):
    typeCard='ground'
    narrate=''
    typeG=''
    def __init__(self):
        #self.typeG=typ
        super().__init__()
        self.cost=[]
    def whenUse(self,MyMaster,Master):
        MyMaster.cardHand.pop(MyMaster.cardHand.index(self))
        MyMaster.groundList[typeGround.index(self.typeG)]+=1
        MyMaster.termGround[typeGround.index(self.typeG)]+=1
    def whenCheck(self,Master,OpMaster=None):#when card is used use this function
        if Master.haveUseGround==False:
            Master.haveUseGround=True
            return True
        else:
            Master.client.send('syou have used ground in this term')
            return False
class shelter(card):
    typeCard='shelter'
    narrate=''

    buffNar=None#input buff narrate
    def whenUse(self,MyMaster,Master):
        self.buff=[]
        MyMaster.cardGround.append(self)
        MyMaster.cardHand.pop(MyMaster.cardHand.index(self))
        
        self.ability(MyMaster,Master)



class Master:
    live=35
    MyTerm=False
    client=None#client (self)
    ifProtect=''#是否开始进行防御
    
    OptionCard=None#有选择功能的牌
    selectMode=''
    #whenUseCard=[]#To make sure opponent my use special card
    
    haveUseGround=False

    def __init__(self,clie,name):
        self.clientName=name
        self.ring=[]#buff collect
        self.client=clie
        self.cardHand=list([])
        self.groundList=[10,10,10,10,10]#white blue black red green
        self.cardGround=[]
        self.cardStorage=[]
        self.tomb=[]#墓地
        self.termGround=self.groundList.copy()
        
    def whenStart(self):
        self.getCard(1)
    def whenOver(self):
        if len(self.cardHand)>7:
            self.loseCard(len(self.cardHand)-7)
    def loseCard(self,num):
        for i in range(num):
            pass
    def getCard(self,num):
        try:
            arr=[]
            for i in range(int(num)):
                ind=random.randint(0,len(self.cardStorage)-1)
                get=self.cardStorage[ind]
                self.cardHand.append(get)
                self.cardStorage.remove(get)
                arr.append(get)
            return arr
        except:
            return arr
            print('Cards empty')
    def sendServent(self,index):
        get=self.cardHand[index]
        self.cardGround.append(get)
        self.cardHand.remove(get)

def findBuff(name,servent):
    for i in servent.buff:
        if i.buffType==name:
            return True
    return False
class referee:
    allClock=0
    
    runTime=0 #each term clock
    timelimit=120
    playerTerm=''
    run=True

    attackCheck=False

    serventRegister=None

    def __init__(self,Master1,Master2) -> None:
        self.Master1=Master1
        self.Master2=Master2
    def gameOver():
        pass
    def firstStar(self,Master1,Master2):
        die=random.randint(0,1)
        print(Master1)
        if die==1:
            Master1.MyTerm=True
            Master2.MyTerm=False
        else:
            Master2.MyTerm=True
            Master1.MyTerm=False
        self.thread=threading.Thread(target=self.timePeriod,args=(Master1,Master2,))
        self.thread.start()
    def timePeriod(self,Master1,Master2):
        self.time1=time.time()
        while self.run:
            if time.time()-self.time1>1:
                
                self.runTime+=1
                self.allClock+=1
                self.time1=time.time()
                Master1.client.send('c'+str(121-self.runTime))
                Master2.client.send('c'+str(121-self.runTime))
                #print(self.runTime)
                if self.runTime>120:
                    self.whenPlayerFinsh(Master1,Master2)
                    


    def whenPlayerFinsh(self,Master1,Master2):
        self.runTime=0
        Master1.MyTerm=not(Master1.MyTerm)
        Master2.MyTerm=not(Master2.MyTerm)
        if Master1.MyTerm==True:
            for finish in Master2.cardGround:
                finish.whenTermFinish(Master2,Master1)
            Master1.getCard(1)
            for relieve in Master1.cardGround:
                relieve.sleep=False
                relieve.haveAttack=False
        else:
            for finish2 in Master1.cardGround:
                finish2.whenTermFinish(Master1,Master2)
            Master2.getCard(1)
            
            for relieve in Master2.cardGround:
                relieve.sleep=False
                relieve.haveAttack=False
        Master2.haveUseGround=False
        Master1.haveUseGround=False
        Master1.termGround=Master1.groundList.copy()
        Master2.termGround=Master2.groundList.copy()
        consumers.sendAllDataToPage(Master1,Master2)
        consumers.sendAllDataToPage(Master2,Master1)

    #def sendCard(self):
        #pass
    def checkAttack(self,attackServent=None,MyMaster=None,OpMaster=None,OpServentInd=None):
        if self.attackCheck==False:
            
            OpMaster.client.send('mo'+str(OpServentInd))
            MyMaster.client.send('mm'+str(OpServentInd))
            if len(OpMaster.cardGround)!=0:
                OpMaster.client.send('d')
                OpMaster.ifProtect='d'
            self.serventRegister=attackServent
            self.attackCheck=True
        else:
            self.startAttack(OpMaster,self.serventRegister,MyMaster,OpServentInd)
    def startAttack(self,MyMaster,servent,Master,index):#servent and be attacked master
        print(index)
        servent.WhenAttack(MyMaster,Master)
        if index[0]=='F':
            servent.attackMaster(MyMaster,Master)
        else:
            servent.attackServent(MyMaster,Master.cardGround[int(index[1:])],Master)#Mymaster anotherservant ,opmaster
        self.attackCheck=False
        self.serventRegister=None
        Master.ifProtect=''
        servent.haveAttack=True
        consumers.sendAllDataToPage(MyMaster,Master)
        consumers.sendAllDataToPage(Master,MyMaster)
