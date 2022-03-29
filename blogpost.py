class BlogPostHistory:
    FILENAME = "posts.txt"
    SEPARATOR = ","

    def __init__(self, title, desc):
        self._title = title
        self._desc = desc

    def save(self):
        with open(self.FILENAME, "a+") as f:
            data = f"{self._title}{self.SEPARATOR}{self._desc}\n"
            f.write(data)

    @property
    def title(self):
        return self._title
    @property
    def description(self):
        return self._desc

    def change_title(self, title):
        self._title = title
        try:
            self.save()
        except OSError:
            raise Exception("BlogPostHistory can't save history")

    def change_description(self, desc):
        self._desc = desc
        try:
            self.save()
        except OSError:
            raise Exception("BlogPostHistory can't save history")

    def get_properties(self):
        return self._title, self._desc

    print("Hello")
    



