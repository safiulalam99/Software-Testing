from ArithmeticOperations import ArithmeticOperations
from BankAccount import BankAccount
from DateManipulations import DateManipulations
from GeometryCalculations import GeometryCalculations
from ListManager import ListManager
from Stack import Stack
from StringManipulation import StringManipulation
from StringFormatting import StringFormatting
from BasicStatistics import BasicStatistics
from Queue import Queue
import datetime


def main():
    # ArithmeticOperations demo
    print("*********************************")
    print("ArithmeticOperations")
    print("*********************************")
    arithmetic = ArithmeticOperations()
    print("Addition:", arithmetic.add(2, 3))
    print("Subtraction:", arithmetic.subtract(5, 3))
    print("Multiplication:", arithmetic.multiply(2, 3))
    print("Division:", arithmetic.divide(6, 3))
    print("Power:", arithmetic.power(2, 3))

    # BankAccount demo
    print("")
    print("*********************************")
    print("BankAccount")
    print("*********************************")
    account1 = BankAccount(100)
    account2 = BankAccount(200)
    account1.deposit(50)
    account1.withdraw(25)
    account1.transfer(account2, 50)
    print("Account 1 balance:", account1.get_balance())
    print("Account 2 balance:", account2.get_balance())

    # DateManipulations demo
    print("")
    print("*********************************")
    print("DateManipulations")
    print("*********************************")
    date1 = datetime.date(2022, 1, 1)
    date2 = datetime.date(2023, 1, 1)
    print("Days between dates:", DateManipulations.days_between_dates(date1, date2))
    print("Leap year check:", DateManipulations.is_leap_year(2020))
    print("Day of week:", DateManipulations.day_of_week(date1))
    print("Days in month:", DateManipulations.days_in_month(2022, 2))

    # GeometryCalculations demo
    print("")
    print("*********************************")
    print("GeometryCalculations")
    print("*********************************")
    print("Rectangle area:", GeometryCalculations.rectangle_area(2, 3))
    print("Triangle area:", GeometryCalculations.triangle_area(3, 4))
    print("Circle area:", GeometryCalculations.circle_area(5))
    print("Circle circumference:", GeometryCalculations.circle_circumference(5))
    print("Can form triangle:", GeometryCalculations.can_form_triangle(3, 4, 5))

    # ListManager demo
    print("")
    print("*********************************")
    print("ListManager")
    print("*********************************")
    list_manager = ListManager()
    list_manager.add_item(1)
    list_manager.add_item(2)
    list_manager.add_item(3)
    list_manager.remove_item(2)
    print("ListManager items:", list_manager.data)
    print("ListManager item count:", list_manager.count_items())
    print("ListManager reversed items:", list_manager.reverse_items())

    # Stack demo
    print("")
    print("*********************************")
    print("Stack")
    print("*********************************")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack size:", stack.size())
    print("Stack is empty:", stack.is_empty())
    print("Stack top item:", stack.peek())
    print("Stack pop:", stack.pop())
    print("Stack size after pop:", stack.size())
    print(f"Stack size: {stack.size()}, top: {stack.peek()}")

    # Queue demo
    print("")
    print("*********************************")
    print("Queue")
    print("*********************************")
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"Queue front: {queue.peek()}")
    print(f"Dequeued value: {queue.dequeue()}")
    print(f"Dequeued value: {queue.dequeue()}")
    print(f"Is the queue empty? {queue.is_empty()}")
    print(f"Queue size: {queue.size()}")
    print(f"Dequeued value: {queue.dequeue()}")

    # StringFormatting demo
    print("")
    print("*********************************")
    print("StringFormatting")
    print("*********************************")
    text = "hello world"
    print("Uppercase:", StringFormatting.to_uppercase(text))
    print("Lowercase:", StringFormatting.to_lowercase(text))
    print("Capitalize words:", StringFormatting.capitalize_words(text))
    print("Strip whitespace:", StringFormatting.strip_whitespace(text))
    print("Replace spaces with underscores:",
          StringFormatting.replace_spaces_with_underscores(text))

    # StringManipulation demo
    print("")
    print("*********************************")
    print("StringManipulation")
    print("*********************************")
    string = "racecar"
    print("Reverse string:", StringManipulation.reverse_string(string))
    print("Palindrome check:", StringManipulation.is_palindrome(string))
    print("Vowel count:", StringManipulation.count_vowels(string))
    print("Substring count:", StringManipulation.count_substring(string, "c"))
    print("Replace substring:",
          StringManipulation.replace_substring(string, "c", "d"))

    # BasicStatistics demo
    print("")
    print("*********************************")
    print("BasicStatistics")
    print("*********************************")
    numbers = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9]
    print("Mean:", BasicStatistics.mean(numbers))
    print("Median:", BasicStatistics.median(numbers))
    print("Mode:", BasicStatistics.mode(numbers))
    print("Range:", BasicStatistics.range_of_numbers(numbers))
    print("Standard Deviation:", BasicStatistics.standard_deviation(numbers))


if __name__ == "__main__":
    main()
