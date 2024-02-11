using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

//關於Dictionary<K,V>，的key是不能重復的，如果添加相同的key就會拋出 ArgumentException異常
/*
從一組鍵（Key）到一組值（Value）的對映，每一個新增項都是由一個值及其相關連的鍵組成
任何鍵都必須是唯一的
鍵不能為空引用null，若值為引用型別，則可以為空值
Key和Value可以是任何型別（string，int，custom class 等）
*/

namespace vcs_Dictionary
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 180;
            dy = 70;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void showDictionaryData(Dictionary<string, int> AnimalData)
        {
            //richTextBox1.Text += "顯示目前字典內的所有資料\n";
            richTextBox1.Text += "字典內的元素 : " + AnimalData.Count.ToString() + " 個, 分別是 :\n";
            foreach (string n in AnimalData.Keys)  //使用Keys和values屬性迭代集合中的鍵和值, 也可從Values找回Keys
            {
                int p;
                if (AnimalData.ContainsKey(n))
                    p = AnimalData[n];
                else
                    p = 0;
                richTextBox1.Text += n + "  " + p.ToString() + "\t";
            }
            richTextBox1.Text += "\n";

            /*
            richTextBox1.Text += "另法顯示所有資料\n";
            //迭代集合中的各個項，把每個項作為一個 KeyValuePair<K,V>實例來獲取所有Dictionary資料
            foreach (KeyValuePair<string, int> pop in AnimalData)
            {
                richTextBox1.Text += "Key : " + pop.Key + "\tValue : " + pop.Value + "\n";
            }
            */
        }

        private void button0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Dictionary字典用法0\n";

            //richTextBox1.Text += "建立Dictionary<K,V>，然後新增元素\n";

            richTextBox1.Text += "初始化字典, 3個項目 鼠牛虎\n";
            Dictionary<string, int> AnimalData = new Dictionary<string, int>() {
            { "鼠", 3 },
            { "牛", 48 },
            { "虎", 33 }
            };

            richTextBox1.Text += "字典, 加入3個項目 兔龍蛇\n";
            AnimalData.Add("兔", 8);
            AnimalData.Add("龍", 38);
            AnimalData.Add("蛇", 16);

            showDictionaryData(AnimalData);

            richTextBox1.Text += "刪除一個項目 兔\n";
            //移除指定的鍵值By Remove方法
            string cname = "兔";
            AnimalData.Remove(cname);
            showDictionaryData(AnimalData);

            richTextBox1.Text += "-------------------------------------------------------------\n";

            richTextBox1.Text += "新增一個項目 象\n";
            AnimalData.Add("象", 100);

            richTextBox1.Text += "新增一個項目 狼\n";

            richTextBox1.Text += "檢查元素是否存在，如不存在，則新增之\n";
            if (!AnimalData.ContainsKey("狼"))
            {
                richTextBox1.Text += "該元素不存在，新增之\n";
                AnimalData.Add("狼", 25);
            }
            else
            {
                richTextBox1.Text += "該元素已存在\n";
            }

            showDictionaryData(AnimalData);

            richTextBox1.Text += "-------------------------------------------------------------\n";

            richTextBox1.Text += "查詢元素By Key\n";
            cname = "牛";
            if (AnimalData.ContainsKey(cname))
            {
                int weight = AnimalData[cname];
                richTextBox1.Text += "找到, Key = " + cname + ", Value = " + weight.ToString() + "\n";
                //richTextBox1.Text += "名稱 : " + cname + "\t體重 : " + weight.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "找不到\n";
            }

            richTextBox1.Text += "獲取鍵對應值的TryGetValue方法\n";
            int w = 0;
            if (AnimalData.TryGetValue("蛇", out w))
            {
                richTextBox1.Text += "蛇 : " + w + "\n";
            }
            else
            {
                richTextBox1.Text += "沒有 蛇\n";
            }

            richTextBox1.Text += "-------------------------------------------------------------\n";

            richTextBox1.Text += "找全部Key\n";
            //richTextBox1.Text += "僅遍歷鍵 By Keys 屬性\n";
            Dictionary<string, int>.KeyCollection keys = AnimalData.Keys;

            foreach (string key in keys/*string key in AnimalData.Keys*/)
            {
                richTextBox1.Text += "Key = " + key + "\n";
            }

            richTextBox1.Text += "找全部Key, 另法\n";
            foreach (string key in AnimalData.Keys)
            {
                richTextBox1.Text += "Key = " + key + "\n";
            }

            richTextBox1.Text += "-------------------------------------------------------------\n";

            richTextBox1.Text += "找全部Value\n";
            //richTextBox1.Text += "僅遍歷值By Valus屬性\n";
            Dictionary<string, int>.ValueCollection values = AnimalData.Values;
            foreach (int value in values)
            {
                richTextBox1.Text += "Value = " + value.ToString() + "\n";
            }

            richTextBox1.Text += "找全部Value, 另法\n";
            foreach (int value in AnimalData.Values)
            {
                richTextBox1.Text += "Value = " + value.ToString() + "\n";
            }

            richTextBox1.Text += "-------------------------------------------------------------\n";

            richTextBox1.Text += "找全部Key-Value對\n";
            //richTextBox1.Text += "遍歷元素 By KeyValuePair\n";
            foreach (KeyValuePair<string, int> kvp in AnimalData)
            {
                richTextBox1.Text += "找到, Key = " + kvp.Key + ", Value = " + kvp.Value + "\n";
            }

            richTextBox1.Text += "-------------------------------------------------------------\n";

            richTextBox1.Text += "show_data()\n";
            showDictionaryData(AnimalData);

            richTextBox1.Text += "-------------------------------------------------------------\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Dictionary字典用法1, 數字對上中文字\n";

            // The dictionary of digit names.
            Dictionary<int, string> Numbers = new Dictionary<int, string>() {
            {0, "零"},
            {1, "壹"},
            {2, "貳"},
            {3, "參"},
            {4, "肆"},
            {5, "伍"},
            {6, "陸"},
            {7, "柒"},
            {8, "捌"},
            {9, "玖"}
            };

            for (int i = 0; i < 10; i++)
            {
                richTextBox1.Text += i.ToString() + '\t' + Numbers[i] + "\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Dictionary字典用法2\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Dictionary字典用法3, 用Class\n";

            DictionaryWithDefault<string, string> AnimalData = new DictionaryWithDefault<string, string>("<Missing>");

            //加入字典
            AnimalData["鼠"] = "mouse";
            AnimalData["虎"] = "tiger";
            AnimalData["兔"] = "rabbit";

            //查詢字典
            richTextBox1.Text += "鼠" + "\t" + AnimalData["鼠"] + "\n";
            richTextBox1.Text += "牛" + "\t" + AnimalData["牛"] + "\n";
            richTextBox1.Text += "虎" + "\t" + AnimalData["虎"] + "\n";
            richTextBox1.Text += "兔" + "\t" + AnimalData["兔"] + "\n";
            richTextBox1.Text += "龍" + "\t" + AnimalData["龍"] + "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Dictionary字典用法4\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Dictionary字典用法5\n";

        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }
    }


    class DictionaryWithDefault<TKey, TValue>
    {
        // Store items here.
        private Dictionary<TKey, TValue> Entries
            = new Dictionary<TKey, TValue>();

        // The default value.
        private TValue DefaultValue;

        // Constructor.
        public DictionaryWithDefault(TValue default_value)
        {
            DefaultValue = default_value;
        }

        // Make the indexer property.
        public TValue this[TKey key]
        {
            get
            {
                // Return the value for this key or the default value.
                if (Entries.ContainsKey(key)) return Entries[key];
                return DefaultValue;
            }
            set
            {
                // Set the property's value for the key.
                Entries.Add(key, value);
            }
        }
    }
}

