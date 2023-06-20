def print_star_name(str):
    str = str.upper()
    for i in range(0,len(str)):
        for x in range(0,len(str)):
            if i==x:
                print(str[i],end=' ')
            else:     
                print('*',end=' ')
        print('')        


print(print_star_name(str(input('Enter your word: '))))    