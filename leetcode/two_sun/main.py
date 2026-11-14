import time


def two_sum_dict(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []


def two_sum_list(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []


def main() -> None:
    nums = list(range(10_000))
    target = 19_997

    start = time.perf_counter()
    result_dict = two_sum_dict(nums, target)
    end = time.perf_counter()

    dict_time = end - start

    start = time.perf_counter()
    result_list = two_sum_list(nums, target)
    end = time.perf_counter()

    list_time = end - start

    print(f"Dict:   resultado={result_dict}, tempo={dict_time:.6f}s")
    print(f"Lista:  resultado={result_list}, tempo={list_time:.6f}s")


if __name__ == "__main__":
    main()