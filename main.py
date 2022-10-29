# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def add_number(a, b):
    if not isinstance(a, (int, float)):
        print("a is not a number")
        return
    if not isinstance(b, (int, float)):
        print("b is not a number")
        return
    print("a + b = " + str(a + b))


# ---------------------- 一元二次方程解法 ---------------------------

def judge_root(a, b, c):
    return b * b - 4 * a * c


def quadratic(a, b, c):
    if not isinstance(a + b + c, (int, float)):
        print("传参不是数字！")
        return
    if judge_root(a, b, c) < 0:
        print("无解！")
        return
    if judge_root(a, b, c) == 0:
        print("有同一个解")
    if judge_root(a, b, c) > 0:
        print("有两个不同的解")
    x1 = ((-b) + math.sqrt(b * b - 4 * a * c)) / 2 * a
    x2 = ((-b) - math.sqrt(b * b - 4 * a * c)) / 2 * a
    print("一元二次方程的解为：", (x1, x2))
    return x1, x2


# ---------------------- 默认参数 ---------------------------
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s *= x
    print("%d的%d次方为：%d" % (x, n, s))


# ---------------------- 可变参数 ---------------------------
# list，tuple转化为可变参数，前面直接加*
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n

    print("cal = %d" % sum)
    return sum


def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    L = len(height)
    i = 0
    j = L - 1
    max_value = 0
    while i < j:
        temp = min(height[i], height[j]) * (j - i)
        max_value = max(max_value, temp)
        if height[i] < height[j]:
            i = i + 1
        else:
            j = j - 1

    return max_value


def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    # phone_data = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
    L = len(digits)
    result = []
    if L == 0:
        return result
    getChar(result, "", digits, 0)
    print(result)


def getChar(result, strs, digits, deep):
    phone_data = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
                  "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
    digits_L = len(digits)
    # 纵向遍历，返回上一层继续遍历
    if deep >= digits_L:
        result.append(strs)
        return

    # 按层寻找，先确定层
    char = digits[deep]
    data = phone_data[char]

    # 横向遍历
    for single_str in data:
        strs = strs + single_str
        getChar(result, strs, digits, deep + 1)
        strs = strs[:-1]

    # Press the green button in the gutter to run the script.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createList(L3_str):
    head = None
    p = None
    for i in L3_str:
        if head == None:
            head = ListNode(int(i), None)
            p = head
        else:
            temp = ListNode(int(i), None)
            p.next = temp
            p = temp

    return head


def printList(head):
    while head is not None:
        print(head.val)
        head = head.next


def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """

    p = head
    tail = head
    L = 0

    while tail is not None:
        L = L + 1
        tail = tail.next

    if L - n == 0:
        p = head.next
        head = None
        return p
    for i in range(L - n - 1):
        p = p.next

    q = p.next
    p.next = q.next
    q = None
    return head


def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    p = head
    if p is None or p.next is None:
        return head
    q = p.next
    index = 1
    changed = False
    last = ListNode(-1, head)
    while (not changed and p.next is not None) or (changed and q.next is not None):
        if index % 2 == 1:
            # 交换顺序
            if not changed:
                last.next = q
                p.next = q.next
                q.next = p
                changed = True
                last = p
            else:
                last.next = p
                q.next = p.next
                p.next = q
                last = q
                changed = False
            if index == 1:
                head = q

        p = p.next
        q = q.next

        index = index + 1

    return head


def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    L = len(nums)
    head = i = 0
    tail = j = L - 1
    start = -1
    end = -1

    while i <= j:
        mid = int((i + j) / 2)
        if nums[mid] == target:
            start = end = mid
            mid_head = mid_tail = mid
            while mid_tail >= head:
                if nums[mid_tail] == target:
                    start = mid_tail

                mid_tail = mid_tail - 1
            while mid_head <= tail:
                if nums[mid_head] == target:
                    end = mid_head
                mid_head = mid_head + 1
            break
        elif nums[mid] > target:
            j = mid - 1
        else:
            i = mid + 1

    return [start, end]


if __name__ == '__main__':
    print(searchRange([1], 1))
    # head = createList([1, 2, 3, 4, 5])
    # head = swapPairs(head)
    # printList(head)
    # letterCombinations("")
    # print_hi('PyCharm')
    # add_number(2, 4)
    # add_number("154", 52)
    # quadratic(2, 3, 1)
    # quadratic(1, 3, -4)
    # power(4, 3)
    # # print_hi('PyCharm')
    # # print(r"\\\t\\\"")
    # print('中文'.encode("utf-8"))
    # print('asd'.encode("ascii"))
    # print(ord('a'))
    # print('成绩提升了%.2f%%' % 13232.343)
    # s = 13234.4334534
    # print(f'dkfjdl{s:.3f}')
    #
    # calc(1, 2)
    # print(maxArea([1, 1]))
    pass
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
