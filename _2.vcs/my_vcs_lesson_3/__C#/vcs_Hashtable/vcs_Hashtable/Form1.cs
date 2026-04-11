using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Collections;   //for Hashtable

namespace vcs_Hashtable
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
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);

            groupBox1.Location = new Point(x_st + dx * 1 + 10, y_st + dy * 0);

            x_st = 15;
            y_st = 15;
            dx = 140 + 5;
            dy = 40 + 5;

            ht0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            ht1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            ht2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            ht3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            ht4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            ht5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            ht6.Location = new Point(x_st + dx * 0, y_st + dy * 6);

            ht7.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            ht8.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            ht9.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            ht10.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            ht11.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            ht12.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            ht13.Location = new Point(x_st + dx * 1, y_st + dy * 6);

            richTextBox1.Size = new Size(500, 600);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1273, 784);
            this.Text = "vcs_Hashtable";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Hashtable的用法0\n";
            Hashtable ht = new Hashtable();
            ht.Add(5, "Apple");
            ht.Add(1, "Banana");
            ht.Add(4, "Cat");

            foreach (int ID in ht.Keys)
            {
                richTextBox1.Text += ID.ToString() + "\n";
            }

            foreach (string name in ht.Values)
            {
                richTextBox1.Text += name + "\n";
            }

            richTextBox1.Text += "直接列印某項\n";
            richTextBox1.Text += ht[4] + "\n";

            richTextBox1.Text += "先檢查有無項目再列印\n";
            if (ht.ContainsKey(4))
            {
                richTextBox1.Text += ht[4] + "\n";
            }
            else
            {
                richTextBox1.Text += "無此項\n";
            }

            ht.Remove(4);

            richTextBox1.Text += "先檢查有無項目再列印\n";
            if (ht.ContainsKey(4))
            {
                richTextBox1.Text += ht[4] + "\n";
            }
            else
            {
                richTextBox1.Text += "無此項\n";
            }



        }

        private void button1_Click(object sender, EventArgs e)
        {
            //Hashtable的用法1

            Hashtable ht = new Hashtable();

            richTextBox1.Text += "加入資料到HashTable, key不能重複, value可以重複\n";
            ht.Add("鼠", 3);
            ht.Add("牛", 48);
            ht.Add("虎", 48);
            ht.Add("兔", 8);

            richTextBox1.Text += "For key = \"rtf\", value = " + ht["虎"] + "\n";

            richTextBox1.Text += "修改資料\n";
            ht["虎"] = 33;
            richTextBox1.Text += "For key = \"rtf\", value = " + ht["虎"] + "\n";

            richTextBox1.Text += "新增資料\n";
            ht["龍"] = 38;

            richTextBox1.Text += "先檢查key是否存在, 若無, 再加入資料\n";
            if (!ht.ContainsKey("蛇"))
            {
                ht.Add("蛇", 16);
            }

            richTextBox1.Text += "列出 Hashtable 內的所有資料\n";
            foreach (DictionaryEntry de in ht)
            {
                richTextBox1.Text += "Key = " + de.Key + ", Value = " + de.Value + "\n";
            }

            richTextBox1.Text += "取出所有values\n";
            ICollection valueColl = ht.Values;
            foreach (int s in valueColl)
            {
                richTextBox1.Text += "Value = " + s + "\n";
            }

            richTextBox1.Text += "取出所有keys\n";
            ICollection keyColl = ht.Keys;
            foreach (string s in keyColl)
            {
                richTextBox1.Text += "Key = " + s + "\n";
            }

            richTextBox1.Text += "刪除資料\n";
            ht.Remove("龍");

            if (!ht.ContainsKey("龍"))
            {
                richTextBox1.Text += "Key \"龍\" 已被刪除" + "\n";
            }
        }

        public static void PrintOut(IEnumerable tmyHT)
        {
            Console.WriteLine("   品名 (Key)  價格 (Value)");
            foreach (DictionaryEntry de in tmyHT)
            {
                Console.WriteLine("    {0}\t {1}", de.Key, de.Value);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Hashtable ht = new Hashtable(); // 建立ht為一個屬於Hashtable的實體

            Console.WriteLine("\n 1.置入四筆 Key & Value 鍵值到 HashTable 內.");
            ht.Add("iPhone5S", 22000);  //添加 key&value鍵值對
            ht.Add("iPhone5C", 18000);  //添加 key&value鍵值對
            ht.Add("iPad2", 12500);     //添加 key&value鍵值對
            ht.Add("iPadMini", 15900);  //添加 key&value鍵值對

            //PrintKeysAndValues(mySL);
            PrintOut(ht);
            Console.WriteLine(" 1.目前 HashTable 內元素總個數 : {0}", ht.Count);
            Console.WriteLine(" ------------------------------------------");

            // 查詢產品單價
            Console.Write(" 2.請輸入 Apple 產品名稱 : ");
            string item = Console.ReadLine();
            if (!ht.ContainsKey(item))      // 判斷HashTable是否含特定鍵,傳回值true或false
            {
                Console.WriteLine(" 2. {0} 不存在 !!", item);
            }
            else
            {
                Console.WriteLine(" 2.{0}單價 : {1}", item, ht[item]);
            }
            Console.WriteLine(" ------------------------------------------");

            // 移除剛查詢的 Key & Value 鍵值對
            Console.WriteLine(" 3.移除剛查詢鍵值 {0}", item);
            ht.Remove(item);
            PrintOut(ht);
            Console.WriteLine(" 3.目前 HashTable 內元素總個數 : {0}", ht.Count);
            Console.WriteLine(" ------------------------------------------");

            //移除所有元素
            Console.WriteLine(" 4.移除 HashTable 內所有元素");
            ht.Clear();
            Console.WriteLine(" 4.目前 HashTable 內元素總個數 : {0}", ht.Count);
            Console.WriteLine(" ------------------------------------------");
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Hashtable ht = new Hashtable();  // 非泛型

            ht.Add("David", new Member() { Name = "David", Select = true, Score = 70 });
            ht.Add("Mary", new Member() { Name = "Mary", Select = false, Score = 65 });
            ht.Add("Tom", new Member() { Name = "Tom", Select = true, Score = 85 });
            ht.Add("Jack", new Member() { Name = "Jack", Select = true, Score = 95 });

            //非泛型操作
            Console.WriteLine("=== 非泛型 HasnTable 操作需強制轉換 .... \n");
            foreach (DictionaryEntry item in ht)
            {
                Console.WriteLine(((Member)item.Value).ToString());
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //Hashtable的用法4

            Hashtable ht = new Hashtable();
            ht.Clear();
            ht.Add("aaa", 123);
            ht.Add("bbb", 456);
            ht.Add("ccc", 789);
            foreach (DictionaryEntry de in ht)  // 遍历Hashtable
            {
                richTextBox1.Text += de.Key + " / " + de.Value + "\n";
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
        }



        //Hashtable 測試 ST

        Hashtable ht = new Hashtable();         //雜湊表 (key, value)

        void show_hashtable(Hashtable ht)
        {
            int len = ht.Count;

            richTextBox1.Text += "共有 : " + len.ToString() + " 個項目\n";

            //方法一：遍歷traversal 1:
            foreach (DictionaryEntry de in ht)
            {
                richTextBox1.Text += "key = " + de.Key + "\t" + "value = " + de.Value + "\n";
            }

            //方法二：遍歷traversal 2:
            IDictionaryEnumerator d = ht.GetEnumerator();
            while (d.MoveNext())
            {
                //richTextBox1.Text += "key = " + d.Entry.Key + "\t" + "value = " + d.Entry.Value + "\n";
            }
        }

        private void ht0_Click(object sender, EventArgs e)
        {
            show_hashtable(ht);
        }

        bool flag_already_added_items = false;
        private void ht1_Click(object sender, EventArgs e)
        {
            if (flag_already_added_items == false)
            {
                string name = string.Empty;
                int weight = 0;

                name = "鼠";
                weight = 3;
                ht.Add(name, weight);        //加入雜湊表，Key: name, Value: weight, Key不能重複
                richTextBox1.Text += "加入雜湊表，Key: " + name + ", Value: " + weight + "\n";

                name = "牛";
                weight = 48;
                ht.Add(name, weight);        //加入雜湊表，Key: name, Value: weight, Key不能重複
                richTextBox1.Text += "加入雜湊表，Key: " + name + ", Value: " + weight + "\n";

                name = "虎";
                weight = 33;
                ht.Add(name, weight);        //加入雜湊表，Key: name, Value: weight, Key不能重複
                richTextBox1.Text += "加入雜湊表，Key: " + name + ", Value: " + weight + "\n";

                name = "兔";
                weight = 8;
                ht.Add(name, weight);        //加入雜湊表，Key: name, Value: weight, Key不能重複
                richTextBox1.Text += "加入雜湊表，Key: " + name + ", Value: " + weight + "\n";

                name = "龍";
                weight = 38;
                ht.Add(name, weight);        //加入雜湊表，Key: name, Value: weight, Key不能重複
                richTextBox1.Text += "加入雜湊表，Key: " + name + ", Value: " + weight + "\n";

                flag_already_added_items = true;
            }
        }

        private void ht2_Click(object sender, EventArgs e)
        {
            int len = ht.Count;

            int cnt = 0;
            foreach (DictionaryEntry de in ht)
            {
                richTextBox1.Text += "key = " + de.Key + "\t" + "value = " + de.Value + "\n";
                if (len > 2)
                {
                    if (cnt == (len - 2))
                    {
                        richTextBox1.Text += "移除 " + de.Key + " 項\n";
                        ht.Remove(de.Key);
                        return;
                    }
                }
                else if (len > 0)
                {
                    if (cnt == (len - 1))
                    {
                        richTextBox1.Text += "移除 " + de.Key + " 項\n";
                        ht.Remove(de.Key);
                        return;
                    }
                }
                else
                {
                    richTextBox1.Text += "無資料可移除\n";
                    return;
                }
                cnt++;
            }
        }

        private void ht3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "ContainsKey\tContainsValue\n";

            richTextBox1.Text += "把aaaa3項的value改變\n";

            if (ht.ContainsKey("兔"))
            {
                richTextBox1.Text += "1111111111111\n";
                ht["兔"] = 10;
            }

            /*
            richTextBox1.Text += "把bbbb3項的value改變\n";

            if (ht.ContainsValue("bbbb1"))
            {
                //不知道怎麼從value找key
                //ht["aaaa3"] = "xxxxxxxx";
                //richTextBox1.Text += "2222222222222222222\n";
            }
            */
        }

        private void ht4_Click(object sender, EventArgs e)
        {
            ht.Clear();
            richTextBox1.Text += "清除雜湊表\n";
        }

        private void ht5_Click(object sender, EventArgs e)
        {
            if (ht.Count < 5)
            {
                richTextBox1.Text += "至少5筆資料\n";
                return;
            }
            richTextBox1.Text += "HashTable排序\n";

            richTextBox1.Text += "排序前\n";
            show_hashtable(ht);

            richTextBox1.Text += "\n排序後\n";

            //key 為 唯一 可用來查value
            //value 為 非唯一 不可用來查key

            ArrayList akeys = new ArrayList(ht.Keys); //from Hashtable
            //ArrayList akeys = new ArrayList(ht.Values); //from Hashtable

            akeys.Sort(); //Sort by leading letter

            foreach (string skey in akeys)
            {
                richTextBox1.Text += "key = " + skey + "\t" + "value = " + ht[skey] + "\n";
            }
        }

        private void ht6_Click(object sender, EventArgs e)
        {
            // 獲取鍵的集合
            ICollection key = ht.Keys;
            foreach (string k in key)
            {
                richTextBox1.Text += "Key : " + k + "\tValue : " + ht[k] + "\n";
            }
        }

        private void ht7_Click(object sender, EventArgs e)
        {
            //Hashtable 物件
            richTextBox1.Text += "建立一個Hashtable\n";

            Hashtable ht = new Hashtable();

            richTextBox1.Text += "給Hashtable賦值, key是唯一, value不唯一\n";
            //            key     value
            ht.Add("txt", "notepad.exe");
            ht.Add("bmp", "paint.exe");
            ht.Add("dib", "paint.exe");
            ht.Add("rtf", "wordpad.exe");

            // When you use foreach to enumerate hash table elements,
            // the elements are retrieved as DictionaryEntry objects.
            foreach (DictionaryEntry var in ht)
            {
                richTextBox1.Text += var.Key + "\t" + var.Value + "\n";
            }

        }

        private void ht8_Click(object sender, EventArgs e)
        {
            //遍歷Hashtable 的幾種方法

            Hashtable ht = new Hashtable();

            ht.Add("first", "Beijing");
            ht.Add("second", "Shanghai");
            ht.Add("third", "Hangzhou");
            ht.Add("forth", "Nanjing");

            //遍歷方法一：遍歷雜湊表中的鍵
            foreach (string key in ht.Keys)
            {
                Console.WriteLine(ht[key]);
            }
            Console.WriteLine("--------------------");

            //遍歷方法二：遍歷雜湊表中的值
            foreach (string value in ht.Values)
            {
                Console.WriteLine(value);
            }
            Console.WriteLine("--------------------");

            //遍歷方法三：遍歷雜湊表中的鍵值
            foreach (DictionaryEntry de in ht)
            {
                Console.WriteLine(de.Value);
                Console.WriteLine(de.Key.ToString());
                Console.WriteLine(de.Value.ToString());
            }
            Console.WriteLine("--------------------");

            //遍歷方法四：遍歷雜湊表中的鍵值
            IDictionaryEnumerator myEnumerator = ht.GetEnumerator();
            while (myEnumerator.MoveNext())
            {
                Console.WriteLine(ht[myEnumerator.Key]);

                //Hashtable關健字
                richTextBox1.Text += "Hashtable關健字 : " + myEnumerator.Key.ToString() + "\n";

                //Hashtable值
                richTextBox1.Text += "Hashtable值 : " + myEnumerator.Value.ToString() + "\n";
            }
        }

        private void ht9_Click(object sender, EventArgs e)
        {
            Hashtable ht = new Hashtable(); //創建一個Hashtable實例

            //key值唯一,value值可以重複.
            ht.Add("E", "e");//添加key/鍵值對
            ht.Add("A", "a");
            ht.Add("C", "c");
            ht.Add("B", "b");
            string s = (string)ht["A"];
            if (ht.Contains("E")) //判斷哈希表是否包含特定鍵,其返回值為true或false
            {
                richTextBox1.Text += "the E key : exists\n";
            }
            else
            {
                richTextBox1.Text += "the E key : no exists\n";

            }

            ht.Remove("C");//移除一個key/鍵值對
            richTextBox1.Text += "輸出 : " + ht["A"] + "\n";  //此處輸出a

            ht.Clear();//移除所有元素

            richTextBox1.Text += "輸出 : " + ht["A"] + "\n";  //此處將不會有任何輸出

            //遍歷哈希表
            //遍歷哈希表需要用到DictionaryEntry Object，代碼如下：
            foreach (DictionaryEntry de in ht)
            {
                Console.WriteLine(de.Key);//de.Key對應于key/value鍵值對key
                Console.WriteLine(de.Value);//de.Key對應于key/value鍵值對value

            }



            //對哈希表進行排序
            /*
            對哈希表進行排序在這里的定義是對key/value鍵值對中的key按一定規則重新排列，但是實際上這個定義是不能實現的，因為我們無法直接在Hashtable進行對key進行重新排列，如果需要Hashtable提供某種規則的輸出，可以采用一種變通的做法：
            */
            ArrayList akeys = new ArrayList(ht.Keys);
            akeys.Sort(); //按字母順序進行排序
            foreach (string skey in akeys)
            {
                Console.Write(skey + ":");
                Console.WriteLine(ht[skey]);//排序後輸出
            }

        }

        private void ht10_Click(object sender, EventArgs e)
        {

        }

        private void ht11_Click(object sender, EventArgs e)
        {

        }

        private void ht12_Click(object sender, EventArgs e)
        {

        }

        private void ht13_Click(object sender, EventArgs e)
        {

        }


        //Hashtable 測試 SP



    }

    class Member
    {
        public string Name { get; set; }      // 姓名屬性          
        public bool Select { get; set; }      // 選課屬性
        public int Score { get; set; }        // 成績屬性  

        public override string ToString()    // 覆寫覆類別 ToString()方法
        {
            return string.Format("姓名 : {0} \t 選課 :{1} \t 成績: {2} \n ", Name, Select ? "是" : "否", Score.ToString());
        }
    }
}
