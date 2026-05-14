using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DynamicAddRemoveControls2
{
    public partial class Form1 : Form
    {
        Label label0 = new Label();
        Label label1 = new Label();
        Label label2 = new Label();
        Label label3 = new Label();
        Label label4 = new Label();
        Label label5 = new Label();
        Label label6 = new Label();
        Label label7 = new Label();

        //將 ToolStrip 加入 toolStripContainer1 的 TopToolStripPanel
        //將 toolStripContainer1 加入 表單
        ToolStripContainer toolStripContainer1;
        ToolStrip toolStrip1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10 + 30;
            int dx = 200 + 10;
            int dy = 60 + 10;
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            richTextBox1.Size = new Size(300, 690);
            richTextBox1.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1273, 750 + 30);
            this.Text = "vcs_DynamicAddRemoveControls2";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //建立控件

            int x_st = 250;
            int y_st = 50;
            int dx = 150;
            int dy = 150;

            //控件一維陣列
            Label[] label_array = new Label[] { label0, label1, label2, label3, label4, label5, label6, label7 };
            for (int i = 0; i < 8; i++)
            {
                label_array[i].BackColor = System.Drawing.SystemColors.ActiveBorder;
                label_array[i].FlatStyle = System.Windows.Forms.FlatStyle.Popup;
                label_array[i].Font = new System.Drawing.Font("微軟正黑體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
                label_array[i].Size = new System.Drawing.Size(72, 90);
                label_array[i].Text = i.ToString();
                label_array[i].Name = "label" + i.ToString();
                label_array[i].TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
                label_array[i].Location = new Point(x_st + dx * (i % 4), y_st + dy * (i / 4));
                this.Controls.Add(label_array[i]);
            }
            for (int i = 0; i < 8; i++)
            {
                richTextBox1.Text += label_array[i].Name + "\n";
            }

            /*
            //控件一維陣列
            TextBox[] textArray = new TextBox[] { numText1a, numText2a, numText3a, numText4a, numText5a, numText6a, numText7a, numText8a };

            for (int i = 0; i < 8; i++)
            {
                //textArray[i].BackColor = SystemColors.Window;
                textArray[i].BackColor = Color.Pink;
                textArray[i].Text = i.ToString();
            }
            */
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //全部更動
            //this.Controls From中的所有元件控制權
            //foreach (Control child in this.Controls)表示每次從this.Controls中取一個元件的控制權
            foreach (Control child in this.Controls)
            {
                //取元件是Label的控制權
                if (child is Label)
                {
                    //做想做的事
                    child.BackColor = Color.SkyBlue;
                    child.Text = "^^";
                    //.................
                    //.................
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //偶數label更動
            int temp = 6;
            foreach (Control child in this.Controls)
            {
                if (child is Label)
                {
                    richTextBox1.Text += "aaaaa : " + child.Name + "\n";
                    if (child.Name == "label" + temp.ToString())
                    {
                        richTextBox1.Text += "取得 : " + child.Name + "\n";
                        temp -= 2;
                        child.BackColor = Color.YellowGreen;
                        child.Text = "QQ";
                    }
                }
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //恢復
            int temp = 0;
            foreach (Control child in this.Controls)
            {
                if (child is Label)
                {
                    temp++;
                    child.BackColor = SystemColors.ActiveBorder;
                    child.Text = temp.ToString();
                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //對控件的修改
            foreach (Control x in Controls)
            {
                if (x.GetType().ToString() == "System.Windows.Forms.Button")
                {
                    Button Button = (System.Windows.Forms.Button)x;
                    Button.BackColor = Color.Pink;
                }
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            toolStripContainer1 = new System.Windows.Forms.ToolStripContainer();

            toolStrip1 = new System.Windows.Forms.ToolStrip();
            toolStrip1.Items.Add("新增檔案");
            toolStrip1.Items.Add("開啟檔案");
            toolStrip1.Items.Add("儲存檔案");
            toolStrip1.Items.Add("關閉檔案");
            toolStripContainer1.TopToolStripPanel.Controls.Add(toolStrip1);

            Controls.Add(toolStripContainer1);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            PropertyGrid PG = new PropertyGrid();
            Form PGForm = new Form();
            PGForm.Owner = this;
            PGForm.StartPosition = FormStartPosition.Manual;
            PGForm.Left = this.Left + this.Width;
            PGForm.Top = this.Top;
            PGForm.ShowInTaskbar = false;
            PGForm.Controls.Add(PG);
            PG.Dock = DockStyle.Fill;
            PG.SelectedObject = this.label1;  //選擇要顯示的控件名稱
            PGForm.Text = "Label 屬性編輯視窗";
            PGForm.Show();
        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

*/




/*

        //清空文本框
        private void btnReset_Click(object sender, EventArgs e)
        {
            foreach (Control ctl in groupBox1.Controls)
            {
                if (ctl.GetType().ToString() == "System.Windows.Forms.TextBox")
                {
                    ctl.Text = "";
                }
            }
            txt_id.Focus();
            cbox_Sex.SelectedIndex = 0;
        }


            //遍歷所有控件, 找出TextBox, 檢查是否為空
            foreach (object ct in Controls)
            {
                if (ct.GetType().ToString() == "System.Windows.Forms.TextBox")
                {
                    TextBox tx = (TextBox)ct;
                    if (tx.Text == "")
                    {
                        MessageBox.Show(tx.Tag.ToString() + "不能為空");
                    }
                }
            }

//------------------------------------------------------------  # 60個

                    ControlInfo(true);
            ControlInfo(false);


        private void ControlInfo(Boolean B)
        {
            foreach (Control ct in this.groupBox1.Controls)
            {
                if (ct is TextBox)
                {
                    if (B)
                    {
                        ct.Enabled = true;
                    }
                    else
                    {
                        ct.Enabled = false;
                    }
                }
            }
        }

//------------------------------------------------------------  # 60個

            ControlInfo(false);
            ControlInfo(false);
            ControlInfo(true);
        private void ControlInfo(Boolean B)
        {
            foreach (Control ct in this.groupBox1.Controls)
            {
                if (ct is TextBox)
                {
                    ct.Text = "";
                    if (B)
                    {
                        ct.Enabled = true;
                    }
                    else
                    {
                        ct.Enabled = false;
                    }
                }
            }
        }


        private Boolean TextClear()
        {
            foreach (Control c in this.groupBox1.Controls)
            {
                if (c is TextBox)
                {
                    if (c.Text == "")
                    {
                        return false;
                    }
                    else
                    {
                        return true;
                    }
                }
            }
            return true;
        }


        private void clearText()
        {
            foreach (Control cl in this.groupBox1.Controls)
            {
                if (cl is TextBox)
                {
                    cl.Text = "";
                }
            }
        }


        private Boolean TextInfo()
        {
            foreach (Control c in groupBox1.Controls)
            {
                if (c is TextBox)
                {
                    if (c.Text == "")
                    {
                        return false;
                    }
                    else
                    {
                        return true;
                    }
                }
            }
            return true;
        }



        private void clearText()
        {
            foreach (Control c in groupBox1.Controls)
            {
                if (c is TextBox)
                {
                    c.Text = "";
                }
            }
            pictureBox1.Image = null;
        }

//------------------------------------------------------------  # 60個



*/

