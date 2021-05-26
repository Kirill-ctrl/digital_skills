
def list_to_dict(arr: list) -> dict:
    return {
        item: arr.count(item)
        for item in arr
    }


def strings_interspec(str1: str, str2: str) -> set:
    result = {
        ''.join(item)
        for item in str1.split()
        for symb in str2.split()
        if item == symb
    }
    return result


def longest_ascending_seq(arr: list[int]) -> list:
    result = []
    prom = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            prom.append(arr[i])
        else:
            result.append(prom)
            prom = [arr[i]]
    else:
        result.append(prom)
    return max(result, key=len)
