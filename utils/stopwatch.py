import time

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0

    def start(self):
        if not self.start_time:
            self.start_time = time.time()

    def stop(self):
        if self.start_time:
            self.elapsed_time += time.time() - self.start_time
            self.start_time = None

    def reset(self):
        self.start_time = None
        self.elapsed_time = 0

    def get_time(self):
        if self.start_time:
            return self.elapsed_time + (time.time() - self.start_time)
        return self.elapsed_time
