using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_FormSendData2
{
    public partial class Form_GetData : Form
    {
        private Form1 FractalForm;

        // Get and set the Power value.
        public double Power
        {
            get
            {
                Console.WriteLine("cccc");
                return double.Parse(textBox1.Text);
            }
            set
            {
                Console.WriteLine("dddd");
                textBox1.Text = value.ToString();
            }
        }

        public Form_GetData()
        {
            InitializeComponent();
        }

        public void Initialize(Form1 frm)
        {
            richTextBox1.Text += "呼叫了 VortexConfig 的 Initialize\n";
            richTextBox1.Text += "取得 MaxIterations : " + frm.MaxIterations + "\n";

            FractalForm = frm;
            int max_iter = FractalForm.MaxIterations;
        }

        private void Form_GetData_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //呼叫父表單的函數
            FractalForm.ResetColors();

            richTextBox1.Text += "MaxIterations 改成 12345\n";
            FractalForm.MaxIterations = 12345;

            double value111;
            if (double.TryParse(textBox1.Text, out value111))
            {
                Console.WriteLine("aaaa");
                this.DialogResult = DialogResult.OK;
            }
            else
            {
                Console.WriteLine("bbbb");
                MessageBox.Show("Please enter a number.");
                //textBox1.SelectAll();
                //textBox1.Focus();
            }

            this.Close();
        }
    }
}
