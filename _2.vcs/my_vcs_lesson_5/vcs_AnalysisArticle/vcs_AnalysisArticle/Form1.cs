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
            int i;
            //if ((y[i + t] == '：') || (y[i + t] == '﹒') || (y[i + t] == '「') || (y[i + t] == '」') || (y[i + t] == '？') || (y[i + t] == '…') || (y[i + t] == '、') || (y[i + t] == '\t') || (y[i + t] == '　') || (y[i + t] == '"'))
            richTextBox1.Text += "：\t" + ((int)'：').ToString() + "\n";

            string ss = "俄羅斯火槍手作亂　";
            for (i = 0; i < ss.Length; i++)
            {
                richTextBox1.Text += ss[i] + "\t" + ((int)ss[i]).ToString() + "\n";

            }


            string y = File.ReadAllText("novel.txt", System.Text.Encoding.Default);
            richTextBox1.Text += "\n總長度：" + y.Length.ToString() + "\n";

            for (i = 0; i < y.Length; i++)
            //for (i = 0; i < 5000; i++)
            {
                if ((i % 5) == 4)
                {
                    richTextBox1.Text += "\n";
                }

                if (y[i] == 0x0A)
                    continue;
                if (y[i] == 0x0D)
                    continue;
                if (y[i] == 0x20)
                    continue;
                if (y[i] == 0x22)
                    continue;

                //if (y[i] < 13000)
                    //richTextBox1.Text += "i = " + i.ToString() + "\t|" + y[i] + "|\t" + ((int)y[i]).ToString("X2") + "\t" + ((int)y[i]).ToString() + "\t";

                    if ((y[i] >= 0x2E80) && (y[i] <= 0x33FF))
                    {
                        richTextBox1.Text += "_A\t|" + y[i] + "|\t" + ((int)y[i]).ToString("X2") + "\t" + ((int)y[i]).ToString() + "\t";
                    }

                    if ((y[i] >= 0x3400) && (y[i] <= 0x4DFF))
                    {
                        richTextBox1.Text += "_B\t|" + y[i] + "|\t" + ((int)y[i]).ToString("X2") + "\t" + ((int)y[i]).ToString() + "\t";
                    }
                    if ((y[i] >= 0x4E00) && (y[i] <= 0x9FFF))
                    {
                        richTextBox1.Text += "_C\t|" + y[i] + "|\t" + ((int)y[i]).ToString("X2") + "\t" + ((int)y[i]).ToString() + "\t";
                    }
                    if ((y[i] >= 0xA000) && (y[i] <= 0xA4FF))
                    {
                        richTextBox1.Text += "_D\t|" + y[i] + "|\t" + ((int)y[i]).ToString("X2") + "\t" + ((int)y[i]).ToString() + "\t";
                    }
                    if ((y[i] >= 0xAC00) && (y[i] <= 0xD7FF))
                    {
                        richTextBox1.Text += "_E\t|" + y[i] + "|\t" + ((int)y[i]).ToString("X2") + "\t" + ((int)y[i]).ToString() + "\t";
                    }
                    if ((y[i] >= 0xF900) && (y[i] <= 0xFAFF))
                    {
                        richTextBox1.Text += "_F\t|" + y[i] + "|\t" + ((int)y[i]).ToString("X2") + "\t" + ((int)y[i]).ToString() + "\t";
                    }
                    if ((y[i] >= 0xFB00) && (y[i] <= 0xFFFD))
                    {
                        richTextBox1.Text += "_X\t|" + y[i] + "|\t" + ((int)y[i]).ToString("X2") + "\t" + ((int)y[i]).ToString() + "\t";
                    }

/*
A   2E80～33FFh：中日韓符號區。收容康熙字典部首、中日韓輔助部首、注音符號、日本假名、韓文音符，中日韓的符號、標點、帶圈或帶括符文數字、月份，以及日本的假名組合、單位、年號、月份、日期、時間等。
B   3400～4DFFh：中日韓認同表意文字擴充A區，總計收容6,582個中日韓漢字。
C   4E00～9FFFh：中日韓認同表意文字區，總計收容20,902個中日韓漢字。
D   A000～A4FFh：彝族文字區，收容中國南方彝族文字和字根。
E   AC00～D7FFh：韓文拼音組合字區，收容以韓文音符拼成的文字。
F   F900～FAFFh：中日韓兼容表意文字區，總計收容302個中日韓漢字。
X   FB00～FFFDh：文字表現形式區，收容組合拉丁文字、希伯來文、阿拉伯文、中日韓直式標點、小符號、半角符號、全角符號等。
*/

            }


        }

        private void button5_Click(object sender, EventArgs e)
        {
            int i;
            int j = 0;
            string aaa = string.Empty;
            for (i = 0x4E2D; i < 0x4FFF; i++)
            {
                //richTextBox1.Text += "_A\t|" + y[i] + "|\t" + ((int)y[i]).ToString("X2") + "\t" + ((int)y[i]).ToString() + "\t";
                //richTextBox1.Text += (string)(i) + "\t";
                //aaa[j] = (char)i;
                //j++;
            }
        }
    }
}




/*



_X	|～|	FF5E	65374	
_X	|：|	FF1A	65306	
_C	|中|	4E2D	20013	_C	|日|	65E5	26085	_C	|韓|	97D3	38867	_C	|符|	7B26	31526	_C	|號|	865F	34399	
_C	|區|	5340	21312	_A	|。|	3002	12290	_C	|收|	6536	25910	_C	|容|	5BB9	23481	_C	|康|	5EB7	24247	
_C	|熙|	7199	29081	_C	|字|	5B57	23383	_C	|典|	5178	20856	_C	|部|	90E8	37096	_C	|首|	9996	39318	
_A	|、|	3001	12289	_C	|中|	4E2D	20013	_C	|日|	65E5	26085	_C	|韓|	97D3	38867	_C	|輔|	8F14	36628	
_C	|助|	52A9	21161	_C	|部|	90E8	37096	_C	|首|	9996	39318	_A	|、|	3001	12289	_C	|注|	6CE8	27880	
_C	|音|	97F3	38899	_C	|符|	7B26	31526	_C	|號|	865F	34399	_A	|、|	3001	12289	_C	|日|	65E5	26085	
_C	|本|	672C	26412	_C	|假|	5047	20551	_C	|名|	540D	21517	_A	|、|	3001	12289	_C	|韓|	97D3	38867	
_C	|文|	6587	25991	_C	|音|	97F3	38899	_C	|符|	7B26	31526	_X	|，|	FF0C	65292	_C	|中|	4E2D	20013	
_C	|日|	65E5	26085	_C	|韓|	97D3	38867	_C	|的|	7684	30340	_C	|符|	7B26	31526	_C	|號|	865F	34399	
_A	|、|	3001	12289	_C	|標|	6A19	27161	_C	|點|	9EDE	40670	_A	|、|	3001	12289	_C	|帶|	5E36	24118	
_C	|圈|	5708	22280	_C	|或|	6216	25110	_C	|帶|	5E36	24118	_C	|括|	62EC	25324	_C	|符|	7B26	31526	
_C	|文|	6587	25991	_C	|數|	6578	25976	_C	|字|	5B57	23383	_A	|、|	3001	12289	_C	|月|	6708	26376	
_C	|份|	4EFD	20221	_X	|，|	FF0C	65292	_C	|以|	4EE5	20197	_C	|及|	53CA	21450	_C	|日|	65E5	26085	
_C	|本|	672C	26412	_C	|的|	7684	30340	_C	|假|	5047	20551	_C	|名|	540D	21517	_C	|組|	7D44	32068	
_C	|合|	5408	21512	_A	|、|	3001	12289	_C	|單|	55AE	21934	_C	|位|	4F4D	20301	_A	|、|	3001	12289	
 * 





*/