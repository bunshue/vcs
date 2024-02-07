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

        private void button0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Dictionary字典用法0\n";

            Dictionary<string, int> AnimalData = new Dictionary<string, int>() {
            { "鼠", 3 },
            { "牛", 48 },
            { "虎", 33 },
            { "兔", 8 }
            };
            string cname;
            int weight;

            cname = "鼠";
            if (AnimalData.ContainsKey(cname))
            {
                weight = AnimalData[cname];
                richTextBox1.Text += "名稱 : " + cname + ", 找到 : " + weight + "\n";
            }
            else
                richTextBox1.Text += "找不到\n";

            cname = "牛";
            if (AnimalData.ContainsKey(cname))
            {
                weight = AnimalData[cname];
                richTextBox1.Text += "名稱 : " + cname + ", 找到 : " + weight + "\n";
            }
            else
                richTextBox1.Text += "找不到\n";

            cname = "虎";
            if (AnimalData.ContainsKey(cname))
            {
                weight = AnimalData[cname];
                richTextBox1.Text += "名稱 : " + cname + ", 找到 : " + weight + "\n";
            }
            else
                richTextBox1.Text += "找不到\n";

            cname = "兔";
            if (AnimalData.ContainsKey(cname))
            {
                weight = AnimalData[cname];
                richTextBox1.Text += "名稱 : " + cname + ", 找到 : " + weight + "\n";
            }
            else
                richTextBox1.Text += "找不到\n";

            cname = "龍";
            if (AnimalData.ContainsKey(cname))
            {
                weight = AnimalData[cname];
                richTextBox1.Text += "名稱 : " + cname + ", 找到 : " + weight + "\n";
            }
            else
                richTextBox1.Text += "找不到\n";
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

            Dictionary<string, int> AnimalData = new Dictionary<string, int>();

            AnimalData.Add("鼠", 3);
            AnimalData.Add("牛", 48);
            AnimalData.Add("虎", 33);
            AnimalData.Add("兔", 8);
            AnimalData.Add("龍", 38);
            AnimalData.Add("蛇", 16);

            int all_weight = 0;
            foreach (int value in AnimalData.Values)
            {
                all_weight += value;
            }
            AnimalData.Add("全部動物", all_weight);

            richTextBox1.Text += "顯示此Dictionary的資料\n";
            richTextBox1.Text += "共有 " + AnimalData.Count.ToString() + " 筆資料\n";

            foreach (string n in AnimalData.Keys)  //使用Keys和values屬性迭代集合中的鍵和值, 也可從Values找回Keys
            {
                int p;
                richTextBox1.Text += "找到 " + n + "\t";
                if (AnimalData.ContainsKey(n))
                    p = AnimalData[n];
                else
                    p = 0;
                richTextBox1.Text += "體重 : " + p.ToString() + "\n";
            }

            richTextBox1.Text += "另法顯示所有資料\n";
            //迭代集合中的各個項，把每個項作為一個 KeyValuePair<K,V>實例來獲取所有Dictionary資料
            foreach (KeyValuePair<string, int> pop in AnimalData)
            {
                richTextBox1.Text += "名稱 : " + pop.Key + "\t體重 : " + pop.Value + "\n";
            }

            string cname;
            int weight;

            cname = "鼠";
            if (AnimalData.ContainsKey(cname))
                weight = AnimalData[cname];
            else
                weight = 0;
            richTextBox1.Text += "名稱 : " + cname + "\t體重 : " + weight.ToString() + "\n";

            cname = "牛";
            if (AnimalData.ContainsKey(cname))
                weight = AnimalData[cname];
            else
                weight = 0;
            richTextBox1.Text += "名稱 : " + cname + "\t體重 : " + weight.ToString() + "\n";

            cname = "全部動物";
            if (AnimalData.ContainsKey(cname))
                weight = AnimalData[cname];
            else
                weight = 0;
            richTextBox1.Text += "全部動物 :\t體重 : " + weight.ToString() + "\n";

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
            richTextBox1.Text += "Dictionary字典用法4, 增刪查改\n";

            //建立及初始化

            Dictionary<string, int> AnimalData = new Dictionary<string, int>();

            //新增元素
            AnimalData.Add("鼠", 3);
            AnimalData.Add("牛", 48);
            AnimalData.Add("虎", 33);
            AnimalData.Add("兔", 8);

            //查詢元素By Key
            string cname = "鼠";
            if (AnimalData.ContainsKey(cname))
            {
                richTextBox1.Text += "Key:" + cname + ",Value:" + AnimalData[cname] + "\n";
            }

            //遍歷元素 By KeyValuePair

            foreach (KeyValuePair<string, int> kvp in AnimalData)
            {
                richTextBox1.Text += "Key = " + kvp.Key + ",Value = " + kvp.Value + "\n";
            }

            //僅遍歷鍵 By Keys 屬性
            Dictionary<string, int>.KeyCollection keyCol = AnimalData.Keys;
            foreach (string key in keyCol/*string key in AnimalData.Keys*/)
            {
                richTextBox1.Text += "Key = " + key + "\n";
            }

            //僅遍歷值By Valus屬性
            Dictionary<string, int>.ValueCollection valueCol = AnimalData.Values;
            foreach (int value in valueCol)
            {
                richTextBox1.Text += "Value = " + value + "\n";
            }

            //移除指定的鍵值By Remove方法
            cname = "鼠";
            AnimalData.Remove(cname);
            if (AnimalData.ContainsKey(cname))
            {
                richTextBox1.Text += "Key:" + cname + ",Value:" + AnimalData[cname] + "\n";
            }
            else
            {
                richTextBox1.Text += "不存在 Key:" + cname + "\n";
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Dictionary字典用法5\n";

            /*
            從一組鍵（Key）到一組值（Value）的對映，每一個新增項都是由一個值及其相關連的鍵組成
            任何鍵都必須是唯一的
            鍵不能為空引用null，若值為引用型別，則可以為空值
            Key和Value可以是任何型別（string，int，custom class 等）
            */

            richTextBox1.Text += "建立Dictionary<K,V>，然後新增元素\n";
            Dictionary<string, string> AnimalData = new Dictionary<string, string>();
            AnimalData.Add("鼠", "mouse");
            AnimalData.Add("牛", "ox");
            AnimalData.Add("虎", "tiger");
            AnimalData.Add("兔", "rabbit");
            AnimalData.Add("龍", "dragon");
            richTextBox1.Text += "集合現在的元素個數為 " + AnimalData.Count.ToString() + "\n";

            richTextBox1.Text += "移除一個\n";
            AnimalData.Remove("兔");
            richTextBox1.Text += "集合現在的元素個數為 " + AnimalData.Count.ToString() + "\n";

            richTextBox1.Text += "遍歷字典\n";
            richTextBox1.Text += "\t中文名\t英文名\n";
            foreach (KeyValuePair<string, string> kvp in AnimalData)
            {
                richTextBox1.Text += "\t" + kvp.Key + "\t" + kvp.Value + "\n";
            }

            richTextBox1.Text += "檢查元素是否存在，如不存在，則新增之\n";
            if (!AnimalData.ContainsKey("蛇"))
            {
                richTextBox1.Text += "該元素不存在，新增之\n";
                AnimalData.Add("蛇", "snake");
            }
            else
            {
                richTextBox1.Text += "該元素已存在\n";
            }

            richTextBox1.Text += "獲取鍵的集合\n";
            Dictionary<string, string>.KeyCollection keys = AnimalData.Keys;

            richTextBox1.Text += "遍歷 key\n";
            richTextBox1.Text += "中文名\n";
            foreach (string str in keys)
            {
                richTextBox1.Text += str + "\n";
            }

            Dictionary<string, string>.ValueCollection values = AnimalData.Values;
            richTextBox1.Text += "遍歷 value\n";
            richTextBox1.Text += "英文名\n";
            foreach (string name in values)
            {
                richTextBox1.Text += name + "\n";
            }

            richTextBox1.Text += "遍歷元素的另一種方法\n";
            richTextBox1.Text += "和雜湊表相同的遍歷元素方法\n";
            foreach (string strname in AnimalData.Values)
            {
                richTextBox1.Text += strname + "\n";
            }

            richTextBox1.Text += "獲取鍵對應的值\n";
            string ename = AnimalData["龍"];
            richTextBox1.Text += "龍 : " + ename + "\n";

            richTextBox1.Text += "獲取鍵對應值的TryGetValue方法\n";
            string ename2 = string.Empty;
            if (AnimalData.TryGetValue("蛇", out ename2))
            {
                richTextBox1.Text += "蛇 : " + ename2 + "\n";
            }
            else
            {
                richTextBox1.Text += "沒有 蛇\n";
            }
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
