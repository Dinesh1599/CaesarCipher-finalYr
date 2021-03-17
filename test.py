#import Section
import time
import datetime
import socket
import geocoder

#All Functions Required
def encrypt(ch, key):
    enc_final = ''
    edit94 = []
    edit126 = []
    #print('Key',key)
    for index, i in enumerate(ch):
        val  = ord(i) +  key
        if (val > 126):
            #print('Change',val)
            val = val - 126
            if val < 32:
                val += 32
                edit94.append(index)
            else:
                edit126.append(index)
        listA.append(chr(val))  
        enc_final += chr(val)  
        #print(index,':',i,':', val , ':', chr(val))
    return [edit126, edit94, enc_final]

def decrypt(ch, key, l94, l126):
    l = []
    dec_final = ''
    for index, i in enumerate(ch):
        val = ord(i) - key
        if index in l94:
            val = val + 94
        elif index in l126:
            val = val + 126
        l.append(chr(val))
        dec_final += chr(val)
    return(dec_final)

def genKeys(ts, g, ip):
    keyA = int(ts) % 126
    keyB = int(g) % 126
    keyC = int(ip)  % 126
    if(keyA == 0 or keyA == 126):
        keyA = (int(ts)*3) % 126
    if(keyB == 0  or keyB == 126):
        keyB = (int(ts)*3) % 126
    if(keyC == 0 or keyC == 126):
        keyC = (int(ts)*3) % 126 
    return [keyA, keyB, keyC]   

def toString(val):
    val = str(val)
    return val.replace('.','')

def rotate(val, shift):
    x = shift % len(val)
    temp  = []
    final_r = ''
    for i in val:
        temp.append(i)
    test_list = temp[x:] + temp[:x]
    for i in test_list:
        final_r += i
    return final_r

def revRotate(val, shift):
    x = shift % len(val)
    temp  = []
    final_r = ''
    for i in val:
        temp.append(i)
    test_list = temp[-x:] + temp[:-x]
    for i in test_list:
        final_r += i
    return final_r

#Variable Preset Declaration
ch = input('Enter cipher text \n')
ts = time.time()
ip = socket.gethostbyname(socket.gethostname())
g = geocoder.ip('me').latlng
g_lat = g[0]
g_lon = g[1]
ts = toString(ts)
ip = toString(ip)
g = toString(g_lat)

listA = []
edit126_A = []
edit94_A = []
edit126_B = []
edit94_B = []
edit126_C = []
edit94_C = []

#KEYS GENERATION
myKeys = genKeys(ts, g, ip)
keyA = myKeys[0] 
keyB = myKeys[1]
keyC = myKeys[2]
final = ''

#Encryption Generator
ciph1 = encrypt(ch, keyA)
edit126_A = ciph1[0]
edit94_A = ciph1[1]
finalA = ciph1[2]
ciph1_r = rotate(finalA, int(g_lon))

ciph2 = encrypt(ciph1_r, keyB)
edit126_B = ciph2[0]
edit94_B = ciph2[1]
finalB = ciph2[2]
ciph2_r = rotate(finalB, int(g_lon))

ciph3 = encrypt(ciph2_r, keyC)
edit126_C = ciph3[0]
edit94_C = ciph3[1]
finalC = ciph3[2]
ciph3_r = rotate(finalC, int(g_lon))


print('\n\n////////////////////////////////////////////////////////////////////////////')
print('///                               ENCRYPTION                              /')
print('//////////////////////////////////////////////////////////////////////////\n\n')

print('finalA', finalA)
print('finalA_r', ciph1_r)
print('listA', [edit94_A, edit126_A])
print('\n')

print('finalB', finalB)
print('finalB_r', ciph2_r)
print('listB', [edit94_B, edit126_B])
print('\n')

print('finalC', finalC)
print('finalC_r', ciph3_r)
print('listC', [edit94_C, edit126_C])

print('\n\nFinal Encryption', ciph3_r, '\n\n')


print('\n\n////////////////////////////////////////////////////////////////////////////')
print('///                               DECRYPTION                              /')
print('//////////////////////////////////////////////////////////////////////////\n\n')


revCiph3_r = revRotate(ciph3_r,int(g_lon))
print('rev3',revCiph3_r)
revCiph3 = decrypt(revCiph3_r, keyC, edit94_C, edit126_C)
print('Outer Layer',revCiph3, '\n')

revCiph2_r = revRotate(revCiph3,int(g_lon))
print('rev2',revCiph2_r)
revCiph2 = decrypt(revCiph2_r, keyB, edit94_B, edit126_B)
print('Middle Layer',revCiph2, '\n')

revCiph1_r = revRotate(revCiph2,int(g_lon))
print('rev1',revCiph1_r)
revCiph1 = decrypt(revCiph1_r, keyA, edit94_A, edit126_A)
print('Final Text',revCiph1, '\n')

print('\n\nFinal Decryption', revCiph1, '\n\n')