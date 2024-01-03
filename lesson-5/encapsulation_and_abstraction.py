from abc import ABC, abstractmethod  # Importing ABC (Abstract Base Class) for abstraction

class Developer(ABC):  # Developer (base) class with abstraction
    def __init__(self, type='software'):
        self._type = type  # Encapsulation: Using a single leading underscore to indicate a protected attribute

    @abstractmethod
    def role(self):  # Abstract method for promoting abstraction
        pass

    # Encapsulation: Using getter and setter methods to access and modify private attributes
    def get_type(self):
        return self._type

    def set_type(self, new_type):
        self._type = new_type

class PythonDeveloper(Developer):  # Inheriting from Developer class
    def __init__(self, type='software', specialization='Python'):
        super().__init__(type)
        self._specialization = specialization

    # Overriding the role method to include specialization
    def role(self):
        print(f"{self.get_type().title()} developer with specialization in {self._specialization}")

class JavaScriptDeveloper(Developer):  # Inheriting from Developer class
    def __init__(self, type='software', framework='React'):
        super().__init__(type)
        self._framework = framework

    # Overriding the role method to include the framework
    def role(self):
        print(f"{self.get_type().title()} developer using {self._framework}")

class FullStackDeveloper(PythonDeveloper, JavaScriptDeveloper):  # Multiple inheritance
    def __init__(self, type='software', specialization='Python', framework='React'):
        super().__init__(type, specialization)
        self._framework = framework

    # Overriding the role method to include both specialization and framework
    def role(self):
        print(f"{self.get_type().title()} Full Stack Developer with specialization in {self._specialization} "
              f"and using {self._framework}")

# Creating instances of the classes
web_developer = PythonDeveloper('web', 'Python')
# embedded_developer = Developer('embedded')  # This line should be removed as Developer is an abstract class
block_chain_developer = JavaScriptDeveloper('blockchain', 'React')
full_stack_developer = FullStackDeveloper()  # Using multiple inheritance

# Polymorphism in action - calling the overridden role method
web_developer.role()
# Output: Web developer with specialization in Python

# embedded_developer.role()  # This line should be removed as Developer is an abstract class

block_chain_developer.role()
# Output: Blockchain developer using React

full_stack_developer.role()
# Output: Software Full Stack Developer with specialization in Python and using React

# Encapsulation example
print(web_developer.get_type())  # Output: web
web_developer.set_type('mobile')
print(web_developer.get_type())  # Output: mobile
