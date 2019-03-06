class Bob:
    def fizzbuzz(self, number):
        if (number % 15 == 0):
            print('FizzBuzz')
        elif (number % 5 == 0):
            print('Buzz')
        elif (number % 3 == 0):
            print('Fizz')
        else:
            print(number)

bob = Bob()
bob.fizzbuzz(30)

print("Hello, World!")
