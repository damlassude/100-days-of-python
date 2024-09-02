#maximum element

scores = [5, 6, 7, 8]

# İlk elemanı başlangıçta en büyük olarak kabul edin
max_score = scores[0]

# Liste elemanlarını dolaşarak en büyük olanı bulun
for score in scores:
    if score > max_score:
        max_score = score

# En büyük elemanı yazdırın
print(max_score)