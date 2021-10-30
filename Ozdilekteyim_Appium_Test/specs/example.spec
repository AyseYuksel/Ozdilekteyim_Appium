OZDILEKTEYIM SENARYOSU
======================

SENARYO
-------------
Uygulama Acilisi Kontrolu Yapılır
* "2" saniye bekle
*"com.ozdilek.ozdilekteyim:id/tv_startShoppingStore" id'li element sayfada var mı doğru sayfada mıyım kontrolü yap

Alisverise Basla Butonuna Basılır
* "2" saniye bekle
* "com.ozdilek.ozdilekteyim:id/tv_startShoppingStore" id'li elementine tıkla

Alisveris Sayfasında Olundugu Kontrolu Yapılır
* "2" saniye bekle
* "com.ozdilek.ozdilekteyim:id/relLayMarket" id'li element sayfada var mı doğru sayfada mıyım kontrolü yap

Kategoriler Sayfasına Gidilir
* "2" saniye bekle
* "com.ozdilek.ozdilekteyim:id/nav_categories" id'li elementine tıkla

Kategoriler Sayfasında Olundugu Kontrolu Yapılır
* "2" saniye bekle
*  "//android.widget.LinearLayout[@content-desc='Kategoriler']" xpath'ine sahip element sayfada var mı, doğru sayfada mıyım kontrolü yap

Kadın Secenegine Tıklanır
* "2" saniye bekle
* "//*[@resource-id='com.ozdilek.ozdilekteyim:id/relLayCategoriesItem'][2]" xpath'li elemente tıkla

Pantolon Kategorisi Acilir
* "2" saniye bekle
* "//*[@resource-id='com.ozdilek.ozdilekteyim:id/relLayCategoriesItem'][4]" xpath'li elemente tıkla

Sayfayı 2 defa scroll etme
* "2" saniye bekle
*Sayfayı asagi indir
* "1" saniye bekle
*Sayfayı asagi indir

Urun secimi yapilir
* "2" saniye bekle
* "//*[@resource-id='com.ozdilek.ozdilekteyim:id/recyclerView']/android.widget.FrameLayout[3]" xpath'li elemente tıkla

Urun Detay sayfası kontrolu
* "2" saniye bekle
*"com.ozdilek.ozdilekteyim:id/tvItemDescription" id'li element sayfada var mı doğru sayfada mıyım kontrolü yap

Favoriler Butonuna tıklanır
* "2" saniye bekle
*ürün sayfasını asagi indir
*"2" saniye bekle
* "com.ozdilek.ozdilekteyim:id/relLayAddFav" id'li elementine tıkla

Kullanıcı adı girisi yapılır
* "2" saniye bekle
*"com.ozdilek.ozdilekteyim:id/etEposta" İd'li elemente "ayseyuksel240819981@hotmail.com" değerini yaz

Sifre girisi yapılır
* "2" saniye bekle
* "com.ozdilek.ozdilekteyim:id/etPassword" İd'li elemente "aysenur123*" değerini yaz

Giris yap butonuna double click yapılması
* "2" saniye bekle
* "com.ozdilek.ozdilekteyim:id/btnLogin" id'li elemente double click yapılması
* "2" saniye bekle

Urun secilmesi
*"2" saniye bekle
*"//*[@resource-id='com.ozdilek.ozdilekteyim:id/textView13']" xpath'li elemente tıkla

Urunun sepete eklenmesi
*"2" saniye bekle
*"com.ozdilek.ozdilekteyim:id/relLayAddCartBtn" id'li elementine tıkla

Urunun sepette goruntulenmesi
Menude geri git
*"2" saniye bekle
* "com.ozdilek.ozdilekteyim:id/ivBack" id'li elementine tıkla

Sepete git
*"2" saniye bekle
*"//android.widget.FrameLayout[@content-desc='Sepetim, 1 new notification']/android.widget.ImageView" xpath'li elemente tıkla
*"2" saniye bekle