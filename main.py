from mapapi_pg import show_map


def main():
    ll = input("Введите координаты без пробелов через запятую: ")
    spn = input("Введите масштаб: ")
    ll_spn = f"ll={ll}&spn={spn}"
    show_map(ll_spn, "map")


if __name__ == '__main__':
    main()


# пример
# координаты: 47.508581,42.981583
# spn: 0.0041055000000014275,0.003014499999999032
