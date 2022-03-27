def rc4(key):
    key_length = len(key)
    s = list(range(256))  # 0 dan 255 e kadar olan sayıları S istesine atadık k=[]
    j = 0
   
    for i in range(256):
        # anahtarı arka arkaya yazıyo böylece 255 den kısa olan anahtar tamamnlanıyo ex-or işlemi için
        #k = key(i % key_length)
       # j = (j+s[i]+k) % 256  # kullanacğımız anahtarda karıştırma işlemi geçekleştiriliyo eğer toplam 256 dan büyük olursa s listesinin dışına çıkar ve stackoweflow sorunu olur bunun olmaması için mo256 yazdık ki 256 dan üyük olmasın
        j=(j+s[i]+key[i%key_length])%256
        s[i], s[j] = s[j], s[i]  # swap işlemi
    return s
    # açık metin ne kadarsa anahtar uzunluğu o kadar olmalı


def prga(s, n):
    i = 0
    j = 0
    key = []
    while(n > 0):
        n = n-1
        i = (i+1) % 256
        j = (j+s[i]) % 256
        s[i], s[j] = s[j], s[i]
        k = s[(s[i]+s[j]) % 256]
        key.append(k)
# şifreleme için anahtar hazır
    return key


key = 'eda'
plaintext = 'odevimiyaptiim'


def asci_code(s):
    return [ord(c) for c in s]


# anahtarımız ascii değerlerine çevirdik ve metodu çağırdık
key = asci_code(key)

import numpy as np
s = rc4(key)

# şifrelenmiş metni
ciphertext = np.array(prga(s, len(plaintext)))
print(ciphertext)