# 💖 Katkı Sağlama Rehberi

## 🤝 Destek İhtiyaçları

- 📈 En az karşılaştırma ile sıralama algoritması gerekmekte
    - 👮‍♂️ Kullanıcıya çok fazla sorulmaması lazım
    - 🤦‍♂️ Yoksa sıkıcı bir hale dönüşür
- 💁‍♂️ Eğer `A < B` ise `A`; `B`'den büyük olan her şeyden küçüktür
- 💁‍♂️ Eğer `A > B` ise `A`; `B`'den küçük olan her şeyden büyüktür
- 🙄 Bellek kullanımı mühim değildir

> 👨‍💻 Kodlama işlemlerinde `<` veya `>` işlemleri yerine `choice.py` metotlarını kullanın


## 💡 Seçim Yaptırma

- 👮‍♂️ `choice.py` metodundakiler kullanılacaktır
- 📦 `from choice.py import isBetter, isWorse` ile projeye dahil edilebilir

💘 Karşılaştırma | 💎 Metot | 📝 Açıklama
-- | -- | --
`a > b` | `isBetter(a, b)` | Daha iyi ise `true`
`a >= b` | `isBetter(a, b, equal=True)` | Daha iyi veya eşitse `true`
`a < b` | `isWorse(a, b)` | Daha kötü ise `true`
`a <= b` | `isWorse(a, b, equal=True)` | Daha kötü veya eşitse `true`

## 🚧 Çalışma Süreci

👨‍🔬 Şu anda neyle uğraşılmakta:

- 📋 Cache yapısı ile sorular azaltılmaya çalışılmakta
    - 💁‍♂️ Eğer `A < B` ise `A`; `B`'den büyük olan her şeyden küçüktür
    - 💁‍♂️ Eğer `A > B` ise `A`; `B`'den küçük olan her şeyden büyüktür
    - 👆 Yukarıdaki koşullar sağanıyorsa kullanıcıya sorulmamalı
