using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Collections;  // for IEnumerator

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

            //------------------------------------------------------------  # 60個

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

            groupBox_rgb.BackColor = Color.FromArgb(hScrollBar_r.Value, hScrollBar_g.Value, hScrollBar_b.Value);
            tb_r.BackColor = Color.FromArgb(hScrollBar_r.Value, 0, 0);
            tb_g.BackColor = Color.FromArgb(0, hScrollBar_g.Value, 0);
            tb_b.BackColor = Color.FromArgb(0, 0, hScrollBar_b.Value);

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

            //------------------------------------------------------------  # 60個

            lb_time_interval.Text = "------------";

            //------------------------------------------------------------  # 60個

            // 建立Product陣列用來存放產品
            string[] Product = new string[] { "火影忍者", "航海王",
 				"史瑞克4", "葉問2", "鋼鐵人2", "偷心大聖PS男", "阿凡達",
 				"半夜鬼上床", "第一次愛上你", "松藥局的兒子們", "老婆，給我飯" };
            // 將Product陣列的所有選項放入checkedListBox1內
            checkedListBox1.Items.AddRange(Product);
            checkedListBox1.MultiColumn = true;	// 核取清單方塊設為多欄
            checkedListBox1.ColumnWidth = 150; 	// 核取清單方塊欄寬150
            checkedListBox1.CheckOnClick = true; // 只按一下選取

            /*
            checkedListBox1.MultiColumn = true;	// chkListLot水平欄顯示
            checkedListBox1.ColumnWidth = 100;    	// chkListLot水平欄寬
            // 在chkListLot核取清單方塊加入項目, 可讓使用者勾選
            for (int i = 1; i <= 100; i++)
            {
                checkedListBox1.Items.Add(i.ToString());
            }
            */

            /*
            checkedListBox1.Items.AddRange(
                new object[]
                { 
                    "滑鼠",
                    "鍵盤",
                    "網卡",
                    "螢幕",
                    "音效卡",
                    "數據機",
                    "外接硬碟"
                });
            checkedListBox1.MultiColumn = true;
            checkedListBox1.ColumnWidth = 120;
            checkedListBox1.CheckOnClick = true;
            */

            //------------------------------------------------------------  # 60個

            // 設定進度列的最大值與最小值
            progressBar0.Maximum = 100;
            progressBar0.Minimum = 0;

            // 設定Timer每一秒鐘會執行Tick事件一次
            timer1.Interval = 1000;

            // 跑馬燈式的進度列會一直有動畫，
            // 為避免誤解，當進度為0時，將其樣式更改為Block
            if (progressBar0.Minimum == 0)
            {
                progressBar0.Style = ProgressBarStyle.Blocks;
            }

            //------------------------------------------------------------  # 60個
        }

        void show_item_location()
        {
            int W = 150;
            int H = 100;
            int x_st = 20;
            int y_st = 20;
            int dx = W + 10;
            int dy = H + 10;

            groupBox_radiobutton0.Size = new Size(W, H);
            groupBox_radiobutton1.Size = new Size(W, H);
            groupBox_radiobutton2.Size = new Size(W, H);
            groupBox_radiobutton3.Size = new Size(W, H);
            groupBox_numericupdown.Size = new Size(W * 2, H);
            groupBox_trackbar.Size = new Size(W * 2, H);
            groupBox_domainupdown.Size = new Size(W * 2, H);
            groupBox_radiobutton0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox_radiobutton1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            groupBox_radiobutton2.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox_radiobutton3.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            groupBox_numericupdown.Location = new Point(x_st + dx * 2 + 20, y_st + dy * 0);
            groupBox_trackbar.Location = new Point(x_st + dx * 2 + 20, y_st + dy * 1);
            groupBox_domainupdown.Location = new Point(x_st + dx * 4 + 60, y_st + dy * 0);

            groupBox_dtp1.Location = new Point(x_st + dx * 2 + 20, y_st + dy * 2);
            groupBox_dtp2.Location = new Point(x_st + dx * 2 + 20, y_st + dy * 3 + 50);
            groupBox_dtp3.Location = new Point(x_st + dx * 4 - 70, y_st + dy * 3 + 50);
            groupBox_checkedlistbox.Location = new Point(x_st + dx * 2 + 20, y_st + dy * 5 - 20);
            groupBox_progress.Location = new Point(x_st + dx * 4 + 60, y_st + dy * 1);

            richTextBox1.Size = new Size(300, 690);
            richTextBox1.Location = new Point(1100, 10);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1400, 850);
            this.Text = "vcs__small";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        //重定義基類OnPaint()方法
        protected override void OnPaint(PaintEventArgs e)
        {
            int W = this.ClientSize.Width;
            int H = this.ClientSize.Height;
            e.Graphics.Clear(Color.White);
            e.Graphics.DrawRectangle(Pens.Red, 0, 0, W - 1, H - 1);

            int dx = W / 4;
            int dy = H / 3;
            for (int xx = 0; xx < W; xx += dx)
            {
                e.Graphics.DrawLine(Pens.Red, xx, 0, xx, H);  // 直線
            }
            for (int yy = 0; yy < H; yy += dy)
            {
                e.Graphics.DrawLine(Pens.Red, 0, yy, W, yy);  // 橫線
            }

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
            ManageCheckGroupBox(chkBreakfast, groupBox_radiobutton2);
        }

        private void chkLunch_CheckedChanged(object sender, EventArgs e)
        {
            ManageCheckGroupBox(chkLunch, groupBox_radiobutton3);
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
            groupBox_rgb.BackColor = Color.FromArgb(hScrollBar_r.Value, hScrollBar_g.Value, hScrollBar_b.Value);
            tb_r.Text = hScrollBar_r.Value.ToString();
            tb_g.Text = hScrollBar_g.Value.ToString();
            tb_b.Text = hScrollBar_b.Value.ToString();
            tb_r.BackColor = Color.FromArgb(hScrollBar_r.Value, 0, 0);
            tb_g.BackColor = Color.FromArgb(0, hScrollBar_g.Value, 0);
            tb_b.BackColor = Color.FromArgb(0, 0, hScrollBar_b.Value);
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

        int flag_timer_counter_down_enable = 0;
        DateTime dt_timer_st = DateTime.Now;
        int wait_seconds = 0;

        private void bt1_Click(object sender, EventArgs e)
        {
            this.TopMost = false;
            if (flag_timer_counter_down_enable == 1)
            {
                flag_timer_counter_down_enable = 0;
                bt1.Text = "倒數";
            }
            else
            {
                flag_timer_counter_down_enable = 1;
                bt1.Text = "停止";

                dt_timer_st = DateTime.Now;
                wait_seconds = int.Parse(textBox2.Text) * 60;
                richTextBox1.Text += "等待時間： " + wait_seconds.ToString() + "\n";
            }

        }

        private void bt2_Click(object sender, EventArgs e)
        {
            //dateTimePicker3.Value = new DateTime(2006, 3, 11);                //特定日期
            //dateTimePicker3.Value = Convert.ToDateTime("2006/3/11 9:15:30");  //特定日期與時間
            //dateTimePicker3.Value = DateTime.Today;                      //今天日期
            this.dateTimePicker3.Value = DateTime.Now;                          //現在時刻

        }

        private void bt_dtp_set_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "設定DateTimePicker的顯示範圍\n";
            richTextBox1.Text += "顯示現在到未來12天\n";
            dateTimePicker4.MinDate = DateTime.Today;//當天時間
            dateTimePicker4.MaxDate = DateTime.Today.AddDays(12);
        }

        private void bt_dtp_get_Click(object sender, EventArgs e)
        {
            string date1 = dateTimePicker4.Value.Month.ToString() + "/" + dateTimePicker4.Value.Day.ToString();
            richTextBox1.Text += "你選取的日期是 : " + date1.ToString() + "\n";

            string date2 = DateTime.Today.AddDays(12).Month.ToString() + "/" + DateTime.Today.AddDays(12).Day.ToString();
            richTextBox1.Text += "12天後的日期是 : " + date2.ToString() + "\n";
        }

        private void dateTimePicker3_ValueChanged(object sender, EventArgs e)
        {
            richTextBox1.Text += "The selected value is " + dateTimePicker3.Value + "\n";
            richTextBox1.Text += "The selected value is " + dateTimePicker3.Text + "\n";
            richTextBox1.Text += "The day of the week is " + dateTimePicker3.Value.DayOfWeek.ToString() + "\n";
            richTextBox1.Text += "The day of the year is " + dateTimePicker3.Value.DayOfYear.ToString() + "\n";
            richTextBox1.Text += "Millisecond is: " + dateTimePicker3.Value.Millisecond.ToString() + "\n";

            richTextBox1.Text += "\n";
            richTextBox1.Text += dateTimePicker3.Value.Year.ToString();
            richTextBox1.Text += "/" + dateTimePicker3.Value.Month.ToString();
            richTextBox1.Text += "/" + dateTimePicker3.Value.Day.ToString();

            DateTime dt = DateTime.Now;
            richTextBox1.Text += " " + dt.Hour;
            richTextBox1.Text += ":" + dt.Minute;
            richTextBox1.Text += ":" + dt.Second;
            richTextBox1.Text += "\n";

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (flag_timer_counter_down_enable == 1)
            {
                DateTime dt = DateTime.Now;
                TimeSpan interval = dt - dt_timer_st;

                //richTextBox1.Text += "與現在相距：" + ts2.ToString() + "\n";

                //TimeSpan interval = dt - dt.Date;
                //richTextBox1.Text += dt.ToString() + "\n";
                //richTextBox1.Text += dt.Date.ToString() + "\n";
                //richTextBox1.Text += "xxx " + interval.TotalSeconds.ToString();// +"\n";
                lb_time_interval.Text = "經過 : " + interval.TotalSeconds.ToString();

                if (interval.TotalSeconds > wait_seconds)
                {
                    this.TopMost = true;
                    lb_time_interval.Text += "yyyy";
                    richTextBox1.Text += "Q ";
                }
            }
        }

        //------------------------------------------------------------  # 60個

        private void bt_clb0_Click(object sender, EventArgs e)
        {
            //Info
            //全選

            //全不選

            //Info

            // 宣告 count變數，用來記錄使用者勾選大樂透幾個號碼
            int count = 0;
            // 使用for 迴圈記錄目前共勾選幾個號碼
            for (int i = 0; i < checkedListBox1.Items.Count; i++)
            {
                if (checkedListBox1.GetItemChecked(i))
                {
                    richTextBox1.Text += "你選擇了 : " + checkedListBox1.GetItemChecked(i).ToString() + "\n";
                    count++;
                }
            }

            // 將使用者在chkListLot所選號碼逐一指定給myNumStr字串變數
            // 以便將來和大樂透號碼pcNumStr字串比對
            string myNumStr = string.Empty;
            for (int i = 0; i < checkedListBox1.Items.Count; i++)
            {
                if (checkedListBox1.GetItemChecked(i))
                {
                    myNumStr += checkedListBox1.Items[i].ToString() + ", ";
                }
            }

            richTextBox1.Text += "myNumStr = " + myNumStr + "\n";
        }

        private void bt_clb1_Click(object sender, EventArgs e)
        {
            //勾選狀態
            string result;
            foreach (int indexChecked in checkedListBox1.CheckedIndices)
            {
                result = "索引 " + indexChecked.ToString() + ", 已被勾選. 勾選的狀態是->" + checkedListBox1.GetItemCheckState(indexChecked).ToString();
                richTextBox1.Text += result + "\n";
            }

            foreach (object itemChecked in checkedListBox1.CheckedItems)
            {
                result = "被勾選的項目是\"" + itemChecked.ToString() + "\"勾選的狀態是->" + checkedListBox1.GetItemCheckState(checkedListBox1.Items.IndexOf(itemChecked)).ToString();
                richTextBox1.Text += result + "\n";
            }

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "訂購產品如下\n";
            // 逐一檢查每一個核取方塊是否被選取
            for (int i = 0; i < checkedListBox1.Items.Count; i++)
            {
                // 若第i個核取方塊被選取，即將該產品顯示在textBox1
                if (checkedListBox1.GetItemChecked(i))
                {
                    richTextBox1.Text += "　．" + checkedListBox1.Items[i].ToString() + "\n";
                }
            }
        }

        private void bt_clb2_Click(object sender, EventArgs e)
        {
            //取消勾選
            IEnumerator myEnumerator;
            myEnumerator = checkedListBox1.CheckedIndices.GetEnumerator();
            while (myEnumerator.MoveNext() != false)
            {
                int y = (int)myEnumerator.Current;
                checkedListBox1.SetItemChecked(y, false);
            }

            //------------------------------------------------------------  # 60個

            // 設定所有核取方塊不勾選
            for (int i = 0; i < checkedListBox1.Items.Count; i++)
            {
                checkedListBox1.SetItemChecked(i, false);
            }
        }

        //------------------------------------------------------------  # 60個

        private void timer_progress_Tick(object sender, EventArgs e)
        {
            if (progressBar0.Value >= progressBar0.Maximum)
            {
                timer_progress.Stop();
                lb_status0.Text = "完成";
                progressBar0.Value = 0;
                progressBar0.Style = ProgressBarStyle.Blocks;
            }
            else
            {
                progressBar0.Value += 10;
                lb_status0.Text = progressBar0.Value.ToString() + "%";
            }

        }

        private void bt_start_Click(object sender, EventArgs e)
        {
            progressBar0.Style = ProgressBarStyle.Marquee;
            timer_progress.Start();
        }

        private void bt_stop_Click(object sender, EventArgs e)
        {
            timer_progress.Stop();
        }

        //------------------------------------------------------------  # 60個

    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/

