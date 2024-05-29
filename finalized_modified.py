import math
import base64
import random
import colorama
from colorama import Fore
import fileinput 

# def takeip(dt):
#     if(dt.opt == 1):
#         data = dt.data

    

# opt = int(input('''options:
# 0 ---> type the hashvalue
# 1 ---> paste the file path
# --->'''))

# if opt == 1 :
#     data = input(Fore.YELLOW + 'type the filepath(exclude"") to be hashed: ')

#     try:
#         for line in fileinput.input(files =data):
#             data += line
#     except FileNotFoundError:
#         print('file not found :/ check your file path')
#         exit()

# elif opt == 0:
#     data = input(Fore.YELLOW + 'type the string to be hashed :')

# else:
#     print(Fore.RED + 'type a valid input')
#     exit()

def calculate(data):
    
    try:
        rotstr = data[:5] + data[:5]
    except IndexError:
        print("out of range")
        exit()
    str_bytes = data.encode()
    base64_bytes = base64.b64encode(str_bytes)
    b64str = base64_bytes.decode()

    binr = ''.join(format(ord(i), '08b') for i in b64str)

    p = math.ceil(len(binr)/128)

    N = p * 128
    bins1 = binr.zfill(N)

    random.seed(len(data))
    def replace_random(string):
        string_list = list(string)
        for i in random.sample(range(len(string_list)), random.randint(1, len(string_list))):
            string_list[i] = '1'
        # Convert list back to string
        return ''.join(string_list)

    bins = replace_random(bins1)
    #replaced bits with 1s at random positions (fixed seed  for const hash...)

    cutlist = []
    cutlist = [bins[i:i+128] for i in range(0,len(bins),128)]


    if len(cutlist)>1:
        res2 = cutlist[-1]
        for i in range(len(cutlist)):
            resl = ''
            for j in range(len(res2)):
                x = '0' if int(res2[j]) == int(cutlist[i][j]) else '1'
                
                resl += f"{x}"
            res2 = resl

    else: res2=bins
    # bitwise result...
    #code correct
    fbin = hex(int(res2,2))
    fbin = fbin[2:]
    return fbin

# fbin = calculate(data)

# print(Fore.BLUE + 'here is your hash:',Fore.GREEN + fbin)
# print(Fore.WHITE)
# # hexval output



    

    
    






