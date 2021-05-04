using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace StaticMember
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        
        private void Form1_Load(object sender, EventArgs e)
        {
            Student Aaita = new Student("愛妮達", 100);
            Student Jasper = new Student("賈思伯", 56);
            Student Aliya = new Student("愛麗雅", 99);
            label1.Text = Aaita.GetMsg() + "\n";
            label1.Text += Jasper.GetMsg() + "\n";
            label1.Text += Aliya.GetMsg() + "\n";
            label1.Text += "=====================\n";
            //呼叫Student類別的GetTotalStudent靜態方法取得目前有多少位學生
            label1.Text += Student.GetTotalStudent();
        }
    }
}
