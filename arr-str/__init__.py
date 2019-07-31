from collections import defaultdict


def all_unique_dict(s):
    d = defaultdict(int)
    for c in s:
        if d[c] == 1:
            return False
        d[c] += 1
    return True


def all_unique(s):
    for i, c in enumerate(s):
        for j in range(i + 1, len(s)):
            r = s[j]
            if c == r:
                return False
    return True


def main():
    assert all_unique_dict("abc") is True
    assert all_unique_dict("aba") is False
    assert all_unique_dict("aaa") is False

    assert all_unique("abc") is True
    assert all_unique("aba") is False
    assert all_unique("aaa") is False


if __name__ == "__main__":
    main()
