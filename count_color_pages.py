#!/usr/bin/python

import sys
import numpy as np
from PyPDF2 import PdfFileReader
import pdf2image


def main():
	if len(sys.argv) != 2:
		print('One command line argument required: path to PDF file that shall be analyzed')
		return

	pdf_file = sys.argv[1]

	with open(pdf_file, 'rb') as f:
		pdf = PdfFileReader(f)
		number_of_pages = pdf.getNumPages()

	print('Number of pages: ' + str(number_of_pages))

	color_pages = []

	for page_number in range(1, number_of_pages + 1):
		print('\rProcessing page ' + str(page_number) + ' of ' + str(number_of_pages), end='')

		images = pdf2image.convert_from_path(pdf_file, first_page=page_number, last_page=page_number)  # process only one page
		im = images[0]

		colors = im.getcolors(maxcolors=im.width*im.height)

		assert colors is not None

		color_found = check_for_any_non_gray_color(colors)
		if color_found:
			color_pages.append(page_number)

	print('\n' + str(len(color_pages)) + ' color pages: ' + str(color_pages))
	

def check_for_any_non_gray_color(colors):
	"""
	Check for all colors found in the current page if any of them is not a gray level.

	:param colors: list of tuples (count, color tuple)
	:return: True if color found, False if only gray levels
	"""
	for c in colors:
		color = np.array(c[1])
		max_diff = np.abs(color - np.median(color)).max()
		if max_diff > 3:
			return True
	return False


if __name__ == '__main__':
	main()
