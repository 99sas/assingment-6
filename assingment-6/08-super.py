

class person:

    def __init__(self, name):
        self.name = name


class Teacher(person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

t = Teacher("Saira", "programming")
print(t.name, t.subject)