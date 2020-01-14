from fizzbuzz import fb

inputs = [1, 3, 5, 15]
results = ["1", "Fizz", "Buzz", "FizzBuzz"]


def test_fb():
    for i in range(len(inputs)):
        assert fb(inputs[i]) == results[i]
