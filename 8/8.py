import argparse

parser = argparse.ArgumentParser(description="Простой CLI")
parser.add_argument("name", help="Ваше имя")
parser.add_argument("-a", "--age", type=int, help="Ваш возраст")
parser.add_argument("--verbose", action="store_true", help="Подробный вывод")

args = parser.parse_args()
args.age = args.age if args.age else "Неизвестен"
if args.verbose:
    print(f"Привет, {args.name}! Твой возраст: {args.age}.")
else:
    print(f"Привет, {args.name}!")
