from car import Car, CarException


def main():
    try:
        Car().run()
    except CarException as exc:
        print(f"Application failed with error : {exc}")


if __name__ == '__main__':
    main()
