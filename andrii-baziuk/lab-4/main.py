# Functions
def function():
    print("Hello from function")


# Functions with arguments
def function_with_args(greeting, name):
    print("%s %s, from function with args" % (greeting, name))


def sum_two_numbers(a, b):
    return a + b


# Callbacks
def list_benefits():
    return [
        "More organized code",
        "More readable code",
        "Easier code reuse",
        "Allowing programmers to share and connect code together",
    ]


def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions(benefits):
    for benefit in benefits:
        print(build_sentence(benefit))


function()
function_with_args("Hello", "Andrii")
print("Sum of 5 and 3 equals %d" % sum_two_numbers(5, 3))
benefits = list_benefits()
name_the_benefits_of_functions(benefits)
