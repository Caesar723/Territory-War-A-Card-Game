import copy
import re
class buffFather:
    r=re.compile(r"'.+'")
    def __init__(self) -> None:
        self.buffType=copy.deepcopy(self.buffType)
        self.Name=self.r.findall(str(type(self)))[0]
        self.Name=str(self.Name).split('.')[2].replace("'",':')
        #print(self.buffName)
class successFlag(buffFather):
    buffName='body'
    buffType=[['p',1],['l',1]]
    
class toxic(buffFather):
    buffName='other'
    buffType='toxic'
class invincible(buffFather):
    buffName='other'
    buffType='invincible'
class liliBuff(buffFather):
    buffName='other'
    buffType='liliBuff'
class NaturalSelect(buffFather):
    buffName='body'
    buffType=[['p',1],['l',1]]
class Mecha(buffFather):
    buffName='body'
    buffType=[['p',5],['l',5]]
class General(buffFather):
    buffName='body'
    buffType=[['p',1],['l',1]]
class CrazyInstructor(buffFather):
    buffName='body'
    buffType=[['p',1],['l',0]]
class SummonSandworm(buffFather):
    buffName='body'
    buffType=[['p',2],['l',0]]
class Reinforce(buffFather):
    buffName='body'
    buffType=[['p',1],['l',0]]
class WorldTreePower(buffFather):
    buffName='body'
    buffType=[['p',5],['l',5]]
class RainAndDew(buffFather):
    buffName='body'
    buffType=[['p',1],['l',1]]
class ForestSpore(buffFather):
    buffName='body'
    buffType=[['p',1],['l',1]]
class Zathog(buffFather):
    buffName='body'
    buffType=[['p',0],['l',5]]
class Ruby(buffFather):
    buffName='body'
    buffType=[['p',1],['l',1]]
class InnerFire(buffFather):
    buffName='body'
    buffType=[['p',0],['l',0]]
class HolyGuider(buffFather):
    buffName='body'
    buffType=[['p',0],['l',2]]
class SellYourSoul(buffFather):
    buffName='body'
    buffType=[['p',4],['l',4]]
class DarkestOfDays(buffFather):
    buffName='body'
    buffType=[['p',1],['l',1]]
class FearOfClowns(buffFather):
    buffName='body'
    buffType=[['p',2],['l',2]]