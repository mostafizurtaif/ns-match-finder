from sanitize import sanitize_ns

number_sequence = ''
print('\nAdd your .txt file containing random integer sequence by entering its path.\n')

while True:
    file_path = input('Enter the file path: ')

    try:
        with open(file_path) as file:
            string = file.read()
    except FileNotFoundError:
        print('File not found! Check your file path, and try again.\n')
        continue
    else:
        sanitize = sanitize_ns(string)
        number_sequence = sanitize[0]

        if sanitize[1] == True:
            print(f'\nNumber sequence in the given file has been sanitized.', end='')

        print('\nNumber sequence:')
        print(number_sequence)
        break


while True:
    while True:
        to_be_matched_num_seq = input('\nEnter your to-be-matched number sequence: ')
        
        if to_be_matched_num_seq == 'q':
            break

        sanitize = sanitize_ns(to_be_matched_num_seq)

        if not sanitize[0]:
            print('No number sequence has been found!')
            continue
        else:
            if sanitize[1]:
                print('This number sequence has been sanitized.')
            break

    
    if to_be_matched_num_seq == 'q':
        print('The program has been quit.')
        break
    
    total_match = 0
    i = 0

    while (len(sanitize[0])+i) <= len(number_sequence):
        if sanitize[0] == number_sequence[i:len(sanitize[0])+i]:
            total_match += 1
        i += 1

    print(f'Total match: {total_match}')

