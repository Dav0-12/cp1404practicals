"""Project Class"""

from datetime import datetime


class Project:
    def __init__(self, project, start_date, priority, estimate, completion):
        self.project = project
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return (f'{self.project}, start: {self.start_date.strftime("%d/%m/%Y")}, priority {self.priority}, '
                f'estimate: ${self.estimate}, completion: {self.completion}%')

    def is_complete(self):
        return self.completion == 100
