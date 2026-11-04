# Assessment 3.2 - Array Implementation
def main():
    array = []

    # Operations according to Assessment 3.1
    # Adding elements: 'L', 'A', 'T', 'A', 'Y', 'A', 'D', 'A'
    elements_to_add = ['L', 'A', 'T', 'A', 'Y', 'A', 'D', 'A']

    print("--- Adding Elements to Array ---")
    for item in elements_to_add:
        array.append(item)
        print(f"Added '{item}': Current Array = {array}")

    print(f"\nFinal filled array: {array}\n")

    # Removing elements in reverse sequence as specified in algorithm
    elements_to_remove = ['A', 'D', 'A', 'Y', 'A', 'T', 'A', 'L']

    print("--- Removing Elements from Array ---")
    for item in elements_to_remove:
        array.remove(item)
        print(f"Removed '{item}': Current Array = {array}")

    print("\nArray is now Empty. End.")


if __name__ == "__main__":
    main()