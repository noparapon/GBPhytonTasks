class ErrDiv(Exception):

    def __str__(self):
        return "Детская ошибка! Нельзя делить на ноль!"


def div(op1, op2):
    try:
        if op2 == 0:
            raise ErrDiv
        return op1 / op2
    except Exception as e:
        print("хм... что-то пошло не так:", e)


print(div(2, 3))
print(div(4, 0))