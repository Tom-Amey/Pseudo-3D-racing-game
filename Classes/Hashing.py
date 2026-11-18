import hashlib #import hash


class Hash:
    def HashText(Text):
        hash_obj = hashlib.md5(Text.encode()) #convert text to hash
        #using md5 algorithm
        return (hash_obj.hexdigest()) #return hex value

