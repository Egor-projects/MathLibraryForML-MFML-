class MFML:
    def __init__(self, input_list):
        self.list = input_list

    def desc(self):
        # find min, middle and max values
        self.minv = min(self.list)
        self.maxv = max(self.list)
        self.midv = sum(self.list)/len(self.list)
        self.new = [self.minv, self.midv, self.maxv]
        return self.new
    def once(self):
        # find unique values
        self.new = []
        for i in self.list:
            if i not in self.new:
                self.new.append(i)
        return self.new
    def delzero(self):
        # delete zeros
        self.new = []
        for i in self.list:
            if i != 0:
                self.new.append(i)
        return self.new
    def onehot(self):
        # one hot encoding
        self.dict = []
        self.values = []
        for i in self.list:
            if i not in self.dict:
                self.dict.append(i)
        for i in range(len(self.dict)):
            self.l = [0]*len(self.dict)
            self.l[i] = 1
            self.values.append(self.l)
        self.res = []
        for i in self.list:
            self.res.append(self.values[self.dict.index(i)])
        
        return self.res
        
    def sygmoid(self):
        # find sygmoid
        import math
        self.new = []
        for i in self.list:
            self.new.append(1/(1+math.exp(-i)))
        return self.new
