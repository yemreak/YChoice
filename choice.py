
def compare(x, *keys, equal=False) -> bool:

    def _compare():
        msg = "Büyük olanı seçin\n"
        msg += "Seçin - Sayı\n"
        msg += "----------------\n"
        for i, key in enumerate(keys):
            msg += f"{i} - {key}\n"

        while(True):
            try:
                y = int(input(msg))
                break
            except ValueError:
                print("Hatalı seçim, tekrar deneyin")

        return x == y

    return (equal and keys[0] == keys[1]) or _compare()


def isBetter(key1, key2, equal=False) -> bool:
    return compare(0, key1, key2)


def isWorse(key1, key2, equal=False) -> bool:
    return compare(1, key1, key2)
