using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//方案總管/右鍵/加入/新增項目/類別/預設Class1.cs改成Person.cs

namespace vcs_Class1
{
    public partial class Form1 : Form
    {
        //建立 Animal 類別
        public class Animal
        {
            public string recorder;
            public int number;
            public string name;
            public string type;
            //A class被實例化時，會立即執行建構子內容，並且可以傳入參數
            public string Show
            {
                // 可以透過 get 存取子，將字串進行判斷、處理.... 再返回結果
                get { return name; }

                // set含有特殊的keyword: value, 當有值傳入時，都會存入value中
                set
                {
                    name = type;
                    recorder = value;
                    //Console.WriteLine("I am " + value);
                }
            }
        }

        class Sale
        {
            public Sale(string productName, DateTime saleDate, double salePrice)
            {
                this.ProductName = productName;
                this.SaleDate = saleDate;
                this.SalePrice = salePrice;
            }
            public string ProductName { get; set; }//货品名称
            public DateTime SaleDate { get; set; }//销售日期
            public double SalePrice { get; set; }//销售单价
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //empty
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //實例化A類別
            Animal people = new Animal();

            people.type = "zzz";
            people.name = "Brown";
            people.Show = "Joe";
            richTextBox1.Text += people.Show + "\n";

            richTextBox1.Text += "ttt = " + people.recorder + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Person p1 = new Person();

            richTextBox1.Text += "Default firstname = " + p1.FirstName + "\n";
            //讀FirstName
            p1.FirstName = "FN"; //寫firstname
            richTextBox1.Text += "set new firstname = " + p1.FirstName + "\n";
            //p1.LastName ="LN";
            //由於LastName不可寫，因此此行會顯示readonly無法編譯
            richTextBox1.Text += "Default lastname = " + p1.LastName + "\n";
            p1.Age = 5;
            richTextBox1.Text += "condition change Age = " + p1.Age + "\n";
            p1.Age = 20;
            richTextBox1.Text += "condition change Age =" + p1.Age + "\n";
            richTextBox1.Text += "Default sex =" + p1.Sex + "\n";
            p1.Sex = "male";
            richTextBox1.Text += "set new sex =" + p1.Sex + "\n";
            //p1.ADDR = "123"; ADDR不可寫，因此此行會顯示readonly無法編譯
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //获取某类商品最后一次销售单价

            //创建销售列表
            List<Sale> SaleList = new List<Sale>
            {
                new Sale("洗衣机",Convert.ToDateTime("2010-3-3"),600),
                new Sale("冰箱",Convert.ToDateTime("2010-12-12"),1900),
                new Sale("洗衣机",Convert.ToDateTime("2010-2-2"),550),
                new Sale("洗衣机",Convert.ToDateTime("2010-1-1"),500)
            };
            Sale sa = SaleList.Where(itm => itm.ProductName == "洗衣机").OrderBy(itm => itm.SaleDate).Last();//获取洗衣机最后一次销售单价
            //输出查询结果
            //label1.Text = "数据源：{\"洗衣机\",\"2010-3-3\",600}" + Environment.NewLine + "        {\"洗衣机\",\"2010-2-2\",550}" + Environment.NewLine + "        {\"洗衣机\",\"2010-1-1\",500}";//数据源
            //label2.Text = "查询表达式：Last()";//查询表达式/操作
            //label3.Text = "查询结果：" + sa.SalePrice.ToString();//查询结果

            richTextBox1.Text += "数据源：{\"洗衣机\",\"2010-3-3\",600}" + "\n"
                + "        {\"洗衣机\",\"2010-2-2\",550}" + "\n"
                + "        {\"洗衣机\",\"2010-1-1\",500}" + "\n";//数据源
            richTextBox1.Text += "查询表达式：Last()" + "\n";//查询表达式/操作
            richTextBox1.Text += "查询结果：" + sa.SalePrice.ToString() + "\n";//查询结果
        }
    }
}
