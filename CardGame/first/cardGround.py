from os import name


type=0
if type==0:
    import first.father as father
    import first.Database as database

else:
    import father as father
    import Database as database
     
class Forest(father.ground):
    name='Forest'
    typeG='g'
class Flame(father.ground):
    name='Flame'
    typeG='r'
class Dark(father.ground):
    name='Dark'
    typeG='bk'
class Light(father.ground):
    name='Light'
    typeG='w'
class Ocean(father.ground):
    name='Ocean'
    typeG='bl'

