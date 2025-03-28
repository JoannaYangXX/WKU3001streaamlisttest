# code_05_10_change_me.py
#5.5: Passing Arguments to Functions

# 이 예제는 패러미터의 값을 바꿨을떄 생기는 일을 보여주는 예제

def main():
    value = 99
    print('The value is', value)
    change_me(value)
    print('Back in main value is', value)

def change_me(arg):
    print('I am change the value.')
    arg = 0
    print('Now the valu is', arg)

main()