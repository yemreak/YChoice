KEYS = {}


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


def registerCache(result, key1, key2):

    calcCount = 0

    def _exists(value):
        return value in KEYS.values

    def _calcValue(value):
        nonlocal calcCount
        calcCount += 1

        if result:
            value += (1 / 2) ** calcCount
        else:
            value -= (1 / 2) ** calcCount

        return value

    def _addIfEmpty(key, value):
        if not _exists(value):
            KEYS[key] = value
        else:
            value = _calcValue(value)
            _addIfEmpty(key, value)

    pass


def isBetter(key1, key2, equal=False) -> bool:
    result = compare(0, key1, key2)
    registerCache(result, key1, key2)
    return result


def isWorse(key1, key2, equal=False) -> bool:
    return compare(1, key1, key2)
