# Demonstrate the use of all logical operators (and, or, not) below.
# Create variables that hold boolean values, then combine them
# to express the following sentence:
#   do two wrongs make a right?
# Note that the truth value of the statement doesn't matter,
# but try to use all three logical operators in one line of code
# to get another boolean value as your result :)

wrong = False
right = True
oper_and = wrong and wrong
print(oper_and)
oper_or = wrong or right
print(oper_or)
oper_not = not right
print(oper_not)
oper_all = (right and right) and (right or wrong) or (not right)
print(oper_all)
