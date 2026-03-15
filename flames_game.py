def get_clean_name(prompt):
    while True:
        name = input(prompt).strip()
        if not name:
            print("Name cannot be empty. Please enter again.")
            continue
        # Keep only alphabetic characters and convert to lowercase
        clean = "".join(ch.lower() for ch in name if ch.isalpha())
        if not clean:
            print("Name must contain at least one letter. Please enter again.")
            continue
        return clean


def count_uncommon_letters(name1, name2):
    # Convert to lists so we can "cancel out" common letters
    list1 = list(name1)
    list2 = list(name2)

    for ch in name1:
        if ch in list2:
            list1.remove(ch)
            list2.remove(ch)

    return len(list1) + len(list2)


def flames_result(count):
    flames = ["F", "L", "A", "M", "E", "S"]
    meanings = {
        "F": "Friends",
        "L": "Love",
        "A": "Affection",
        "M": "Marriage",
        "E": "Enemies",
        "S": "Siblings",
    }

    # If count is 0, treat them as Friends by default
    if count == 0:
        return "Friends"

    index = 0
    while len(flames) > 1:
        # Index of letter to remove based on count
        index = (index + count - 1) % len(flames)
        flames.pop(index)

    return meanings[flames[0]]


def main():
    print("===== FLAMES GAME =====")
    name1 = get_clean_name("Enter the first name: ")
    name2 = get_clean_name("Enter the second name: ")

    count = count_uncommon_letters(name1, name2)
    result = flames_result(count)

    print("\nResult:")
    print(f"The relationship between {name1.title()} and {name2.title()} is: {result}")


if __name__ == "__main__":
    main()