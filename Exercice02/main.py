students = {
    'Alice': {
        'Mathematiques': 90,
        'Francais': 80,
        'Histoire': 95
    },
    'Bob': {
        'Mathematiques': 75,
        'Francais': 85,
        'Histoire': 70
    },
    'Charlie': {
        'Mathematiques': 88,
        'Francais': 92,
        'Histoire': 78
    }
}

def ex02(students_list):
    name = input(f"Entrez le nom de l’étudiant : ")
    if name in students_list:
        student = students_list[name]
        total_note = 0
        for category in student:
            note = student[category]
            total_note += int(note)
            print(f"Notes de {name} : {category} {str(note)}")
        print(f"Moyenne de {name} : {str(total_note/3)}")
    else:
        print(f"L'étudiant {name} n'existe pas dans la liste")


if __name__ == '__main__':
    ex02(students)
