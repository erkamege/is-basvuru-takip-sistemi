import streamlit as st
import pandas as pd
import plotly.express as px
import os
import random

# Sayfa genel ayarları 
st.set_page_config(page_title="İş Başvuru Takip", page_icon="💼", layout="wide")

# --- SABİT BEYAZ TEMA AYARI ---
if not os.path.exists(".streamlit"):
    os.makedirs(".streamlit")

config_yolu = ".streamlit/config.toml"
with open(config_yolu, "w") as f:
    f.write('[theme]\nbase="light"\nbackgroundColor="#ffffff"\nsecondaryBackgroundColor="#f0f2f6"\ntextColor="#31333F"\nprimaryColor="#0077B5"\n')

# --- MOTİVASYON KÖŞESİ (Üretim, Tasarım ve Başarı Üzerine Sözler) ---
if "gunun_sozu" not in st.session_state:
    st.session_state["gunun_sozu"] = random.choice([
        
        {"soz": "Kimsenin sana bir şeyi yapamayacağını söylemesine izin verme... Bir hayalin varsa onu korumalısın.", "kisi": "Chris Gardner", "eser": "The Pursuit of Happyness (Umudunu Kaybetme)"},
        {"soz": "Önemli olan ne kadar sert vurabildiğin değil, ne kadar sert darbe alıp yola devam edebildiğindir.", "kisi": "Rocky Balboa", "eser": "Rocky Balboa"},
        {"soz": "Korku seni tutsak eder, umut ise özgür bırakır.", "kisi": "Andy Dufresne", "eser": "The Shawshank Redemption (Esaretin Bedeli)"},
        {"soz": "Bize asıl kim olduğumuzu gösteren şey yeteneklerimiz değil, seçimlerimizdir.", "kisi": "Albus Dumbledore", "eser": "Harry Potter"},
        {"soz": "Yap ya da yapma. Denemek diye bir şey yoktur.", "kisi": "Yoda", "eser": "Star Wars (Yıldız Savaşları)"},
        {"soz": "Hayat ne kadar zor görünürse görünsün, her zaman yapabileceğin ve başarabileceğin bir şey vardır.", "kisi": "Stephen Hawking", "eser": "The Theory of Everything (Her Şeyin Teorisi)"},
        {"soz": "Bazı insanlar sadece normal olmak için harika olmaktan vazgeçerler. Sen onlardan olma.", "kisi": "Alan Turing", "eser": "The Imitation Game (Enigma)"},
        {"soz": "Neden düşeriz? Yeniden ayağa kalkmayı öğrenmek için.", "kisi": "Alfred Pennyworth", "eser": "Batman Begins (Batman Başlıyor)"},
        {"soz": "Yapman gereken tek şey, sana verilen zamanla ne yapacağına karar vermek.", "kisi": "Gandalf", "eser": "The Lord of the Rings (Yüzüklerin Efendisi)"},
        {"soz": "Yolun nereye gideceğini bilmekle, o yolda yürümek farklı şeylerdir.", "kisi": "Morpheus", "eser": "The Matrix"},
        {"soz": "Sadece yüzmeye devam et.", "kisi": "Dory", "eser": "Finding Nemo (Kayıp Balık Nemo)"},
        {"soz": "Geçmiş acıtabilir. Ama benim bakış açıma göre, ondan ya kaçarsın ya da ondan ders alırsın.", "kisi": "Rafiki", "eser": "The Lion King (Aslan Kral)"},
        {"soz": "Her gün biraz daha kolaylaşır. Ama her gün yapman gerekir, asıl zor olan kısım bu.", "kisi": "Koşan Maymun", "eser": "BoJack Horseman"},
        {"soz": "Bir fikrin gücünü asla küçümseme.", "kisi": "Cobb", "eser": "Inception (Başlangıç)"},
        {"soz": "Asla pes etme, asla teslim olma!", "kisi": "Jason Nesmith", "eser": "Galaxy Quest (Galaksi Savaşçıları)"},
        {"soz": "Hayat bir kutu çikolata gibidir, içinden ne çıkacağını asla bilemezsin.", "kisi": "Forrest Gump", "eser": "Forrest Gump"},
        {"soz": "Benim için tek bir kural var: Geri adım atma, teslim olma.", "kisi": "Kral Leonidas", "eser": "300 Spartalı"},
        {"soz": "Büyük adamlar büyük doğmazlar, büyük olurlar.", "kisi": "Don Vito Corleone", "eser": "The Godfather (Baba)"},
        {"soz": "Korkmamalıyım. Korku akıl katilidir.", "kisi": "Paul Atreides", "eser": "Dune"},
        {"soz": "Geçmiş geride kaldı, önemli olan şu an ne yaptığımız.", "kisi": "Po", "eser": "Kung Fu Panda"},
        {"soz": "Bugün dünden daha iyi bir gün olacak.", "kisi": "Ted Lasso", "eser": "Ted Lasso"},
        {"soz": "Eğer bir şeyde iyiysen, onu asla bedavaya yapma.", "kisi": "The Joker", "eser": "The Dark Knight (Kara Şövalye)"},
        {"soz": "Bizler bu dünyayı kurtaracak olanlarız.", "kisi": "Tony Stark", "eser": "Avengers: Endgame"},
        {"soz": "Düştüğümüzde ne yaparız? Tekrar ayağa kalkarız.", "kisi": "Kaptan Amerika", "eser": "The Avengers (Yenilmezler)"},
        {"soz": "Yarın güneş doğacak. Kim bilir akıntı ne getirecek?", "kisi": "Chuck Noland", "eser": "Cast Away (Yeni Hayat)"},
        {"soz": "Carpe Diem. Anı yaşayın çocuklar. Hayatınızı olağanüstü yapın.", "kisi": "John Keating", "eser": "Dead Poets Society"},
        {"soz": "Umut, bizim en büyük gücümüzdür.", "kisi": "Professor X", "eser": "X-Men"},
        {"soz": "Gerçek cesaret, yenileceğini bile bile savaşmaktır.", "kisi": "Atticus Finch", "eser": "To Kill a Mockingbird"},
        {"soz": "Karanlık en çok şafaktan önce çöker.", "kisi": "Harvey Dent", "eser": "The Dark Knight (Kara Şövalye)"},
        {"soz": "Kelimeler ve fikirler dünyayı değiştirebilir.", "kisi": "John Keating", "eser": "Dead Poets Society"},
        {"soz": "Hayatta sadece iki seçeneğin var: Yaşamakla meşgul ol ya da ölmekle meşgul ol.", "kisi": "Andy Dufresne", "eser": "The Shawshank Redemption"},
        {"soz": "Bir şeyleri değiştirmek için asla çok geç değildir.", "kisi": "Benjamin Button", "eser": "The Curious Case of Benjamin Button"},
        {"soz": "Gideceğin yeri bilmiyorsan, hangi yoldan gittiğinin bir önemi yoktur.", "kisi": "Cheshire Kedisi", "eser": "Alice in Wonderland"},
        {"soz": "Hayatta yaptıklarımız, sonsuzlukta yankılanır.", "kisi": "Maximus", "eser": "Gladiator (Gladyatör)"},
        {"soz": "Her insan ölür, ama her insan gerçekten yaşamaz.", "kisi": "William Wallace", "eser": "Braveheart (Cesur Yürek)"},
        {"soz": "Bu dünyada hala iyi bir şeyler var ve uğruna savaşmaya değer.", "kisi": "Samwise Gamgee", "eser": "The Lord of the Rings"},
        {"soz": "Belki bir gün cesaretimizi kaybederiz... Ama o gün, bugün değil!", "kisi": "Aragorn", "eser": "The Lord of the Rings"},
        {"soz": "Fikirler kurşun geçirmezdir.", "kisi": "V", "eser": "V for Vendetta"},
        {"soz": "Bir şeyi istiyorsan, git ve al. Nokta.", "kisi": "Chris Gardner", "eser": "The Pursuit of Happyness"},
        {"soz": "Dünyanın sana sunduğu gerçeği kabul etmek zorunda değilsin.", "kisi": "Truman Burbank", "eser": "The Truman Show"},
        {"soz": "Dünyayı görmek, tehlikeli şeylerin üstesinden gelmek... Hayatın amacı budur.", "kisi": "Walter Mitty", "eser": "The Secret Life of Walter Mitty"},
        {"soz": "Hayat oldukça hızlı ilerliyor. Eğer arada bir durup etrafına bakmazsan, onu kaçırabilirsin.", "kisi": "Ferris Bueller", "eser": "Ferris Bueller's Day Off"},
        {"soz": "Eğer bir hedefin varsa, onun için savaşmalısın. Kalk ayağa!", "kisi": "Mickey Goldmill", "eser": "Rocky"},
        {"soz": "Odaklandığın şey, gerçeğini belirler.", "kisi": "Qui-Gon Jinn", "eser": "Star Wars"},
        {"soz": "Beni tanımlayan şey içimde kim olduğum değil, ne yaptığımdır.", "kisi": "Batman", "eser": "Batman Begins"},
        {"soz": "Denge sadece karate için değil, tüm hayat için önemlidir.", "kisi": "Mr. Miyagi", "eser": "The Karate Kid"},
        {"soz": "Gelecek henüz yazılmadı. Senin geleceğin, senin ne yapacağına bağlı. O yüzden iyi bir tane yap.", "kisi": "Doc Brown", "eser": "Back to the Future III"},
        {"soz": "Mutluluk en karanlık zamanlarda bile bulunabilir, sadece ışığı açmayı hatırlamak yeterlidir.", "kisi": "Albus Dumbledore", "eser": "Harry Potter"},
        {"soz": "Sınırlarını aş, daha uzağa git!", "kisi": "All Might", "eser": "My Hero Academia"},
        {"soz": "Sır diye bir şey yoktur. Sır sadece sensin.", "kisi": "Bay Ping", "eser": "Kung Fu Panda"},
        {"soz": "Sadece korkusuz olanlar gerçekten harika olabilir.", "kisi": "Şef Gusteau", "eser": "Ratatouille (Aşçı Fare)"},
        {"soz": "Gerçekçi ol, imkansızı iste.", "kisi": "Ernesto 'Che' Guevara", "eser": "The Motorcycle Diaries"},
        {"soz": "Ne kadar dibe vurursan, o kadar yükseğe zıplarsın.", "kisi": "Buster Moon", "eser": "Sing (Şarkını Söyle)"},
        {"soz": "Bazen hayat seni yere serer... Ama kalkıp kalkmamak senin elindedir.", "kisi": "Mr. Han", "eser": "The Karate Kid"},
        {"soz": "Hiçbir şey bitmedi! Bizim için bitene kadar bitmez!", "kisi": "John Rambo", "eser": "First Blood (İlk Kan)"},
        {"soz": "Seni öldürmeyen şey, seni tuhaflaştırır.", "kisi": "The Joker", "eser": "The Dark Knight"},
        {"soz": "Mükemmellik, sadece çok pratik yapmanın bir sonucudur.", "kisi": "Terence Fletcher", "eser": "Whiplash"},
        {"soz": "Büyük güç, büyük sorumluluk getirir.", "kisi": "Ben Amca", "eser": "Spider-Man (Örümcek Adam)"},
        {"soz": "En büyük zafer düşmemek değil, her düştüğünde yeniden kalkmaktır.", "kisi": "Nelson Mandela", "eser": "Invictus (Yenilmez)"},
        {"soz": "Hayat, fırtınanın geçmesini beklemekle ilgili değildir; yağmurda dans etmeyi öğrenmekle ilgilidir.", "kisi": "Vivian Ward", "eser": "Pretty Woman"},
        {"soz": "Yeterince istersen her şeyi başarabilirsin.", "kisi": "Gatsby", "eser": "The Great Gatsby"},
        {"soz": "Şu anki durumun nihai hedefin değil, sadece hazırlık aşaman.", "kisi": "Jim Braddock", "eser": "Cinderella Man"},
        {"soz": "Bir adım daha atabilirsin. Her zaman bir adım daha atabilirsin.", "kisi": "Ajan K", "eser": "Men in Black"},
        {"soz": "Karanlıktan korkma, karanlık sadece ışığın yokluğudur.", "kisi": "Splinter Usta", "eser": "Ninja Kaplumbağalar"},
        {"soz": "Ne pahasına olursa olsun pes etme. Tünelin sonunda her zaman ışık vardır.", "kisi": "Superman", "eser": "Man of Steel"},
        {"soz": "Zorluklar olmasaydı başarıların bir anlamı olmazdı.", "kisi": "Stephen Hawking", "eser": "The Theory of Everything"},
        {"soz": "Kendinden şüphe duymayı bırak ve sadece yap.", "kisi": "Sonny Vaccaro", "eser": "Air"},
        {"soz": "Daha iyisi olmak için sadece istemek yetmez, savaşmak gerekir.", "kisi": "Diana Prince", "eser": "Wonder Woman"},
        {"soz": "Başarı, bir varış noktası değil, yolculuğun kendisidir.", "kisi": "Dan Millman", "eser": "Peaceful Warrior"},
        {"soz": "Bırak her şey yansın. Sen küllerinden yeniden doğarsın.", "kisi": "Katniss Everdeen", "eser": "The Hunger Games"},
        {"soz": "Zihnini özgür bırak.", "kisi": "Morpheus", "eser": "The Matrix"},
        {"soz": "Dünyayı değiştirenler, bunu yapabileceklerini düşünecek kadar deli olanlardır.", "kisi": "Steve Jobs", "eser": "Jobs"},
        {"soz": "Şu ana kadar hayatının en kötü gününü yaşamış olabilirsin, ama yarın en iyisi olabilir.", "kisi": "Phil Connors", "eser": "Groundhog Day"},
        {"soz": "Beklemek zaman kaybıdır, harekete geçmek ise her şeydir.", "kisi": "Ethan Hunt", "eser": "Mission: Impossible"},
        {"soz": "Gerçek gücün sırrı kaslarda değil, zihindedir.", "kisi": "Prof. Charles Xavier", "eser": "X-Men First Class"},
        {"soz": "Bir şeyi seviyorsan, uğruna savaşmalısın.", "kisi": "Brian O'Conner", "eser": "Fast & Furious"},
        {"soz": "Ne kadar zorlarlarsa zorlasınlar, seni asıl sen yapan şeyi asla ellerinden alamazlar.", "kisi": "William Wallace", "eser": "Braveheart"},
        {"soz": "Rüzgar ne kadar sert eserse essin, dağ asla eğilmez.", "kisi": "İmparator", "eser": "Mulan"},
        {"soz": "Eğer yolculukta ter dökmediysen, zirvenin manzarası o kadar da güzel gelmez.", "kisi": "Tenzing Norgay", "eser": "Everest"},
        {"soz": "Hayat bir satranç oyunudur. Bir hamle yapmadan önce her zaman sonrakini düşünmelisin.", "kisi": "Beth Harmon", "eser": "The Queen's Gambit"},
        {"soz": "Karanlık bir odadayken muma küfretmek yerine onu yak.", "kisi": "Master Oogway", "eser": "Kung Fu Panda"},
        {"soz": "Aynaya bak, çünkü seni kurtaracak olan tek kişi orada duruyor.", "kisi": "Neo", "eser": "The Matrix Resurrections"},
        {"soz": "Kendine bir şans ver.", "kisi": "Will Hunting", "eser": "Good Will Hunting"},
        {"soz": "Gözlerini ufka dik ve yürümeye devam et.", "kisi": "Jack Sparrow", "eser": "Pirates of the Caribbean"},
        {"soz": "Ben bir hayatta kalanım.", "kisi": "Lara Croft", "eser": "Tomb Raider"},
        {"soz": "Bir şeyi istiyorsan bütün evren onu başarman için işbirliği yapar.", "kisi": "Santiago", "eser": "The Alchemist (Simyacı)"},
        {"soz": "Başarısızlık, yeniden ve daha zekice başlamak için bir fırsattır.", "kisi": "Henry Ford", "eser": "Ford v Ferrari"},
        {"soz": "Kaderimiz yıldızlarda değil, kendi içimizdedir.", "kisi": "Cassius", "eser": "Julius Caesar"},
        {"soz": "Zor zamanlar güçlü insanlar yaratır.", "kisi": "Gurney Halleck", "eser": "Dune: Çöl Gezegeni"},
        {"soz": "Bir insanın gerçek ölçüsü, gücü nasıl kullandığıdır.", "kisi": "Sirius Black", "eser": "Harry Potter"},
        {"soz": "Bizler kendi hikayelerimizin kahramanlarıyız.", "kisi": "Kral Arthur", "eser": "King Arthur"},
        {"soz": "Asla bana olasılıkları söyleme!", "kisi": "Han Solo", "eser": "Star Wars"},
        {"soz": "Gelecek, ona inananlara aittir.", "kisi": "Bane", "eser": "The Dark Knight Rises"},
        {"soz": "Bazı şeyler beklemeye değerdir.", "kisi": "Captain America", "eser": "Avengers"},
        {"soz": "Zaman her şeyi iyileştirmez, sadece onunla yaşamayı öğretir.", "kisi": "Dr. Grace Augustine", "eser": "Avatar"},
        {"soz": "Kurallar çiğnenmek için vardır, ancak doğru bir amaç uğruna.", "kisi": "James Bond", "eser": "Casino Royale"},
        {"soz": "En karanlık gece bile sona erer ve güneş tekrar doğar.", "kisi": "Victor Hugo", "eser": "Sefiller (Les Misérables)"},
        {"soz": "Ben tehlikede değilim. Tehlike benim!", "kisi": "Walter White", "eser": "Breaking Bad"},
        {"soz": "Kim olduğumuz, ne yaptığımızla tanımlanır.", "kisi": "Jason Bourne", "eser": "The Bourne Identity"},
        {"soz": "Savaşmadan kaybetmek, savaşarak kaybetmekten daha kötüdür.", "kisi": "Mulan", "eser": "Mulan"},
        {"soz": "Sadece bir hayatımız var, neden onu olağanüstü yapmayalım?", "kisi": "P.T. Barnum", "eser": "The Greatest Showman"},
        {"soz": "Şans, hazırlık ve fırsatın buluştuğu yerdir.", "kisi": "Seneca", "eser": "Gladiator"},
        {"soz": "Eğer bir hayalin varsa, uyan ve onu gerçeğe dönüştür.", "kisi": "Inception (Rüya Katmanı)", "eser": "Inception"},
        {"soz": "Küçük adımlar, büyük dağları aşmanı sağlar.", "kisi": "Bilbo Baggins", "eser": "The Hobbit"},
        {"soz": "Acı geçicidir, zafer ise sonsuz.", "kisi": "Apollo Creed", "eser": "Rocky II"},
        {"soz": "Bir şampiyon, düştüğünde bile kalkmasını bilendir.", "kisi": "Muhammad Ali", "eser": "Ali"},
        {"soz": "Geri dönüşler her zaman düşüşlerden daha görkemlidir.", "kisi": "Iron Man", "eser": "Iron Man 3"},
        {"soz": "Sınırlamalar sadece zihnimizdedir.", "kisi": "Dr. Strange", "eser": "Doctor Strange"},
        {"soz": "Ben bir hiç kimse değilim, ben her şeyim.", "kisi": "Arya Stark", "eser": "Game of Thrones"},
        {"soz": "Korkunu silahın yap.", "kisi": "Batman", "eser": "Batman Begins"},
        {"soz": "Umutsuzluk sadece bir yanılsamadır.", "kisi": "Aang", "eser": "Avatar: The Last Airbender"},
        {"soz": "Pes etmek her zaman en kolay yoldur, zor olan devam etmektir.", "kisi": "Naruto Uzumaki", "eser": "Naruto"},
        {"soz": "Benim kurallarım, benim hayatım.", "kisi": "Tommy Shelby", "eser": "Peaky Blinders"},
        {"soz": "Yenilmek ayıp değil, vazgeçmek ayıptır.", "kisi": "Eren Yeager", "eser": "Attack on Titan"},
        {"soz": "Hayal gücü, bilgiden daha önemlidir.", "kisi": "Albert Einstein", "eser": "Genius"},
        {"soz": "Mucizeler her gün olur, sadece onları görmeyi bilmelisin.", "kisi": "John Coffey", "eser": "The Green Mile (Yeşil Yol)"},
        {"soz": "Kararlarımız kaderimizi çizer.", "kisi": "John Connor", "eser": "Terminator 2"},
        {"soz": "Zor yollar her zaman güzel yerlere çıkar.", "kisi": "Cheryl Strayed", "eser": "Wild (Yaban)"},
        {"soz": "Geleceği tahmin etmenin en iyi yolu, onu icat etmektir.", "kisi": "Emmett Brown", "eser": "Back to the Future"},
        {"soz": "Savaşçı olmak, mükemmel olmak demek değildir. Kırılgan olmaktır.", "kisi": "Socrates", "eser": "Peaceful Warrior"},
        {"soz": "Kendine inanmazsan, kimse sana inanmaz.", "kisi": "Kobe Bryant", "eser": "The Last Dance"},
        {"soz": "Hedefine ulaşmak için önce yola çıkmalısın.", "kisi": "Frodo Baggins", "eser": "The Lord of the Rings"},
        {"soz": "Gerçek mucize, senin içindeki inançtır.", "kisi": "Neo", "eser": "The Matrix"},
        {"soz": "Karanlık olmadan yıldızları göremezsin.", "kisi": "Dexter", "eser": "Dexter"},
        {"soz": "Zafer hazırlığı seven bir dosttur.", "kisi": "The Mechanic", "eser": "The Mechanic"},
        {"soz": "Özgürlük, korkunun bittiği yerde başlar.", "kisi": "William Wallace", "eser": "Braveheart"},
        {"soz": "En büyük risk, hiç risk almamaktır.", "kisi": "Mark Zuckerberg", "eser": "The Social Network"},
        {"soz": "Başarmak için önce başlamalısın.", "kisi": "Wolverine", "eser": "Logan"},
        {"soz": "Seni durdurabilecek tek kişi sensin.", "kisi": "Black Panther", "eser": "Black Panther"},
        {"soz": "Her son, yeni bir başlangıçtır.", "kisi": "Vision", "eser": "WandaVision"},
        {"soz": "Kader, cesurlara güler.", "kisi": "Rey", "eser": "Star Wars: The Force Awakens"},
        {"soz": "Zayıflığını kabullen, onu güce çevir.", "kisi": "Tyrion Lannister", "eser": "Game of Thrones"},
        {"soz": "Gerçek hazine, yolculuğun kendisidir.", "kisi": "Monkey D. Luffy", "eser": "One Piece"},
        {"soz": "Gözyaşları, ruhun yağmurudur.", "kisi": "Iroh", "eser": "Avatar: The Last Airbender"},
        {"soz": "Savaş sadece kazanmak için değil, inandığın şey için verilir.", "kisi": "Optimus Prime", "eser": "Transformers"},
        {"soz": "En karanlık sırların, en büyük gücün olabilir.", "kisi": "Geralt of Rivia", "eser": "The Witcher"},
        {"soz": "Gülümse, çünkü hayat bir sahnedir.", "kisi": "The Joker", "eser": "Joker"},
        {"soz": "Yarın her zaman taze, hiçbir hatanın yapılmadığı yeni bir gündür.", "kisi": "Anne Shirley", "eser": "Anne with an E"},
        {"soz": "Kırık kalpler, daha güçlü atar.", "kisi": "John Wick", "eser": "John Wick"},
        {"soz": "Güçlü olan hayatta kalmaz, hayatta kalan güçlü olur.", "kisi": "Rick Grimes", "eser": "The Walking Dead"},
        {"soz": "Her fırtına er ya da geç diner.", "kisi": "Clark Kent", "eser": "Superman Returns"},
        {"soz": "Bir şeyi seviyorsan, onu serbest bırak.", "kisi": "Gollum", "eser": "The Lord of the Rings"},
        {"soz": "Geçmiş bir hayaldir, gelecek ise umut.", "kisi": "Master Shifu", "eser": "Kung Fu Panda"},
        {"soz": "Hiç kimse geride bırakılmaz.", "kisi": "Lilo", "eser": "Lilo & Stitch"},
        {"soz": "Küçük bir inanç, dünyaları yerinden oynatır.", "kisi": "Mulan", "eser": "Mulan"},
        {"soz": "Dünyayı değiştiremiyorsan, kendini değiştir.", "kisi": "Katniss Everdeen", "eser": "The Hunger Games"},
        {"soz": "Kahramanlar ağlamaz, savaşır.", "kisi": "Goku", "eser": "Dragon Ball Z"},
        {"soz": "Başarı, düşüp tekrar ayağa kalkmaktır.", "kisi": "Ash Ketchum", "eser": "Pokémon"},
        {"soz": "Bir insanın gözleri, ruhunun aynasıdır.", "kisi": "Hannibal Lecter", "eser": "The Silence of the Lambs"},
        {"soz": "Sonsuzluk ve ötesine!", "kisi": "Buzz Lightyear", "eser": "Toy Story"},
        {"soz": "Gerçek sihir, asla pes etmemektir.", "kisi": "Mickey Mouse", "eser": "Fantasia"},
        {"soz": "Bazen kimsenin hayal bile edemeyeceği şeyleri, kimsenin hiçbir şey beklemediği insanlar yapar.", "kisi": "Alan Turing", "eser": "The Imitation Game (Enigma)"},
        {"soz": "Sana sadece kapıyı gösterebilirim. İçinden geçmek zorunda olan sensin.", "kisi": "Morpheus", "eser": "The Matrix"},
        {"soz": "Atmadığın şutların %100'ünü kaçırırsın.", "kisi": "Michael Scott", "eser": "The Office"},
        {"soz": "En küçük insan bile geleceğin seyrini değiştirebilir.", "kisi": "Galadriel", "eser": "The Lord of the Rings (Yüzüklerin Efendisi)"},
        {"soz": "Benim tecrübelerime göre şans diye bir şey yoktur.", "kisi": "Obi-Wan Kenobi", "eser": "Star Wars (Yıldız Savaşları)"},
        {"soz": "Kendi mutluluğundan sadece sen sorumlusun. Başkalarının seni kurtarmasını bekleyemezsin.", "kisi": "BoJack Horseman", "eser": "BoJack Horseman"},
        {"soz": "Gelecek korkutucudur, ama sırf tanıdık geliyor diye geçmişe kaçamazsın.", "kisi": "Robin Scherbatsky", "eser": "How I Met Your Mother"},
        {"soz": "Zorluklar içinde açan çiçek, en nadir ve en güzel olanıdır.", "kisi": "İmparator", "eser": "Mulan"},
        {"soz": "Herkes harika bir sanatçı olamaz, ancak harika bir sanatçı herhangi bir yerden çıkabilir.", "kisi": "Anton Ego", "eser": "Ratatouille (Aşçı Fare)"},
        {"soz": "Pek çok şeyde olduğu gibi, önemli olan dışarıda olan değil, içeride olandır.", "kisi": "Tüccar", "eser": "Aladdin"},
        {"soz": "Sonunda hepimiz birer hikayeyiz. Sadece iyi bir hikaye olduğundan emin ol.", "kisi": "The Doctor", "eser": "Doctor Who"},
        {"soz": "Sadece başlarsın. Bir problemi çözersin, sonra diğerini... Yeterince problem çözersen, evine dönersin.", "kisi": "Mark Watney", "eser": "The Martian (Marslı)"},
        {"soz": "İki küçük fare krema dolu bir kovaya düştü. İkinci fare o kadar sıkı çırpındı ki, kremayı yağa çevirip dışarı tırmandı. Sen o ikinci faresin.", "kisi": "Frank Abagnale Sr.", "eser": "Catch Me If You Can (Sıkıysa Yakala)"},
        {"soz": "Önemli olan uçak değil, pilottur.", "kisi": "Pete 'Maverick' Mitchell", "eser": "Top Gun: Maverick"},
        {"soz": "Biz her zaman kendimizi imkansızı aşma yeteneğimizle tanımladık.", "kisi": "Cooper", "eser": "Interstellar (Yıldızlararası)"},
        {"soz": "Her seferinde tek bir adım. Tek bir yumruk. Tek bir raunt.", "kisi": "Rocky Balboa", "eser": "Creed"},
        {"soz": "Kötü zamanlar geçireceksin, ama bu seni her zaman dikkat etmediğin iyi şeylere uyandıracaktır.", "kisi": "Sean Maguire", "eser": "Good Will Hunting (Can Dostum)"},
        {"soz": "Elinden gelen her şeyi yapmalısın... Eğer bunları yapar ve pozitif kalırsan, o zaman umut ışığını bulursun.", "kisi": "Pat Solitano", "eser": "Silver Linings Playbook (Umut Işığım)"},
        {"soz": "Gelecek olan gelir ve geldiğinde onunla yüzleşiriz.", "kisi": "Rubeus Hagrid", "eser": "Harry Potter"},
        {"soz": "Normal olan hiç kimse bu dünyada anlamlı bir şey başaramamıştır.", "kisi": "Jonathan Byers", "eser": "Stranger Things"},
        {"soz": "Ancak her şeyi kaybettikten sonra her şeyi yapmakta özgür oluruz.", "kisi": "Tyler Durden", "eser": "Fight Club (Dövüş Kulübü)"},
        {"soz": "Mükemmellik, 'yeterince iyi'nin düşmanıdır.", "kisi": "Saul Goodman", "eser": "Better Call Saul"},
        {"soz": "Kendisine inanmayanlar için çok çalışmanın hiçbir değeri yoktur.", "kisi": "Naruto Uzumaki", "eser": "Naruto"},
        {"soz": "İnsanların gerçek gücü, kendilerini değiştirebilme yeteneklerinde yatar.", "kisi": "Saitama", "eser": "One Punch Man"},
        {"soz": "Ağla, sızla ama sakın pes etme!", "kisi": "Zenitsu Agatsuma", "eser": "Demon Slayer"},
        {"soz": "Bazen kahvaltıdan önce tam altı tane imkansız şeye inandığım olur.", "kisi": "The White Queen", "eser": "Alice in Wonderland (Alis Harikalar Diyarında)"},
        {"soz": "Hepsi bu kadar Miles. Sadece bir inanç sıçraması.", "kisi": "Peter B. Parker", "eser": "Spider-Man: Into the Spider-Verse (Örümcek-Adam: Örümcek Evreninde)"},
        {"soz": "Hayattaki en üzücü şey harcanmış yetenektir.", "kisi": "Lorenzo", "eser": "A Bronx Tale (Günaha Davet)"},
        {"soz": "Senin zihnin de bu su gibi dostum. Durulmasına izin verdiğinde, cevap netleşir.", "kisi": "Master Oogway", "eser": "Kung Fu Panda"},
        {"soz": "Ben buyum ve bu gayet iyi. Başka biri olmak istemezdim.", "kisi": "Wreck-It Ralph", "eser": "Wreck-It Ralph (Oyunbozan Ralph)"},
        {"soz": "Macera dışarıda bir yerlerde seni bekliyor!", "kisi": "Charles Muntz", "eser": "Up (Yukarı Bak)"},
        {"soz": "Yolculuğu ve nereye varacağını bilmeme rağmen, onu kucaklıyorum.", "kisi": "Louise Banks", "eser": "Arrival (Geliş)"},
        {"soz": "Benim dünyamda savaşmak zorundasın. İstediğin her şey için savaşmalısın.", "kisi": "Ragnar Lothbrok", "eser": "Vikings"},
        {"soz": "Zirveye çıkmak sancılıdır ama manzara buna değer.", "kisi": "Mary Jackson", "eser": "Hidden Figures (Gizli Sayılar)"},
        {"soz": "Cesur ol ve nazik davran.", "kisi": "Sindirella", "eser": "Cinderella (Sindirella)"},
        {"soz": "Bir hayat kurtaran, bütün dünyayı kurtarmış olur.", "kisi": "Itzhak Stern", "eser": "Schindler's List (Schindler'in Listesi)"},
        {"soz": "İnsanoğlu Dünya'da doğdu. Ancak burada ölmek zorunda değil.", "kisi": "Cooper", "eser": "Interstellar (Yıldızlararası)"},
        {"soz": "Umut aramak, sahip olduğumuz en büyük isyandır.", "kisi": "Max Rockatansky", "eser": "Mad Max: Fury Road"},
        {"soz": "Bazen tüm hayatın tek bir çılgınca hamleye bağlıdır.", "kisi": "Jake Sully", "eser": "Avatar"},
        {"soz": "Bir şey feda etmeden hiçbir şey elde edemezsin.", "kisi": "Edward Elric", "eser": "Fullmetal Alchemist"},
        {"soz": "Bir kahramanın asıl ölçüsü gücü değil, kalbinin büyüklüğüdür.", "kisi": "Zeus", "eser": "Hercules (Herkül)"},
        {"soz": "Ya uyum sağlarsın ya da yok olursun.", "kisi": "Billy Beane", "eser": "Moneyball (Kazanma Sanatı)"},
        {"soz": "Birinin sana sınırlarını söylemesine asla izin verme.", "kisi": "Remmy", "eser": "Ratatouille (Aşçı Fare)"},
        {"soz": "Bugünün zorlukları, yarının başarıları için ödediğimiz bedeldir.", "kisi": "Master Splinter", "eser": "Teenage Mutant Ninja Turtles (Ninja Kaplumbağalar)"},
        {"soz": "Asla geriye bakma canım, bu şimdiki zamandan çalıyor.", "kisi": "Edna Mode", "eser": "The Incredibles (İnanılmaz Aile)"},
        {"soz": "Dün tarihtir, yarın bir gizemdir, ama bugün bir armağandır.", "kisi": "Master Oogway", "eser": "Kung Fu Panda"},
        {"soz": "Sorun problemin kendisi değil. Sorun, senin probleme karşı takındığın tavırdır.", "kisi": "Jack Sparrow", "eser": "Pirates of the Caribbean (Karayip Korsanları)"},
        {"soz": "Ben bu dünyada kimsenin acımasına ihtiyaç duymadan kendi yolumu çizerim.", "kisi": "Tommy Shelby", "eser": "Peaky Blinders"},
        {"soz": "Hatalarını unut ve ilerle. Tıpkı 10 saniyelik hafızası olan bir japon balığı gibi.", "kisi": "Ted Lasso", "eser": "Ted Lasso"},
        {"soz": "Bazen en iyi kararlar, hiçbir mantığı olmayanlardır.", "kisi": "Sheldon Cooper", "eser": "The Big Bang Theory"},
        {"soz": "Ben başarısız olmadım. Sadece işe yaramayan 10.000 yol buldum.", "kisi": "Thomas Edison", "eser": "Mucit"},
        {"soz": "Mükemmellik eklenecek bir şey kalmadığında değil, çıkarılacak bir şey kalmadığında elde edilir.", "kisi": "Antoine de Saint-Exupéry", "eser": "Yazar & Pilot"},
        {"soz": "Bırakın doğruları gelecek söylesin ve herkesi eserlerine ve başarılarına göre değerlendirsin.", "kisi": "Nikola Tesla", "eser": "Elektrik Mühendisi & Mucit"},
        {"soz": "Mantık sizi A noktasından B noktasına götürür. Hayal gücü ise her yere.", "kisi": "Albert Einstein", "eser": "Teorik Fizikçi"},
        {"soz": "Tasarım sadece nasıl göründüğü veya hissettirdiği değildir. Tasarım nasıl çalıştığıdır.", "kisi": "Steve Jobs", "eser": "Teknoloji Girişimcisi"},
        {"soz": "Başarı, coşkunuzu kaybetmeden başarısızlıktan başarısızlığa koşabilme yeteneğidir.", "kisi": "Winston Churchill", "eser": "Devlet Adamı"},
        {"soz": "En büyük risk, hiç risk almamaktır. Hızla değişen bir dünyada başarısız olması garanti olan tek strateji budur.", "kisi": "Mark Zuckerberg", "eser": "Yazılımcı & Girişimci"},
        {"soz": "Fırsatlar genellikle çok çalışmak kılığına girmiş olarak gelir, bu yüzden çoğu insan onları tanımaz.", "kisi": "Ann Landers", "eser": "Yazar"},
        {"soz": "Eğer her şey kontrol altında görünüyorsa, yeterince hızlı gitmiyorsunuz demektir.", "kisi": "Mario Andretti", "eser": "Dünya Şampiyonu Pilot"},
        {"soz": "Bir makine 50 sıradan insanın işini yapabilir. Ancak hiçbir makine, sıra dışı bir insanın işini yapamaz.", "kisi": "Elbert Hubbard", "eser": "Yazar & Filozof"},
        {"soz": "Sorunları, onları yaratan aynı düşünce tarzıyla çözemeyiz.", "kisi": "Albert Einstein", "eser": "Teorik Fizikçi"},
        {"soz": "Dünyayı değiştirenler, bunu yapabileceklerini düşünecek kadar deli olanlardır.", "kisi": "Steve Jobs", "eser": "Teknoloji Girişimcisi"},
        {"soz": "Yapılmış küçük bir iş, planlanmış büyük bir işten çok daha iyidir.", "kisi": "Peter Marshall", "eser": "Hatip"},
        {"soz": "Başlamak için mükemmel olmanıza gerek yok, ama mükemmel olmak için başlamanız gerekir.", "kisi": "Zig Ziglar", "eser": "Yazar & Motivasyon Konuşmacısı"},
        {"soz": "Taşı delen suyun gücü değil, damlaların sürekliliğidir.", "kisi": "Latin Atasözü", "eser": "Anonim"},
        {"soz": "Bekleyenlere iyi şeyler gelebilir, ama sadece çabalayanların bıraktıkları kadarı.", "kisi": "Abraham Lincoln", "eser": "ABD Başkanı"},
        {"soz": "İlham bekleyemezsiniz. Onun peşinden elinizde bir sopayla gitmelisiniz.", "kisi": "Jack London", "eser": "Yazar"},
        {"soz": "Eğer her zaman yaptığını yaparsan, her zaman elde ettiğini elde edersin.", "kisi": "Henry Ford", "eser": "Sanayici & Mühendis"},
        {"soz": "Sadece güneşli günlerde yürürsen, hedefine asla ulaşamazsın.", "kisi": "Paulo Coelho", "eser": "Yazar"},
        {"soz": "Zorluklar, sıradan insanları sıra dışı bir kadere hazırlar.", "kisi": "C.S. Lewis", "eser": "Yazar & Akademisyen"},
        {"soz": "İyi bir mühendis, bir başkasının iki dolara zar zor yaptığı işi bir dolara yapabilen kişidir.", "kisi": "Arthur M. Wellington", "eser": "İnşaat Mühendisi"},
        {"soz": "En iyi hazırlık, bugünün işini harika yapmaktır.", "kisi": "H. Jackson Brown Jr.", "eser": "Yazar"},
        {"soz": "Hayat bisiklete binmek gibidir. Dengede kalmak için hareket etmeye devam etmelisiniz.", "kisi": "Albert Einstein", "eser": "Teorik Fizikçi"},
        {"soz": "Bir şeyler inşa etmek istiyorsanız, önce yıkımı göze almalısınız.", "kisi": "Anonim", "eser": "Mühendislik Prensibi"},
        {"soz": "Düşünmek zor bir sanattır, bu yüzden çoğu insan sadece yargılamayı seçer.", "kisi": "Carl Jung", "eser": "Psikiyatr"},
        {"soz": "Denemeyi bırakana kadar asla başarısız sayılmazsın.", "kisi": "Albert Einstein", "eser": "Teorik Fizikçi"},
        {"soz": "İnsanların ne dediğine takılma; çünkü onlar senin ne yaptığınla değil, kendilerine ne fayda sağladığınla ilgilenir.", "kisi": "Gerçeklik", "eser": "Hayat"},
        {"soz": "Eğer bir şeyin imkansız olduğuna inanırsanız, aklınız bunun neden imkansız olduğunu ispatlamak üzere çalışmaya başlar.", "kisi": "David J. Schwartz", "eser": "Yazar"},
        {"soz": "Yaratıcılık bulaşıcıdır. Onu yayın.", "kisi": "Albert Einstein", "eser": "Teorik Fizikçi"},
        {"soz": "Teori, her şeyin bilinip hiçbir şeyin çalışmadığı durumdur. Pratik ise her şeyin çalışıp kimsenin nedenini bilmediği durumdur.", "kisi": "Albert Einstein", "eser": "Teorik Fizikçi"},
        {"soz": "Dilimizdeki en tehlikeli cümle şudur: 'Biz bunu hep böyle yaptık.'", "kisi": "Grace Hopper", "eser": "Bilgisayar Bilimcisi & Amiral"},
        {"soz": "Yaratamadığım şeyi anlayamam.", "kisi": "Richard Feynman", "eser": "Teorik Fizikçi"},
        {"soz": "Uzman, dar bir alanda yapılabilecek tüm hataları yapmış kişidir.", "kisi": "Niels Bohr", "eser": "Fizikçi"},
        {"soz": "Sadelik, gelişmişliğin en üst noktasıdır.", "kisi": "Leonardo da Vinci", "eser": "Hezarfen & Mühendis"},
        {"soz": "Limandaki gemi güvendedir, ama gemiler bunun için inşa edilmemiştir.", "kisi": "Grace Hopper", "eser": "Bilgisayar Bilimcisi"},
        {"soz": "Bir şey yeterince önemliyse, ihtimaller aleyhinize olsa bile onu yaparsınız.", "kisi": "Elon Musk", "eser": "Teknoloji Girişimcisi"},
        {"soz": "Eyleme engel olan şey, eylemi ileriye taşır. Yolda duran şey, yolun kendisi olur.", "kisi": "Marcus Aurelius", "eser": "Filozof & İmparator"},
        {"soz": "Başarının sırrı yoktur. O; hazırlık, çok çalışma ve başarısızlıktan ders almanın sonucudur.", "kisi": "Colin Powell", "eser": "Devlet Adamı"},
        {"soz": "Hedeflerinizin seviyesine yükselemezsiniz, sistemlerinizin seviyesine düşersiniz.", "kisi": "James Clear", "eser": "Yazar (Atomik Alışkanlıklar)"},
        {"soz": "Mükemmele ulaşmak için iyiden vazgeçmekten korkmayın.", "kisi": "John D. Rockefeller", "eser": "İş İnsanı"},
        {"soz": "Zamanı gelmiş bir fikirden daha güçlü hiçbir şey yoktur.", "kisi": "Victor Hugo", "eser": "Yazar"},
        {"soz": "Motivasyon başlamanızı sağlar. Alışkanlık ise devam etmenizi.", "kisi": "Jim Rohn", "eser": "Girişimci & Yazar"},
        {"soz": "Yapabileceğinizi düşünseniz de, yapamayacağınızı düşünseniz de haklısınız.", "kisi": "Henry Ford", "eser": "Sanayici & Mühendis"},
        {"soz": "Zihniniz üzerinde gücünüz var, dış olaylar üzerinde değil. Bunu fark ettiğinizde güç bulacaksınız.", "kisi": "Epiktetos", "eser": "Filozof"},
        {"soz": "Eğer daha uzağı görebildiysem, bu devlerin omuzlarında durduğum içindir.", "kisi": "Isaac Newton", "eser": "Fizikçi & Matematikçi"},
        {"soz": "Büyük başarılar, her zaman yüksek beklentiler çerçevesinde gerçekleşir.", "kisi": "Charles Kettering", "eser": "Elektrik Mühendisi & Mucit"},
        {"soz": "Ürününüzün ilk versiyonundan utanmıyorsanız, piyasaya çıkmakta geç kalmışsınız demektir.", "kisi": "Reid Hoffman", "eser": "Girişimci"},
        {"soz": "Hiç hata yapmamış bir insan, yeni bir şey denememiş demektir.", "kisi": "Albert Einstein", "eser": "Teorik Fizikçi"},
        {"soz": "Hayatta hiçbir şeyden korkulmamalıdır, sadece anlaşılmalıdır.", "kisi": "Marie Curie", "eser": "Bilim İnsanı"},
        {"soz": "Eylem, tüm başarıların temel anahtarıdır.", "kisi": "Pablo Picasso", "eser": "Ressam & Tasarımcı"},
        {"soz": "Durmadığınız sürece ne kadar yavaş gittiğinizin bir önemi yoktur.", "kisi": "Konfüçyüs", "eser": "Filozof"},
        {"soz": "Bilim bilmektir, mühendislik ise yapmaktır.", "kisi": "Gordon Rogers", "eser": "Mühendis"},
        {"soz": "En iyi tasarımlar, sorunları görünmez kılanlardır.", "kisi": "Dieter Rams", "eser": "Endüstriyel Tasarımcı"},
        {"soz": "Fırsat kapıyı çalmıyorsa, bir kapı inşa et.", "kisi": "Milton Berle", "eser": "Yazar"},
        {"soz": "Bir problemi anlamak, onu çözmenin yarısıdır.", "kisi": "Charles Kettering", "eser": "Mühendis & Mucit"},
        {"soz": "Dünyadaki en önemli şeylerin çoğu, hiç umut görünmediği halde denemeye devam eden insanlar tarafından başarılmıştır.", "kisi": "Dale Carnegie", "eser": "Yazar"},
        {"soz": "Yeteneğinizi her gün bir milimetre daha ileri taşımak, bir gün aniden sıçramaktan daha kalıcıdır.", "kisi": "Kaizen Felsefesi", "eser": "Sürekli Gelişim Pratiği"},
        {"soz": "Kalite bir eylem değil, bir alışkanlıktır.", "kisi": "Aristoteles", "eser": "Filozof"},
        {"soz": "Hayal gücü, bilginin ulaşamadığı yerlere köprü kurar.", "kisi": "Carl Sagan", "eser": "Astrofizikçi"},
        {"soz": "Büyük yapılar aniden ortaya çıkmaz; katman katman, sabırla inşa edilir.", "kisi": "Mimari Prensip", "eser": "Tasarım Felsefesi"},
        {"soz": "Her şeyin bir bedeli vardır; hiçbir şey yapmamanın bedeli ise potansiyelinizin yok olmasıdır.", "kisi": "Anonim", "eser": "Mühendislik Kuralı"},
        {"soz": "Düşüncelerinizi değiştirin, dünyanız değişsin.", "kisi": "Norman Vincent Peale", "eser": "Yazar"},
        {"soz": "Kaybetme korkusunun, kazanma heyecanından daha büyük olmasına izin vermeyin.", "kisi": "Robert Kiyosaki", "eser": "Yatırımcı & Yazar"},
        {"soz": "10.000 farklı tekmeyi bir kez çalışandan korkmam, aynı tekmeyi 10.000 kez çalışandan korkarım.", "kisi": "Bruce Lee", "eser": "Dövüş Sanatçısı & Filozof"},
        {"soz": "Yapabildiğinizi hissettiğiniz anda, zaten yarı yolu geçmişsinizdir.", "kisi": "Theodore Roosevelt", "eser": "Devlet Adamı"}
    ])

secilen_soz = st.session_state["gunun_sozu"]

# --- ANA SAYFA BAŞLIK VE MOTİVASYON METNİ ---
col_baslik, col_motivasyon = st.columns([5, 4])

with col_baslik:
    st.title("İş Başvuru Takip Sistemi")

with col_motivasyon:
    st.markdown(f"""
        <div style="text-align: right; padding-top: 15px;">
            <div style="font-size: 0.95em; font-style: italic; color: #444;">"{secilen_soz['soz']}"</div>
            <div style="font-size: 0.85em; color: #888; margin-top: 6px;">
                <strong style="color: #222;">{secilen_soz['kisi']}</strong> • {secilen_soz['eser']}
            </div>
        </div>
    """, unsafe_allow_html=True)


# --- KİŞİSEL HESAPLAR ---
st.markdown("""
    <div style="display: flex; gap: 15px; margin-bottom: 25px;">
        <a href="https://www.linkedin.com/jobs/" target="_blank" style="text-decoration: none;">
            <img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
        </a>
        <a href="https://www.kariyer.net/is-ilanlari" target="_blank" style="text-decoration: none;">
            <img src="https://img.shields.io/badge/Kariyer.net-%23832388.svg?style=for-the-badge&logo=reverbnation&logoColor=white" alt="Kariyer.net"/> 
        </a>
        <a href="https://github.com/" target="_blank" style="text-decoration: none;">
            <img src="https://img.shields.io/badge/GitHub-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
        </a>
    </div>
""", unsafe_allow_html=True)

DURUMLAR = [
    "✅ Başvuru Yapıldı",  "🗣️ İK Mülakatı", "💻 Çevrim içi Mülakat", 
    "🎉 Teklif Alındı", "⏳ Cevap Gelmedi", "❌ Reddedildi"
]

PLATFORMLAR = ["LinkedIn", "Kariyer.net", "Toptalent" , "Şirket Sitesi", "Referans", "Diğer"]

@st.cache_data
def veri_yukle():
    try:
        df_lokal = pd.read_csv("basvurular.csv")
        metin_sutunlari = ["Sirket", "Pozisyon", "Platform", "Durum"]
        for sutun in metin_sutunlari:
            if sutun in df_lokal.columns:
                df_lokal[sutun] = df_lokal[sutun].fillna("")
                df_lokal[sutun] = df_lokal[sutun].replace({"None": "", "nan": ""})
                
        df_lokal["Tarih"] = pd.to_datetime(df_lokal["Tarih"], dayfirst=True, errors="coerce")
        df_lokal["Tarih"] = df_lokal["Tarih"].fillna(pd.Timestamp.now()).dt.date
        
        # DÜZELTME: Sıralamayı tam veri yüklenirken 1'den başlatıyoruz, NameError riskini sıfırlıyoruz.
        df_lokal.index = range(1, len(df_lokal) + 1)
        return df_lokal
    except FileNotFoundError:
        empty_df = pd.DataFrame(columns=["Sirket", "Pozisyon", "Platform", "Tarih", "Durum"])
        empty_df.index = range(1, len(empty_df) + 1)
        return empty_df

df = veri_yukle()


# --- OYUNLAŞTIRMA: HAFTALIK BAŞVURU HEDEFİ ---
st.subheader("🎯 Haftalık Başvuru Hedefi")
haftalik_hedef = 5

bugun = pd.Timestamp.now().date()
haftanin_basi = bugun - pd.Timedelta(days=bugun.weekday())

df_hedef = df.copy()
df_hedef["Tarih"] = pd.to_datetime(df_hedef["Tarih"], errors="coerce").dt.date
bu_hafta_sayi = len(df_hedef[df_hedef["Tarih"] >= haftanin_basi])

ilerleme_orani = min(bu_hafta_sayi / haftalik_hedef, 1.0)
st.progress(ilerleme_orani, text=f"Bu hafta {bu_hafta_sayi} / {haftalik_hedef} başvuru tamamlandı!")

if bu_hafta_sayi >= haftalik_hedef:
    st.success("🎉 Tebrikler! Bu haftaki başvuru hedefine ulaştın. Gönder Gelsin!")
    if "konfeti_patladi" not in st.session_state:
        st.balloons()
        st.session_state["konfeti_patladi"] = True
else:
    if "konfeti_patladi" in st.session_state:
        del st.session_state["konfeti_patladi"]

#st.divider()


# --- YENİ BAŞVURU EKLEME FORMU ---
with st.expander("➕ Yeni Başvuru Ekle", expanded=False):
    
    # 1. Varsayılan (Sabit ve Kalıcı) Listelerimiz
    varsayilan_sirketler = [
        "Aselsan", "TUSAŞ", "Baykar", "Ford Otosan", "Toyota", "Teksan", 
        "Mercedes-Benz", "Siemens", "Enerjisa", "Zorlu Enerji", "Tüpraş", "Şişecam", "Otokar"
    ]
    
    varsayilan_pozisyonlar = [
        "Teknik Ressam", "Proje Tasarım Uzman Yardımcısı", "Elektrik-Elektronik Teknisyeni", 
        "Enerji Yöneticisi", "Ar-Ge Asistanı", "CAD/CAM Tasarımcısı", "Üretim Teknisyeni" , "Mühendis" , "Mimar" , "Tekniker"
    ]

    # 2. CSV'den mevcutları öğren ve varsayılanlarla birleştir 
    mevcut_sirketler = df["Sirket"].dropna().unique().tolist() if "Sirket" in df.columns else []
    mevcut_pozisyonlar = df["Pozisyon"].dropna().unique().tolist() if "Pozisyon" in df.columns else []

    tum_sirketler = sorted(list(set(varsayilan_sirketler + mevcut_sirketler)))
    tum_pozisyonlar = sorted(list(set(varsayilan_pozisyonlar + mevcut_pozisyonlar)))

    # 3. Tüm Listelerin Başına "Seçiniz" Eklendi
    sirket_secenekleri = [" Seçiniz..."] + tum_sirketler + ["Diğer (Yeni Ekle)"]
    pozisyon_secenekleri = [" Seçiniz..."] + tum_pozisyonlar + ["Diğer (Yeni Ekle)"]
    platform_secenekleri = [" Seçiniz..."] + PLATFORMLAR
    durum_secenekleri = [" Seçiniz..."] + DURUMLAR

    col1, col2 = st.columns(2)
    
    with col1:
        secilen_sirket = st.selectbox("Şirket Adı *", sirket_secenekleri)
        if secilen_sirket == "Diğer (Yeni Ekle)":
            yeni_sirket = st.text_input("✨ Yeni Şirket Adını Yazın", placeholder="Örn: BMC")
        elif secilen_sirket == " Seçiniz...":
            yeni_sirket = ""
        else:
            yeni_sirket = secilen_sirket

        secilen_pozisyon = st.selectbox("Pozisyon *", pozisyon_secenekleri)
        if secilen_pozisyon == "Diğer (Yeni Ekle)":
            yeni_pozisyon = st.text_input("✨ Yeni Pozisyonu Yazın", placeholder="Örn: Kalite Kontrol Uzmanı")
        elif secilen_pozisyon == " Seçiniz...":
            yeni_pozisyon = ""
        else:
            yeni_pozisyon = secilen_pozisyon

        yeni_platform = st.selectbox("Platform *", platform_secenekleri)
        
    with col2:
        # Tarih kutusunu "value=None" ile başlangıçta tamamen boş yapıyoruz
        yeni_tarih = st.date_input("Başvuru Tarihi *", value=None, format="DD/MM/YYYY")
        
        yeni_durum = st.selectbox("Güncel Durum *", durum_secenekleri)
        
    if st.button("💾 Başvuruyu Kaydet"):
        # Boş bırakılan alan var mı diye tüm kutuları kontrol ediyoruz
        if yeni_sirket == "" or yeni_pozisyon == "" or yeni_platform == " Seçiniz..." or yeni_durum == " Seçiniz..." or yeni_tarih is None:
            st.warning("⚠️ Lütfen yıldızlı (*) tüm zorunlu alanları (Şirket, Pozisyon, Platform, Tarih, Durum) doldurunuz!")
        else:
            yeni_veri = {
                "Sirket": yeni_sirket, "Pozisyon": yeni_pozisyon, "Platform": yeni_platform,
                "Tarih": yeni_tarih.strftime("%d/%m/%Y"), "Durum": yeni_durum
            }
            yeni_df = pd.DataFrame([yeni_veri])
            
            df_csv = pd.read_csv("basvurular.csv") if os.path.exists("basvurular.csv") else pd.DataFrame(columns=["Sirket", "Pozisyon", "Platform", "Tarih", "Durum"])
            df_csv = pd.concat([df_csv, yeni_df], ignore_index=True)
            df_csv.to_csv("basvurular.csv", index=False)
            st.cache_data.clear()
            st.success("✅ Yeni başvuru eklendi!")
            st.rerun()

# --- 2. DÜZENLENEBİLİR TABLO VE ARAMA MOTORU ---
st.subheader("📋 Başvuru Listesi")

col1, col2 = st.columns(2)

with col1:
    arama = st.text_input("🏢 Şirket Adını Ara", "")

with col2:
    secilen_durum = st.multiselect("📌 Duruma Göre Filtrele", DURUMLAR, placeholder=" ")

filtrelenmis_df = df.copy()

if arama:
    filtrelenmis_df = filtrelenmis_df[filtrelenmis_df["Sirket"].str.contains(arama, case=False, na=False)]

if secilen_durum:
    filtrelenmis_df = filtrelenmis_df[filtrelenmis_df["Durum"].isin(secilen_durum)]

TABLO_SIRALAMASI = ["Sirket", "Pozisyon", "Platform", "Tarih", "Durum"]
filtrelenmis_df = filtrelenmis_df[TABLO_SIRALAMASI]

st.markdown("") 

if arama or secilen_durum:
    st.info("💡 Arama modundayken yanlışlıkla veri silinmemesi için tablo 'Sadece Okunabilir' moddadır. Düzenlemek ve silmek için yukarıdaki filtreleri temizleyin.")
    # Sade tablo ekrana basılır
    st.dataframe(filtrelenmis_df, use_container_width=True, hide_index=False)
    edited_df = filtrelenmis_df
else:
    # Sade ve kilitli tablo (Şirket ve Pozisyon düzenlenemez)
    edited_df = st.data_editor(
        filtrelenmis_df, 
        use_container_width=True,
        hide_index=False, 
        num_rows="dynamic", 
        disabled=["Sirket", "Pozisyon"], 
        column_config={
            "Durum": st.column_config.SelectboxColumn("Güncel Durum", options=DURUMLAR, required=True),
            "Platform": st.column_config.SelectboxColumn("Platform", options=PLATFORMLAR, required=True),
            "Tarih": st.column_config.DateColumn("Başvuru Tarihi", format="DD/MM/YYYY")
        }
    )

    if st.button("🔄 Değişiklikleri Kaydet"):
        save_df = edited_df.copy()
        save_df["Tarih"] = pd.to_datetime(save_df["Tarih"], dayfirst=True).dt.strftime("%d/%m/%Y")
        save_df.to_csv("basvurular.csv", index=False)
        st.cache_data.clear()
        st.success("✅ Tüm güncellemeler başarıyla veritabanına işlendi!")
        st.rerun()
        
st.divider()


# --- 3. GRAFİK VE ÖZEL İSTATİSTİKLER ---
st.subheader("📊 Başvuru Analizi")

toplam_basvuru = len(edited_df)
red_sayisi = len(edited_df[edited_df["Durum"] == "❌ Reddedildi"])
cevap_gelmeyen = len(edited_df[edited_df["Durum"] == "⏳ Cevap Gelmedi"])
mulakat_asamasinda = len(edited_df[edited_df["Durum"].str.contains("Mülakat", na=False)])

col_m1, col_m2, col_m3, col_m4 = st.columns(4)
col_m1.metric(label="Toplam Başvuru", value=toplam_basvuru)
col_m2.metric(label="Mülakat Aşamasında", value=mulakat_asamasinda)
col_m3.metric(label="Cevap Beklenen/Gelmeyen", value=cevap_gelmeyen)
col_m4.metric(label="Reddedilen", value=red_sayisi)

if not edited_df.empty:
    durum_sayilari = edited_df["Durum"].value_counts().reset_index()
    durum_sayilari.columns = ["Durum", "Sayı"]
    
    fig = px.bar(
        durum_sayilari, 
        x="Durum", 
        y="Sayı", 
        color="Durum", 
        text_auto=True, 
        title="Durumlara Göre Dağılım",
        category_orders={"Durum": DURUMLAR}
    )
    fig.update_layout(height=300, showlegend=False, xaxis_title="", yaxis_title="Şirket Sayısı")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Grafik oluşturulacak veri henüz yok.")