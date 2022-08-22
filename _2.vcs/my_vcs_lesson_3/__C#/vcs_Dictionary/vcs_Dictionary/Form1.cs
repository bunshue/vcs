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
            dy = 80;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);


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

            //Dictionary的用法
            Dictionary<string, string> AnimalData = new Dictionary<string, string>() {
            { "mouse", "Mickey" },
            { "bull", "Benny" },
            { "tiger", "Eric" },
            { "rabbit", "Cony" }
            };
            string animal_type;
            string animal_name;

            animal_type = "mouse";
            if (AnimalData.ContainsKey(animal_type))
            {
                animal_name = AnimalData[animal_type];
                richTextBox1.Text += "got animal name = " + animal_name + "\n";
            }
            else
                richTextBox1.Text += "no matched animal name\n";

            animal_type = "bull";
            if (AnimalData.ContainsKey(animal_type))
            {
                animal_name = AnimalData[animal_type];
                richTextBox1.Text += "got animal name = " + animal_name + "\n";
            }
            else
                richTextBox1.Text += "no matched animal name\n";

            animal_type = "tiger";
            if (AnimalData.ContainsKey(animal_type))
            {
                animal_name = AnimalData[animal_type];
                richTextBox1.Text += "got animal name = " + animal_name + "\n";
            }
            else
                richTextBox1.Text += "no matched animal name\n";

            animal_type = "rabbit";
            if (AnimalData.ContainsKey(animal_type))
            {
                animal_name = AnimalData[animal_type];
                richTextBox1.Text += "got animal name = " + animal_name + "\n";
            }
            else
                richTextBox1.Text += "no matched animal name\n";

            animal_type = "dragon";
            if (AnimalData.ContainsKey(animal_type))
            {
                animal_name = AnimalData[animal_type];
                richTextBox1.Text += "got animal name = " + animal_name + "\n";
            }
            else
                richTextBox1.Text += "no matched animal name\n";

        }

        // The dictionary of digit names.
        private Dictionary<int, string> Numbers = new Dictionary<int, string>()
        {
            {0, "Zero"},
            {1, "One"},
            {2, "Two"},
            {3, "Three"},
            {4, "Four"},
            {5, "Five"},
            {6, "Six"},
            {7, "Seven"},
            {8, "Eight"},
            {9, "Nine"}
        };

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Dictionary字典用法1\n";

            // Display values from the dictionary.
            for (int i = 0; i < 10; i++)
            {
                richTextBox1.Text += i.ToString() + '\t' + Numbers[i] + "\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Dictionary字典用法2\n";

            Dictionary<string, long> population_dict = new Dictionary<string, long>();

            // Population data from https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States_by_population.
            population_dict.Add("AK", 731545);
            population_dict.Add("AL", 4903185);
            population_dict.Add("AR", 3017825);
            population_dict.Add("AS", 55641);
            population_dict.Add("AZ", 7278717);
            population_dict.Add("CA", 39512223);
            population_dict.Add("CO", 5758736);
            population_dict.Add("CT", 3565287);
            population_dict.Add("DC", 705749);
            population_dict.Add("DE", 973764);
            population_dict.Add("FL", 21477737);
            population_dict.Add("GA", 10617423);
            population_dict.Add("GU", 165718);
            population_dict.Add("HI", 1415872);
            population_dict.Add("IA", 3155070);
            population_dict.Add("ID", 1787065);
            population_dict.Add("IL", 12671821);
            population_dict.Add("IN", 6732219);
            population_dict.Add("KS", 2913314);
            population_dict.Add("KY", 4467673);
            population_dict.Add("LA", 4648794);
            population_dict.Add("MA", 6949503);
            population_dict.Add("MD", 6045680);
            population_dict.Add("ME", 1344212);
            population_dict.Add("MI", 9986857);
            population_dict.Add("MN", 5639632);
            population_dict.Add("MO", 6137428);
            population_dict.Add("MP", 55194);
            population_dict.Add("MS", 2976149);
            population_dict.Add("MT", 1068778);
            population_dict.Add("NC", 10488084);
            population_dict.Add("ND", 762062);
            population_dict.Add("NE", 1934408);
            population_dict.Add("NH", 1359711);
            population_dict.Add("NJ", 8882190);
            population_dict.Add("NM", 2096829);
            population_dict.Add("NV", 3080156);
            population_dict.Add("NY", 19453561);
            population_dict.Add("OH", 11689100);
            population_dict.Add("OK", 3956971);
            population_dict.Add("OR", 4217737);
            population_dict.Add("PA", 12801989);
            population_dict.Add("PR", 3193694);
            population_dict.Add("RI", 1059361);
            population_dict.Add("SC", 5148714);
            population_dict.Add("SD", 884659);
            population_dict.Add("TN", 6833174);
            population_dict.Add("TX", 28995881);
            population_dict.Add("UT", 3205958);
            population_dict.Add("VA", 8535519);
            population_dict.Add("VI", 104914);
            population_dict.Add("VT", 623989);
            population_dict.Add("WA", 7614893);
            population_dict.Add("WI", 5822434);
            population_dict.Add("WV", 1792147);
            population_dict.Add("WY", 578759);

            // Get the state population.
            long all_pop = 0;
            foreach (int value in population_dict.Values)
            {
                all_pop += value;
            }
            population_dict.Add("ALL STATES", all_pop);

            richTextBox1.Text += "顯示此Dictionary的資料\n";
            richTextBox1.Text += "共有 " + population_dict.Count.ToString() + " 筆資料\n";

            foreach (string n in population_dict.Keys)  //使用Keys和values屬性迭代集合中的鍵和值, 也可從Values找回Keys
            {
                long p;
                richTextBox1.Text += "找到 州 " + n + "\t";
                if (population_dict.ContainsKey(n))
                    p = population_dict[n];
                else
                    p = 0;
                richTextBox1.Text += "人口 : " + p.ToString() + "\n";
            }

            richTextBox1.Text += "另法顯示所有資料\n";
            //迭代集合中的各個項，把每個項作為一個 KeyValuePair<K,V>實例來獲取所有Dictionary資料
            foreach (KeyValuePair<string, long> pop in population_dict)
            {
                richTextBox1.Text += "州 : " + pop.Key + "\t人口 : " + pop.Value + "\n";
            }

            string state_name;
            long population;

            state_name = "NY";
            if (population_dict.ContainsKey(state_name))
                population = population_dict[state_name];
            else
                population = 0;
            richTextBox1.Text += "州 : " + state_name + "\t人口 : " + population.ToString() + "\n";

            state_name = "CA";
            if (population_dict.ContainsKey(state_name))
                population = population_dict[state_name];
            else
                population = 0;
            richTextBox1.Text += "州 : " + state_name + "\t人口 : " + population.ToString() + "\n";

            state_name = "ALL STATES";
            if (population_dict.ContainsKey(state_name))
                population = population_dict[state_name];
            else
                population = 0;
            richTextBox1.Text += "全國 :\t人口 : " + population.ToString() + "\n";

        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Dictionary字典用法3 用Class\n";

            // Make a dictionary.
            DictionaryWithDefault<string, string> dict = new DictionaryWithDefault<string, string>("<Missing>");

            // Add some items to the dictionary.
            dict["Ann"] = "Archer";
            dict["Chuck"] = "Cider";
            dict["Dora"] = "Deevers";

            // Display some values.
            richTextBox1.Text += "Ann" + "\t" + dict["Ann"] + "\n";
            richTextBox1.Text += "Ben" + "\t" + dict["Ben"] + "\n";
            richTextBox1.Text += "Chuck" + "\t" + dict["Chuck"] + "\n";
            richTextBox1.Text += "Dora" + "\t" + dict["Dora"] + "\n";
            richTextBox1.Text += "Ed" + "\t" + dict["Ed"] + "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Dictionary字典用法4\n";

            //建立及初始化

            Dictionary<string, int> myDictionary = new Dictionary<string, int>();

            //新增元素

            myDictionary.Add("C#", 0);
            myDictionary.Add("C++", 1);
            myDictionary.Add("C", 2);
            myDictionary.Add("VB", 2);

            //查詢元素By Key

            if (myDictionary.ContainsKey("C#"))
            {
                Console.WriteLine("Key:{0},Value:{1}", "C#", myDictionary["C#"]);
            }

            //遍歷元素 By KeyValuePair

            foreach (KeyValuePair<string, int> kvp in myDictionary)
            {
                Console.WriteLine("Key = {0}, Value = {1}", kvp.Key, kvp.Value);
            }

            //僅遍歷鍵 By Keys 屬性

            Dictionary<string, int>.KeyCollection keyCol = myDictionary.Keys;
            foreach (string key in keyCol/*string key in myDictionary.Keys*/)
            {
                Console.WriteLine("Key = {0}", key);
            }

            //僅遍歷值By Valus屬性

            Dictionary<string, int>.ValueCollection valueCol = myDictionary.Values;
            foreach (int value in valueCol)
            {
                Console.WriteLine("Value = {0}", value);
            }

            //移除指定的鍵值By Remove方法

            myDictionary.Remove("C#");
            if (myDictionary.ContainsKey("C#"))
            {
                Console.WriteLine("Key:{0},Value:{1}", "C#", myDictionary["C#"]);
            }
            else
            {
                Console.WriteLine("不存在 Key : C#");
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Dictionary字典用法5\n";

            /*
            從一組鍵（Key）到一組值（Value）的對映，每一個新增項都是由一個值及其相關連的鍵組成  
            任何鍵都必須是唯一的  
            鍵不能為空引用null（VB中的Nothing），若值為引用型別，則可以為空值  
            Key和Value可以是任何型別（string，int，custom class 等）
            */

            richTextBox1.Text += "建立Dictionary<K,V>，然後新增元素\n";
            Dictionary<string, string> film = new Dictionary<string, string>();
            film.Add("韋小寶", "鹿鼎記");
            film.Add("陸小鳳", "陸小鳳傳奇");
            film.Add("張無忌", "倚天屠龍記");
            film.Add("楊過", "神鵰俠侶");
            film.Add("令狐沖", "笑傲江湖");
            richTextBox1.Text += "集合現在的元素個數為 " + film.Count.ToString() + "\n";

            richTextBox1.Text += "移除一個\n";
            film.Remove("楊過");
            richTextBox1.Text += "集合現在的元素個數為 " + film.Count.ToString() + "\n";

            richTextBox1.Text += "遍歷集合\n";
            richTextBox1.Text += "所有武俠電影的主角及電影名\n";
            richTextBox1.Text += "\t主角\t電影\n";
            foreach (KeyValuePair<string, string> kvp in film)
            {
                richTextBox1.Text += "\t" + kvp.Key + "\t" + kvp.Value + "\n";
            }

            richTextBox1.Text += "檢查元素是否存在，如不存在，新增\n";
            if (!film.ContainsKey("段譽"))
            {
                richTextBox1.Text += "該元素不存在，新增\n";
                film.Add("段譽", "天龍八部");
            }
            else
            {
                richTextBox1.Text += "該元素已存在\n";
            }

            richTextBox1.Text += "獲取鍵的集合\n";
            Dictionary<string, string>.KeyCollection keys = film.Keys;

            richTextBox1.Text += "遍歷鍵的集合\n";
            richTextBox1.Text += "受歡迎的武俠片中主角名\n";
            foreach (string str in keys)
            {
                richTextBox1.Text += str + "\n";
            }

            Dictionary<string, string>.ValueCollection values = film.Values;
            richTextBox1.Text += "遍歷值的集合\n";
            richTextBox1.Text += "最受歡迎的武俠片\n";
            foreach (string strfilm in values)
            {
                richTextBox1.Text += strfilm + "\n";
            }

            richTextBox1.Text += "遍歷元素的另一種方法\n";
            richTextBox1.Text += "和雜湊表相同的遍歷元素方法\n";
            foreach (string strname in film.Values)
            {
                richTextBox1.Text += strname + "\n";
            }

            richTextBox1.Text += "獲取鍵對應的值\n";
            string myfilm = film["令狐沖"];
            richTextBox1.Text += "主角為令狐沖的電影名 : " + myfilm + "\n";

            richTextBox1.Text += "獲取鍵對應值的TryGetValue方法\n";
            string objfilm = string.Empty;
            if (film.TryGetValue("段譽", out objfilm))
            {
                richTextBox1.Text += "主角為段譽的電影是 : " + objfilm + "\n";
            }
            else
            {
                richTextBox1.Text += "沒有主角為段譽的電影\n";
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Dictionary字典用法6\n";

            Dictionary<string, string> ImageTypes = new Dictionary<string, string>()
            {
            { "FFD8", ".jpg" },
            { "424D", ".bmp" },
            { "474946", ".gif" },
            { "89504E470D0A1A0A", ".png" }
            };

            richTextBox1.Text += "len = " + ImageTypes.Count.ToString() + "\n";

            string filename = @"C:\______test_files\picture1.jpg";

            string builtHex = string.Empty;
            string ext = string.Empty;
            using (Stream S = File.OpenRead(filename))
            {
                for (int i = 0; i < 8; i++)
                {
                    builtHex += S.ReadByte().ToString("X2");
                    if (ImageTypes.ContainsKey(builtHex))
                    {
                        ext = ImageTypes[builtHex];
                        break;
                    }
                }
            }
            richTextBox1.Text += "取得真實副檔名 : " + ext + "\n";
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
