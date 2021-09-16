using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh8_5_1_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private DataTable MakeTable()
        {
            DataTable t = new DataTable("Control");
            t.Columns.Add("BackColor", typeof(Color));
            t.Columns.Add("ForeColor", typeof(Color));
            t.Columns.Add("Text");

            DataRow r;

            r = t.NewRow();
            r["BackColor"] = Color.Blue;
            r["ForeColor"] = Color.Yellow;
            r["Text"] = "藍底黃字";
            t.Rows.Add(r);

            r = t.NewRow();
            r["BackColor"] = Color.White;
            r["ForeColor"] = Color.Green;
            r["Text"] = "白底綠字";
            t.Rows.Add(r);

            r = t.NewRow();
            r["BackColor"] = Color.Orange;
            r["ForeColor"] = Color.Black;
            r["Text"] = "橙底黑字";
            t.Rows.Add(r);

            return t;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            textBox1.DataBindings.Clear();

            DataTable t = MakeTable();

            this.BindingContext[t].Position = 2;

            Binding myText = new Binding("Text", t, "Text");
            Binding myForeColor = new Binding("ForeColor", t, "ForeColor");
            Binding myBackColor = new Binding("BackColor", t, "BackColor");

            textBox1.DataBindings.Add(myText);
            textBox1.DataBindings.Add(myForeColor);
            textBox1.DataBindings.Add(myBackColor);
            //textBox1.DataBindings.Add("Text", t, "Text");
            //textBox1.DataBindings.Add("BackColor",t, "BackColor");
            //textBox1.DataBindings.Add("ForeColor", t, "ForeColor");
        }
    }
}
