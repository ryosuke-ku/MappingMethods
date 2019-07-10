import re

class rdict(dict):
    def __getitem__(self, key):
        try:
            return super(rdict, self).__getitem__(key)
        except:
            try:
                ret=[]
                for i in self.keys():
                    m= re.match("^"+key+"$",i)
                    if m:ret.append( super(rdict, self).__getitem__(m.group(0)) )
            except:raise(KeyError(key))
        return ret


production = open(r'MappingText/callmethods_log.txt','r',encoding="utf-8_sig")
ProductionPath = production.readlines()
PPath = [Pline.replace('\n', '') for Pline in ProductionPath]

production.close()
#print(ProductionPath)

Test = open(r'MappingText/methods_log.txt','r',encoding="utf-8_sig")
TestPath = Test.readlines()
TPath = [Tline.replace('\n', '') for Tline in TestPath]

Test.close()
#print(TestPath)

dic = dict(zip(PPath,TPath))

methodname = dic.get("createModelBuildingRequest(p)")
methodname = dic.get("result.get()")
# print(methodname)

print(dic)
# d = {'#adwsegui': 'item1', '#bdsjfudc': 'item2','q#dxsw': 'item3'}
# rd = rdict(d)
# print(rd["#.*"])
# word = '#'
# print(rd["^(?=.*" + word + ").*$"])
# print(len(rd["^(?=.*" + word + ").*$"]))

rd2 = rdict(dic)
word = 'Manifest getJarManifest'
print(rd2["^(?=.*" + word + ").*$"])
print(len(rd2["^(?=.*" + word + ").*$"]))

# method_keys = dic.keys()
# print(method_keys)

