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
    public partial class Form1 : Form
    {
        public int MaxIterations;  // Form1的公用參數

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            MaxIterations = 123;
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            richTextBox1.Size = new Size(600, 400);
            //richTextBox1.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //this.Size = new Size(1273, 750);
            this.Text = "vcs_FormSendData2";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        // 給他表單呼叫的函數
        public void ResetColors()
        {
            richTextBox1.Text += "AAAAAAAAAAAAAAAAAAAA\n";
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //由新表單取得資料

            richTextBox1.Text += "呼叫前, MaxIterations = " + MaxIterations.ToString() + "\n";
            Form_GetData frm = new Form_GetData();
            frm.Initialize(this);
            frm.ShowDialog();

            richTextBox1.Text += "呼叫後, MaxIterations = " + MaxIterations.ToString() + "\n";


            /* 呼叫子表單的函數
            VortexConfig frm = new VortexConfig();
            frm.Initialize(this);
            frm.SetDefaultColors();
            frm.AcceptSelections();
            frm.Close();
            */
            /*
            NewFormData dlg = new NewFormData(this);
            try
            {
                if (dlg.ShowDialog() == DialogResult.OK)
                {
                    richTextBox1.Text += "取得Power : " + dlg.Power + "\n";
                    richTextBox1.Text += "取得MaxIterations : " + MaxIterations + "\n";

                }
            }
            catch
            {
            }
            */
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個


