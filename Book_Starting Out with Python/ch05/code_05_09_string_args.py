# code_05_09_string_args.py
#5.5: Passing Arguments to Functions

# 이 예제는 2개의 문자열을 보냄

def main():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    print('Your name reversed is')
    reverse_name(first_name, last_name)

def reverse_name(first, last):
    print(last, first)

main()