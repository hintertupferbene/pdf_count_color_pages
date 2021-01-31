# pdf_count_color_pages
Short Python script to count the number of color pages in a PDF file

# Setup
Set up python environment, e.g. with anaconda:
```sh
conda env create --prefix ./env -f environment.yml
```
Then activate it:
```sh
conda activate ./env
```

# Usage
Simply pass the path to the PDF file that shall be analyzed as command line argument, like
```sh
python count_color_pages.py document.pdf
```
for the file `document.pdf`.

# How it works
For each page of the PDF file, an image (PIL) of this page is created using the `pdf2image` package.
Using the PIL method `getcolors`, all existing colors (or gray levels) within the image are determined.
Colors returned by this method are represented as RGB tuples.
A color is interpreted as a gray level if all three RGB values are almost equal. 
If this condition is not fulfilled for any of the returned colors, the page is considered as a color page.

