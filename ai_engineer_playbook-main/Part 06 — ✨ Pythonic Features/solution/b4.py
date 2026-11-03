class AcademySession:
    def __enter__(self):
        print("🚪 Academy session opened.")
        return self
    def add(self,name):
        return f'{name} joined the sesson'
    def start_training(self, drill):
        print(f'Training drill: {drill}')
    def __exit__(self,exc_type,exc_value,traceback):
        if exc_type:
            print("fix issue")
        print(f"🧹 Cleaning up academy resources.\n🔒 Academy session closed.")


with AcademySession() as session:
    print(session.add("greydev"))
    session.start_training("running")