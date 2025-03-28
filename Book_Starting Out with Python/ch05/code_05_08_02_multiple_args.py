# code_05_08_02_multiple_args.py
#5.5: Passing Arguments to Functions

# 이 프로그램은 두개의 인자를 보내는 예제임

def main():
    print('Input 2 numbers')
    n1 = int(input('Enter 1st number: '))
    n2 = int(input('Enter 2nd number: '))
    show_sum(n1, n2)

# show_sum 함수는 두개의 인자를 수용함 그리고 그 합을 출력
def show_sum(num1, num2):
    result = num1 + num2
    print('the sum is', result)

# main() 펑션을 불러옴
main()