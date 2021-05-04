using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Property
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Student Jasper = new Student();
            Jasper.Name = "賈思伯";
            Jasper.Score = 5000;
            Jasper.ShowMsg();
            Student Anita = new Student();
            Anita.Name = "愛妮達";
            Anita.Score = -100;
            Anita.ShowMsg();
        }
    }
}
