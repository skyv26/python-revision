'''
   Class and Object, In this exercice we will learn
   how to create a class and it's multiple object to
   understand the OOP behaviour.
'''

class Developer: # Developer (base) class
    def __init__(self, type='software'):
        self.type = type
    
    def role(self): # class method or function
        print(f"{self.type.title()} developer") # Print the type of developer with first letter capital

web_developer = Developer('web')
web_developer.role()
# Output: web developer

embedded_developer = Developer('embedded')
embedded_developer.role()
# Output: embedded developer

block_chain_developer = Developer('blockchain')
block_chain_developer.role()
# Output: blockchain developer

