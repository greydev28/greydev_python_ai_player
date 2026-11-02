class AcademySession:
    def __enter__(self):
        print("🚪 Academy session opened.")
        return self
    def add(self,name):
        return f'{name} joined the sesson'
