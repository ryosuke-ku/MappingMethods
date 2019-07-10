callmethods = open(r'callmethods_log.txt','r',encoding="utf-8_sig")
callmethodsname = callmethods.readlines()
callmethodsArray = [callmethod.replace('\n', '') for callmethod in callmethodsname]
# print(callmethodsArray)

cnt = 1
for callmethodName in callmethodsArray:
    print(str(cnt) + ' ' + str(callmethodName))
    cnt+=1