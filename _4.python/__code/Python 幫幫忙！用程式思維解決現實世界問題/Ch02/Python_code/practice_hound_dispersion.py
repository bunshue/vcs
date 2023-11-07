"""使用 NLP (nltk) 來製作分佈圖"""
import nltk
import file_loader

corpus = file_loader.text_to_string('hound.txt')
tokens = nltk.word_tokenize(corpus)
tokens = nltk.Text(tokens)  # NLTK wrapper 適用於自動文體分析

dispersion = tokens.dispersion_plot(['Holmes',
                                     'Watson',
                                     'Mortimer',
                                     'Henry',
                                     'Barrymore',                                                                        
                                     'Stapleton',
                                     'Selden',
                                     'hound'])
