students = {
    'Alice': {
        'Math': 85,
        'Science': 92,
        'English': 88
    },
    'Bob': {
        'Math': 78,
        'Science': 81,
        'English': 79
    },
    'Charlie': {
        'Math': 95,
        'Science': 89,
        'English': 93
    }
}


def accessing_values(n,s):
    for name,subjects in students.items():
        if name ==n:
            print(name,subjects[s])

accessing_values('Charlie','English')

for stu in students['Alice']:
    print(stu)




