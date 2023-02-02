### Notlar 

- DC encoding: DC_code + DC_value 

  + DC_code, dc degerin boyutuna gore belirlenir. Mesela dc deger 6 ise binary formatinda 110 olarak ifade edilir ve dc code'u 100 dir. 
  
  + 100 in yanina 110 eklenir ve dc deger: 100110 seklinde kodlanir.  

  + DC_code tablosu:
     
       ![dc_code](images/dc_code.png)

- AC encoding: AC_code + AC_value

  + AC_code, ac degerden onceki 0'a esit olan toplam AC sayisina ve ac degerin binary formatindaki uzunluguna gore hesaplanir.   
 
  + AC code tablosundan bir parca:

       ![ac_code](images/ac_code.png)

  + RUN, non-zero sayidan once kac tane 0 oldugunu, CAT ise non-zero ac degerin binary formatinda kac bit ile ifade edilecegini belirtiyor. 
     

 - AC ve DC degerleri bu tablolardaki farkliligi kullanarak ayirt edecegim insallah.
 
 
 - Image decoder algoritma akisi soyledir:

  +  Bitstream den okudugum ilk deger DC deger olacaktir. Bu degerin DC_code tablosunda eslestigi deger bulunur ve ardindan binary degeri okunur. Decimal degere cevrilir. 

  + Daha sonra AC degerler AC_code tablosuna gore AC degerler saptanir ve decimal a cevrilir. Toplam AC degeri 63 oldugunda yeni dc deger alinir ayni zamanda 1 dc 63 ac den olusan 1*64 luk blok olusturulur.  
      
  + 1200 dc deger alindiktan sonraki ac encode lar da cozumlenir. 63 decimal ac deger olusturulduktan sonra son 1*64 luk dc, ac blok olusturulur. Ve netice olarak 1*76800 luk array olusturulmus olunur. 

  + inverse zigzag yapilir. [zigzag_izigzag_pythoncode_link](https://github.com/getsanjeev/compression-DCT/blob/master/zigzag.py) 

  + inverse quantization yapilir. 
      
  + Inverce dct yapilir. `scipy.fft.idct` 

  + piksel degerlerine 128 eklenir. Bitstream cozumlenmis olunur. 

  + Algoritma flowchart : 

    ![bitstream](images/Bitsream.png)

- MBA ile revizyon:

  + Decoding aşamasından sonra 0 dan küçük ve 255 ten büyük sayılar oluşuyor.
Oluşmaması lazımsa nerede hata yaptım. Oluşması normalse nasıl 0-255 arasına map edelim.

  + Son blokta sıkıntı var. Son blok hiç dekode olunmuyor gibi.    

  + uint8() ile cast edip kaydettiğim için negatif sayılar büyük piksel değerlerine dönüşmüş olabilir.

  + denemek için - sayıları 0 a; 255 ten büyük sayıları 255 e çeken bir for loop ekleyebilirim. 
Ya da direk 0-255 arasına map ederim değerleri.

- Bir makaleden: "Any value that ends up being greater than 255 is set to 255 and all negative values are set to 0. This is done sinceall the
pixel values must be in the range of 0 to 255 coming from the IDCT and due to rounding and quantization, some values fromthe IDCT can be out ofthose ranges." 

 
- 0-255 arasına map eden for loopları yazdım. Son bloktaki problemin nerede olduğunu keşfettim.  

	
