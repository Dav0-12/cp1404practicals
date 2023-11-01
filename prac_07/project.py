"""Project Class"""


class Project:
    def __init__(self, project, start_date, priority, estimate, completion):
        self.project = project
        self.start_date = start_date
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return (f"{self.project}, start: {self.start_date}, priority {self.priority}, estimate: ${self.estimate}, "
                f"completion: {self.completion}%")

    def is_complete(self):
        return self.completion == 100
