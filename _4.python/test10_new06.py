import os

def is_image(filename):
    f = filename.lower()
    return f.endswith('.png') or f.endswith('.jpg') or \
           f.endswith('.jpeg') or f.endswith('.bmp') or \
           f.endswith('.gif') or '.jpg' in f or f.endswith('.svg')


def find_similar_images(foldername):
    image_filenames = []
    image_filenames += [os.path.join(foldername, path) for path in os.listdir(foldername) if is_image(path)]
    for img in sorted(image_filenames):
        print(img)

foldername = 'C:/_git/vcs/_1.data/______test_files5'
find_similar_images(foldername)
