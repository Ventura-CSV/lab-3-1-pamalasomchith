def main():
    number = int(input('Enter a number: '))
    if number < 50:
        range = 1
    else:
        if (50 <= number < 100):
            range = 2
        else:
            range = 3
    print(f'Range is {range}')
    ########################################
    # Do not delete the return statement
    ########################################
    return range


if __name__ == '__main__':
    main()
