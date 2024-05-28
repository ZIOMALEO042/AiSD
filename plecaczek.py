import itertools
def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Proszę podać poprawną liczbę całkowitą.")


def get_item_input():
    while True:
        try:
            x, y = map(int, input().split())
            if x > 0 and y > 0:
                return x, y
            else:
                print("Obie wartości muszą być dodatnie.")
        except ValueError:
            print("Proszę podać dwie liczby całkowite oddzielone spacją.")


def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            n, c = map(int, lines[0].strip().split())
            items = []
            for i in range(1, len(lines)):
                x, y = map(int, lines[i].strip().split())
                items.append([i, x, y])
            return n, c, items
    except FileNotFoundError:
        print("Plik nie został znaleziony.")
        return None
    except Exception as e:
        print(f"Błąd podczas wczytywania pliku: {e}")
        return None


def knapsack_bf(n, c, items):
    result = []
    max_value = 0
    elements = range(1, n + 1)
    all_combinations = []

    for r in range(1, n + 1):
        combinations = itertools.combinations(elements, r)
        all_combinations.extend(combinations)

    for combo in all_combinations:
        c_rest = c
        w = 0
        f = 0

        for el in combo:
            w += items[el - 1][1]
            f += items[el - 1][2]
            c_rest -= items[el - 1][1]

        if w <= c and max_value < f:
            result = combo
            max_value = f
            result_w = w
    if len(result)==0:
        print("Zadnego przedmiotu nie da sie wlozyc do plecaka")
        return
    print("id_elementow: ", end="")
    for el in result:
        print(el, end=" ")
    print(f"\nw(X)={result_w} fmax(X)={max_value}")


def knapsack_greedy(n, c, items):
    result = []
    w = 0
    f = 0
    items_with_profits = [[i + 1, item[1], item[2], item[2] / item[1]] for i, item in enumerate(items)]
    items_with_profits = sorted(items_with_profits, key=lambda x: x[3], reverse=True)
    c_rest = c

    for i in range(n):
        if w + items_with_profits[i][1] <= c:
            w += items_with_profits[i][1]
            f += items_with_profits[i][2]
            c_rest -= items_with_profits[i][1]
            result.append(items_with_profits[i])
        else:
            break
    if len(result)==0:
        print("Zadnego przedmiotu nie da sie wlozyc do plecaka")
        return
    print("id_elementow: ", end="")
    for el in result:
        print(el[0], end=" ")
    print(f"\nw(X)={w} f(X)={f} reszta miejsca={c_rest}")


def main():
    print("Wybierz tryb:")
    print("1. Wszystkie kombinacje")
    print("2. Algorytm zachłanny")
    choice = get_int_input("Podaj wybor: ")

    print("Wybierz źródło danych:")
    print("1. Wprowadz dane ręcznie")
    print("2. Wczytaj dane z pliku")
    data_choice = get_int_input("Podaj wybor: ")

    if data_choice == 1:
        n = get_int_input("Podaj liczbe przedmiotow: ")
        c = get_int_input("Podaj udzwig plecaka: ")
        items = []
        for i in range(n):
            print(f"Przedmiot {(i + 1)}: ", end=" ")
            x, y = get_item_input()
            items.append([i + 1, x, y])
    elif data_choice == 2:
        filename = "plecak.txt"
        data = read_from_file(filename)
        if data:
            n, c, items = data
        else:
            return
    else:
        print("Nieprawidłowy wybór!")
        return

    if choice == 1:
        knapsack_bf(n, c, items)
    elif choice == 2:
        knapsack_greedy(n, c, items)
    else:
        print("Nieprawidłowy wybór!")


if __name__ == "__main__":
    main()
