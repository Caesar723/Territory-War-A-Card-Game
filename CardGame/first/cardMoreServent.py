#from first.father import servent


typ=0
if typ==0:
    import first.father as father
    import first.Database as database
    import first.buff as buff

else:
    import father as father
    import Database as database
    import buff
import random
def findBuff(name,servent):
    for i in servent.buff:
        if i.buffType==name:
            return True
    return False
#print(father.servent.__bases__, dict(father.servent.__dict__))
def findBuff(name,servent):
    for i in servent.buff:
        if i.buffType==name:
            return True
    return False
def getRanGroundindex(arr):
    get=random.randint(0,4)
    if arr[get]!=0:
        return get
    else:
        return getRanGroundindex(arr)

def getAlldir(cla):
    num=dir(cla)
    for i in num:
        if i[0]!='_':
            print(i+":"+str(getattr(cla,i)))
    print()
   
servent=father.getServentClass()
class Caesar(servent):
    name="Caesar"
    live=888
    power=888
    narrate='身材好大！'
    def __init__(self) -> None:
        super().__init__()
        self.allCost=5
        self.buff=[]
class javas(servent):
    name="javas"
    narrate='每有一个随从该牌的法力消耗-1并获得+1+2'
    live=6
    power=6
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bk' for i in range(10)]
    def Rcost(self,MyMaster,Master):
        self.newF=self.cost.copy()
        for dele in Master.cardGround:
            try:
                self.newF.remove('g')
            except:pass
        for delet in MyMaster.cardGround:
            try:
                self.newF.remove('g')
            except:pass
        return self.newF
    def Rlive(self, MyMaster=None, Master=None):
        return super().Rlive()+len(Master.cardGround)*2+len(MyMaster.cardGround)*2


    def Rpower(self, MyMaster=None, Master=None):
        return super().Rpower()+len(Master.cardGround)+len(MyMaster.cardGround)
    def ZhanHong(self,MyMaster,Master):
        self.live+=len(Master.cardGround)*2+len(MyMaster.cardGround)*2
        self.power+=len(Master.cardGround)+len(MyMaster.cardGround)
        self.iniLive+=len(Master.cardGround)*2+len(MyMaster.cardGround)*2
        self.iniPower+=len(Master.cardGround)+len(MyMaster.cardGround)
        self.Rlive=super().Rlive
        self.Rpower=super().Rpower
        self.Rcost=super().Rcost

class jakey(servent):
    name="jakey"
    narrate='当将要被攻击时恢复所有血量'
    live=8
    power=5
    def __init__(self) -> None:
        super().__init__()
        self.allCost=5
    def WhenBeAttack(self, MyMaster, Master, otherServent):
        self.live=int(self.iniLive)
class rain(servent):
    name="rain"
    live=2
    power=3
    narrate='亡语:召唤6个代有剧毒的dio'
    def __init__(self) -> None:
        super().__init__()
        self.allCost=5
    def WangYu(self, MyMaster, Master):
        for i in range(6):
            MyMaster.cardGround.append(DioOfGPS())
class leo(servent):
    name="leo"
    live=2
    power=2
    narrate='亡语:消灭敌方所有随从'
    def __init__(self) -> None:
        super().__init__()
        self.allCost=6
    def WangYu(self, MyMaster, Master):
        for i in Master.cardGround:

            Master.cardGround.remove(i)
            Master.tomb.append(i)
class lily(servent):
    name="lily"
    live=6
    power=2
    narrate='战吼：使一个随从获得当要被攻击时先对攻击这造成其双倍的伤害'
    selectMode='osm'
    def __init__(self) -> None:
        super().__init__()
        self.allCost=4
        self.buff=[]
    def ZhanHong(self,MyMaster,Master,Role):
        Role.buff.append(buff.liliBuff())
        self.funBackUp=Role.WhenBeAttack
        Role.WhenBeAttack=self.anFun
    def anFun(self,MyMaster,Master,otherServent):
        self.funBackUp(MyMaster,Master,otherServent)
        otherServent.live-=otherServent.Rpower(MyMaster,Master)*2
class raymond(servent):
    name="raymond"
    live=5
    narrate="战吼：摧毁对方所有手牌。自己的攻击改为摧毁双方一个地"
    def __init__(self) -> None:
        super().__init__()
        self.allCost=4
    def ZhanHong(self,MyMaster,Master):
        Master.cardHand=[]
    def attackServent(self,MyMaster,Servent,Master):
        if MyMaster.groundList!=[0,0,0,0,0]:
            MyMaster.groundList[getRanGroundindex(MyMaster.groundList)]-=1
        if Master.groundList!=[0,0,0,0,0]:
            Master.groundList[getRanGroundindex(Master.groundList)]-=1
    def attackMaster(self,MyMaster,Master):
        if Master.groundList!=[0,0,0,0,0]:
            Master.groundList[getRanGroundindex(Master.groundList)]-=1
        if MyMaster.groundList!=[0,0,0,0,0]:
            MyMaster.groundList[getRanGroundindex(MyMaster.groundList)]-=1
class eli(servent):
    name='eli'
    live=9
    power=4
    narrate="当回合结束吸走敌方两点法力值"
    def __init__(self) -> None:
        super().__init__()
        self.allCost=4
    def whenTermFinish(self, MyMaster, Master):
        
        for i in range(2):
            arr=[]
            for ii in range(len(Master.groundList)):
                if Master.groundList[ii]>0:
                    arr.append(ii)
            if len(arr)!=0:
                ran=arr[random.randint(0,len(arr)-1)]
                Master.groundList[ran]-=1
                MyMaster.groundList[ran]+=1
class DioOfGPS(servent):
    name="DioOfGPS"
    live=2
    power=2
    narrate='Toxic'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['g','g']
        self.buff=[buff.toxic()]
class fish(servent):
    name="fish"
    live=1
    power=1
    def __init__(self) -> None:
        super().__init__()
        self.allCost=1
class WoofBaby(servent):
    name="WoofBaby"
    live=1
    power=1
    def __init__(self) -> None:
        super().__init__()
        self.allCost=1
class Spider(servent):
    name="Spider"
    live=1
    power=1
    def __init__(self) -> None:
        super().__init__()
        self.allCost=1
class SmallDemon(servent):
    name="SmallDemon"
    live=2
    power=2
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bk']
class Pirate(servent):
    name="Pirate"
    live=1
    power=2
    def __init__(self) -> None:
        super().__init__()
        self.cost=['r']
class Phantom(servent):
    name="Phantom"
    live=1
    power=1
    def __init__(self) -> None:
        super().__init__()
        self.cost=['g']
class SmallFire(servent):
    name="SmallFire"
    live=1
    power=2
    def __init__(self) -> None:
        super().__init__()
        self.cost=['r']
class Sapling(servent):
    name="Sapling"
    live=2
    power=2
    def __init__(self) -> None:
        super().__init__()
        self.cost=['g']
class Beetle(servent):
    name="Beetle"
    live=5
    power=1
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bl','bl','bl']
class squirrel(servent):
    name="squirrel"
    live=1
    power=1
    def __init__(self) -> None:
        super().__init__()
        self.cost=['g']
class Cthulhu(servent):
    name="Cthulhu"
    live=0
    power=0
    narrate='神秘且可怕'
    def __init__(self) -> None:
        super().__init__()
