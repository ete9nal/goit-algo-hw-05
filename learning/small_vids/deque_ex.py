from collections import deque

def main():
    user_inputs = deque(maxlen=10)
    while True:
        user_input = input('>>> ')
        user_inputs.append(user_input)
        if user_input == 'q':
            break
    print('Good Bye')
    print(f'User steps: {user_inputs}')

if __name__ == '__main__':
    main()