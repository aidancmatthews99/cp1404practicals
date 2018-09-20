""" Programming Language Practical """


class ProgrammingLanguage:
    def __init__(self, field, typing, reflection, year):
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year
        assert typing == 'Dynamic' or typing == 'Static'

    def is_dynamic(self):
        return self.typing == 'Dynamic'

    def __str__(self):
        return "{}, {} typing, Reflection={}, First appeared in {}".format(self.field, self.typing, self.reflection,
                                                                           self.year)
