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
        if len(self.set) != len(other.set):
            return False
        
        for self_elemet in self.set:
            if other.set.count(self_elemet) == 0:
                return False
        return True
    
    def __and__(self, other: object):
        meet_of_tow_set = []
        
        for element in self.set:
            if other.set.count(element) != 0:
                meet_of_tow_set.append(element)
                
        return meet_of_tow_set
    
    def __or__(self, other: object):
        union = []
        
        for element in self.set:
            union.append(element)
            
        for element in other.set:
            if union.count(element) == 0:
                union.append(element)
                
        return union