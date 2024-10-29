foo = { 1: "Belajar", 2: "Python", 3: "di Duniasasha" }
bar = { "mengapa": "Belajar", "apa": "Python", "dimana": "di Duniasasha" }
baz = { 1: "Belajar", "apa": "Python", "dimana": "di Duniasasha" }
 
print(type(foo))
print(type(bar))
print(type(baz))
 
print(foo)
print(bar)
print(baz)
foo = { 1: "Belajar", 
        2: ["Pascal", "C", "Python"],
        "website": "Duniasasha",
        "menyerah" : False,
        "target": 2024,
        "riwayat_sekolah": {
          "SD": "SDN 07 bali",
          "SMP": "SMP frater mamasa",
          "SMk": "Smk negeri 1 mamasa"}
      }
       
print(foo)
foo = { "kegiatan": "Belajar Python",
        "website": "Duniasasha",
        "hasil": "pasti bisa dong!" }
 
print(foo["website"])

2
3
4
5
6
foo = { "kegiatan": "Belajar Python",
        "website": "Duniasasha",
        "hasil": "Yakin bisa!" }
 
foo["kegiatan"] = "Belajar Bahasa Pemrograman"
print(foo)

foo = { "kegiatan": "Belajar Python",
        "website": "Duniasasha",
        "hasil": "bisalah!" }
 
foo["target"] = 2025
print(foo)
