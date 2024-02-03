[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11651240&assignment_repo_type=AssignmentRepo)
# Level-2-Mini-Cinema
Mini Cinema system like console app in terminal

![cinema-hall-886778-1599978918](https://user-images.githubusercontent.com/85978779/230436166-860ecb9c-4cb1-46fe-a388-dcaf9afef5c4.jpeg)


Bu mini proyekt hissələrə bölünəcək. Sonda bu hissələri "from ... import ..." məntiqi ilə (bir fayldan digərinə, başqa modullara access yaratmaq) tək bir python faylında cəmləşdirib ümumi nəticə olan məntiqimizi həmin faylda (məsələn: main.py) run edəcəyik.

QEYD: Bütün hissələrin main.py - da işləyən hissəsində ümumi bir məntiq - try except və exit məsələləri.
Əgər siz insan, mall, film seçimində ədəd deyil başqa simvol daxil etsəniz except məntiqi işləməli və "Enter valid value" nəticəsi görünməlidir. Bu nəticə isə printdə yox exit məntiqində işləməlidir ki, proses orda da qırılsın və davam etməsin. Uyğun olmayan rəqəm isə sonda else hissəsində görünməli və "Wrong input" yazısı görünməlidir - exit nəzərə alınaraq.
Ümumiyyətlə bütün məntiqlərimizdə əgər hardasa kod dayanmalıdırsa prosesə davam etmək mümkün deyilsə exit-dən istifadə etməniz vacibdir.
_____
1-ci hissə:

  Başlanğıcda sinemaya gələn insanın mall işçisi və ya normal vətəndaş olmasına dair məntiq işləməlidir. 2 class yaranacaq Worker və Normal Person olaraq hər ikisinin içərisində sadəcə bir metod işləyəcək və içərisində bir return ilə kim olduğunu təsdiq edəcək. Metodlarda "Polymorphism" məntiqi işləməlidir.

  Main.py faylına import edildikdən sonra iş burada başlayacaq. Terminalda ədədlər ilə seçim qoyulmalıdır müvafiq olaraq kimliyə dair. Hər rəqəmdə müvafiq olaraq özünə aid nəticə göstərilməlidir (normal insan və ya işçi)
_____
2-ci hissə:

  Ümümi Mall classı olacaq. 3 atributu olmalıdır - location (ünvanı), floor (mərtəbə sayı), hall count (zal sayı). 5 əlavə Mall class-ı olacaq hərəsi öz adında və ümumi Mall classından inheritance etməlidir, atributlar oradan çəkilməlidir və bu sayədə metodlar da işləməlidir
  1-ci metod: working_time() metodu olacaq. Datetime modulundan istifadə olunacaq. Hazırda saatın neçə olduğu təyin edilməli və bir variable-a mənimsədilməlidir. Daha sonra açılış vaxtı (10) və bağlanış vaxtı (23) adlı variablelar verilməlidir və sadəcə saatları başqa olmalıdır (hazırkı saatınızı göstərən variabledan istifadə edib onun bir metod ilə saatını dəyişib bu 2 variable-ı təyin edə bilərsiz). Daha sonra həmin working_time metodunda hazırkı saat ilə bu açılış, bağlanış saatı arasında müqayisə aparılmalıdır. Əgər saat uyğundursa açıqdır bildirimi gəlməli və iş davam etməlidir, bağlıdırsa bu bildirilməli və sizi terminaldan atmalıdır.
  [Qeyd: Kodu işlədiyiniz zaman (məsələn gecə işləsəniz müqayisə zamanı vaxt sizə gecə həmin saatı qaytarır deyə, müqayisədən sonra işinizə davam edə bilməyəcəksiniz) işinizin davam etməsi üçün müvəqqəti açılış və bağlanış saatlarını başqa cür təyin edə bilərsiniz. Sonda proyekt bitdiyi zaman bildirilən default saatları təyin etməlisiniz 10 və 23]
  _
  2-ci metod: Yaş məsələsi, 14 yaşdan aşağı girməməlidir (bunun inputu main.py-da metod işləyən zaman istənilməlidir)
  _
  3-cü metod: Vaksinasiya. Əgər "Active" olsa proses davam etməlidir. Əks halda kod dayanmalıdır
  _
  4-cü metod: İnformasiya. Yuxarıdakı mərhələlər tam uğurla bitirsə, Mall-a giriş etmək mümkündür. Mall haqqında ümümi məlumat təqdim edilməlidir atributlarına verilən məlumatlardan istifadə edərək.
  
  Main.py faylına hamısı import edilməlidir əvvəlcə 5 mall-un hər biri üçün ayrıca obyekt təyin edilir və məlumatlar mənimsədilir. Print hissəsinə yazılaraq terminalda ədədlər ilə mall seçimləri verilir. Sonra şərt başlayır hər rəqəm müvafiq olaraq 1 mall-u işarə edir daxil olduqdan sonra həmin mall-un sıra ilə yuxarıdakı 4 metodu işləməlidir. 
  
_____
3-cü hissə:

  Hours class-ı olacaq. Filmlərin seansları üçün təyin etməliyik, 2 atribut - start time və end time. Str metodu ilə sadəcə seansların Ümumi Movie classı olacaq. 8 atribut olmalıdır - name, director, year, genre, duration, imdb, hours, price. 

  1-ci metod: show_info metodu. Metodun başlanğıcında seanslara aid məntiq qurulmalıdır. Movie class-ı içərisində olan hours metodu boş bir list kimi təyin edilməlidir. İçərisində dövr edilməlidir və bir dictionary açılaraq digər Hours classından olan start time və end time hissələri olmalı daha sonra həmin dictionary boş olan hours listinə mənimsədilməlidir. Sonda ümumi return verilməlidir və filmə aid bütün məlumatlar atributlara verilən məlumatlar ilə show metodunda gəlməlidr (hours atributundan başqa, onu daha sonra bildirəcəyik).
  2-ci metod: year_info. 2000-ci ildən əvvələ aiddirsə "Old category" əks halda "New category" yazılmalıdır.
  3-cü metod: duration_info. 120 dəqiqədən qısa filmlər "Short movie" əks halda "Long movie" kateqoriyasında olmalıdır.
  4-cü metod: rating_info. 6-dan aşağı E, 6-7 D, 7-8 C, 8-9 B, 9-10 A kateqoriyası sayılmalı, başqa rəqəmlər Not found yazısını çap etməlidir
  
  Main.py faylına hamısı import edilməlidir əvvəlcə 10 film hər biri ayrlca obyekt təyin edilir və məlumatlar yazılır. Həmçinin film seansları üçün də obyektlər yaradılmalı və Hours classına əsasən təyin edilməlidir. Movie-yə aid obyektlərin təyini zamanı hours atributuna sıra çatdıqda, bir filmin bir neçə seansı nəzərə alınaraq həmin hissə bayaq yazılan list şəklində verilməli və içərisində bayaq Hours classından təyin edilən obyektlər ilə azı 2 seans təyin edilməlidir. Print hissəsinə filmlərin adı yazılaraq terminalda ədədlər ilə film seçimləri verilir. Sonra şərt başlayır hər rəqəm müvafiq olaraq 1 filmi işarə edir daxil olduqdan sonra həmin filmin sıra ilə yuxarıdakı 4 metodu işləməlidir. Davamı növbəti hissəmizdən sonra davam etməlidir. Seans seçimləri üçün Choices hissəsi print edilməlidi daha sonra film üçün artıq mənimsədilən hours listində gəzərək hansı seansların olduğu seçimləri təqdim edilməlidir. Növbəti addımda siz bu seanslardan birini rəqəm ilə seçməli və bildirməlisiniz. Daha sonra sizin seansınızı göstərəcək. Biletin qiyməti price atributu sayəsində göstəriləcək və bilet alıb-almamaq istəyi soruşulacaq. "Yes" yazılsa davamı digər məntiqdən sonra ardıcıl şəkildə buradan davam edəcək. Başqa nə isə yazılsa kod bitəcək
  
_____
4-cü hissə:
  Money class-ı olacaq. 1 atributu olacaq hazırda olan pulumuz (current_money). get_money metodu olmalıdır hazırda olan pulumuzu bizə return edəcək. set_money metodu olmalıdır. İçərisində bir film adlı variable mənimsədəcəyik. Ən əvvəldə də movie-yə dair məlumatları bu fayla import etməliyik. Daha sonra yazdığımız variable ilə Movie class-ı içərisində olan price atributuna çatacayıq. Əgər pulumuz bu filmin biletinin qiymətindən çox olsa bilet ala bildiyimizi və qalan pulumuzu yazacaq. Əks halda sizin bu film üçün lazımi məbləğinizin olmadığını bildirəcək.
  
  Main.py faylını ən son bilet alınma hissəsində saxlamışdıq. "Yes" seçilsə bir inputda öz pulunuzu daxil etməsi istəniləcək və bu daxil edildikdən sonra həmin məbləği get_money metoduna mənimsədəcəyik bunun sayəsində hazırda pulumuzu göstərəcək. Daha sonra da set_money methodu çağırılacaq və digər faylda yazdığımız if else məntiqi işə düşəcək. Pulumuz çatsa bilet alınacaq əks halda kifayət etmədiyi bildiriləcək.
  
  
Yazılan kodlar bütün mall və filmlər üçün tətbiq ediləcək !
Good Luck and be patient, Enjoy the Movie:)



