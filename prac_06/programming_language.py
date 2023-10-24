"""Programming language classes"""


class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.language}, {self.typing} Typing, reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Check whether the coding language has dynamic typing"""
        return self.typing == "Dynamic"
