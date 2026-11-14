def longest_common_prefix(strs: list[str]) -> str:
    for i in range(len(strs[0])):
        char = strs[0][i]

        for string in strs[1:]:
            if i >= len(string) or string[i] != char:
                return strs[0][:i]

    return strs[0]


def longest_common_prefix_python(strs: list[str]) -> str:
    prefix = strs[0]

    for string in strs[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]

            if not prefix:
                return ""

    return prefix