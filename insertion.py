import sys
from pathlib import Path
from choice import isWorse

SEPERATOR = "\n"

# Function to do insertion sort


def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and isWorse(arr[j], key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def main(args):
    path = Path(args[0])

    if not path.exists():
        return

    arr = path.read_text(encoding="utf-8").split(SEPERATOR)

    insertionSort(arr)
    print(arr)

    outpath = (Path)(path.parent / "slist.txt")
    outpath.write_text(SEPERATOR.join(arr), encoding="utf-8")


def test():
    arr = ["Android", "Java", "Python", "YEmreAk"]
    insertionSort(arr)

    print(arr)


if __name__ == "__main__":
    main(sys.argv[1:]) if len(sys.argv) > 1 else test()
    input()
