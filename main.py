# Modify your program from Exercise 6-2 (page
# 99) so each person can have more than one
# favorite number. Then print each person's name
# along with their favorite numbers.

favorite_numbers = {
    'ernest': {
        48,
        49,
    },
    'dad': {
        6,
        8,
    },
    'mom': {
        17,
        27,
    },
}

for key, value in favorite_numbers.items():
    print(f"\n{key}'s favorite numbers are: ")
    print(f"{value}")
