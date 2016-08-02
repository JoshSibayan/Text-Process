import string

######## Begin code which needs to be modified ##########
        
class MyChainDict(object):     
    def __init__(self, newtsize = 1000):
        self.tsize = newtsize
        self.mychaindict = []
        for i in range(self.tsize):
            self.mychaindict.append(None)
        return
        
    def hash(self, key):
        h = 0
        for a in key:
            h += ord(a)
        return h % self.tsize    
        
    def insert(self, key, value):
        j = self.hash(key)
        if self.mychaindict[j] == None:
            self.mychaindict[j] = []
            self.mychaindict[j].insert(0, (key, value))
            return
        for i in range(len(self.mychaindict[j])):
            if self.mychaindict[j][i][0] == key:
                self.mychaindict[j][i] = (key, value)
                return
        self.mychaindict[j].insert(0, (key, value))
                
    def contains(self, key):
        j = self.hash(key)
        if self.mychaindict[j] == None:
            return False
        for i in self.mychaindict[j]:
            if i[0] == key:
                return True
        return False

    def value(self, key):    
        j = self.hash(key)
        for i in self.mychaindict[j]:
            if i[0] == key:
                return i[1]
        
    def delete(self, key):
        j = self.hash(key)
        if self.mychaindict[j] == None:
            return
        for i in range(len(self.mychaindict[j])):
            if self.mychaindict[j][i][0] == key:
                self.mychaindict[j].pop(i)
                
    def get_key_values(self):
        keys = []
        for x in range(self.tsize):
            if self.mychaindict[x] != None:
                for i in self.mychaindict[x]:
                    keys.append(i)
        return keys
    
    def dump(self):
        for x in range(self.tsize):
            if self.mychaindict[x] != None:
                for i in self.mychaindict[x]:
                    print(i)
    
class MyOpenLinearDict(object):
    def __init__(self, newtsize = 1000):
        self.tsize = newtsize
        self.sloc = 0
        self.myoldict = []
        for i in range(self.tsize):
            self.myoldict.append(None)
        return
        
    def hash(self, key):
        h = 0
        for a in key:
            h += ord(a)
        return h % self.tsize
    
    def linhash(self, key, i):
        return (self.hash(key) + i) % self.tsize
    
    def contains(self, key):
        for i in range(self.tsize):
            j = self.linhash(key, i)
            if self.myoldict[j] == None:
                return False
            if self.myoldict[j][0] == key:
                return True
        return False

    def value(self, key):
        for i in range(self.tsize):
            j = self.linhash(key, i)
            if self.myoldict[j] == None:
                break
            if self.myoldict[j][0] == key:
                return self.myoldict[j][1]

    def delete(self, key):
        for i in range(self.tsize):
            j = self.linhash(key, i)
            if self.myoldict[j] == None:
                return
            if self.myoldict[j][0] == key:
                self.myoldict[j] = 'DELETE'
            
    def get_key_values(self):
        keys = []
        for x in range(self.tsize):
            if self.myoldict[x] != None and self.myoldict[x] != 'DELETE':
                keys.append(self.myoldict[x])
        return keys
    
    def dump(self):
        for x in range(self.tsize):
            if self.myoldict[x] != None and self.myoldict[x] != 'DELETE':
                print(self.myoldict[x])

    def insert(self, key, value):
        for i in range(self.tsize):
            j = self.linhash(key, i)
            if self.myoldict[j] == None:
                break
            if self.myoldict[j][0] == key:
                self.myoldict[j] = (key, value)
                return
        for i in range(self.tsize):
            j = self.linhash(key, i)
            if self.myoldict[j] == None or self.myoldict[j] == 'DELETE':
                self.myoldict[j] = (key, value)
                self.sloc += 1
                if (self.sloc/self.tsize) >= .75:
                    self.reHash()
                return
            
    def reHash(self):
        keys = self.get_key_values()
        self.tsize *= 2
        self.sloc = 0
        self.myoldict = []
        for i in range(self.tsize):
            self.myoldict.append(None)
        for key, value in keys:
            self.insert(key, value)

class MyOpenQuadDict(object):
    def __init__(self, newtsize = 1000):
        self.tsize = newtsize
        self.sloc = 0
        self.myoqdict = []
        for i in range(self.tsize):
            self.myoqdict.append(None)
        return
        
    def hash(self, key):
        h = 0
        for a in key:
            h += ord(a)
        return h % self.tsize
    
    def quadhash(self, key, i):
        return (self.hash(key) + 8*i + 4*i**2) % self.tsize
    
    def contains(self, key):
        for i in range(self.tsize):
            j = self.quadhash(key, i)
            if self.myoqdict[j] == None:
                return False
            if self.myoqdict[j][0] == key:
                return True
        return False

    def value(self, key):
        for i in range(self.tsize):
            j = self.quadhash(key, i)
            if self.myoqdict[j] == None:
                break
            if self.myoqdict[j][0] == key:
                return self.myoqdict[j][1]

    def delete(self, key):
        for i in range(self.tsize):
            j = self.quadhash(key, i)
            if self.myoqdict[j] == None:
                return
            if self.myoqdict[j][0] == key:
                self.myoqdict[j] = 'DELETE'
            
    def get_key_values(self):
        keys = []
        for x in range(self.tsize):
            if self.myoqdict[x] != None and self.myoqdict[x] != 'DELETE':
                keys.append(self.myoqdict[x])
        return keys
    
    def dump(self):
        for x in range(self.tsize):
            if self.myoqdict[x] != None and self.myoqdict[x] != 'DELETE':
                print(self.myoqdict[x])

    def insert(self, key, value):
        for i in range(self.tsize):
            j = self.quadhash(key, i)
            if self.myoqdict[j] == None:
                break
            if self.myoqdict[j][0] == key:
                self.myoqdict[j] = (key, value)
                return
        for i in range(self.tsize):
            j = self.quadhash(key, i)
            if self.myoqdict[j] == None or self.myoqdict[j] == 'DELETE':
                self.myoqdict[j] = (key, value)
                self.sloc += 1
                if (self.sloc/self.tsize) >= .75:
                    self.reHash()
                return
            
    def reHash(self):
        keys = self.get_key_values()
        self.tsize *= 2
        self.sloc = 0
        self.myoqdict = []
        for i in range(self.tsize):
            self.myoqdict.append(None)
        for key, value in keys:
            self.insert(key, value)
        
# list of keys    
class MySet(object):
    def __init__(self):
        self.myset = MyChainDict()
        return

    def insert(self, key):
        self.myset.insert(key, None)
        return
    
    def contains(self, key):
        return self.myset.contains(key)
        
    def dump(self):
        self.myset.dump()
        return

######## End code which needs to be modified ##########


# Store the set of stop words in a set object
stop_words_file = "stopwords.txt"
stop_words = MySet()

with open(stop_words_file) as f:
    for l in f:
        stop_words.insert(l.strip())


# Download file from https://snap.stanford.edu/data/finefoods.txt.gz        
# Remember to gunzip before using
review_file = "foods_test.txt"

review_words = []
for i in range(5):
    #review_words.append(MyOpenQuadDict())
    #review_words.append(MyOpenLinearDict())
    review_words.append(MyChainDict())
    
with open(review_file, encoding='LATIN-1') as f:
    lines = f.readlines()
    idx = 0
    num_lines = len(lines) - 2
    while idx < num_lines:
        while not lines[idx].startswith("review/score"):
            idx = idx + 1

        # Jump through hoops to satisfy the Unicode encodings 
        l = lines[idx].encode('ascii', 'ignore').decode('ascii')
        l = l.strip().split(":")[1].strip()

        # Extract rating
        rating = int(float(l))
        while not lines[idx].startswith("review/text"):
            idx = idx + 1
            
        l = lines[idx].encode('ascii', 'ignore').decode('ascii').strip().lower()
        text = l.split(":")[1].strip()
        text = text.translate(str.maketrans("","", string.punctuation))

        # Extract words in the text 
        words = text.split(" ")
        # words = [x.strip(string.punctuation) for x in text.split(" ")]
        for w in words:
            if len(w) and not stop_words.contains(w):
                if review_words[rating - 1].contains(w):
                    count = review_words[rating - 1].value(w) + 1
                else:
                    count = 1
                review_words[rating - 1].insert(w, count)

# Print out the top words for each of the five ratings 
for i in range(5):
    freq_words = sorted(review_words[i].get_key_values(), key=lambda tup: tup[1], reverse=True)
    print(i+1, freq_words[0:20])