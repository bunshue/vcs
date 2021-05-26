using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Class5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Student0 Jasper = new Student0();  //建立Jasper屬於Student類別的物件
            Jasper.Name = "賈思伯";       //設定Jasper物件的學生姓名
            Jasper.Score = 98;             //設定Jasper物件的學生成績
            Jasper.ShowMsg();            //呼叫ShowMsg()方法顯示學生姓名和分數

            Student0 Anita = new Student0();
            Anita.Name = "愛妮達";
            Anita.Score = 85;
            Anita.ShowMsg();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //無參數的建構式
            Student Anita = new Student();
            Anita.Name = "愛妮達";
            Anita.Score = 88;
            richTextBox1.Text += Anita.GetMsg() + "\n";
            //傳一個參數的建構式
            Student Jasper = new Student("賈思伯");
            Jasper.Score = 77;
            richTextBox1.Text += Jasper.GetMsg() + "\n";
            //傳兩個參數的建構式
            Student Aliya = new Student("愛麗雅", 99);
            richTextBox1.Text += Aliya.GetMsg() + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //繼承範例
            Empolyee Jasper = new Empolyee();  //Employee父類別
            Jasper.Name = "賈思伯";
            Jasper.Salary = 30000;
            richTextBox1.Text += "員工姓名：" + Jasper.Name + "\n實領薪水：" + Convert.ToString(Jasper.Salary) + "\n";
            richTextBox1.Text += "======================\n";
            Manager Aliya = new Manager();      //Manager子類別
            Aliya.Name = "愛麗雅";
            Aliya.Salary = 40000;
            Aliya.Bonus = 20000;    //Manager子類別新增的Bonus屬性
            //Manager子類別新增的GetTotal()方法
            richTextBox1.Text += Aliya.GetTotal() + "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //繼承表單範例
            MyForm f = new MyForm();    //建立f 為MyForm類別
            f.ShowDialog();			//呼叫f.ShowDialog()方法使視窗顯示
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //物件檢查參數
            //給錯誤參數, 讓系統自動訂正
            Student Jasper = new Student();
            Jasper.Name = "賈思伯";
            Jasper.Score = 5000;
            Jasper.ShowMsg();
            Student Anita = new Student();
            Anita.Name = "愛妮達";
            Anita.Score = -100;
            Anita.ShowMsg();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //使用靜態成員
            Student Aaita = new Student("愛妮達", 100);
            Student Jasper = new Student("賈思伯", 56);
            Student Aliya = new Student("愛麗雅", 99);


            richTextBox1.Text += Aaita.GetMsg() + "\n";
            richTextBox1.Text += Jasper.GetMsg() + "\n";
            richTextBox1.Text += Aliya.GetMsg() + "\n";
            richTextBox1.Text += "=====================\n";

            //呼叫Student類別的GetTotalStudent靜態方法取得目前有多少位學生

            richTextBox1.Text += Student.GetTotalStudent() + "\n";
        }

    }
}
