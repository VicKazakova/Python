def thesaurus(*args):
    employees = {}
    for name in sorted(args):
        key = name[0]
        if key not in employees:
            employees[key] = []
        if key in employees:
            employees[key].append(name)
    return employees


print(thesaurus("Елена", "Раиса", "Максим", "Елизавета", "Николай", "Борис", "Андрей"))
