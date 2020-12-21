def product_three(list_nums):
    if len(list_nums) < 3:
        raise ValueError("Less than 3 items!")

    highest = max(list_nums[0], list_nums[1])
    lowest = min(list_nums[0], list_nums[1])
    highest_product_2 = list_nums[0] * list_nums[1]
    lowest_product_2 = list_nums[0] * list_nums[1]

    highest_product_3 = list_nums[0] * list_nums[1] * list_nums[3]
    for i in range(2, len(list_nums)):
        current = list_nums[i]

        highest = max(highest, current)
        lowest = min(lowest, current)

        highest_product_2 = max(highest_product_2, highest * current, lowest * current)
        lowest_product_2 = min(lowest_product_2, current * highest, current * lowest_product_2)

        highest_product_3 = max(highest_product_3, current * highest_product_2, current * lowest_product_2)



def main():
    nums = [1,2,3,4]