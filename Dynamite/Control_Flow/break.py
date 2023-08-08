for i in range(10):
    print(f'Start loop with i == {i}')
    if i == 3:
        print('Break out')
        break
    if i < 2:
        print(f'Continue')
        continue
    print('End loop')