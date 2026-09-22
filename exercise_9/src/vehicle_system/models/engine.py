class Engine:
    def __init__(self):
        self.status = 'Stopped'

    def start(self):
        self.status = 'Running'

    def stop(self):
        self.status = 'Stopped'