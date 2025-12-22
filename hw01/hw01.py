'''ФУНКЦІЯ caching_fibonacci
    Створити порожній словник cache

    ФУНКЦІЯ fibonacci(n)
        Якщо n <= 0, повернути 0
        Якщо n == 1, повернути 1
        Якщо n у cache, повернути cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        Повернути cache[n]

    Повернути функцію fibonacci
КІНЕЦЬ ФУНКЦІЇ caching_fibonacci
'''


def caching_fibonacci() -> int: 
    '''
    Функція caching_fibonacci створює внутрішню функцію fibonacci і 
    словник cache для зберігання результатів обчислення чисел Фібоначчі. 
    '''
    # створєюмо пустий словник
    cache = {} 

    def fibonacci(n: int) -> int: 
        if n <= 0: 
            return 0
        if n == 1:
            return 1
        if n in cache: 
            # якщо число вже в кеші - повертаємо значення з кешу
            return cache[n] 
        
        # якщо числа немає - робимо обчислення і добавляємо в кеш
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2) 
        return cache[n] 
    
    return fibonacci


def main():
    fib = caching_fibonacci()   
    print(fib(10)) 
    print(fib(15))





if __name__ == '__main__':
    main()