class dictionaryMethods:
    def __init__(self):
        pass  #no relevant variables to be stored
    def changeKeyDict(self, Dictionary, old_key, new_key, default_value):
        Dictionary[new_key] = Dictionary.pop(old_key,default_value)  
        return Dictionary
# popping old key along with object and creating a new key with that same popped object

    def getFirstKey(self, Dictionary):
        firstkey = next(iter(Dictionary))    #return key at index 0 
        return firstkey
        
    def getLastKey(self, Dictionary):
        lastkey = list(Dictionary)[-1] #return key at index len(dictionary)-1
        return lastkey