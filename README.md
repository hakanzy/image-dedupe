image-dedupe
============

Image Dedupe (compare two images for similarity)

**About**

- It is a simple image duplication tool.

- It uses average hash method for image hashing.

- It uses hamming distance for comparing image hashes.


**Usage**

`In [1]: from image-dedupe import ImageSimilarity`

`In [2]: sim = ImageSimilarity()`

`In [3]: sim.is_similar('1.jpg', '2.jpg')`

`Out[3]: True`

