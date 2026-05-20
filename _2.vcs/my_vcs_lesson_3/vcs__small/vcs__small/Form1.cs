using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//DomainUpDown 表示會顯示字串值的 Windows 微調方塊 (也稱為上下按鈕控制項)。

namespace vcs__small
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            // pictureBox1顯示圖片
            pictureBox1.Image = new Bitmap(filename);
            pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;
            pictureBox1.BorderStyle = BorderStyle.Fixed3D;
            // 圖片方塊寬度指定給水平捲軸最大值
            hScrollBar1.Maximum = pictureBox1.Width;
            // 圖片方塊寬度指定給水平捲軸的值
            hScrollBar1.Value = pictureBox1.Width;
            // 圖片方塊高度指定給垂直捲軸最大值
            vScrollBar1.Maximum = pictureBox1.Height;
            // 圖片方塊高度指定給垂直捲軸的值
            vScrollBar1.Value = pictureBox1.Height;
            // label1顯示目前水平捲軸與垂直捲軸的值
            label1.Text = "寬：" + hScrollBar1.Value.ToString() + "       " + "高：" + vScrollBar1.Value.ToString();

            hScrollBar1.Minimum = 0;
            hScrollBar1.Maximum = pictureBox1.Width;

            vScrollBar1.Minimum = 0;
            vScrollBar1.Maximum = pictureBox1.Height;

            //pictureBox1.Width = 300;
            //pictureBox1.Height = 225;
            //hScrollBar1.Value = 300;
            //vScrollBar1.Value = 225;

            //------------------------------------------------------------  # 60個

            panel_rgb.BackColor = Color.FromArgb(hScrollBar_r.Value, hScrollBar_g.Value, hScrollBar_b.Value);
            panel_r.BackColor = Color.FromArgb(hScrollBar_r.Value, 0, 0);
            panel_g.BackColor = Color.FromArgb(0, hScrollBar_g.Value, 0);
            panel_b.BackColor = Color.FromArgb(0, 0, hScrollBar_b.Value);

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "建立 DomainUpDown 內容\n";
            domainUpDown1.Items.Add("Mouse");
            domainUpDown1.Items.Add("Ox");
            domainUpDown1.Items.Add("Tiger");
            domainUpDown1.Items.Add("Rabbit");
            domainUpDown1.Items.Add("Dragon");

            //是否排序
            //domainUpDown1.Sorted = true;
            //是否循環切換
            //domainUpDown1.Wrap = true;
            //是否鍵盤選值
            //domainUpDown1.InterceptArrowKeys = true;

            domainUpDown1.SelectedIndex = 0;

            richTextBox1.Text += "目前共有 " + domainUpDown1.Items.Count + " 個選項\n";

            //------------------------------------------------------------  # 60個

            trackBar1.Value = 50;
            lb_trackber.Text = "取得 : " + trackBar1.Value.ToString();
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            richTextBox1.Size = new Size(300, 690);
            richTextBox1.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1273, 850);
            this.Text = "vcs__small";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //重定義基類OnPaint()方法
        protected override void OnPaint(PaintEventArgs e)
        {
            int W = this.ClientSize.Width;
            int H = this.ClientSize.Height;
            e.Graphics.Clear(Color.White);
            e.Graphics.DrawRectangle(Pens.Red, 10, 10, W - 10 * 2, H - 10 * 2);

            Font f = new Font("微軟正黑體", 22, FontStyle.Bold);//建立字體物件
            Rectangle rect = new Rectangle(100, 100, 500, f.Height);
            string str = "重定義基類OnPaint()方法";
            //e.Graphics.DrawString(str, f, Brushes.Black, rect);
            //e.Graphics.DrawString("使用Resize()方法", f, Brushes.Black, 100, 150);
            f.Dispose();
        }

        //------------------------------------------------------------  # 60個

        private void chkBreakfast_CheckedChanged(object sender, EventArgs e)
        {
            ManageCheckGroupBox(chkBreakfast, groupBox1);
        }

        private void chkLunch_CheckedChanged(object sender, EventArgs e)
        {
            ManageCheckGroupBox(chkLunch, groupBox2);
        }

        private void ManageCheckGroupBox(CheckBox chk, GroupBox grp)
        {
            // Make sure the CheckBox isn't in the GroupBox.
            // This will only happen the first time.
            if (chk.Parent == grp)
            {
                // Reparent the CheckBox so it's not in the GroupBox.
                grp.Parent.Controls.Add(chk);

                // Adjust the CheckBox's location.
                chk.Location = new Point(chk.Left + grp.Left, chk.Top + grp.Top);

                // Move the CheckBox to the top of the stacking order.
                chk.BringToFront();
            }

            // Enable or disable the GroupBox.
            grp.Enabled = chk.Checked;
        }

        //------------------------------------------------------------  # 60個

        private void radioButton_CheckedChanged(object sender, EventArgs e)
        {
            //RadioButton共用函數

            RadioButton radioButton = (RadioButton)sender;
            if (radioButton.Checked == false)
            {
                return;
            }

            richTextBox1.Text += "你選擇了 : ";

            // 顏色選項
            if (radioButton == rb_color1)
                richTextBox1.Text += "紅色\n";
            else if (radioButton == rb_color2)
                richTextBox1.Text += "綠色\n";
            else if (radioButton == rb_color3)
                richTextBox1.Text += "藍色\n";

            // 樣式選項
            else if (radioButton == rb_style1)
                richTextBox1.Text += "實線\n";
            else if (radioButton == rb_style2)
                richTextBox1.Text += "虛線\n";
            else if (radioButton == rb_style3)
                richTextBox1.Text += "點線\n";
        }

        //------------------------------------------------------------  # 60個

        private void vScrollBar1_Scroll(object sender, ScrollEventArgs e)
        {
            // ===  當vScrollBar1垂直捲軸捲動時會執行此事件
            // 圖片的高度依目前垂直捲軸的值調整
            pictureBox1.Height = vScrollBar1.Value;
            label1.Text = "寬：" + hScrollBar1.Value.ToString() + "       高：" + vScrollBar1.Value.ToString();
        }

        private void hScrollBar1_Scroll(object sender, ScrollEventArgs e)
        {
            // ===  當hScrollBar1水平捲軸捲動時會執行此事件
            // 圖片的寬度依目前水平捲軸的值調整
            pictureBox1.Width = hScrollBar1.Value;
            label1.Text = "寬：" + hScrollBar1.Value.ToString() + "       高：" + vScrollBar1.Value.ToString();
        }

        private void hScrollBar_rgb_Scroll(object sender, ScrollEventArgs e)
        {
            //用水平滾動條調整背景色的實例
            //调用了方法，另外把hScrollBar2的scrooll时间设置成hScrollBar1的scroll事件就行了
            panel_rgb.BackColor = Color.FromArgb(hScrollBar_r.Value, hScrollBar_g.Value, hScrollBar_b.Value);
            tb_r.Text = hScrollBar_r.Value.ToString();
            tb_g.Text = hScrollBar_g.Value.ToString();
            tb_b.Text = hScrollBar_b.Value.ToString();
            panel_r.BackColor = Color.FromArgb(hScrollBar_r.Value, 0, 0);
            panel_g.BackColor = Color.FromArgb(0, hScrollBar_g.Value, 0);
            panel_b.BackColor = Color.FromArgb(0, 0, hScrollBar_b.Value);
        }

        //------------------------------------------------------------  # 60個

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            richTextBox1.Text += "目前數量 : " + numericUpDown1.Value + "\n";
        }

        private void bt_plus_Click(object sender, EventArgs e)
        {
            numericUpDown1.UpButton();
        }

        private void bt_minus_Click(object sender, EventArgs e)
        {
            numericUpDown1.DownButton();
        }

        //------------------------------------------------------------  # 60個

        private void domainUpDown1_SelectedItemChanged(object sender, EventArgs e)
        {
            richTextBox1.Text += "Index : " + domainUpDown1.SelectedIndex.ToString() + "\t" + "內容 : " + domainUpDown1.SelectedItem.ToString() + "\n";
            richTextBox1.Text += "目前選到的是：" + domainUpDown1.Text + "\n";
            richTextBox1.Text += "目前選到的是：" + (string)domainUpDown1.SelectedItem + "\n";
        }

        //------------------------------------------------------------  # 60個

        bool flag_mouse_down = false;
        private void trackBar1_MouseDown(object sender, MouseEventArgs e)
        {
            flag_mouse_down = true;
            richTextBox1.Text += "MouseDown :" + trackBar1.Value.ToString() + "\n";
        }

        private void trackBar1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_mouse_down == true)
            {
                lb_trackber.Text = "取得 : " + trackBar1.Value.ToString();
            }
        }

        private void trackBar1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_mouse_down = false;
            richTextBox1.Text += "MouseUp :" + trackBar1.Value.ToString() + "\n";
        }

        //------------------------------------------------------------  # 60個

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



