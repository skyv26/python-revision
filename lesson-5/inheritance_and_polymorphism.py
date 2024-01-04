class Developer:  # Developer (base) class
    def __init__(self, type='software'):
        self.type = type

    def role(self):  # class method or function
        print(f"{self.type.title()} developer")  # Print the type of developer with first letter capital


class PythonDeveloper(Developer):  # Inheriting from Developer class
    def __init__(self, type='software', specialization='Python'):
        super().__init__(type)
        self.specialization = specialization

    # Overriding the role method to include specialization
    def role(self):
        print(f"{self.type.title()} developer with specialization in {self.specialization}")


class JavaScriptDeveloper(Developer):  # Inheriting from Developer class
    def __init__(self, type='software', framework='React'):
        super().__init__(type)
        self.framework = framework

    # Overriding the role method to include the framework
    def role(self):
        print(f"{self.type.title()} developer using {self.framework}")

class FullStackDeveloper(PythonDeveloper, JavaScriptDeveloper):  # Multiple inheritance
    def __init__(self, type='software', specialization='Python', framework='React'):
        # Call constructors of both base classes
        PythonDeveloper.__init__(self, type, specialization)
        JavaScriptDeveloper.__init__(self, type, framework)

    # Overriding the role method to include both specialization and framework
    def role(self):
        print(f"{self.type.title()} Full Stack Developer with specialization in {self.specialization} "
              f"and using {self.framework}")

# Creating instances of the derived classes
web_developer = PythonDeveloper('web', 'Python')
embedded_developer = Developer('embedded')  # Using the base class
block_chain_developer = JavaScriptDeveloper('blockchain', 'React')
full_stack_developer = FullStackDeveloper()  # Using multiple inheritance

# Polymorphism in action - calling the overridden role method
web_developer.role()
# Output: Web developer with specialization in Python

embedded_developer.role()
# Output: Embedded developer

block_chain_developer.role()
# Output: Blockchain developer using React

full_stack_developer.role()
# Output: Software Full Stack Developer with specialization in Python and using React
'''
Explanation:

1. Single Inheritance:

We created two new classes, PythonDeveloper and JavaScriptDeveloper, 
both inheriting from the base class Developer. super().__init__(type) 
is used to call the constructor of the base class to initialize the 
common attribute type. Each derived class has its own additional attributes
(specialization and framework) specific to its type of development.

2. Multiple Inheritance:

We introduced a new class FullStackDeveloper that inherits from both 
PythonDeveloper and JavaScriptDeveloper. The __init__ method of 
FullStackDeveloper calls the constructors of both parent classes using 
PythonDeveloper.__init__(self, type, specialization) and 
JavaScriptDeveloper.__init__(self, type, framework).

3. Polymorphism:

We overrode the role method in both derived classes. This demonstrates 
polymorphism, where objects of different classes can be treated as 
objects of the common base class (Developer). When calling the role method 
on instances of different classes, it executes the overridden method in 
the respective class, showcasing polymorphic behavior.
'''
