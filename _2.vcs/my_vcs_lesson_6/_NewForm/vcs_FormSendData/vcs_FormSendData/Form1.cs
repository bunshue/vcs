using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//http://www.jysblog.com/coding/c-%e7%88%b6%e5%ad%90%e8%a6%96%e7%aa%97%e5%82%b3%e5%80%bc%e5%95%8f%e9%a1%8c/

/*
簡單的說，
就是利用class中get, set以及form owner來控制變數值的傳遞。
*/

namespace vcs_FormSendData
{
    public partial class Form1 : Form
    {
        private string form1_data;
        public string SetupForm1Data
        {
            set
            {
                form1_data = value;
            }
        }

        public void setForm1Value()
        {
            this.richTextBox1.Text += "父得到信息 : " + form1_data + "\n";
        }

        //使用自己建立的Form2表單
        Form2 childForm = new Form2();      //實體化Form2視窗物件
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            childForm.SetupForm2Data = "父告訴子一件事~~~~~~~";
            childForm.setForm2Value();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //childForm.StartPosition = FormStartPosition.CenterScreen;      //設定新表單的顯示位置, 居中顯示
            //childForm.StartPosition = FormStartPosition.CenterParent;
            childForm.StartPosition = FormStartPosition.Manual;
            childForm.Location = new Point(this.Location.X + 550, this.Location.Y);
            childForm.Owner = this;
            //childForm.ShowDialog();
            childForm.Show();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Form2 childForm = new Form2();//產生Form2的物件，才可以使用它所提供的Method
            //childForm.Show();         //不等結束
            //childForm.ShowDialog();   //要等結束
            childForm.ShowDialog(this); //設定Form2為Form1的上層，並開啟Form2視窗。由於在Form1的程式碼內使用this，所以this為Form1的物件本身

            if (childForm.DialogResult == System.Windows.Forms.DialogResult.OK)
            {
                //若使用者在Form2按下了OK，則進入這個判斷式
                richTextBox1.Text += "按下了" + childForm.DialogResult.ToString() + "\n";
            }
            else if (childForm.DialogResult == System.Windows.Forms.DialogResult.Cancel)
            {
                //若使用者在Form2按下了Cancel或者直接點選X關閉視窗，都會進入這個判斷式
                richTextBox1.Text += "按下了" + childForm.DialogResult.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "按下了" + childForm.DialogResult.ToString() + "\n";
            }


        }

        private void button5_Click(object sender, EventArgs e)
        {
            // 繼承Form類別產生新的視窗表單
            Form form_new = new Form();

            form_new.Cursor = System.Windows.Forms.Cursors.Cross;
            form_new.FormBorderStyle = FormBorderStyle.Sizable;
            form_new.Height = 400;
            form_new.HelpButton = true;
            form_new.MaximizeBox = true;
            form_new.MinimizeBox = true;
            form_new.Name = "New Form";
            form_new.ShowInTaskbar = true;
            form_new.StartPosition = FormStartPosition.CenterParent;
            form_new.Text = "New Form";
            form_new.Width = 500;
            form_new.WindowState = FormWindowState.Normal;
            form_new.Enabled = true;

            // 以Form類別的ShowDialog方法顯示視窗表單, 需要等到新表單結束, 不可重複開啟新表單
            //form_new.ShowDialog();

            // 以Form類別的Show方法顯示視窗表單, 不用等到新表單結束, 可重複開啟新表單
            form_new.Show();

        }

        private Form3 frm3 = null;
        private void button6_Click(object sender, EventArgs e)
        {
            //Form1之 button6的「Modifiers」屬性變更為“public”，以供Form3存取。
            //將Form1傳入Form3中
            frm3 = new Form3(this);
            //frm3.ShowDialog();
            frm3.Show();
        }

        private double sind(double d)
        {
            return Math.Sin(d * Math.PI / 180.0);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //傳送資料到新表單並顯示之
            //目前只能顯示在新表單的Panel上

            int N = 360;
            int[] histoData;
            histoData = new int[N];
            for (int i = 0; i < N; ++i)
            {
                histoData[i] = (int)(100 * sind(i)) + 100;
            }

            Form4 form4 = new Form4(histoData);
            form4.Show();

        }
    }
}
