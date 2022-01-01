# taskin
# input ile kullanıcıdan değer bekliyorum
vize =int (input('lütfen vize notunu gir:'))
final_notu= int (input('lütfen final notunu gir:'))

#vize notunun %40'ını final notunun %60'ını hesaplıyorum  
ortalama = vize*0.40 + final_notu*0.60

# ortalama 50 den büyük ve eşit ise sınavdan geçtiniz ekrana yazdırıyorum. 
if ortalama >= 50:
    print('sınavdan geçtiniz!', 'ortalama notunuz:', ortalama )
#küçükse 'sınavdan kaldınız' ekrana yazdırıyorum.
else:
    print('sınavdan kaldınız!' , 'ortalama notunuz:', ortalama ) 
