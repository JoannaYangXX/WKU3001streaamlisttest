# code_05_08_01_multiple_args.py
#5.5: Passing Arguments to Functions

# 이 프로그램은 두개의 인자를 보내는 예제임

def main():
    print('The sum of 12 and 45 is ')
    show_sum(12, 45)

# show_sum 함수는 두개의 인자를 수용함 그리고 그 합을 출력
def show_sum(num1, num2):
    result = num1 + num2
    print(result)

# main() 펑션을 불러옴
main()