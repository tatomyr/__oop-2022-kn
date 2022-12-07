def function():
    print("Hello World!")


def sum_two_numbers(a, b):
    return a + b


def list_benefits():
    return [
        "More organized code",
        "More readable code",
        "Easier code reuse",
        "Allowing programmers to share and connect code together",
    ]


def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))


function()
print("Sum of 5 and 3 equals %d" % sum_two_numbers(5, 3))
name_the_benefits_of_functions()
