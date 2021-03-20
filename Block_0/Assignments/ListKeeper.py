class ListKeeper:      
    def __init__(self):
        self.dict = {'example':[1,2,3,4,5]} #Init of default values for dictonary
        
    def show(self):
        '''Returns all list names.'''
        return list(self.dict.keys())  #return all available keys in dictonary
    
    def add(self, name, list):
        '''Adds a new list.'''
        self.dict[name] = list #List assigment for specified key
        
    def delete(self, name):
        '''Deletes list with given name.'''
        self.dict.pop(name) #Deletes the list associated with given key
        
    def sort(self, name):
        '''Returns the sorted list associated with given name.'''
        return sorted(self.dict[name]) #Returns a the sorted list associated with given key
    
    def append(self, name, list):
        '''Appends list to list::name.'''
        self.dict[name] += list #Appends given list to stored list associated with given key