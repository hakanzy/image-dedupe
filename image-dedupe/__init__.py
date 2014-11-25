from PIL import Image


class ImageSimilarity(object):

    def ahash(self, image):
        # This is average hash
        # http://www.hackerfactor.com/blog/?/archives/432-Looks-Like-It.html
        image = image.resize((8, 8), Image.ANTIALIAS).convert('L')
        pixels = list(image.getdata())
        avg = sum(pixels) / len(pixels)
        bits = "".join(map(lambda pixel: '1' if pixel > avg else '0', pixels))

        return int(bits, 2).__format__('016x')

    def hamming_distance(self, string1, string2):
        # See: http://en.wikipedia.org/wiki/Hamming_distance
        diffs = 0
        for c1, c2 in zip(string1, string2):
            if c1 != c2:
                diffs += 1
        return diffs

    def is_similar(self, image_path1, image_path2, threshold=90):
        image1 = Image.open(image_path1)
        image2 = Image.open(image_path2)

        hash1 = self.ahash(image1)
        hash2 = self.ahash(image2)

        distance = self.hamming_distance(hash1, hash2)

        return int(100 - ((100 / 16) * distance)) >= threshold
