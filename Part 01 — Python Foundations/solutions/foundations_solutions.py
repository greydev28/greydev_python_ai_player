"""Reference solutions for selected Part 01 exercises. Run with Python 3."""

def minutes_to_hours(minutes: int) -> tuple[int, int]:
    if minutes < 0:
        raise ValueError("minutes cannot be negative")
    return divmod(minutes, 60)


def is_leap_year(year: int) -> bool:
    if year < 1:
        raise ValueError("year must be positive")
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def count_vowels(text: str) -> int:
    return sum(character.lower() in "aeiou" for character in text)


def multiplication_table(number: int) -> list[str]:
    return [f"{number} x {factor} = {number * factor}" for factor in range(1, 13)]


if __name__ == "__main__":
    print(minutes_to_hours(135))  # (2, 15)
    print(is_leap_year(2000))     # True
    print(is_leap_year(1900))     # False
    print(count_vowels("Greydev AI"))  # 4
    print("\\n".join(multiplication_table(7)))
