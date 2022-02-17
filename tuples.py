
def employee_check(work_hours):

    max = 0
    emp1 = ''

    for employee, work in work_hours:
        if work > max:
            max = work
            # print(max)
            emp1 = employee
        else:
            pass

    return (emp1, max)

work_hours = [('a',100),('b',80),('c',10)]
# result = employee_check(work_hours)
# print(result)
name,hours=employee_check(work_hours)
# print(name,hours)
print(name,hours)