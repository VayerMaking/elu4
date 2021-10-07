# a tool for mass addition of new books
import os
import natsort

path = os.getcwd() + "/images/math_uchebnik_new" # last part is the folder u have the new images

files = os.listdir(path) # make an array with all the filenames in the directory

file = open("generated.txt", "a") # write generated div elements in a file for copy/paste later

files = natsort.natsorted(files) # sort files names to be in book order

for f in files: # make div elements for every filename in the directory
	file.write(
	"""<div class="swiper-slide">
	<img data-src="images/math_pomagalo/""" + str(f) + """ "   class="swiper-lazy">
	<div class="swiper-lazy-preloader swiper-lazy-preloader-white"></div>
	</div>""" + "\n")

file.close()
