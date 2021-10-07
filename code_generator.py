import os
import natsort

path = os.getcwd() + "/images/math_uchebnik_new" # last part is the folder u have the new images

files = os.listdir(path)

file = open("generated.txt", "a")

files = natsort.natsorted(files)
#print(files)

for f in files:
	#print(f)
	file.write(
	"""<div class="swiper-slide">
	<img data-src="images/math_pomagalo/""" + str(f) + """ "   class="swiper-lazy">
	<div class="swiper-lazy-preloader swiper-lazy-preloader-white"></div>
	</div>""" + "\n")

file.close()
