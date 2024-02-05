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

            groupBox1.Location = new Point(x_st + dx * 1+10, y_st + dy * 0);

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

            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Hashtable的用法0\n";
            Hashtable mTable = new Hashtable();
            mTable.Add(5, "Apple");
            mTable.Add(1, "Banana");
            mTable.Add(4, "Cat");

            foreach (int ID in mTable.Keys)
            {
                richTextBox1.Text += ID.ToString() + "\n";
            }

            foreach (string name in mTable.Values)
            {
                richTextBox1.Text += name + "\n";
            }

            richTextBox1.Text += "直接列印某項\n";
            richTextBox1.Text += mTable[4] + "\n";

            richTextBox1.Text += "先檢查有無項目再列印\n";
            if (mTable.ContainsKey(4))
            {
                richTextBox1.Text += mTable[4] + "\n";
            }
            else
            {
                richTextBox1.Text += "無此項\n";
            }

            mTable.Remove(4);

            richTextBox1.Text += "先檢查有無項目再列印\n";
            if (mTable.ContainsKey(4))
            {
                richTextBox1.Text += mTable[4] + "\n";
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

        private void button2_Click(object sender, EventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
        }



        //Hashtable 測試 ST

        Hashtable HT = new Hashtable();         //雜湊表 (key, value)

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
            show_hashtable(HT);
        }

        int cnt = 0;
        bool flag_already_added_items = false;
        private void ht1_Click(object sender, EventArgs e)
        {
            if (flag_already_added_items == false)
            {
                string name = string.Empty;
                int weight = 0;

                name = "鼠";
                weight = 3;
                HT.Add(name, weight);        //加入雜湊表，Key: name, Value: weight, Key不能重複
                richTextBox1.Text += "加入雜湊表，Key: " + name + ", Value: " + weight + "\n";

                name = "牛";
                weight = 48;
                HT.Add(name, weight);        //加入雜湊表，Key: name, Value: weight, Key不能重複
                richTextBox1.Text += "加入雜湊表，Key: " + name + ", Value: " + weight + "\n";

                name = "虎";
                weight = 33;
                HT.Add(name, weight);        //加入雜湊表，Key: name, Value: weight, Key不能重複
                richTextBox1.Text += "加入雜湊表，Key: " + name + ", Value: " + weight + "\n";

                name = "兔";
                weight = 8;
                HT.Add(name, weight);        //加入雜湊表，Key: name, Value: weight, Key不能重複
                richTextBox1.Text += "加入雜湊表，Key: " + name + ", Value: " + weight + "\n";

                name = "龍";
                weight = 38;
                HT.Add(name, weight);        //加入雜湊表，Key: name, Value: weight, Key不能重複
                richTextBox1.Text += "加入雜湊表，Key: " + name + ", Value: " + weight + "\n";

                flag_already_added_items = true;
            }
        }

        private void ht2_Click(object sender, EventArgs e)
        {
            int len = HT.Count;

            int cnt = 0;
            foreach (DictionaryEntry de in HT)
            {
                richTextBox1.Text += "key = " + de.Key + "\t" + "value = " + de.Value + "\n";
                if (len > 2)
                {
                    if (cnt == (len - 2))
                    {
                        richTextBox1.Text += "移除 " + de.Key + " 項\n";
                        HT.Remove(de.Key);
                        return;
                    }
                }
                else if (len > 0)
                {
                    if (cnt == (len - 1))
                    {
                        richTextBox1.Text += "移除 " + de.Key + " 項\n";
                        HT.Remove(de.Key);
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

            if (HT.ContainsKey("兔"))
            {
                richTextBox1.Text += "1111111111111\n";
                HT["兔"] = 10;
            }

            /*
            richTextBox1.Text += "把bbbb3項的value改變\n";

            if (HT.ContainsValue("bbbb1"))
            {
                //不知道怎麼從value找key
                //HT["aaaa3"] = "xxxxxxxx";
                //richTextBox1.Text += "2222222222222222222\n";
            }
            */
        }

        private void ht4_Click(object sender, EventArgs e)
        {
            HT.Clear();
            richTextBox1.Text += "清除雜湊表\n";
        }

        private void ht5_Click(object sender, EventArgs e)
        {
            if (HT.Count < 5)
            {
                richTextBox1.Text += "至少5筆資料\n";
                return;
            }
            richTextBox1.Text += "HashTable排序\n";

            richTextBox1.Text += "排序前\n";
            show_hashtable(HT);

            richTextBox1.Text += "\n排序後\n";

            //key 為 唯一 可用來查value
            //value 為 非唯一 不可用來查key

            ArrayList akeys = new ArrayList(HT.Keys); //from Hashtable
            //ArrayList akeys = new ArrayList(HT.Values); //from Hashtable

            akeys.Sort(); //Sort by leading letter

            foreach (string skey in akeys)
            {
                richTextBox1.Text += "key = " + skey + "\t" + "value = " + HT[skey] + "\n";
            }
        }

        private void ht6_Click(object sender, EventArgs e)
        {
            // 獲取鍵的集合
            ICollection key = HT.Keys;
            foreach (string k in key)
            {
                richTextBox1.Text += "Key : " + k + "\tValue : " + HT[k] + "\n";
            }
        }

        private void ht7_Click(object sender, EventArgs e)
        {
            //Hashtable 物件
            richTextBox1.Text += "建立一個Hashtable\n";

            Hashtable openWith = new Hashtable();

            richTextBox1.Text += "給Hashtable賦值, key是唯一, value不唯一\n";
            //            key     value
            openWith.Add("txt", "notepad.exe");
            openWith.Add("bmp", "paint.exe");
            openWith.Add("dib", "paint.exe");
            openWith.Add("rtf", "wordpad.exe");

            // When you use foreach to enumerate hash table elements,
            // the elements are retrieved as DictionaryEntry objects.
            foreach (DictionaryEntry var in openWith)
            {
                richTextBox1.Text += var.Key + "\t" + var.Value + "\n";
            }

        }

        private void ht8_Click(object sender, EventArgs e)
        {
            //遍歷Hashtable 的幾種方法

            Hashtable hashtable = new Hashtable();

            hashtable.Add("first", "Beijing");
            hashtable.Add("second", "Shanghai");
            hashtable.Add("third", "Hangzhou");
            hashtable.Add("forth", "Nanjing");

            //遍歷方法一：遍歷雜湊表中的鍵
            foreach (string key in hashtable.Keys)
            {
                Console.WriteLine(hashtable[key]);
            }
            Console.WriteLine("--------------------");

            //遍歷方法二：遍歷雜湊表中的值
            foreach (string value in hashtable.Values)
            {
                Console.WriteLine(value);
            }
            Console.WriteLine("--------------------");

            //遍歷方法三：遍歷雜湊表中的鍵值
            foreach (DictionaryEntry de in hashtable)
            {
                Console.WriteLine(de.Value);
                Console.WriteLine(de.Key.ToString());
                Console.WriteLine(de.Value.ToString());
            }
            Console.WriteLine("--------------------");

            //遍歷方法四：遍歷雜湊表中的鍵值
            IDictionaryEnumerator myEnumerator = hashtable.GetEnumerator();
            while (myEnumerator.MoveNext())
            {
                Console.WriteLine(hashtable[myEnumerator.Key]);

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
}
