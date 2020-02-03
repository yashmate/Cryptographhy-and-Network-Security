
alphabet_list=[chr(i) for i in range(ord('a'),ord('z')+1)]
number_list=[str(i) for i in range(1,27)]
alphabet_to_number=dict(zip(alphabet_list,number_list))
number_to_alphabet=dict(zip(number_list,alphabet_list))


def caesar_cipher(string,key):
    new_string=[]
    for char in string:
        char_number=alphabet_to_number[char]
        new_index=(int(char_number)+key)%26
        new_string.append(number_to_alphabet[str(new_index)])
    new_string=''.join(new_string)
    return new_string



def decrypt_caesar_cipher(string,key):
    new_string=[]
    for char in string:
        char_number=alphabet_to_number[char]
        new_index=(int(char_number)-key)%26
        new_string.append(number_to_alphabet[str(new_index)])
    new_string=''.join(new_string)
    return new_string


def transposition_cipher(string,column_order):
    columns=len(column_order)
    from math import ceil
    rows=ceil(len(string)/columns)
    total_chars=["*" for i in range(rows*columns)]
    #print(total_chars)
    for i in range(len(string)):
        total_chars[i]=string[i]
    #print(total_chars)
    matrix=[]
    for i in range(0,len(total_chars),columns):
        matrix.append(list(total_chars[i:i+columns]))
    #for row in matrix:
        #print(row)
    #print("___________")
    t_matrix = list(map(list, zip(*matrix)))
    #for row in t_matrix:
        #print(row)
    new_matrix=[]
    for i in range(len(t_matrix)):
        new_matrix.append(t_matrix[column_order[i]-1])
    #print("_________________")
    #for row in new_matrix:
       # print(row)
    #print("_________________")
    t_matrix = list(map(list, zip(*new_matrix)))
    #for row in t_matrix:
        #print(row)
    new_string=[]
    for i in range(len(t_matrix)):
        for j in range(len(t_matrix[i])):
            new_string.append(t_matrix[i][j])
    new_string=''.join(new_string)
    print("The final encyrpted text is ",new_string)
    return new_string


def decrypt_transposition_cipher(string,column_order):
    columns=len(column_order)
    from math import ceil
    rows=ceil(len(string)/columns)
    total_chars=["*" for i in range(rows*columns)]
    #print(total_chars)
    for i in range(len(string)):
        total_chars[i]=string[i]
    #print(total_chars)
    matrix=[]
    for i in range(0,len(total_chars),columns):
        matrix.append(list(total_chars[i:i+columns]))
    #for row in matrix:
        #print(row)
    #print("___________")
    t_matrix = list(map(list, zip(*matrix)))
    #for row in t_matrix:
        #print(row)
    new_matrix=[]
    for i in range(len(t_matrix)):
        new_matrix.append(t_matrix[column_order.index(i+1)])
    #print("______________________")
    #for row in new_matrix:
        #print(row)
   # print("______________________")
    t_matrix = list(map(list, zip(*new_matrix)))
    #for row in t_matrix:
        #print(row)
    new_string=[]
    for i in range(len(t_matrix)):
        for j in range(len(t_matrix[i])):
            new_string.append(t_matrix[i][j])
    new_string=''.join(new_string)
    new_string=new_string.rstrip('*')
    print("The final decyrpted text is ",new_string)
options=['Caesar Cipher','Transposition Cipher']
print("Enter your Choice")
for i,option in enumerate(options):
    print("{} -- > {}".format(i+1,option))
choice=int(input())
if choice == 1:
    string = input("Enter the string to be encrypted")
    key=int(input("Enter the key"))
    print("The encrpyted text is {}".format(caesar_cipher(string,key)))
    print("The decrypted text is {}".format(decrypt_caesar_cipher(caesar_cipher(string,key),key)))
elif choice == 2:
    string = input("Enter the string to be encrypted")
    key=list(map(int,input('Enter the order of columns').split()))
    x=transposition_cipher(string,key)
    decrypt_transposition_cipher(x,key)
else:
    print("Invalid Choice")





