from dataclasses import dataclass
from operator import itemgetter

class StudentGroup:
    def __init__(self, id, name, avg_grade ,dept_id):
        self.id = id
        self.name = name
        self.avg_grade = avg_grade
        self.dept_id = dept_id

@dataclass
class Department:
    id: int
    name: str

@dataclass
class GroupDept:
    dept_id: int
    group_id: int

depts = [
    Department(1, 'Кафедра информатики'),
    Department(2, 'Кафедра математики'),
    Department(3, 'Кафедра физики'),
    Department(4, 'Кафедра иностранных языков'),
]

groups = [
    StudentGroup(1, 'ИС-21', 4.3, 1),
    StudentGroup(2, 'ПМ-22', 4.1, 2),
    StudentGroup(3, 'ФЗ-23', 3.9, 3),
    StudentGroup(4, 'ИС-22', 4.6, 1),
    StudentGroup(5, 'ЛГ-21', 4.0, 4),
]

groups_depts = [
    GroupDept(1, 1),
    GroupDept(1, 2),
    GroupDept(2, 2),
    GroupDept(3, 3),
    GroupDept(1, 4),
    GroupDept(2, 4),
    GroupDept(4, 5),
]

def main():
    one_to_many = [(s.name, s.avg_grade, g.name)
                   for s in groups
                   for g in depts
                   if s.dept_id == g.id]

    many_to_many_temp = [(d.name, gd.dept_id, gd.group_id)
                         for d in depts
                         for gd in groups_depts
                         if d.id == gd.dept_id]

    many_to_many = [(g.name, g.avg_grade, dept_name)
                    for dept_name, dept_id, group_id in many_to_many_temp
                    for g in groups
                    if group_id == g.id]

    res_1 = sorted(one_to_many, key=itemgetter(2))
    print(res_1)

    res_12_unsorted = []
    for d in depts:
        d_groups = list(filter(lambda i: i[2] == d.name, one_to_many))
        if len(d_groups) > 0:
            d_grades = [grade for _, grade, _ in d_groups]
            d_grades_sum = sum(d_grades)
            res_12_unsorted.append((d.name, d_grades_sum))
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print("\n")
    print(res_12)

    res_13 = {}
    for d in depts:
        if 'кафедра' in d.name.lower():
            d_groups = list(filter(lambda i: i[2] == d.name, many_to_many))
            d_group_names = [name for name, _, _ in d_groups]
            res_13[d.name] = d_group_names
    print("\n")
    print(res_13)


if __name__ == '__main__':
    main()