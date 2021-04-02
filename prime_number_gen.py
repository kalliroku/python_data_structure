# prime number generator

def main():
    import sys
    import math
    inp = lambda: int(sys.stdin.readline())
    input_number = inp()
    limit = input_number // 2
    nums = [2] + [(i * 2) + 1 for i in range(1, limit)]
    check = [0] * (limit + 1)
    for idx in range(1, int(math.sqrt(input_number)) // 2):
        if not check[idx]:
            num = nums[idx]
            check_idx = (num ** 2 - 1) // 2
            while check_idx < limit + 1:
                check[check_idx] = 1
                check_idx += num

    prime_nums = []
    for j in range(len(check)):
        if not check[j]:
            prime_nums.append(nums[j])

    print(prime_nums)
    print(len(prime_nums))
