typ=0
if typ==0:
    import first.father as father
    import first.Database as database
    import first.cardMoreServent as moreS
    import first.buff as buff
    import first.cardGround as ground
    import first.cardMoreServent
    import first.cardServent

else:
    import father as father
    import Database as database
    import cardMoreServent as moreS
    import buff
    import cardGround as ground
import random
import re
import copy
def selectCards(ty,storage,haveUsed=[]):
    arr=[]
    for i in storage:
        if i.typeCard==ty and not(i in haveUsed):
            arr.append(i)
    return (arr[random.randint(0,len(arr)-1)]) if len(arr)!=0 else False

class sweeping(father.magic):
    name='sweeping'
    narrate='对所有随从造成1点伤害'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['w']
    def ability(self, MyMaster, Master, selectIndex=None):
        for i in MyMaster.cardGround:
            i.live-=1
        for ii in Master.cardGround:
            ii.live-=1
class NaturalSelect(father.magic):
    name='NaturalSelect'
    narrate='使你的随从+1+1'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['g','g']
        self.buffNar=buff.NaturalSelect()
    def ability(self, MyMaster, Master, selectIndex=None):
        for i in MyMaster.cardGround:
            i.buff.append(self.buffNar)
class BigClever(father.magic):
    name='BigClever'
    narrate='抽两张牌'
    def __init__(self) -> None:
        super().__init__()
        self.allCost=3
    def ability(self, MyMaster, Master, selectIndex=None):
        MyMaster.getCard(2)
class GodPower(father.magic):
    name='GodPower'
    narrate='杀死一个随从，自己恢复4点血量'
    selectMode='osa'
    def __init__(self) -> None:
        super().__init__()
        self.allCost=2
        self.cost=['w','w']
    def ability(self, MyMaster, Master, selectIndex=None):
        selectIndex.live-=9999
        MyMaster.live+=4
class ancientTsunami(father.magic):
    name='ancientTsunami'
    narrate='消灭所有随从'
    
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bl' for i in range(7)]
    def ability(self, MyMaster, Master, selectIndex=None):
        for i in MyMaster.cardGround.copy():
            i.dieth(MyMaster,Master)
        for ii in Master.cardGround.copy():
            ii.dieth(Master,MyMaster)
class Mecha(father.magic):
    name='Mecha'
    narrate='选择一个随从，使其 +5+5'
    selectMode='osm'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['g' for i in range(3)]
        self.allCost=2
        self.buffNar=buff.Mecha()
    def ability(self, MyMaster, Master, selectIndex=None):
        selectIndex.buff.append(self.buffNar)
class Healing(father.magic):
    name='Healing'
    narrate='选择一个角色，恢复4血'
    selectMode='oaa'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['w' for i in range(2)]
    def ability(self, MyMaster, Master, selectIndex=None):
        selectIndex.live+=4
class Cannon(father.magic):
    name='Cannon'
    narrate='选择一个角色，造成5点伤害'
    selectMode='oaa'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['r' for i in range(3)]
    def ability(self, MyMaster, Master, selectIndex=None):
        selectIndex.live-=5
class FlameThrower(father.magic):
    name='FlameThrower'
    narrate='对所有敌方随从造成4点伤害'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bl' for i in range(4)]
    def ability(self, MyMaster, Master, selectIndex=None):
        for i in Master.cardGround:
            i.live-=4
class FireBall(father.magic):
    name='FireBall'
    narrate='对一个随从造成2点伤害，抽一张牌'
    selectMode='oaa'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['r' for i in range(2)]
    def ability(self, MyMaster, Master, selectIndex=None):
        selectIndex.live-=2
        MyMaster.getCard(1)
class SoulExplosion(father.magic):
    name='SoulExplosion'
    narrate='选择一个随从，造成4点伤害，溢出的伤害传给自己'
    selectMode='osa'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bk' for i in range(2)]
    def ability(self, MyMaster, Master, selectIndex=None):
        selectIndex.live-=4
        if selectIndex.Rlive()<0:
            MyMaster.live+=selectIndex.Rlive()
class NaturalGift(father.magic):
    name='NaturalGift'
    narrate='获得5种地'
    def __init__(self) -> None:
        super().__init__()
        self.allCost=2
    def ability(self, MyMaster, Master, selectIndex=None):
        MyMaster.cardHand+=[ground.Forest(),ground.Flame(),ground.Dark(),ground.Light(),ground.Ocean()]
class Blasphemy(father.magic):
    name='Blasphemy'
    narrate='对所有随从造成1点伤害，如果有随从死亡，再次释放该法术'
    def __init__(self) -> None:
        super().__init__()
        self.allCost=1
        self.cost=['bk' for i in range(2)]
    def ability(self, MyMaster, Master, selectIndex=None):
        check=False
        for i in MyMaster.cardGround.copy():
            i.live-=1
            if i.Rlive()<=0:
                check=True
                i.dieth(MyMaster, Master)
        for ii in Master.cardGround.copy():
            ii.live-=1
            if ii.Rlive()<=0:
                check=True
                ii.dieth(MyMaster, Master)
        if check==True:
            self.ability(MyMaster, Master)
class SpellOverload(father.magic):
    
    name='SpellOverload'
    narrate='消耗所有地，每消耗一个地，召唤一个1-1的幽灵'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['g']
    def ability(self, MyMaster, Master, selectIndex=None):
        for i in MyMaster.termGround:
            for ii in range(i):
                MyMaster.cardGround.append(moreS.Phantom())
        MyMaster.termGround=[0,0,0,0,0]
class StageAComeback(father.magic):
    name='StageAComeback'
    narrate='复活所有死过的随从'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bk' for i in range(9)]
    def ability(self, MyMaster, Master, selectIndex=None):
        r=re.compile(r"'.+'")
        cop=MyMaster.tomb.copy()
        random.shuffle(cop)
        for i in cop:
            print(type(i))
            servent=eval((r.findall(str(type(i)))[0]).replace("'",'')+'()')
            MyMaster.cardGround.append(servent)
class Greed(father.magic):
    name='Greed'
    narrate='抽一张牌，如果牌的法力大于4，扣1滴血再抽一张'
    def __init__(self) -> None:
        super().__init__()
        self.allCost=1
        self.cost=['bk']
    def ability(self, MyMaster, Master, selectIndex=None):
        get=MyMaster.getCard(1)
        if len(get)>0:
            getArr=get[0]
            if len(getArr.Rcost(MyMaster, Master))+getArr.allCost>4:
                self.ability(MyMaster, Master)
                MyMaster.live-=1
class Lifemanship(father.magic):
    name='Lifemanship'
    narrate='所有随从获得冲锋'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['r' for i in range(3)]
    def ability(self, MyMaster, Master, selectIndex=None):
        for i in MyMaster.cardGround.copy():
            i.sleep=False
class SummonSandworm(father.magic):
    name='SummonSandworm'
    narrate='对敌方所有随从造成4点伤害，我方所有随从+2攻击力'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['r' for i in range(4)]
        self.allCost=3
        self.buffNar=buff.SummonSandworm()
    def ability(self, MyMaster, Master, selectIndex=None):
        for i in Master.cardGround.copy():
            i.live-=4
        for ii in MyMaster.cardGround.copy():
            ii.buff.append(self.buffNar)
class Reinforce(father.magic):
    name='Reinforce'
    narrate='从牌库里召唤2个随从，所有随从+1攻击力'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['r' for i in range(6)]
        self.allCost=3
        self.buffNar=buff.Reinforce()
    def ability(self, MyMaster, Master, selectIndex=None):
        count=0
        for i in range(2):
            get=selectCards('servent',MyMaster.cardStorage)
            if get!=False:
                MyMaster.cardGround.append(get)
                MyMaster.cardStorage.remove(get)
        for ii in MyMaster.cardGround:
            ii.buff.append(self.buffNar)
class ElementAgitation(father.magic):
    name='ElementAgitation'
    narrate='召唤2个2-1的小火苗'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['r' for i in range(2)]
    def ability(self, MyMaster, Master, selectIndex=None):
        MyMaster.cardGround.append(moreS.SmallFire())
        MyMaster.cardGround.append(moreS.SmallFire())
class ForestCover(father.magic):
    name='ForestCover'
    narrate='每有一张手牌，召唤一个2-2的树苗'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['g' for i in range(3)]
        self.allCost=1
    def ability(self, MyMaster, Master, selectIndex=None):
        for i in range(len(MyMaster.cardHand)):
            MyMaster.cardGround.append(moreS.Sapling())
class DiffusePlague(father.magic):
    name='DiffusePlague'
    narrate='召唤1-5的甲虫，直到我方随从数量等于敌方随从数量'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bl' for i in range(4)]
        self.allCost=2
    def ability(self, MyMaster, Master, selectIndex=None):
        if len(MyMaster.cardGround)<len(Master.cardGround):
            for i in range(len(Master.cardGround)-len(MyMaster.cardGround)):
                MyMaster.cardGround.append(moreS.Beetle())
        else:
            MyMaster.cardGround.append(moreS.Beetle())
class WorldTreePower(father.magic):
    name='WorldTreePower'
    narrate='友方场上随从和牌库里的随从+5+5'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['g' for i in range(8)]
        self.allCost=2
        self.buffNar=buff.WorldTreePower()
    def ability(self, MyMaster, Master, selectIndex=None):
        for i in MyMaster.cardGround:
            i.buff.append(self.buffNar)
        for ii in MyMaster.cardStorage:
            if ii.typeCard=='servent':
                ii.buff.append(self.buffNar)
class RainAndDew(father.magic):
    name='RainAndDew'
    narrate='+8+8分配给所有随从'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['g' for i in range(4)]
        self.allCost=2
        self.buffNar=buff.RainAndDew()
    def ability(self, MyMaster, Master, selectIndex=None):
        for i in range(8):
            if len(MyMaster.cardGround)!=0:
                MyMaster.cardGround[random.randint(0,len(MyMaster.cardGround)-1)].buff.append(self.buffNar)
class ForestSpore(father.magic):
    name='ForestSpore'
    narrate='对所有敌方随从-1-1，对友方随从+1+1'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['g' for i in range(3)]
        self.allCost=2
        self.buffNar=buff.ForestSpore()
    def ability(self, MyMaster, Master, selectIndex=None):
        for i in Master.cardGround:
            i.power-=1
            i.live-=1
        for ii in MyMaster.cardGround:
            ii.buff.append(self.buffNar)
class ExploreUnknow(father.magic):
    name='ExploreUnknow'
    narrate='抽两张牌，如果抽到的牌是法术则召唤1个2-2对树苗'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['g' for i in range(3)]
        self.allCost=1
    def ability(self, MyMaster, Master, selectIndex=None):
        get=MyMaster.getCard(2)
        for i in get:
            if i.typeCard=='magic':
                MyMaster.cardGround.append(moreS.Sapling())
class GodGrace(father.magic):
    name='GodGrace'
    narrate='复活一个随从'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['w' for i in range(2)]
    def ability(self, MyMaster, Master, selectIndex=None):
        if len(MyMaster.tomb)>0:
            r=re.compile(r"'.+'")
            getServent=MyMaster.tomb[random.randint(0,len(MyMaster.tomb)-1)]
            servent=eval((r.findall(str(type(getServent)))[0]).replace("'",'')+'()')
            MyMaster.cardGround.append(servent)
class HolyLightDispel(father.magic):
    name='HolyLightDispel'
    narrate='对敌方随从造成2点伤害，对我方随从恢复2点生命值'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['w' for i in range(4)]
    def ability(self, MyMaster, Master, selectIndex=None):
        for i in Master.cardGround:
            i.live-=2
        for ii in MyMaster.cardGround:
            ii.live+=2
class HolyBlessing(father.magic):
    name='HolyBlessing'
    narrate='选择一个友方随从，使其生命翻倍'
    selectMode='osm'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['w' for i in range(1)]
        self.allCost=2
    def ability(self, MyMaster, Master, selectIndex=None):
        selectIndex.live+=selectIndex.Rlive(MyMaster, Master)
        selectIndex.iniLive+=selectIndex.Rlive(MyMaster, Master)
class PuppetPossess(father.magic):
    name='PuppetPossess'
    narrate='复活三个随从，其生命和攻击力均为1'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['w' for i in range(3)]
        self.allCost=1
    def ability(self, MyMaster, Master, selectIndex=None):
        r=re.compile(r"'.+'")
        cop=MyMaster.tomb.copy()
        random.shuffle(cop)
        print(cop)

        for i in range(3 if len(cop)>3 else len(cop)):
            
            servent=eval((r.findall(str(type(cop[i])))[0]).replace("'",'')+'()')
            servent.live=1
            servent.power=1
            MyMaster.cardGround.append(servent)
class HolySmite(father.magic):
    name='HolySmite'
    narrate='对一个随从造成3点伤害'
    selectMode='osa'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['w']
    def ability(self, MyMaster, Master, selectIndex=None):
        selectIndex.live-=3
class Opportunity(father.magic):
    name='Opportunity'
    narrate='抽两张牌，如果是随从牌则恢复三点生命'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['w' for i in range(3)]
    def ability(self, MyMaster, Master, selectIndex=None):
        get=MyMaster.getCard(2)
        for i in get:
            if i.typeCard=='servent':
                MyMaster.live+=3
class HeavyRain(father.magic):
    name='HeavyRain'
    narrate='抽两张牌，如果费用小于5则对所有敌方随从造成1点伤害'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bl' for i in range(3)]
        self.allCost=1
    def ability(self, MyMaster, Master, selectIndex=None):
        get=MyMaster.getCard(2)
        for i in get:
            if len(i.cost)+i.allCost<5:
                for ii in Master.cardGround:
                    ii.live-=1
class AbyssDoor(father.magic):
    name='AbyssDoor'
    narrate='消灭场上所有随从，召唤一个所有随从属性总和的怪物'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bl' for i in range(8)]
        self.allCost=2
    def ability(self, MyMaster, Master, selectIndex=None):
        power=0
        live=0
        for i in MyMaster.cardGround.copy():
            power+=i.Rpower(MyMaster, Master)
            live+=i.Rlive(MyMaster, Master)
            i.dieth(MyMaster,Master)
        for ii in Master.cardGround.copy():
            power+=ii.Rpower(Master,MyMaster)
            live+=ii.Rlive(Master,MyMaster)
            ii.dieth(Master,MyMaster)
        servent=moreS.Cthulhu()
        servent.live+=live
        servent.iniLive+=live
        servent.power+=power
        servent.iniPower+=power
        MyMaster.cardGround.append(servent)
class LifeDrain(father.magic):
    name='LifeDrain'
    narrate="造成2点伤害，为我方英雄恢复2点生命"
    selectMode='oaa'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bk' for i in range(3)]
    def ability(self, MyMaster, Master, selectIndex=None):
        selectIndex.live-=2
        MyMaster.live+=2
class InterimAdjustment(father.magic):
    name='InterimAdjustment'
    narrate="为自己恢复5点生命值，抽一张牌"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['w' for i in range(3)]
    def ability(self, MyMaster, Master, selectIndex=None):
        MyMaster.live+=5
        MyMaster.getCard(1)
class DoubleShot(father.magic):
    name='DoubleShot'
    narrate="对敌方随机两个随从造成2点伤害"
    def __init__(self) -> None:
        super().__init__()
        self.allCost=3
    def ability(self, MyMaster, Master, selectIndex=None):
        used=[]
        for i in range(2):
            get=selectCards('servent',Master.cardGround,used)
            if get!=False:
                used.append(get)
                get.live-=2
class InnerFire(father.magic):
    name='InnerFire'
    narrate="使一个随从的攻击力等于生命值"
    selectMode='osa'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['w' for i in range(1)]
        self.buffNar=buff.InnerFire()
    def ability(self, MyMaster, Master, selectIndex=None):
        self.buffNar.buffType[0][1]=selectIndex.Rlive()-selectIndex.Rpower()
        selectIndex.buff.append(self.buffNar)
class UrgentRecruitment(father.magic):
    name='UrgentRecruitment'
    narrate="将你手牌的复制放入牌库"
    def __init__(self) -> None:
        super().__init__()
        self.allCost=3
    def ability(self, MyMaster, Master, selectIndex=None):
        for i in MyMaster.cardHand:
            MyMaster.cardStorage.append(copy.deepcopy(i))
class OceanCultivation(father.magic):
    name='OceanCultivation'
    narrate="加一点Ocean并抽一张牌"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bl' for i in range(3)]
    def ability(self, MyMaster, Master, selectIndex=None):
        MyMaster.groundList[1]+=1
        MyMaster.getCard(1)
class Scheming(father.magic):
    name='Scheming'
    narrate="选择一个随从，把其三张的复制塞入牌库"
    selectMode='osa'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bl' for i in range(2)]
    def ability(self, MyMaster, Master, selectIndex=None):
        for i in range(3):
            MyMaster.cardStorage.append(copy.deepcopy(selectIndex))
class SecretBlessings(father.magic):
    name='SecretBlessings'
    narrate="你卡牌里所有的牌的费用全部变成全比变成1蓝"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bl' for i in range(7)]
    def ability(self, MyMaster, Master, selectIndex=None):
        for i in  MyMaster.cardStorage:
            i.allCost=0
            i.cost=['bl']
class Mimicry(father.magic):
    name='Mimicry'
    narrate="触发所有随从的亡语"
    def __init__(self) -> None:
        super().__init__()
        self.allCost=3
    def ability(self, MyMaster, Master, selectIndex=None):
        for i in MyMaster.cardGround:
            i.WangYu(MyMaster, Master)
class SellYourSoul(father.magic):
    name='SellYourSoul'
    narrate="杀死你的一个随从，是另外一个随从+4+4"
    selectMode='osm'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bk' for i in range(2)]
        self.buffNar=buff.SellYourSoul()
    def ability(self, MyMaster, Master, selectIndex=None):
        selectIndex.dieth(MyMaster,Master)
        if len(MyMaster.cardGround)!=0:
            MyMaster.cardGround[random.randint(0,len(MyMaster.cardGround))].buff.append(self.buffNar)
class  ForestPlot(father.magic):
    name='ForestPlot'
    narrate="消灭场上所有随从，将场上的随从变成2-2的树苗"
    def __init__(self) -> None:
        super().__init__()
        self.cost=['g' for i in range(3)]
        self.allCost=1
    def ability(self, MyMaster, Master, selectIndex=None):
        for i in Master.cardGround.copy():
            i.dieth(Master,MyMaster)
            Master.cardGround.append(moreS.Sapling())
        for ii in MyMaster.cardGround.copy():
            ii.dieth(MyMaster,Master)
            MyMaster.cardGround.append(moreS.Sapling())
class DarkestOfDays(father.magic):
    name='DarkestOfDays'
    narrate="杀死你的一个随从，是所有友方随从+1+1"
    selectMode='osm'
    def __init__(self) -> None:
        super().__init__()
        self.cost=['bk' for i in range(1)]
        self.buffNar=buff.DarkestOfDays()
    def ability(self, MyMaster, Master, selectIndex=None):
        selectIndex.dieth(MyMaster,Master)
        for i in MyMaster.cardGround:
            i.buff.append(self.buffNar)

