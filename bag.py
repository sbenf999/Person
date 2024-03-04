class Bag:
    def __init__(self, maxSize=10):
        self.bag = []
        self.maxSize = maxSize
        self.currentSize = 0
        self.isFull = False
        self.isLost = False
    
    def add(self, item):
        if (self.checkIsFull() == True) or (self.currentSize + len(item) > self.maxSize):
            print("Cannot add anymore items to bag")
            
        else:
            self.bag.append(item)
            self.currentSize += len(item)
            
            if self.currentSize == self.maxSize:
                self.isFull = True
    
    def remove(self, item):
        try:
            if (self.isLost == False) or (self.currentSize == 0):
                self.checkContents(False).remove(item)
                self.currentSize -= len(item)
            
            if self.currentSize < self.maxSize:
                self.isFull = False
            
        except Exception as e:
            return "Your bag is empty, lost or item is not in the bag"
        
    def getItem(self, itemName):
        for item_ in self.bag:
            #print(item_)
            if item_.getInfo("name") == itemName:
                return True
    
    def retreiveItem(self, itemName):
        if (self.currentSize != 0) and ((not self.isFull) and (not self.isLost)):
            for item in self.checkContents(False):
                if item.getInfo("name") == itemName:
                    return item
                
                else:
                    return False     
        else:
            return "Nothing in bag or bag is lost", False
            
    def getLastItem(self):
        if self.currentSize > 0:
            return self.bag[(len(self.bag)-1)]
        else:
            print("Bag is empty")
    
    def checkSize(self):    
        size = 0
        for item in self.bag:
            size += len(item)
            
        return size
        
    def checkIsFull(self):
        if self.checkSize == self.maxSize:
            self.isFull = True
            return True
    
        return False
    
    def checkIsLost(self):
        return self.isLost
    
    def checkIfEmpty(self):
        if self.currentSize == 0:
            return True
        
        else:
            return False
    
    def checkContents(self, printBag=True):
        if printBag:
            tmp = ''
            for index, item in enumerate(self.bag):
                if (index >= 0) and (index != len(self.bag)-1):
                    tmp += str(item) + ", "
                
                else:
                    tmp += str(item)
            
            print(tmp)

        return self.bag
    
    def __str__(self):
        print(self.checkContents(False))
        
class Item:
    def __init__(self, name, volume, function):
        self.name = name
        self.volume = volume
        self.function = function
        
    def getInfo(self, item):
        item = item.lower()
        attributes: dict = {
            "name": self.name,
            "volume": self.volume,
            "function": self.function
        }
        
        return attributes[item]
    
    def action(self):
        return f"Item {self.name} was used to {self.function}"
    
    def __len__(self):
        return self.volume
    
    def __str__(self):
        return self.name

if __name__ == "__main__":
    danielsBag = Bag()
    waterBottle = Item("waterBottle", 3, "drink water from")
    danielsBag.add(waterBottle)
    danielsBag.checkContents()
    print(danielsBag.checkSize())
    print(danielsBag.checkContents(False)[0].getInfo("volume"))
    print(danielsBag.checkContents(False)[0].action())
    print(danielsBag.checkSize())
    cyberDeck = Item("CyberDeck", 7, "survive the nuclear fallout created by the Russians")
    danielsBag.add(cyberDeck)
    danielsBag.checkContents()
    print(danielsBag.checkSize())
    danielsBag.checkContents(True)
    print(danielsBag.getLastItem().action())
    print(danielsBag.getItem("waterBottle"))
    print(danielsBag.checkSize())