using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace FirstClass
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        //表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
            Student Jasper = new Student(); //建立Jasper屬於Student類別的物件
            Jasper.Name = "賈思伯";     //設定Jasper物件的學生姓名
            Jasper.Score = 98;          //設定Jasper物件的學生成績
            Jasper.ShowMsg();           //呼叫ShowMsg()方法顯示學生姓名和分數
            Student Anita = new Student();
            Anita.Name = "愛妮達";
            Anita.Score = 85;
            Anita.ShowMsg();
        }
    }
}
