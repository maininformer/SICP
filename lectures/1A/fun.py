from functools import partial

# how to find sqrt?
def sqrt(x, guess, delta=0.0001):
    if abs(guess - x/guess) < delta:
        return guess
    else:
        return sqrt(x, (guess + x/guess)/2)

##############################################
# how to find fixed points?
def fixed_point(f, guess, delta=0.0001):
    if abs(guess - f(guess)) < delta:
        return guess
    else:
        return fixed_point(f, f(guess))

def sqrt_p(x, guess):
    # if guess == sqrt x then (guess + x/guess) / 2 = guess
    return (guess + x/guess) / 2

###############################################

def new_sqrt(x, y, delta = 0.0001):
    return fixed_point(lambda guess: (guess + x/guess) / 2, y, delta=delta)
# so giving average of guess and x/guess to the fixed point gives us sqrt!
# procedure whose value is another procedure.

print(sqrt(260, 5))
print(fixed_point(partial(sqrt_p,260), 5))
print(new_sqrt(260, 5))


def average(*args):
    return sum(args) / len(args)

def sqrt(x):
    def improve(guess):
        return average(guess, x / guess)

    def is_good_enough(guess):
        return abs(guess ** 2 - x ) < 0.0001

    def try_(guess):
        if is_good_enough(guess):
            return guess
        return try_(improve(guess))

    return try_(1)

print(sqrt(260))
