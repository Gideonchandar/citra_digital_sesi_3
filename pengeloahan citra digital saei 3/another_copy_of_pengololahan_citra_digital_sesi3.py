# -*- coding: utf-8 -*-
"""Another copy of pengololahan_citra_digital_sesi3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1i_pS7kCfh57rcjKSqNo9wZEJc7tC6YCt
"""

import imageio
import numpy as np
import matplotlib.pyplot as plt

# Membaca gambar RGB
image = imageio.imread('/content/RGB.jpg')

# Jika gambar dalam format RGB, konversikan ke grayscale menggunakan rumus konversi
if image.ndim == 3:  # Memastikan gambar dalam format RGB
    grayscale_image = 0.2989 * image[:,:,0] + 0.5870 * image[:,:,1] + 0.1140 * image[:,:,2]
else:
    grayscale_image = image  # Jika sudah grayscale

# Menghitung histogram
histogram, bins = np.histogram(grayscale_image, bins=256, range=(0, 255))

# Plot histogram
plt.figure(figsize=(10, 6))
plt.plot(bins[:-1], histogram, color='black')
plt.title('Histogram Gambar Grayscale')
plt.xlabel('Intensitas Piksel')
plt.ylabel('Frekuensi')
plt.grid(True)
plt.show()

"""a. Berapa jumlah total piksel untuk setiap intensitas pada gambar grayscale?
histogramvariabel:

* Ini adalah array NumPy yang menyimpan frekuensi setiap tingkat intensitas
  piksel dalam gambar.
* histogram[0]mewakili jumlah piksel dengan intensitas 0.
* histogram[1]mewakili jumlah piksel dengan intensitas 1, dan seterusnya.
  
  bins variabel:

* Ini juga merupakan array NumPy yang menentukan tepian bin yang digunakan      dalam histogram.
* Karena Anda menggunakan 256 wadah untuk rentang intensitas 0-255, setiap wadah berhubungan dengan satu tingkat intensitas.

Mengakses jumlah piksel:

* Anda dapat mengakses jumlah total piksel untuk tingkat intensitas tertentu dengan mengindeks histogramarray.
* Misalnya, histogram[50]memberi Anda jumlah total piksel dengan nilai intensitas 50.

b. Apakah ada intensitas tertentu yang dominan dalam gambar tersebut? Jelaskan.

 Menentukan Intensitas Dominan:

Intensitas dominan dalam gambar yang ditampilkan oleh puncak atau nilai tertinggi dalam histogram. Dalam kode yang Anda berikan, histogram disimpan dalam variabel histogram, dan nilai-nilai intensitas yang sesuai disimpan dalam variabel bins.

Untuk menemukan intensitas dominan, kita perlu menemukan elemen indeks maksimum dalam array histogram, yang akan menunjukkan intensitas dengan frekuensi tertinggi. Kita kemudian dapat menggunakan indeks ini untuk mendapatkan nilai intensitas yang sesuai dari array bins.

Kesimpulan:

Dengan menganalisis histogram dan menemukan intensitas dengan frekuensi tertinggi, kita dapat menentukan apakah ada intensitas tertentu yang dominan dalam gambar. Kode yang diberikan di atas dapat membantu Anda mengidentifikasi intensitas dominan ini.
"""