class Set():

    def __init__(self):
        self.set = []
        
    def add(self, element):
        for elemenet_of_set in self.set:
            if element == elemenet_of_set:
                return
            
        self.set.append(element)
        
    def delete(self, element):
        for elemenet_of_set in self.set:
            if element == elemenet_of_set:
                self.set.remove(element)
                return 
        return 
    
    def __eq__(self, other: object) -> bool:
        for self_elemet in self:
            if other.set.count(self_elemet) == 0:
                return False
        return True