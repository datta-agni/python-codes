# Palindrome Dates

from datetime import datetime
from itertools import chain


# palindrome_day :: Int -> [ISO Date]
def palindrome_day(y):
    # A possibly empty list containing the palindromic date for the given year, if such a date exists.

    s = str(y)
    r = s[::-1]
    iso = '-'.join([s, r[0:2], r[2:]])
    try:
        datetime.strptime(iso, '%Y-%m-%d')
        return [iso]
    except ValueError:
        return []


def main():
    # Count and samples of palindromic dates [2021..9999]

    palindrome_dates = list(
        chain.from_iterable(map(palindrome_day, range(2021, 10000))))
    for x in [
            'Count of palindromic dates [2021..9999]:',
            len(palindrome_dates), '\nFirst 15:',
            '\n'.join(palindrome_dates[0:15]), '\nLast 15:',
            '\n'.join(palindrome_dates[-15:])
    ]:
        print(x)


if __name__ == '__main__':
    main()
