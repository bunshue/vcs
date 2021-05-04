using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Contructor
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
            //無參數的建構式
            Student Anita = new Student();
            Anita.Name = "愛妮達";
            Anita.Score = 88;
            label1.Text = Anita.GetMsg() + "\n\n";
            //傳一個參數的建構式
            Student Jasper = new Student("賈思伯");
            Jasper.Score = 77;
            label1.Text += Jasper.GetMsg() + "\n\n";
            //傳兩個參數的建構式
            Student Aliya = new Student("愛麗雅", 99);
            label1.Text += Aliya.GetMsg();
        }
    }
}
