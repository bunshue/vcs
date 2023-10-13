import csv
import os
from collections import defaultdict

import torch
import torchvision.transforms as transforms
from torch.utils.data import Dataset, Subset
from torch import randperm
from PIL import Image


class ImageCaptionDataset(Dataset):
    def __init__(self, img_root, caption_path, img_size=256, seq_len=40):
        super(ImageCaptionDataset).__init__()
        self.img_root = img_root
        self.caption_path = caption_path
        self.img_size = img_size
        self.seq_len = seq_len

        # https://pytorch.org/vision/stable/models.html
        self.transforms = transforms.Compose([
                                transforms.Resize(256),
                                transforms.CenterCrop(224),
                                transforms.ToTensor(),
                                transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                                     std=[0.229, 0.224, 0.225])])

        self.parse_data()

    def __len__(self):
        return self.n

    def __getitem__(self, i):
        img_file = self.img_files[i]
        img = self.parse_image(img_file)
        caption_list = self.caption_list[i]
        caption_lengths = self.caption_lengths[i]
        caption = ' '.join([self.int_to_word[token.item()] for token in caption_list])
        return img, caption_list, caption_lengths, img_file

    def parse_data(self):
        img_files, captions = [], [] 
        with open(self.caption_path, 'r') as f:
            rd = csv.reader(f, delimiter=',')
            next(rd) # ignore header
            for row in rd:
                img_file, caption = row
                img_files.append(img_file)
                captions.append(caption)

        caption_list, caption_lengths = self.process_captions(captions)

        self.img_files = img_files
        self.caption_list = caption_list
        self.caption_lengths = caption_lengths
        self.n = len(caption_list)

        # Map image file to list of captions
        self.img_file_to_idx = defaultdict(list)
        for i, img_file in enumerate(self.img_files):
            self.img_file_to_idx[img_file].append(i)

    def parse_image(self, img_file):
        """
        Load image file, convert to tensor
        """
        img_path = os.path.join(self.img_root, img_file)
        img = Image.open(img_path).convert('RGB')
        img = self.transforms(img)
        return img

    def process_captions(self, captions):
        """
        Build vocab over all captions, convert captions to ints with start and end tokens
        """
        # Lowercase all words
        captions = [caption.lower() for caption in captions]

        # Add special tokens to vocab
        vocab = set()
        vocab.add('<start>')
        vocab.add('<end>')
        vocab.add('<pad>')
        vocab.add('<unk>')

        # Build vocabulary
        words = [set(caption.split(' ')) for caption in captions]
        vocab = vocab.union(set.union(*words))
        vocab = list(sorted(vocab))

        # Map word to int / int to word
        word_to_int = dict((w, i) for i, w in enumerate(vocab))
        int_to_word = dict((i, w) for i, w in enumerate(vocab))

        # Map captions to int
        caption_list = []
        caption_lengths = []
        for caption in captions:
            words = ['<start>'] + caption.split(' ') + ['<end>']
            caption_length = len(words)
            words += ['<pad>'] * (self.seq_len - len(words))
            mapped_captions = [word_to_int[word] for word in words]

            caption_tensor = torch.tensor(mapped_captions, dtype=torch.long)

            caption_list.append(caption_tensor)
            caption_lengths.append(caption_length)

        # Store vocab info
        self.word_to_int, self.int_to_word, self.vocab = word_to_int, int_to_word, vocab

        return caption_list, caption_lengths

    def random_split(self, train_portion=0.8, seed=42):
        """
        Because we don't want the same image with different captionsto appear in both train and test sets,
        define a random split function that splits on image files.
        """
        img_files = list(set(self.img_files))
        n_images = len(img_files)
        train_set_n_images = int(n_images * 0.8)
        test_set_n_images = n_images - train_set_n_images

        img_idx = randperm(n_images, generator=torch.Generator().manual_seed(seed)).tolist()

        train_img_idx, test_img_idx = img_idx[:train_set_n_images], img_idx[train_set_n_images:]
        train_idx = [j for i in train_img_idx for j in self.img_file_to_idx[img_files[i]]]
        test_idx = [j for i in test_img_idx for j in self.img_file_to_idx[img_files[i]]]

        train_set = Subset(self, train_idx)
        test_set = Subset(self, test_idx)

        return train_set, test_set
