class Hashtable:
    def __init__(self, length):
        self.length = length
        self.array = [None for i in range(length)]
        self.count_elements = 0

    def get_array(self):
        #  print("Raw version:", self.array)
        print("Hasthtable:", [i for i in self.array if i is not None])

    def calculate_index_from_key(self, key):
        return hash(key) % self.length

    def put(self, key, value):
        index = self.calculate_index_from_key(key)
        while self.array[index] is not None:
            if self.array[index][0] == key:
                print("Key " + str(key) + "with value " + str(self.array[index][1]) + " will be overwritten with value " + str(value))
                self.array[index] = [key, value]
                return
            if index == self.length - 1:
                index = 0
            else:
                index += 1
        print("Key-Value-Pair " + str(key) + ":" + str(value) + " placed on index " + str(index))
        self.array[index] = [key, value]
        self.count_elements += 1
        self.expand_array()
        return

    def get(self, key):
        index = self.calculate_index_from_key(key)
        while self.array[index] is not None:
            if self.array[index][0] == key:
                print("Key " + str(key) + " with value " + str(self.array[index][1]) + " found on index " + str(index))
                return
            if index == self.length - 1:
                index = 0
            else:
                index += 1
        print("Key " + str(key) + " not found")

    def expand_array(self):
        if self.count_elements / self.length >= 0.6:
            old_length = self.length
            old_array = self.array
            self.count_elements = 0
            self.length = int((self.length * 1.5) // 1)
            self.array = [None for i in range(self.length)]
            for i in range(old_length):
                if old_array[i] is not None:
                    self.put(old_array[i][0], old_array[i][1])
                    self.count_elements += 1
            print("Length " + str(old_length) + " expanded to length " + str(self.length))
            print(str(old_array) + " ---> " + str(self.array))
        else:
            print("Seems okay. Utilization:", str(self.count_elements / self.length))


new_hashtable = Hashtable(4)
new_hashtable.get_array()
new_hashtable.get(5)
new_hashtable.put(1, "hallo")
new_hashtable.put(3, "hallo")
new_hashtable.get_array()
