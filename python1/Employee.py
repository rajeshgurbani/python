from Job import Job
class Employee:
    def __init__(self, name:str):
        self.name = name
        self.monthEndSalary = 0

    def work(self, job:Job):
        if job.name == 'developer':
            self.monthEndSalary = 3000 * job.effort
        elif job.name == 'tester':
            self.monthEndSalary = 1000 * job.effort

    def getTotalSalary(self) -> int:
        return self.monthEndSalary

j1 = Job('developer', 10, 'djskdsjds')
j2 = Job('tester', 10, 'djskdsjds')
emp1 = Employee('Rajesh')
emp2 = Employee('Rahul')
emp1.work(j1)
emp2.work(j2)
print(emp1.getTotalSalary())
print(emp2.getTotalSalary())



