"""Простой пример для лабораторной работы №1."""


def greet(name: str = "Git") -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet())
