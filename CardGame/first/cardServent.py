
typ=0
if typ==0:
    import first.father as father
    import first.Database as database
    import first.buff as buff
    import first.cardMoreServent as moreS
    import first.cardMoreServent
    import first.cardServent
else:
    import father as father
    import Database as database
    import buff
    import cardMoreServent as moreS
import random
import copy
import re
def selectCards(ty,storage):
    arr=[]
    for i in storage:
        if i.typeCard==ty:
            arr.append(i)
    return (arr[random.randint(0,len(arr)-1)]) if len(arr)!=0 else False
class Crocodile(father.servent):
    name="Crocodile"
    live=3
    power=2
    narrate='超模'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['g','g']
        self.buff=[]
class Doctor(father.servent):
    name="Doctor"
    live=1
    power=2
    narrate='战吼：使一个角色恢复两点生命'
    selectMode='oaa'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['g','g']
        self.buff=[]
    def ZhanHong(self,MyMaster,Master,Role):
        Role.live+=2 
class SuccessFlag(father.servent):
    name="SuccessFlag"
    narrate='使我方随从+1+1'
    live=3
    power=0
    def __init__(self) -> None:
        super().__init__()
        self.allCost=4
        self.buffNar=buff.successFlag()
    def whenSendData(self, MyMaster, Master):
        for i in MyMaster.cardGround:
            try:
                i.buff.remove(self.buffNar)
            except:pass
            try:
                if i!=self and self in MyMaster.cardGround:
                    i.buff.append(self.buffNar)
            except:pass
        for ii in Master.cardGround:
            try:
                ii.buff.remove(self.buffNar)
            except:pass
    def WangYu(self,MyMaster,Master):
        for i in MyMaster.cardGround:
            try:
                i.buff.remove(self.buffNar)
            except:
                pass
        try:
            MyMaster.ring.remove(self.buffNar)
        except:
            pass

class FishLeader(father.servent):
    name='FishLeader'
    live=1
    power=2
    narrate="战吼:召唤一条鱼"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['g' for i in range(2)]
    def ZhanHong(self,MyMaster,Master):
        MyMaster.cardGround.append(moreS.fish())
class WoofGroup(father.servent):
    name='WoofGroup'
    live=2
    power=2
    narrate="战吼:召唤2个1-1的狼宝宝"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['g' for i in range(3)]
    def ZhanHong(self,MyMaster,Master):
        MyMaster.cardGround.append(moreS.WoofBaby())
        MyMaster.cardGround.append(moreS.WoofBaby())
class FireLeader(father.servent):
    name='FireLeader'
    live=5
    power=3
    sleep=False
    narrate="冲锋 超杀：获得被击杀的随从的初始属性值"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['r' for i in range(4)]
        self.allCost=2
    def attackServent(self,MyMaster,Servent,Master):# when servent attack Master and other Servent is protect ,use this function
            Servent.WhenBeAttack(MyMaster,Master,self)
            self.CheckLive(MyMaster,Master)
            Servent.CheckLive(Master,MyMaster)
            if self in MyMaster.cardGround:
                Servent.live-=self.Rpower(MyMaster,Master)
                self.live-=Servent.Rpower(MyMaster,Master)
                
                if Servent.live<0:
                    Master.live+=Servent.Rlive(MyMaster,Master)
                    self.live+=Servent.iniLive
                    self.power+=Servent.iniPower
                    self.iniLive+=Servent.iniLive
                    self.iniPower+=Servent.iniPower
                if findBuff('toxic',Servent):
                    self.live=-99999
                if findBuff('toxic',self):
                    Servent.live=-99999
                print(findBuff('toxic',Servent),findBuff('toxic',self))
                
                self.CheckLive(MyMaster,Master)
                Servent.CheckLive(Master,MyMaster)
class BraveFireMan(father.servent):
    name='BraveFireMan'
    live=6
    power=3
    narrate="战吼:对其自身造成3点伤害"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bk' for i in range(2)]
        self.allCost=1
    def ZhanHong(self,MyMaster,Master):
        self.live-=3
class WolfRider(father.servent):
    name='WolfRider'
    live=1
    power=3
    sleep=False
    narrate="冲锋"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['r' for i in range(1)]
        self.allCost=2
class General(father.servent):
    name='General'
    live=2
    power=2
    narrate="其周围的随从+1+1"

    def __init__(self) -> None:
        super().__init__()
        self.allCost=2
        self.cost=['g']
        self.buffNar=buff.General()
    def whenSendData(self, MyMaster, Master):
        for i in range(len(MyMaster.cardGround)):
            try:
                MyMaster.cardGround[i].buff.remove(self.buffNar)
            except:pass
            try:
                if i!=0 and MyMaster.cardGround[i-1]==self:
                    MyMaster.cardGround[i].buff.append(self.buffNar)
                if MyMaster.cardGround[i+1]==self:
                    MyMaster.cardGround[i].buff.append(self.buffNar)
            except:pass
        for ii in Master.cardGround:
            try:
                ii.buff.remove(self.buffNar)
            except:pass
class MegaDemon(father.servent):
    name='MegaDemon'
    live=8
    power=8

    def __init__(self) -> None:
        super().__init__()
        self.allCost=1
        self.cost=['bk' for i in range(5)]
    
class FrozenGiant(father.servent):
    name='FrozenGiant'
    live=5
    power=4

    def __init__(self) -> None:
        super().__init__()
        self.allCost=4
class AncientDemon(father.servent):
    name='AncientDemon'
    live=6
    power=6
    narrate="对你的英雄造成4点伤害，并抽一张牌"
    def __init__(self) -> None:
        super().__init__()
        self.allCost=1
        self.cost=['bk' for i in range(3)]
    def ZhanHong(self,MyMaster,Master):
        MyMaster.live-=4
        MyMaster.getCard(1)
class Pope(father.servent):
    name='Pope'
    live=4
    power=4
    selectMode='oaa'
    narrate="战吼：使一个角色恢复3点生命"
    def __init__(self) -> None:
        super().__init__()
        self.allCost=2
        self.cost=['w' for i in range(2)]
    def ZhanHong(self,MyMaster,Master,Role):
        Role.live+=3
class HellDog(father.servent):
    name='HellDog'
    live=2
    power=4
    selectMode='osa'
    narrate="战吼：对一个随从造成2点伤害"
    def __init__(self) -> None:
        super().__init__()
        self.allCost=1
        self.cost=['r' for i in range(2)]
    def ZhanHong(self,MyMaster,Master,Role):
        Role.live-=2

class CrazyScientist(father.servent):
    name='CrazyScientist'
    live=1
    power=2
    narrate="战吼：对所有随从造成2点伤害，如果死亡，则抽一张牌"
    def __init__(self) -> None:
        super().__init__()
        self.allCost=1
        self.cost=['bk' for i in range(4)]
    def ZhanHong(self,MyMaster,Master):
        for i in MyMaster.cardGround:
            i.live-=2
            if i.Rlive()<=0:
                MyMaster.getCard(1)
        for ii in Master.cardGround:
            ii.live-=2
            if ii.Rlive()<=0:
                MyMaster.getCard(1)
class CatastropheDemon(father.servent):
    name='CatastropheDemon'
    live=6
    power=6
    selectMode='osm'
    narrate="战吼：吃掉一个随从作为召唤它的条件"
    def __init__(self) -> None:
        super().__init__()
        self.allCost=1
        self.cost=['bk' for i in range(3)]
    def ZhanHong(self,MyMaster,Master,Role):
        Role.dieth(MyMaster,Master)
class SpiderMoM(father.servent):
    name='SpiderMoM'
    live=2
    power=1
    narrate="亡语:召唤两个1-1的小蜘蛛"
    def __init__(self) -> None:
        super().__init__()
        self.allCost=3
       
    def WangYu(self,MyMaster,Master):
        MyMaster.cardGround.append(moreS.Spider())
        MyMaster.cardGround.append(moreS.Spider())
class LivingSacrifice(father.servent):
    name='LivingSacrifice'
    live=1
    power=0
    narrate="亡语:召唤1个2-2的小恶魔"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bk']
    def WangYu(self,MyMaster,Master):
        MyMaster.cardGround.append(moreS.SmallDemon())
class UndeadMerchant(father.servent):
    name='UndeadMerchant'
    live=5
    power=3
    narrate="战吼：对你的英雄造成3点伤害"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bk' for i in range(2)]
    def ZhanHong(self,MyMaster,Master):
        MyMaster.live-=3
class DemonMaster(father.servent):
    name='DemonMaster'
    live=7
    power=5
    narrate="亡语:召唤两个3-5的不死商人"
    def __init__(self) -> None:
        super().__init__()
        self.allCost=1
        self.cost=['bk' for i in range(7)]
    def WangYu(self,MyMaster,Master):
        MyMaster.cardGround.append(UndeadMerchant())
        MyMaster.cardGround.append(UndeadMerchant())
class DemonSwallower(father.servent):
    name='DemonSwallower'
    live=2
    power=2
    narrate="战吼：随机弃掉你手牌的一张牌，并获得其法力值作为该随从的属性值"
    def __init__(self) -> None:
        super().__init__()
        self.allCost=2
        self.cost=['bk' for i in range(2)]
    def ZhanHong(self,MyMaster,Master):
        if len(MyMaster.cardHand)!=0:
            get=MyMaster.cardHand[random.randint(0,len(MyMaster.cardHand)-1)]
            self.iniPower+=get.allCost+len(get.Rcost(MyMaster,Master))
            self.iniLive+=get.allCost+len(get.Rcost(MyMaster,Master))
            self.live+=get.allCost+len(get.Rcost(MyMaster,Master))
            self.power+=get.allCost+len(get.Rcost(MyMaster,Master))
            MyMaster.cardHand.remove(get)
class LavaFury(father.servent):
    name='LavaFury'
    live=1
    power=5
    def __init__(self) -> None:
        super().__init__()
        self.allCost=1
        self.cost=['r' for i in range(2)]
class CrazyBusinessman(father.servent):
    name='CrazyBusinessman'
    live=2
    power=3
    narrate="战吼：抽一张牌"
    def __init__(self) -> None:
        super().__init__()
        self.allCost=2
        self.cost=['r']
    def ZhanHong(self,MyMaster,Master):
        MyMaster.getCard(1)
class MysteriousPirate(father.servent):
    name='MysteriousPirate'
    live=1
    power=3
    narrate="战吼：召唤两个2-1的海盗"
    def __init__(self) -> None:
        super().__init__()
        
        self.cost=['r' for i in range(3)]
    def ZhanHong(self,MyMaster,Master):
        MyMaster.cardGround.append(moreS.Pirate())
        MyMaster.cardGround.append(moreS.Pirate())
class DragonCub(father.servent):
    name='DragonCub'
    live=3
    power=2
    narrate="战吼：如果你的场上没有随从，+3攻击力"
    def __init__(self) -> None:
        super().__init__()
        
        self.cost=['r' for i in range(2)]
    def ZhanHong(self,MyMaster,Master):
        if len(MyMaster.cardGround)==0:
            self.power+=3
            self.iniPower+=3
class CrazyInstructor(father.servent):
    name='CrazyInstructor'
    live=1
    power=1
    narrate="战吼：你所有的随从+1攻击"
    def __init__(self) -> None:
        super().__init__()
        self.allCost=1
        self.cost=['r']
        self.buffNar=buff.CrazyInstructor()

    def ZhanHong(self,MyMaster,Master):
        for i in MyMaster.cardGround:
            i.buff.append(self.buffNar)
class DarkenSword(father.servent):
    name='DarkenSword'
    live=2
    power=9
    narrate="冲锋"
    sleep=False
    def __init__(self) -> None:
        super().__init__()
        self.cost=['r' for i in range(8)]
class Horticulturist(father.servent):
    name='Horticulturist'
    live=1
    power=1
    narrate="战吼：召唤2个2-2树苗"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['g' for i in range(2)]
        self.allCost=1
    def ZhanHong(self,MyMaster,Master):
        MyMaster.cardGround.append(moreS.Sapling())
        MyMaster.cardGround.append(moreS.Sapling())
class SquirrelMom(father.servent):
    name='SquirrelMom'
    live=1
    power=1
    narrate="战吼:将两张1-1松鼠置入你的手牌"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['g']
    def ZhanHong(self,MyMaster,Master):
        MyMaster.cardHand.append(moreS.squirrel())
        MyMaster.cardHand.append(moreS.squirrel())
class ForestGiants(father.servent):
    name='ForestGiants'
    live=7
    power=7
    narrate="场上每有友方随从，该牌的法力减1"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['g' for i in range(11)]
    def Rcost(self,MyMaster=None,Master=None):
        arr=self.cost.copy()
        for i in MyMaster.cardGround:
            arr.pop()
        return arr
    def ZhanHong(self,MyMaster,Master):
        self.Rcost=super().Rcost
    
class ForestAdministrator(father.servent):
    name='ForestAdministrator'
    live=7
    power=5
    narrate="战吼：消灭场上所有随从，将场上的随从变成2-2的树苗"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['g' for i in range(7)]
        self.allCost=1
    def ZhanHong(self,MyMaster,Master):
        for i in Master.cardGround.copy():
            i.dieth(Master,MyMaster)
            Master.cardGround.append(moreS.Sapling())
        for ii in MyMaster.cardGround.copy():
            ii.dieth(MyMaster,Master)
            MyMaster.cardGround.append(moreS.Sapling())
class  Immortals(father.servent):
    name='Immortals'
    live=2
    power=1
    narrate="亡语：将此随从重新置入你的手牌"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bk' for i in range(2)]
    def WangYu(self,MyMaster,Master):
        MyMaster.cardHand.append(Immortals())
class Pastor(father.servent):
    name='Pastor'
    live=4
    power=3
    narrate="战吼：复活一个随从"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['w' for i in range(3)]
        self.allCost=1
    def ZhanHong(self,MyMaster,Master):
        if len(MyMaster.tomb)>0:
            r=re.compile(r"'.+'")
            getServent=MyMaster.tomb[random.randint(0,len(MyMaster.tomb)-1)]
            servent=eval((r.findall(str(type(getServent)))[0]).replace("'",'')+'()')
            MyMaster.cardGround.append(servent)
class OceanEnvoy(father.servent):
    name='OceanEnvoy'
    live=3
    power=2
    narrate="战吼：对所有敌方随从造成1点伤害"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bl' for i in range(2)]
    def ZhanHong(self,MyMaster,Master):
        for i in Master.cardGround:
            i.live-=1
class OceanCriminal(father.servent):
    name='OceanCriminal'
    live=7
    power=6
    narrate="战吼：对所有你的随从造成2点伤害"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bl' for i in range(4)]
        self.allCost=1
    def ZhanHong(self,MyMaster,Master):
        for i in MyMaster.cardGround:
            i.live-=2
class OceanWatcher(father.servent):
    name='OceanWatcher'
    live=1
    power=1
    narrate="亡语:随机对一个敌方随从造成1点伤害"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bl']
    def WangYu(self, MyMaster, Master):
        if len(Master.cardGround)!=0:
            Master.cardGround[random.randint(0,len(Master.cardGround)-1)].live-=1
class OceanManager(father.servent):
    name='OceanManager'
    live=8
    power=6
    narrate="战吼：召唤4个1-1的海洋观察者"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bl' for i in range(6)]
        self.allCost=1
    def ZhanHong(self,MyMaster,Master):
        for i in range(4):
            MyMaster.cardGround.append(OceanWatcher())
class Cthugha(father.servent):
    name='Cthugha'
    live=6
    power=7
    narrate="神秘且可怕 战吼：消灭你的所有随从，每消灭一个便对敌方英雄造成3点伤害"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['r' for i in range(9)]
        self.allCost=1
    def ZhanHong(self,MyMaster,Master):
        for i in MyMaster.cardGround.copy():
            i.dieth(MyMaster,Master)
            Master.live-=3
class Zstylzhemgni(father.servent):
    name='Zstylzhemgni'
    live=6
    power=7
    narrate="神秘且可怕 忘语:召唤6个1-2的SpiderMoM"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['g' for i in range(9)]
        self.allCost=1
    def WangYu(self, MyMaster, Master):
        for i in range(6):
            MyMaster.cardGround.append(SpiderMoM())
class Ymnar(father.servent):
    name='Ymnar'
    live=3
    power=3
    narrate="神秘且可怕 战吼：获得敌方3个随从的控制权"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['w' for i in range(8)]
        self.allCost=2
    def ZhanHong(self, MyMaster, Master):
        for i in range(3 if len(Master.cardGround)>3 else len(Master.cardGround)>3):
            get=selectCards('servent',Master.cardGround)
            MyMaster.cardGround.append(get)
            Master.cardGround.remove(get)
class Zathog(father.servent):
    name='Zathog'
    live=12
    power=3
    narrate="神秘且可怕 战吼：所有随从加5点生命值"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bk' for i in range(8)]
        self.allCost=2
    def ZhanHong(self, MyMaster, Master):
        for i in MyMaster.cardGround:
            i.buff.append(buff.Zathog())
class MayanStoneStatus(father.servent):
    name='MayanStoneStatus'
    live=8
    power=2
    narrate="亡语:随机消灭一个敌方随从"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bl' for i in range(6)]
        
    def WangYu(self, MyMaster, Master):
        if len(Master.cardGround)!=0:
            Master.cardGround[random.randint(0,len(Master.cardGround)-1)].dieth(Master,MyMaster)
class BabylonGuard(father.servent):
    name='BabylonGuard'
    live=10
    power=0
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bl' for i in range(6)]
    
class Ruby(father.servent):
    name='Ruby'
    live=4
    power=2
    narrate="当将被攻击时，+1+1"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bl' for i in range(4)]
        self.allCost=1
    def WhenBeAttack(self,MyMaster,Master,otherServent):
        self.buff.append(buff.Ruby())
class GravityPitfall(father.servent):
    name='GravityPitfall'
    live=1
    power=10
    narrate="无法攻击"
    def __init__(self) -> None:
        super().__init__()
        self.allCost=4
    def attackServent(self,MyMaster,Servent,Master):
        pass
    def attackMaster(self,MyMaster,Master):
        pass
class AncientTotem(father.servent):
    name='AncientTotem'
    live=1
    power=1
    narrate="当回合结束时随机加一点法力上限"
    def __init__(self) -> None:
        super().__init__()
        self.allCost=4
    def whenTermFinish(self, MyMaster, Master):
        MyMaster.groundList[random.randint(0,4)]+=1
class ExplosiveTruck(father.servent):
    name='ExplosiveTruck'
    live=1
    power=2
    narrate="亡语：对敌方英雄造成4点伤害"
    def __init__(self) -> None:
        super().__init__()
        self.allCost=3
    def WangYu(self, MyMaster, Master):
        Master.live-=4
class DemonDog(father.servent):
    name='DemonDog'
    live=2
    power=4
    narrate="战吼：随机弃一张自己的手牌"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bk' for i in range(2)]
    def ZhanHong(self, MyMaster, Master):
        if len(MyMaster.cardHand)>0:
            get=MyMaster.cardHand[random.randint(0,len(MyMaster.cardHand)-1)]
            MyMaster.cardHand.remove(get)
class GentleDefender(father.servent):
    name='GentleDefender'
    live=3
    power=3
    narrate="战吼：使一个随从的攻击力变为1"
    selectMode='osa'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bl' for i in range(3)]
    def ZhanHong(self, MyMaster, Master,role):
        role.iniPower=1
        role.power=1
class InternshipEngineer(father.servent):
    name='InternshipEngineer'
    live=1
    power=1
    narrate="战吼：抽一张牌"
    def __init__(self) -> None:
        super().__init__()
        self.allCost=2
    def ZhanHong(self, MyMaster, Master):
        MyMaster.getCard(1)
class FairJudge(father.servent):
    name='FairJudge'
    live=2
    power=2
    narrate="战吼：双方抽2张牌"
    def __init__(self) -> None:
        super().__init__()
        self.allCost=3
    def ZhanHong(self, MyMaster, Master):
        MyMaster.getCard(2)
        Master.getCard(2)
class Magician(father.servent):
    name='Magician'
    live=5
    power=2
    narrate="战吼：随机获得敌方小于等于2攻击力随从的控制权"
    def __init__(self) -> None:
        super().__init__()
        self.allCost=1
        self.cost=['w' for i in range(4)]
    def ZhanHong(self, MyMaster, Master):
        arr=[]
        for i in Master.cardGround:
            if i.Rpower()<=2:
                arr.append(i)
        a=(arr[random.randint(0,len(arr)-1)]) if len(arr)!=0 else False
        if a!=False:
            Master.cardGround.remove(a)
            MyMaster.cardGround.append(a)
class HolyGuider(father.servent):
    name='HolyGuider'
    live=3
    power=2
    narrate="战吼：使一个随从获得+2生命值"
    selectMode='osa'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['w' for i in range(2)]
        self.buffNar=buff.HolyGuider()
    def ZhanHong(self, MyMaster, Master,role):
        role.buff.append(self.buffNar)
class MindReader(father.servent):
    name='MindReader'
    live=1
    power=1
    narrate="战吼：获得对方手牌的一个复制"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['w' for i in range(1)]
    def ZhanHong(self, MyMaster, Master):
        if len(Master.cardHand)>0:
            get=copy.deepcopy(Master.cardHand[random.randint(0,len(Master.cardHand)-1)])
            MyMaster.cardHand.append(get)
class Drummer(father.servent):
    name='Drummer'
    live=5
    power=5
    narrate="回合结束时：为英雄恢复5点生命"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['w' for i in range(6)]
        self.allCost=1
    def whenTermFinish(self,MyMaster,Master):
        MyMaster.live+=5
class ShadowPieces(father.servent):
    name='ShadowPieces'
    live=3
    power=4
    narrate="亡语：对敌方英雄造成3点伤害"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['w' for i in range(2)]
        self.allCost=1
    def WangYu(self, MyMaster, Master):
        Master.live-=3
class CrowdedMotorcade(father.servent):
    name='CrowdedMotorcade'
    live=2
    power=1
    narrate="回合结束时：获得对方牌库里一张牌的复制"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['w' for i in range(2)]
        self.allCost=1
    def whenTermFinish(self,MyMaster,Master):
        if len(Master.cardStorage)>0:
            get=copy.deepcopy(Master.cardStorage[random.randint(0,len(Master.cardStorage)-1)])
            MyMaster.cardHand.append(get)
class HolyElement(father.servent):
    name='HolyElement'
    live=5
    power=0
    narrate="攻击力等于生命值"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['w' for i in range(3)]
        self.allCost=1
    def Rpower(self, MyMaster=None, Master=None):
        return self.Rlive()
class FireTotem(father.servent):
    name='FireTotem'
    live=2
    power=1
    narrate="回合结束时，将牌抽至3张"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['r' for i in range(2)]
        self.allCost=1
    def whenTermFinish(self,MyMaster,Master):
        if len(MyMaster.cardHand)<3:
            MyMaster.getCard(3-len(MyMaster.cardHand))
class Bullet(father.servent):
    name='Bullet'
    live=1
    power=1
    narrate="战吼:召唤2只Bullet"
    def __init__(self) -> None:
        super().__init__()
        self.allCost=2
    def ZhanHong(self,MyMaster,Master):
        MyMaster.cardGround.append(Bullet())
        MyMaster.cardGround.append(Bullet())
class FearOfClowns(father.servent):
    name='FearOfClowns'
    live=1
    power=1
    narrate="战吼:你每召回一只此随从使其+2+2"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bl' for i in range(1)]
        self.buffNar=buff.FearOfClowns()
    def ZhanHong(self,MyMaster,Master):
        try:
            for i in range(MyMaster.FearOfClownsCounter):
                self.buff.append(self.buffNar)
            MyMaster.FearOfClownsCounter+=1
        except:
            MyMaster.FearOfClownsCounter=1
class SecretResearcher(father.servent):
    name='SecretResearcher'
    live=2
    power=3
    narrate="战吼:选择一个友方随从，将其随从3张牌塞入牌库"
    selectMode='osm'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bl' for i in range(2)]
    def ZhanHong(self,MyMaster,Master,role):
        r=re.compile(r"'.+'")
        for i in range(3):
            MyMaster.cardStorage.append(eval((r.findall(str(type(role)))[0]).replace("'",'')+'()'))
class BombWalker(father.servent):
    name='BombWalker'
    live=1
    power=2
    narrate="亡语：对敌方英雄造成2点伤害"
    def __init__(self) -> None:
        super().__init__()
        self.allCost=1
    def WangYu(self, MyMaster, Master):
        Master.live-=2
class FlameSquirter(father.servent):
    name='FlameSquirter'
    live=4
    power=3
    narrate="当随从攻击时：对敌方英雄造成2点伤害"
    def __init__(self) -> None:
        super().__init__()
        self.allCost=2
        self.cost=['r' for i in range(3)]
    def WhenAttack(self,MyMaster,Master):
        Master.live-=2
class MinerInAHurry(father.servent):
    name='MinerInAHurry'
    live=2
    power=3
    narrate="战吼：随机对三个角色造成1点伤害"
    def __init__(self) -> None:
        super().__init__()
        self.allCost=2
    def ZhanHong(self,MyMaster,Master):
        get=MyMaster.cardGround+Master.cardGround+[MyMaster,Master]
        for i in range(3):
            get[random.randint(0,len(get)-1)].live-=1
class Predictor(father.servent):
    name='Predictor'
    live=3
    power=3
    narrate="战吼：触发一个友方随从的亡语"
    selectMode='osm'
    def __init__(self) -> None:
        super().__init__()
        self.allCost=3
    def ZhanHong(self,MyMaster,Master,role):
        role.WangYu(MyMaster,Master)
class Sanctifier(father.servent):
    name='Sanctifier'
    live=10
    power=1
    narrate="战吼：选择一个敌方随从一直攻击它直到有一个随从死亡"
    selectMode='oso'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['w' for i in range(3)]
    def ZhanHong(self,MyMaster,Master,role):
        self.attackServent(MyMaster,role,Master)
        
        if self.Rlive()>0 and role.Rlive()>0:
            self.ZhanHong(MyMaster,Master,role)
class spiderden(father.servent):
    name='spiderden'
    live=3
    power=0
    narrate="亡语:召唤3个1-1的小蜘蛛"
    def __init__(self) -> None:
        super().__init__()
        self.allCost=3
    def WangYu(self, MyMaster, Master):
        MyMaster.cardGround.append(moreS.Spider())
        MyMaster.cardGround.append(moreS.Spider())
        MyMaster.cardGround.append(moreS.Spider())
class mutant(father.servent):
    name='mutant'
    live=5
    power=1
    narrate="亡语:保留所有属性，放入牌库"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['g' for i in range(3)]
    def WangYu(self, MyMaster, Master):
        get=copy.deepcopy(self)
        get.live=self.iniLive
        MyMaster.cardStorage.append(get)
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
