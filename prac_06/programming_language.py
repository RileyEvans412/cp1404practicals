"""
Comparing Programming Languages
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name='', typing='', reflection=True, year=0):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                           self.year)

    def is_dynamic(self):
        return self.typing == "Dynamic"
