using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*
delegate    委託委派

使用delegate定義委托，將一個方法作為參數傳給另一個方法。
委托所指向的函數必須返回值與參數相同
*/

namespace vcs_Delegate
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        //delegate 範例1 ST
        //委托語法
        public delegate void delSayhi(string name); //定義委托
        public static void sayHi(string name, delSayhi del) //定義方法 類型委托
        {
            del(name);
        }

        public static void sayHiChinese(string name)
        {
            Console.WriteLine("你好， 我叫" + name);
        }
        public static void sayHiEnglish(string name)
        {
            Console.WriteLine("hello, my name is {0}, nice to meet you!", name);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            delSayhi del = new delSayhi(sayHiChinese); //實例化委托調用具體方法
            del("san"); //執行

            delSayhi del1 = sayHiChinese; //直接賦值方式
            del1("si");

            //匿名函數
            delSayhi del2 = delegate(string name) { Console.WriteLine(name + "，思密達"); };
            del2("韓國");

            //lambda表達式  ()沒參數也要寫 => { //方法體 } 沒參數可以e=> Console.WriteLine(""); 如果只有一句話不用{} 返回的return可以省略
            delSayhi del3 = (string name) => { Console.WriteLine(name + "，薩瓦迪卡"); };
            del2("泰國");

            sayHi("david", sayHiEnglish); //調用自定義方法 參數要調用的方法
        }
        //delegate 範例1 SP

        //delegate 範例2 ST
        // 求任意數組最大值

        public delegate int delCompre(object o1, object o2); //定義比較委托

        public static int getIntMax(object o1, object o2) //比較int方法
        {
            int n1 = int.Parse(o1.ToString());
            int n2 = int.Parse(o2.ToString());
            return n1 - n2;
        }

        /// <summary>
        /// 取一個任意數組的最大值
        /// </summary>
        /// <param name="objs">數組</param>
        /// <param name="del">委托</param>
        /// <returns></returns>
        public static object getMax(object[] objs, delCompre del)
        {
            object max = objs[0];
            for (int i = 0; i < objs.Length; i++)
            {
                //if (max < objs[i]) object 無法確定是什麼類型 所以不能用<
                if (del(max, objs[i]) < 0) //如果委托值小於0 成立 傳入如何比較即可
                {
                    max = objs[i];
                }
            }
            return max;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //比較int
            object[] objs = new object[] { 1, 2, 3, 4, 5, 32, 1, 243, };
            var max = getMax(objs, getIntMax); //傳入比較int方法
            Console.WriteLine(max);

            var max2 = getMax(objs, delegate(object o1, object o2)
            {
                return int.Parse(o1.ToString()) - int.Parse(o2.ToString());
            }); //匿名函數 與比較int一樣
            Console.WriteLine(max2);

            //比較string
            object[] strs = new object[] { "abc", "efd", "asdf", "sd", "asdff" };
            var maxstrs = getMax(strs, delegate(object o1, object o2)
            {
                return o1.ToString().Length - o2.ToString().Length;
            }); //匿名函數
            Console.WriteLine(maxstrs);

            var maxstrs2 = getMax(strs, (object o1, object o2) =>
            {
                return o1.ToString().Length - o2.ToString().Length;
            }); //lambda 表達式
            Console.WriteLine(maxstrs2);
        }
        //delegate 範例2 SP

        //delegate 範例3 ST
        // 泛型<T>委托

        public delegate int delCompre<T>(T t1, T t2); //定義泛型委托

        public static T getMax2<T>(T[] objs, delCompre<T> del)
        {
            T max = objs[0];
            for (int i = 0; i < objs.Length; i++)
            {
                if (del(max, objs[i]) < 0)
                {
                    max = objs[i];
                }
            }
            return max;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //int
            int[] nums = { 1, 2, 3, 4, 5 };
            int max = getMax2<int>(nums, (int t1, int t2) => { return t1 - t2; });
            Console.WriteLine(max);

            //string
            string[] strs = { "asd", "sdf", "zxcvv", "123", "qwe" };
            string maxStr = getMax2(strs, (string s1, string s2) => { return s1.Length - s2.Length; });
            Console.WriteLine(maxStr);

        }

        //delegate 範例3 SP

    }
}
