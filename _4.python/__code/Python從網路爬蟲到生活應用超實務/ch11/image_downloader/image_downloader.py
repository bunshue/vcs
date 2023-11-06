import csv
import shutil
import os
import urllib.parse
import urllib.request

# http client configuration
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/63.0.3239.84 Chrome/63.0.3239.84 Safari/537.36'

urljoin = urllib.parse.urljoin
urlretrieve = urllib.request.urlretrieve
quote = urllib.parse.quote
# configure headers
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', user_agent)]
urllib.request.install_opener(opener)

def fix_url(url):
    url = quote(url, safe="%/:=&?~#+!$,;'@()*[]")
    return url

def download_csv_row_images(count, row, dest_dir):
    for key in row:
        start_url = ""
        if key.endswith("-src"):
            image_url = row[key]
            image_url = urljoin(start_url, image_url)

            image_filename = "%s-%s" % (key[0:-4], str(count))
            download_image(image_url, dest_dir, image_filename)

def download_image(image_url, dest_dir, image_filename):

    image_url = fix_url(image_url)

    try:
        print("downloading image %s" % image_url)
        tmp_file_name, headers = urlretrieve(image_url)
        content_type = headers.get("Content-Type")

        if content_type == 'image/jpeg' or content_type == 'image/jpg':
            ext = 'jpg'
        elif content_type == 'image/png':
            ext = 'png'
        elif content_type == 'image/gif':
            ext = 'gif'
        else:
            print("unknown image content type %s" % content_type)
            return

        image_path = os.path.join(dest_dir, image_filename+"."+ext)
        shutil.move(tmp_file_name, image_path)
    except Exception as e:
        print("Image download error. %s" % e)

def get_csv_image_dir(csv_filename):

    base = os.path.basename(csv_filename)
    dir = os.path.splitext(base)[0]

    if not os.path.exists(dir):
        os.makedirs(dir)

    return dir

def download_csv_file_images(filename):

    print("importing data from %s" % filename)
    
    dest_dir = get_csv_image_dir(filename)

    #check whether csv file has utf-8 bom char at the beginning
    skip_utf8_seek = 0
    with open(filename, "rb") as csvfile:
        csv_start = csvfile.read(3)
        if csv_start == b'\xef\xbb\xbf':
            skip_utf8_seek = 3


    with open(filename, "r", encoding='big5') as csvfile:

        # remove ut-8 bon sig
        csvfile.seek(skip_utf8_seek)

        csvreader = csv.DictReader(csvfile)
        count = 1
        for row in csvreader:
            download_csv_row_images(count, row, dest_dir)
            count = count + 1

