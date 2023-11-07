import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

LINES = ['-', ':', '--']  # 設定圖表中的線條樣式

def main():
    # 載入文字檔到作者的字典
    strings_by_author = dict()
    strings_by_author['doyle'] = text_to_string('hound.txt')
    strings_by_author['wells'] = text_to_string('war.txt')
    strings_by_author['unknown'] = text_to_string('lost.txt')

    # 檢查文章內容是否已正常載入
    print(strings_by_author['doyle'][:300])

    # 進行斷詞和文體分析
    words_by_author = make_word_dict(strings_by_author)
    len_shortest_corpus = find_shortest_corpus(words_by_author)
    
    word_length_test(words_by_author, len_shortest_corpus)
    stopwords_test(words_by_author, len_shortest_corpus)    
    parts_of_speech_test(words_by_author, len_shortest_corpus)
    vocab_test(words_by_author)
    jaccard_test(words_by_author, len_shortest_corpus) 

def text_to_string(filename):
    """讀取文字檔並以字串形式傳回"""
    with open(filename, encoding='utf-8', errors='ignore') as infile:
        return infile.read()

def make_word_dict(strings_by_author):
    """傳回將作品斷詞後的字典"""
    words_by_author = dict()
    for author in strings_by_author:
        tokens = nltk.word_tokenize(strings_by_author[author])
        words_by_author[author] = ([token.lower() for token in tokens
                                    if token.isalpha()])
    return words_by_author

def find_shortest_corpus(words_by_author):
    """傳回最短語料庫的長度"""
    word_count = []
    for author in words_by_author:
        word_count.append(len(words_by_author[author]))
        print('\nNumber of words for {} = {}\n'.
              format(author, len(words_by_author[author])))
    len_shortest_corpus = min(word_count)
    print('length shortest corpus = {}\n'.format(len_shortest_corpus))        
    return len_shortest_corpus    

def word_length_test(words_by_author, len_shortest_corpus):
    # 下一行程式若在 Anaconda 環境執行請取消註解
    # %matplotlib
    """畫出各作者使用的詞彙長度圖，所有作品都截斷成與最短語料庫相同長度"""
    by_author_length_freq_dist = dict()
    plt.figure(1)    
    plt.ion()
    for i, author in enumerate(words_by_author):
        word_lengths = [len(word) for word in words_by_author[author]
                        [:len_shortest_corpus]]
        by_author_length_freq_dist[author] = nltk.FreqDist(word_lengths)
        by_author_length_freq_dist[author].plot(15,
                                                linestyle=LINES[i],
                                                label=author,
                                                title='Word Length')
    plt.legend()
    # plt.show()  # 要在程式編輯時看到圖案，可取消註解

def stopwords_test(words_by_author, len_shortest_corpus):
    """畫出每位作者使用停用詞的頻率，所有作品都截斷成與最短語料庫的相同長度"""
    stopwords_by_author_freq_dist = dict()
    plt.figure(2) 
    stop_words = set(stopwords.words('english'))
    #print('Number of stopwords = {}\n'.format(len(stop_words)))
    #print('Stopwords = {}\n'.format(stop_words))
    for i, author in enumerate(words_by_author):
        stopwords_by_author = [word for word in words_by_author[author]
                               [:len_shortest_corpus] if word in stop_words]    
        stopwords_by_author_freq_dist[author] = nltk.FreqDist(stopwords_by_author)    
        stopwords_by_author_freq_dist[author].plot(50,
                                                   label=author,
                                                   linestyle=LINES[i],
                                                   title=
                                                   '50 Most Common Stopwords')
    plt.legend()
    # plt.show()  # 要在程式編輯時看到圖案，可取消註解

def parts_of_speech_test(words_by_author, len_shortest_corpus):
    """畫出作者使用名詞、動詞、副詞等不同詞性的圖形"""
    by_author_pos_freq_dist = dict()
    plt.figure(3)
    for i, author in enumerate(words_by_author):
        pos_by_author = [pos[1] for pos in nltk.pos_tag(words_by_author[author]
                                                        [:len_shortest_corpus])] 
        by_author_pos_freq_dist[author] = nltk.FreqDist(pos_by_author)
        by_author_pos_freq_dist[author].plot(35,
                                             label=author,
                                             linestyle=LINES[i],
                                             title='Part of Speech')
    plt.legend()
    plt.show(block=True) # Windows PowerShell的使用者需使用 plt.show(block=True) 防止圖案關閉
                       
def vocab_test(words_by_author):
    """用卡方統計來比較作者的詞彙量"""
    chisquared_by_author = dict()
    for author in words_by_author:
        if author != 'unknown': 
            # 合併作者的語料庫與 unknown 的語料庫，並取得 1000 個最常用的詞彙
            combined_corpus = (words_by_author[author] +
                               words_by_author['unknown'])
            author_proportion = (len(words_by_author[author])/
                                 len(combined_corpus))
            combined_freq_dist = nltk.FreqDist(combined_corpus)
            most_common_words = list(combined_freq_dist.most_common(1000))
            chisquared = 0

            # 取得觀察到的計數值和計算預期的計數值
            for word, combined_count in most_common_words:
                observed_count_author = words_by_author[author].count(word)
                expected_count_author = combined_count * author_proportion
                chisquared += ((observed_count_author -
                                expected_count_author)**2 /
                               expected_count_author)
                chisquared_by_author[author] = chisquared    
            print('Chi-squared for {} = {:.1f}'.format(author, chisquared))
            

    most_likely_author = min(chisquared_by_author, key=chisquared_by_author.get)
    print('Most-likely author by vocabulary is {}\n'.format(most_likely_author))

def jaccard_test(words_by_author, len_shortest_corpus):
    """計算已知作者語料庫對 unknown 語料庫的雅卡爾指數"""
    jaccard_by_author = dict()
    unique_words_unknown = set(words_by_author['unknown']
                               [:len_shortest_corpus])
    authors = (author for author in words_by_author if author != 'unknown')    
    for author in authors:
        unique_words_author = set(words_by_author[author][:len_shortest_corpus]) 
        shared_words = unique_words_author.intersection(unique_words_unknown)
        jaccard_sim = (float(len(shared_words))/ (len(unique_words_author) +
                                                  len(unique_words_unknown) -
                                                  len(shared_words)))
        jaccard_by_author[author] = jaccard_sim
        print('Jaccard Similarity for {} = {}'.format(author, jaccard_sim))
        
    most_likely_author = max(jaccard_by_author, key=jaccard_by_author.get)
    print('Most-likely author by similarity is {}'.format(most_likely_author))

if __name__ == '__main__':
    main()
