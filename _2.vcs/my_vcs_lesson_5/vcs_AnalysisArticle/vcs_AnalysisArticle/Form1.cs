using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for File

namespace vcs_AnalysisArticle
{
    public partial class Form1 : Form
    {
        private const int SEARCH_LEN_MAX = 20;	//搜尋最大長度
        private const int SEARCH_LEN_MIN = 4;	//搜尋最短長度

        int same_count = 0;

        public class WordInfo
        {
            public int keyword_len;
            public string keyword;
            public int keyword_cnt;
            public WordInfo(int l, string s, int c)
            {
                this.keyword_len = l;
                this.keyword = s;
                this.keyword_cnt = c;
            }
        }

        List<WordInfo> word_statistics = new List<WordInfo>();

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //richTextBox1.LoadFile("pipa.txt", RichTextBoxStreamType.PlainText);  //將指定的文字檔載入到richTextBox
            string y = File.ReadAllText("novel.txt", System.Text.Encoding.Default);
            //richTextBox1.Text += "檔案內容 : " + y + "\n";
            richTextBox1.Text += "總長度：" + y.Length.ToString() + "\n";

            word_statistics.Clear();

            int i, j, k;
            int t;
            int ignore = 0;
            string pattern = string.Empty;
            string word;
            int find_pattern_count = 0;

            for (k = SEARCH_LEN_MIN; k < SEARCH_LEN_MAX; k++)
            {
                find_pattern_count = 0;
                richTextBox1.Text += "\n搜尋長度：" + (k + 1).ToString() + "\n";
                for (i = 0; i < (y.Length - (k+1)); i++)
                {
                    same_count = 1;
                    ignore = 0;
                    for (t = 0; t <= k; t++)
                    {
                        /*
                        //需要跳過的字眼
                        if ((y[i + t] == '，') || (y[i + t] == '。') || (y[i + t] == '\n') || (y[i + t] == 0x0d) || (y[i + t] == 0x0a) || (y[i + t] == ' ') || (y[i + t] == 0x20) || (y[i + t] == '\t') || (y[i + t] == '　') || (y[i + t] == '"'))
                        {
                            ignore = 1;
                            break;
                        }
                        if ((y[i + t] == '：') || (y[i + t] == '﹒') || (y[i + t] == '「') || (y[i + t] == '」') || (y[i + t] == '？') || (y[i + t] == '…') || (y[i + t] == '、') || (y[i + t] == '\t') || (y[i + t] == '　') || (y[i + t] == '"'))
                        {
                            ignore = 1;
                            break;
                        }
                        */
                        if ((y[i + t] < 13000) || (y[i + t] > 60000))
                        {
                            ignore = 1;
                            break;
                        }
                    }

                    //跳過已經找過的
                    for (int s = 0; s < word_statistics.Count; s++)
                    {
                        word = word_statistics[s].keyword;
                        if (y.Substring(i, (k + 1)) == word)
                        {
                            //richTextBox1.Text += "X " + y.Substring(i, (k + 1));
                            ignore = 1;
                            break;
                        }
                    }

                    if (ignore == 1)
                        continue;

                    int find_pattern = 1;
                    for (j = i + (k + 1); j < (y.Length - k); j++)
                    {
                        find_pattern = 1;
                        for (t = 0; t <= k; t++)
                        {
                            if (y[i + t] == y[j + t])
                            {
                                find_pattern *= 1;
                            }
                            else
                            {
                                find_pattern *= 0;
                            }
                        }

                        if (find_pattern == 1)
                        {
                            same_count++;
                        }

                        /*
                        if (k == 0)
                        {
                            if (y[i] == y[j])
                            {
                                //richTextBox1.Text += "取得 " + y[i] + " i = " + i.ToString() + " j = " + j.ToString() + "\t";
                                same_count++;
                            }
                        }
                        else if (k == 1)
                        {
                            if ((y[i] == y[j]) && (y[i + 1] == y[j + 1]))
                            {
                                //richTextBox1.Text += "取得 " + y[i] + y[i + 1] + " i = " + i.ToString() + " j = " + j.ToString() + "\t";
                                same_count++;
                            }
                        }
                        else if (k == 2)
                        {
                            if ((y[i] == y[j]) && (y[i + 1] == y[j + 1]) && (y[i + 2] == y[j + 2]))
                            {
                                //richTextBox1.Text += "取得 " + y[i] + y[i + 1] + " i = " + i.ToString() + " j = " + j.ToString() + "\t";
                                same_count++;
                            }
                        }
                        else if (k == 3)
                        {
                            if ((y[i] == y[j]) && (y[i + 1] == y[j + 1]) && (y[i + 2] == y[j + 2]) && (y[i + 3] == y[j + 3]))
                            {
                                //richTextBox1.Text += "取得 " + y[i] + y[i + 1] + " i = " + i.ToString() + " j = " + j.ToString() + "\t";
                                same_count++;
                            }
                        }
                        */

                        if (j == (y.Length - (k + 1)))
                        {
                            if (same_count > 2)
                            {
                                find_pattern_count++;
                                richTextBox1.Text += "取得 \"";
                                for (t = 0; t <= k; t++)
                                {
                                    richTextBox1.Text += y[i + t];
                                }
                                richTextBox1.Text += "\" 共 " + same_count.ToString() + " 個\n";

                                pattern = y.Substring(i, (k + 1));

                                word_statistics.Add(new WordInfo(k, pattern, same_count));


                            }
                        }
                    }
                }
                richTextBox1.Text += "find_pattern_count = " + find_pattern_count.ToString() + "\n";
                if (find_pattern_count == 0)
                {
                    richTextBox1.Text += "不用再找了\n";
                    break;
                }
            }




        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "word_statistics.Count = " + word_statistics.Count.ToString() + "\n";

            int len;
            string word;
            int count;

            for (int i = 0; i < word_statistics.Count; i++)
            {
                len = word_statistics[i].keyword_len;
                word = word_statistics[i].keyword;
                count = word_statistics[i].keyword_cnt;

                richTextBox1.Text += "len = " + len.ToString() + " word = " + word + " count = " + count.ToString() + "\n";

            }


        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //if ((y[i + t] == '：') || (y[i + t] == '﹒') || (y[i + t] == '「') || (y[i + t] == '」') || (y[i + t] == '？') || (y[i + t] == '…') || (y[i + t] == '、') || (y[i + t] == '\t') || (y[i + t] == '　') || (y[i + t] == '"'))
            richTextBox1.Text += "：\t" + ((int)'：').ToString() + "\n";

            string ss = "俄羅斯火槍手作亂　";
            for (int i = 0; i < ss.Length; i++)
            {
                richTextBox1.Text += ss[i] + "\t" + ((int)ss[i]).ToString() + "\n";

            }

        }
    }
}
