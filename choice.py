KEYS = set()


class Key:

    name = ""
    lower = []
    equal = []
    higher = []

    def __init__(self, name):
        self.name = name


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


def registerCache(result: bool, key1_name: str, key2_name: str):
    """Anahtarı hafızaya kaydetme

    Arguments:
        result {bool} -- Key1 büyükse True
        key1_name {str} -- 1. anahtarın ismi
        key2_name {str} -- 2. anahtarın ismi
    """
    def _isHigher():
        return result

    def _addKey():
        key1Object = Key(key1_name)
        key2Object = Key(key2_name)

        if _isHigher():
            key1Object.lower.append(key2Object)
            key2Object.higher.append(key1Object)
        else:
            key1Object.higher.append(key2Object)
            key2Object.lower.append(key1Object)

        KEYS.add(key1_name, key2_name)

    return _addKey()


def isBetter(key1, key2, equal=False) -> bool:
    result = compare(0, key1, key2)
    registerCache(result, key1, key2)
    return result


def isWorse(key1, key2, equal=False) -> bool:
    return compare(1, key1, key2)
