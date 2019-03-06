class Bob:
    def fizzbuzz(self, number):
        if (number % 15 == 0):
            return('FizzBuzz')
        elif (number % 5 == 0):
            return('Buzz')
        elif (number % 3 == 0):
            return('Fizz')
        else:
            return(number)

bob = Bob()
bob.fizzbuzz(3)

print("Hello, World!")
