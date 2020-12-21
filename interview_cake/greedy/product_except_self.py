def product_except_self(nums):
    beforeProduct = [1]
    for i in range(0, len(nums)-1):
        beforeProduct.append(beforeProduct[-1] * nums[i])

    print(beforeProduct)

def main():
    nums = [3, 1, 2, 5, 6, 4]
    product_except_self(nums)

main()