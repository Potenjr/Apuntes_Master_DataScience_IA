# ============================================
# Programación Funcional en Python (con menú)
# ============================================

from functools import reduce

# ============================================
# Utils y dataset
# ============================================

def average(grades):
    return sum(grades) / len(grades)


students = [
    {"name": "Ana", "grades": [8, 7, 9], "absences": 1},
    {"name": "Luis", "grades": [5, 6, 4], "absences": 3},
    {"name": "Marta", "grades": [9, 9, 10], "absences": 0},
    {"name": "Juan", "grades": [6, 7, 6], "absences": 2},
    {"name": "Sofia", "grades": [4, 5, 6], "absences": 4},
]


raw_students = [
    {"name": "Ana", "grades": [8, 7, 9], "absences": 1},
    {"name": "Luis", "grades": [], "absences": 3},
    {"name": "Marta", "grades": [9, 9, 10], "absences": 0},
    {"name": "Juan", "grades": None, "absences": 2},
    {"name": "Sofia", "grades": [4, 5, 6], "absences": 4},
    {"name": "Elena", "grades": [10, 9, 9], "absences": 0},
]


# ============================================
# Ejercicios
# ============================================

def ejercicio1():
    def add_one(x):
        return x + 1

    def apply_twice(fn, x):
        return fn(fn(x))

    print("Resultado:", apply_twice(add_one, 10))


def ejercicio2():
    celsius = [0, 10, 20, 30]
    to_fahrenheit = lambda c: c * (9 / 5) + 32
    fahrenheit = [to_fahrenheit(c) for c in celsius]
    print("Fahrenheit:", fahrenheit)


def ejercicio3():
    averages = list(map(lambda s: (s["name"], average(s["grades"])), students))
    print(averages)


def ejercicio4():
    filtered = list(
        filter(lambda s: average(s["grades"]) >= 6 and s["absences"] <= 2, students)
    )
    print(filtered)


def ejercicio5():
    total = reduce(lambda acc, s: acc + average(s["grades"]), students, 0)
    print("Suma total:", total)


def ejercicio6():
    result = [s["name"] for s in students if s["absences"] == 0]
    print(result)


def ejercicio7():
    has_low = any(grade < 5 for s in students for grade in s["grades"])
    all_pass = all(average(s["grades"]) >= 6 for s in students)

    print("Alguna nota <5:", has_low)
    print("Todos aprueban:", all_pass)


def ejercicio8():
    ranked = sorted(
        students,
        key=lambda s: (-average(s["grades"]), s["absences"]),
    )

    top3 = ranked[:3]

    for s in top3:
        print(s["name"], average(s["grades"]), s["absences"])


def ejercicio9():
    result = filter(lambda s: s["grades"], raw_students)

    result = list(
        map(
            lambda s: {
                "name": s["name"],
                "average": average(s["grades"]),
                "absences": s["absences"],
            },
            result,
        )
    )

    result = list(
        filter(lambda s: s["average"] >= 6 and s["absences"] <= 2, result)
    )

    result = sorted(result, key=lambda s: (-s["average"], s["absences"]))

    for s in result:
        print(s)


def reto():
    honor = [
        s["name"]
        for s in raw_students
        if s["grades"]
        and average(s["grades"]) >= 8.5
        and s["absences"] == 0
    ]
    print("Honor roll:", honor)


# ============================================
# Menú
# ============================================

def mostrar_menu():
    print("\n===== MENÚ =====")
    print("1. apply_twice")
    print("2. lambda Celsius -> Fahrenheit")
    print("3. map (promedios)")
    print("4. filter (aprobados)")
    print("5. reduce (suma)")
    print("6. list comprehension (asistencia perfecta)")
    print("7. any / all")
    print("8. ranking top 3")
    print("9. pipeline funcional")
    print("10. reto (honor roll)")
    print("0. salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            ejercicio1()
        elif opcion == "2":
            ejercicio2()
        elif opcion == "3":
            ejercicio3()
        elif opcion == "4":
            ejercicio4()
        elif opcion == "5":
            ejercicio5()
        elif opcion == "6":
            ejercicio6()
        elif opcion == "7":
            ejercicio7()
        elif opcion == "8":
            ejercicio8()
        elif opcion == "9":
            ejercicio9()
        elif opcion == "10":
            reto()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()