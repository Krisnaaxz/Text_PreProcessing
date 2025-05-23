import re
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


data = [
    #doc 1
    "elearning di PTIIK diatas jam 6 malam kok selalu gak bisa dibuka ya?",
    #doc 2       
    "ub tidak punya lahan parkir yang layak. Dan jalanan terlalu ramai karena di buka untuk umum. Seperti jalan tol saja. Brawijaya oh brawijaya",
    #doc 3       
    "Kelas Arsitektur dan Organisasi Komputer penuh, apakah tidak dibuka kelas lagi. Rugi kalo saya bisa ngambil 24 SKS tapi baru 18 SKS yg terpenuhi",
    #doc 4
    "Informasi tata cara daftar ulang bagi mahasiswa baru PTIIK kurang jelas. Sehingga ketika tanggal terakhir syarat penyerahan berkas daftar ulang, banyak mahasiswa baru yang tidak membawa salah satu syarat daftar ulangnya."
    ]

#Case folding
data = [d.lower() for d in data]

#Menghilangkan spasi, tanda baca, dan angka
data = [re.sub(r'[^a-z\s]', '', d) for d in data]

#Tokenisasi data text
token = [d.split() for d in data]
print("\nHasil Tokenisasi: ", token)

#Stopsword removal
stopword_factory = StopWordRemoverFactory()
stopwords = stopword_factory.get_stop_words()

token = [[k for k in kal if k not in stopwords] for kal in token]
print("\nHasil Stopword Removal: ", token)

#Stemming
stemmer_factory = StemmerFactory()
stemmer = stemmer_factory.create_stemmer()

token = [[stemmer.stem(word) for word in k] for k in token]

#Menghapus duplikasi token
#token = [list(dict.fromkeys(kal)) for kal in token]

print("\nHasil Stemming: ", token)

print("\n\n==============================================")
print("Hasil Preprocessing: \n")
for i, words in enumerate(token):
    words = ", ".join(words)
    print(f"Doc {i+1}: {words}")
print("==============================================")