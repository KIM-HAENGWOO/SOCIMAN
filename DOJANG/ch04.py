def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

result = add_many(1,2,3,4,5)
print(result)

# ------
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)
result = add_mul('mul', 1,2,3,4,5)
print(result)

# -----------

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', age=3)

# ----------

def add_and_mul(a,b):
    return a+b, a*b

result = add_and_mul(3,4)
print(result)

result1, result2 = add_and_mul(3,4)
print(result1, result2)
print(result1)
print(result2)

# ----------

def say_nick(nick):
    if nick == '바보':
        return
    print("나의 별명은 %s 입니다." % nick)

say_nick('심여수')
say_nick('바보')
say_nick('돌덩이')

# ----------

def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살 입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("김행우", 56)
say_myself("김행우", 56, True)
say_myself("윤혜원", 51, False)

# ----------- 초기화 매개변수는 항상 뒤쪽에 놓아야 한다. 





