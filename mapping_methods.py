production = open(r'test_callmethods_log.txt','r',encoding="utf-8_sig")
ProductionPath = production.readlines()
PPath = [Pline.replace('\n', '') for Pline in ProductionPath]

production.close()
#print(ProductionPath)

Test = open(r'test_methods_log.txt','r',encoding="utf-8_sig")
TestPath = Test.readlines()
TPath = [Tline.replace('\n', '') for Tline in TestPath]

Test.close()
#print(TestPath)

dic = dict(zip(PPath,TPath))

methodname = dic.get("createModelBuildingRequest(p)")
methodname = dic.get("result.get()")
print(methodname)