using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;
using System.Reflection;                //for BindingFlags  //刪除控件的事件的方法
using System.Text.RegularExpressions;

namespace vcs_test_all_01_Control
{
    public partial class Form1 : Form
    {
        // The small and large button sizes.
        private Size SmallSize, LargeSize;
        private Font SmallFont, LargeFont;

        private double opacity = 0;//記錄當前窗體的透明度

        //移動控件 ST
        Point CPoint;//記錄滑鼠游標在父容器中的初始位置
        bool isDown = false;//判斷是否可以移動文字
        int tem_x = 0;//記錄滑鼠游標移動文字後的X位置
        int tem_y = 0;//記錄滑鼠游標移動文字後的Y位置

        int W = 0;
        int H = 0;
        //移動控件 SP

        //在控件上加ToolTip
        ToolTip tooltip1 = new ToolTip();
        ToolTip tooltip2 = new ToolTip();
        ToolTip tooltip3 = new ToolTip();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //不同Button共用一個事件
            button6.Click += new EventHandler(button6_Click);//按下button6觸發button1_Click
            button7.Click += new EventHandler(button6_Click);//按下button7觸發button1_Click
            button8.Click += new EventHandler(button6_Click);//按下button8觸發button1_Click
            button9.Click += new EventHandler(button6_Click);//按下button9觸發button1_Click

            //移動控件 ST
            W = this.ClientSize.Width;
            H = this.ClientSize.Height - 100;
            //移動控件 SP

            //先顯示一個訊息, 再開啟主程式
            string str = "";
            for (int i = 1; i <= 6; i++)		// 被乘數
            {
                for (int j = 1; j <= 6; j++) 		// 乘數
                {   // 將 i x j = (i * j) 合併str後再指定給str
                    str += i + "x" + j + "=" + (i * j) + '\t';
                }
                str += '\n';   // 換行
            }
            MessageBox.Show(str, "用MessageBox先顯示一個訊息, 再開啟主程式");  //顯示結果

            // Set the small and large sizes.
            SmallSize = flp1.Size;
            LargeSize = new Size((int)(1.5 * flp1.Size.Width), (int)(1.5 * flp1.Size.Height));

            SmallFont = flp1.Font;
            LargeFont = new Font(SmallFont.FontFamily, SmallFont.Size * 1.5f, FontStyle.Bold);

            lb_checkbox_CheckState.Text = "";

            // Give this button's image a transparent background.
            MakeButtonTransparent(button35);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();

            Opacity = 0;//指定窗體完全透明
            timer2.Enabled = true;

            //使用ToolTip
            tooltip1.SetToolTip(button41, "在控件上加ToolTip 41");
            tooltip1.ToolTipIcon = ToolTipIcon.Info;	//ToolTipIcon:取得或設定值,以便定義要顯示在工具提示文字旁的圖示類型
            tooltip1.ForeColor = Color.Blue;	//ForeColor:取得或設定工具提示的前景色彩
            tooltip1.BackColor = Color.LightGray;	//BackColor:取得或設定工具提示的背景色彩.
            tooltip1.AutoPopDelay = 5000;	//AutoPopDelay:當指標靜止於控制項上時,ToolTip 保持可見的時間 (以毫秒為單位).預設值為 5000.
            tooltip1.ToolTipTitle = "vcs";	//ToolTipTitle:取得或設定工具提示視窗的標題.

            tooltip2.SetToolTip(button42, "在控件上加ToolTip 42");
            tooltip2.ToolTipIcon = ToolTipIcon.Info;	//ToolTipIcon:取得或設定值,以便定義要顯示在工具提示文字旁的圖示類型
            tooltip2.ForeColor = Color.Blue;	//ForeColor:取得或設定工具提示的前景色彩
            tooltip2.BackColor = Color.LightGray;	//BackColor:取得或設定工具提示的背景色彩.
            tooltip2.AutoPopDelay = 5000;	//AutoPopDelay:當指標靜止於控制項上時,ToolTip 保持可見的時間 (以毫秒為單位).預設值為 5000.
            tooltip2.ToolTipTitle = "vcs";	//ToolTipTitle:取得或設定工具提示視窗的標題.

            tooltip3.SetToolTip(button43, "在控件上加ToolTip 43");
            tooltip3.ToolTipIcon = ToolTipIcon.Info;	//ToolTipIcon:取得或設定值,以便定義要顯示在工具提示文字旁的圖示類型
            tooltip3.ForeColor = Color.Blue;	//ForeColor:取得或設定工具提示的前景色彩
            tooltip3.BackColor = Color.LightGray;	//BackColor:取得或設定工具提示的背景色彩.
            tooltip3.AutoPopDelay = 5000;	//AutoPopDelay:當指標靜止於控制項上時,ToolTip 保持可見的時間 (以毫秒為單位).預設值為 5000.
            tooltip3.ToolTipTitle = "vcs";	//ToolTipTitle:取得或設定工具提示視窗的標題.

            //可自由移動所有控件
            //this.TransparencyKey = SystemColors.Control;
            foreach (Control subCtrl in this.Controls)
            {
                new MoveControl(subCtrl);
            }
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 20;
            y_st = 30;
            dx = 120 + 10;
            dy = 55 + 10;

            x_st = 1050;
            y_st = 100;

            bt_help.Location = new Point(x_st + dx * 0, y_st - dy * 1);
            bt_about.Location = new Point(x_st + dx * 1, y_st - dy * 1);

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button10.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button12.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button13.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            button15.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button33.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button34.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button37.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button40.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button46.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button47.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button48.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button49.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button50.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            richTextBox1.Location = new Point(x_st + dx * 2, y_st - dy * 1);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            bt_rtb_info.Location = new Point(richTextBox1.Location.X, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_rtb_info.Size.Height);
        }

        // 做出 去背景 的效果
        // Give the button a transparent background.
        private void MakeButtonTransparent(Button btn)
        {
            Bitmap bm = (Bitmap)btn.Image;
            bm.MakeTransparent(bm.GetPixel(0, 0));
            //btn.Image = bm;   comment also OK
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        /*
        //移動控件 方法一 ST
        private void control_MouseDown(object sender, MouseEventArgs e)
        {
            CPoint = new Point(e.X, e.Y);//取得滑鼠游標在文字上按下時的位置
            tem_x = e.X;//記錄X座標
            tem_y = e.Y;//記錄X座標
            isDown = true;//文字可能移動
        }

        private void control_MouseMove(object sender, MouseEventArgs e)
        {
            Control ctrl = (Control)sender;
            bool tem_b = false;//判斷是否超出邊界
            if (e.Button == MouseButtons.Left && isDown == true)//如果目前按下的是滑鼠游標左鍵，而且文字可以移動
            {
                //如果文字在移動範圍內
                if (ctrl.Left <= 0 || ctrl.Top <= 0 || ctrl.Left >= (this.Width - ctrl.Width) || ctrl.Top >= (this.Height - ctrl.Height))
                {
                    if (ctrl.Left <= 0)//如果文字超出左邊界
                        if (e.X > tem_x)//如果文字還向右移動
                            tem_b = true;//文字移動
                    if (ctrl.Top <= 0)//如果文字超出上邊界
                        if (e.Y > tem_y)//如果文字還向下移動
                            tem_b = true;//文字移動
                    if (ctrl.Left >= (this.Width - ctrl.Width))//如果文字超出右邊界
                        if (e.X < tem_x)//如果文字還向左移動
                            tem_b = true;//文字移動
                    if (ctrl.Top >= (this.Height - ctrl.Height))//如果文字超出下邊界
                        if (e.Y < tem_y)//如果文字還向上移動
                            tem_b = true;//文字移動
                    if (tem_b == false)//如果文字超出邊界
                        return;//退出本次操作
                }
                Point myPosittion = new Point(ctrl.Left + e.X - CPoint.X, ctrl.Top + e.Y - CPoint.Y);//移動Label控制元件
                ctrl.Location = myPosittion;//設定目前控制元件在視窗容器上的位置
            }
            tem_x = e.X;//記錄移動後的X位置
            tem_y = e.Y;//記錄移動後的Y位置
        }
        //移動控件 方法一 SP
        */

        //移動控件 方法二 ST
        //在C#中，實現可拖動控件，並顯示控件的坐標位置
        private Point mouse_offset;

        private void control_MouseDown(object sender, MouseEventArgs e)
        {
            mouse_offset = new Point(-e.X, -e.Y);
        }

        private void control_MouseMove(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                Point mousePos = Control.MousePosition;
                mousePos.Offset(mouse_offset.X, mouse_offset.Y);
                ((Control)sender).Location = ((Control)sender).Parent.PointToClient(mousePos);
            }
            //this.label1.Text ="橫坐標:"+mouse_offset.X+"縱坐標"+mouse_offset.Y;
        }
        //移動控件 方法二 SP


        int i = 0;
        private void button1_Click(object sender, EventArgs e)
        {
            i++;

            i %= 6;
            if (i == 1)
                button1.Dock = DockStyle.Left;
            else if (i == 2)
                button1.Dock = DockStyle.Right;
            else if (i == 3)
                button1.Dock = DockStyle.Top;
            else if (i == 4)
                button1.Dock = DockStyle.Bottom;
            else if (i == 5)
                button1.Dock = DockStyle.Fill;
            else
                button1.Dock = DockStyle.None;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            AddMyGroupBox();
        }

        // Add a GroupBox to a form and set some of its common properties.
        private void AddMyGroupBox()
        {
            // Create a GroupBox and add a TextBox to it.
            GroupBox groupBox1 = new GroupBox();
            TextBox textBox1 = new TextBox();
            textBox1.Location = new Point(15, 15);
            groupBox1.Controls.Add(textBox1);

            // Set the Text and Dock properties of the GroupBox.
            groupBox1.Text = "MyGroupBox";
            groupBox1.Dock = DockStyle.Right;

            // Disable the GroupBox (which disables all its child controls)
            groupBox1.Enabled = true;

            // Add the Groupbox to the form.
            this.Controls.Add(groupBox1);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            CreateMyRichTextBox();
        }

        public void CreateMyRichTextBox()
        {
            RichTextBox richTextBox1 = new RichTextBox();
            richTextBox1.Dock = DockStyle.Fill;

            try
            {
                richTextBox1.LoadFile(@"D:\_git\vcs\_1.data\______test_files1\__RW\_rtf\VS2013Express.rtf");
                richTextBox1.Find("Text", RichTextBoxFinds.MatchCase);

                richTextBox1.SelectionFont = new Font("Verdana", 12, FontStyle.Bold);
                richTextBox1.SelectionColor = Color.Red;

                string filename = Application.StartupPath + "\\rtf_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".rtf";
                richTextBox1.SaveFile(filename, RichTextBoxStreamType.RichText);
                richTextBox1.Text += "已存檔 : " + filename + "\n";

                this.Controls.Add(richTextBox1);
            }
            catch (System.IO.FileNotFoundException)
            {
                MessageBox.Show("找不到檔案");
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "遍歷所有控件\n";
            foreach (Control con in this.Controls)
            {
                System.String strControl = con.GetType().ToString();//获得控件的类型
                System.String strControlName = con.Name.ToString();//获得控件的名称

                richTextBox1.Text += "Type\t" + strControl + "\tName\t" + strControlName + "\n";
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //Sender它代表的是引發這個事件的Object，所以我們可以把他轉型回來使用。
            richTextBox1.Text += "Name : " + ((Button)sender).Name.ToString() + "\n";
            richTextBox1.Text += "Size : " + ((Button)sender).Size.Width.ToString() + " X " + ((Button)sender).Size.Height.ToString() + "\n";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //不同Button共用一個事件
            Button btn = (Button)sender;
            richTextBox1.Text += "你按了 " + btn.Text + "\n";

            richTextBox1.Text += "你按了 " + ((Button)sender).Name.ToString() + "\n";

            Control ctrl = (Control)sender;
            richTextBox1.Text += "控件內容\t" + ctrl + "\n";
            richTextBox1.Text += "Type\t" + ctrl.GetType() + "\n";
            richTextBox1.Text += "Name\t" + ctrl.Name + "\n";
            richTextBox1.Text += "Text\t" + ctrl.Text + "\n";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //Form.Controls 屬性是用來取得這張Form的控制項
            //Controls.GetType 是取得這個控制項的類別名稱

            for (int i = 0; i < this.Controls.Count; i++)
            {
                richTextBox1.Text += "Name: " + this.Controls[i].Name + "\t";
                richTextBox1.Text += "Text: " + this.Controls[i].Text + "\t";
                richTextBox1.Text += "這項是：" + this.Controls[i].GetType() + "\n";

                if (this.Controls[i] is Button)
                {
                    richTextBox1.Text += "這是Button" + "\n";
                }
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //列舉控制項
            int i = 1;
            foreach (Control ctrl in this.Controls)
            {
                //取出控制項的類型
                string TypeName = ctrl.GetType().Name;
                //類型若是Label
                if (TypeName == "Button")
                {
                    ctrl.Name = "test" + i.ToString();
                    richTextBox1.Text += ctrl.Name + "\n";
                    i++;
                }
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //依字串長度改變控件大小
            //AutoSizeControl
            int textPadding = 10;   //表示要套用至控制項所有邊緣的填補量
            button13.Text = "012345678901234567890123456789012345";
            Graphics g = button2.CreateGraphics();      //// Create a Graphics object for the Control.
            // Get the Size needed to accommodate the formatted Text.
            Size preferredSize = g.MeasureString(button13.Text, button13.Font).ToSize();
            richTextBox1.Text += "size W = " + preferredSize.Width.ToString() + "\n";
            richTextBox1.Text += "size H = " + preferredSize.Height.ToString() + "\n";
            // Pad the text and resize the control.
            button13.ClientSize = new Size(preferredSize.Width + (textPadding * 2), preferredSize.Height + (textPadding * 2));
            g.Dispose();    // Clean up the Graphics object.
        }

        MyRecordControlClass mdc = new MyRecordControlClass();
        private void button18_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += button18.Text + "\n";
            mdc.recordAllControls(this);
        }

        private void button17_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += button17.Text + "\n";
            mdc.controlSizeChange(this);
        }

        private void button16_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += button16.Text + "\n";
            int count = mdc.control_data.Count;
            richTextBox1.Text += "共有 " + count.ToString() + " 個控件\n";
            int i;
            for (i = 0; i < count; i++)
            {
                richTextBox1.Text += (i + 1).ToString() + "\t";
                richTextBox1.Text += mdc.control_data[i].name + "\t\t";
                //richTextBox1.Text += mdc.control_data[i].text + "\t\t";
                richTextBox1.Text += mdc.control_data[i].x_st.ToString() + "\t";
                richTextBox1.Text += mdc.control_data[i].y_st.ToString() + "\t";
                //richTextBox1.Text += mdc.control_data[i].index.ToString() + "\t";
                richTextBox1.Text += mdc.control_data[i].Left.ToString() + "\t";
                richTextBox1.Text += mdc.control_data[i].Top.ToString() + "\t";
                richTextBox1.Text += mdc.control_data[i].Width.ToString() + "\t";
                richTextBox1.Text += mdc.control_data[i].Height.ToString() + "\t";
                richTextBox1.Text += mdc.control_data[i].enable.ToString() + "\t";
                richTextBox1.Text += mdc.control_data[i].visible.ToString() + "\n";
            }

            richTextBox1.Text += "找出特定的控件\n";

            string pattern = "記住所有控件";
            // Find the control.
            Control ctl = FindControl(this, pattern);
            if (ctl == null)
            {
                richTextBox1.Text += "找不到控件\t" + pattern + "\n";
            }
            else
            {
                richTextBox1.Text += "找到控件\t" + pattern + "\n";
            }

            richTextBox1.Text += "找出所有控件\n";
            FindAllControls();
        }

        // Recursively find the named control.
        private Control FindControl(Control parent, string name)
        {
            // Check the parent.
            if (parent.Text == name)
            {
                return parent;
            }

            // Recursively search the parent's children.
            foreach (Control ctl in parent.Controls)
            {
                richTextBox1.Text += "檢查\t" + ctl.Name + "\t" + ctl.Text + "\n";
                Control found = FindControl(ctl, name);
                if (found != null)
                {
                    return found;
                }
            }

            // If we still haven't found it, it's not here.
            return null;
        }

        void FindAllControls()
        {
            int i = 1;
            foreach (Control ctl in this.Controls)
            {
                richTextBox1.Text += "找到控件\t" + i.ToString() + "\t" + ctl.Name + "\t" + ctl.Text + "\n";
                i++;
            }
        }

        private void groupBox1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(groupBox1.BackColor);
            e.Graphics.DrawString(groupBox1.Text, groupBox1.Font, Brushes.Red, 10, 1);
            e.Graphics.DrawLine(Pens.Red, 1, 7, 8, 7);
            e.Graphics.DrawLine(Pens.Red, e.Graphics.MeasureString(groupBox1.Text, groupBox1.Font).Width + 8, 7, groupBox1.Width - 2, 7);
            e.Graphics.DrawLine(Pens.Red, 1, 7, 1, groupBox1.Height - 2);
            e.Graphics.DrawLine(Pens.Red, 1, groupBox1.Height - 2, groupBox1.Width - 2, groupBox1.Height - 2);
            e.Graphics.DrawLine(Pens.Red, groupBox1.Width - 2, 7, groupBox1.Width - 2, groupBox1.Height - 2);
        }

        private void button14_MouseMove(object sender, MouseEventArgs e)
        {
            this.button14.FlatStyle = FlatStyle.Flat;
            this.button14.FlatAppearance.BorderColor = Color.Red;
        }

        private void button14_MouseLeave(object sender, EventArgs e)
        {
            this.button14.FlatStyle = FlatStyle.Standard;
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        // Enlarge the button.
        private void flp_MouseEnter(object sender, EventArgs e)
        {
            Button btn = sender as Button;
            btn.Size = LargeSize;
            btn.Font = LargeFont;
        }

        // Shrink the button.
        private void flp_MouseLeave(object sender, EventArgs e)
        {
            Button btn = sender as Button;
            btn.Size = SmallSize;
            btn.Font = SmallFont;
        }

        // Display the CheckBox's current state.
        private void checkBox1_CheckStateChanged(object sender, EventArgs e)
        {
            CheckBox chk = sender as CheckBox;
            lb_checkbox_CheckState.Text = "CheckState :    " + chk.CheckState.ToString();
        }

        // True if we should ignore check change events.
        private bool IgnoreCheckChangeEvents = false;

        // Select or deselect all CheckBoxes.
        private void chkMeals_CheckStateChanged(object sender, EventArgs e)
        {
            if (IgnoreCheckChangeEvents)
            {
                return;
            }

            if (chkMeals.CheckState == CheckState.Indeterminate)
            {
                chkMeals.CheckState = CheckState.Unchecked;
            }

            CheckBox[] meal_boxes = { chkBreakfast, chkLunch, chkDinner };
            IgnoreCheckChangeEvents = true;
            foreach (CheckBox chk in meal_boxes)
            {
                chk.Checked = chkMeals.Checked;
            }
            IgnoreCheckChangeEvents = false;
        }

        // The user changed a meal type selection.
        // Update the chkMeals CheckBox.
        private void chkMealType_CheckedChanged(object sender, EventArgs e)
        {
            if (IgnoreCheckChangeEvents)
            {
                return;
            }

            // See how many meals are selected.
            int num_selected = 0;
            CheckBox[] meal_boxes = { chkBreakfast, chkLunch, chkDinner };
            foreach (CheckBox chk in meal_boxes)
            {
                if (chk.Checked)
                {
                    num_selected++;
                }
            }

            // Set the chkMeals CheckBox appropriately.
            IgnoreCheckChangeEvents = true;
            if (num_selected == 3)
                chkMeals.CheckState = CheckState.Checked;
            else if (num_selected == 0)
                chkMeals.CheckState = CheckState.Unchecked;
            else
                chkMeals.CheckState = CheckState.Indeterminate;
            IgnoreCheckChangeEvents = false;
        }

        private void button15_Click(object sender, EventArgs e)
        {
            Close();
        }

        // Decrease the form's Opacity.
        private void timer1_Tick(object sender, EventArgs e)
        {
            Opacity -= 0.10;
            if (Opacity <= 0)
            {
                Close();
            }
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            // Start the fade out Timer.
            timer1.Enabled = true;

            // Only allow close after fading is done.
            e.Cancel = (Opacity > 0);
        }

        private void bt_accept_button_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了\tAccept Button\n";
        }

        private void bt_cancel_button_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了\tCancel Button\n";
        }

        private void button35_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "此按鈕之圖片  有  去背景效果\n";
        }

        private void button36_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "此按鈕之圖片  無  去背景效果\n";
        }

        private void button37_Click(object sender, EventArgs e)
        {
        }

        private void button38_Click(object sender, EventArgs e)
        {
            MainForm.Instance().ShowForm();//顯示訊息表單
        }

        private void button39_Click(object sender, EventArgs e)
        {
            MainForm.Instance().CloseForm();//隱藏訊息表單
        }

        private void button40_Click(object sender, EventArgs e)
        {
            foreach (Control cont in this.Controls)
            {
                richTextBox1.Text += "取得控件 : " + cont.Name.ToString() + "\tText : " + cont.Text + "\tType : " + cont.GetType().ToString() + "\n";
            }
        }

        private void button41_Click(object sender, EventArgs e)
        {
            //遍歷所有控件
            browse_all_controls(this.Controls);
        }

        public void browse_all_controls(Control.ControlCollection cc)
        {
            foreach (Control c in cc)  //撈出所有控件
            {
                richTextBox1.Text += c.GetType().Name;

                if (c.GetType().Name == "Button")   //判斷是否為 Button 控件
                {
                    richTextBox1.Text += "\t" + ((Button)c).Text + " " + ((Button)c).Size.Width.ToString() + " X " + ((Button)c).Size.Height.ToString();

                    if (((Button)c).Tag != null)
                    {
                        richTextBox1.Text += "\t" + ((Button)c).Tag.ToString().ToString();
                    }
                }
                richTextBox1.Text += "\n";
            }
        }

        private void button42_Click(object sender, EventArgs e)
        {
            //透明的Form背景
            this.TransparencyKey = Color.Red;
            this.BackColor = this.TransparencyKey;
        }

        private void button43_Click(object sender, EventArgs e)
        {
            //透明的RichTextBox背景
            this.TransparencyKey = Color.Red;
            richTextBox1.BackColor = this.TransparencyKey;
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            if (opacity <= 1)
            {
                opacity = opacity + 0.05;
                Opacity = opacity;
            }
            else
            {
                timer2.Enabled = false;
            }
        }

        private void button45_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了 按鍵顯示訊息\n";
        }

        private void button44_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "刪除指定控件的指定事件\n";
            ClearEvent(button45, "Click");//就會清除button1對象的Click事件的所有掛接事件。
        }

        /// <summary>
        /// 刪除指定控件的指定事件
        /// </summary>
        /// <param name="control"></param>
        /// <param name="eventname"></param>
        public void ClearEvent(System.Windows.Forms.Control control, string eventname)
        {
            if (control == null)
            {
                return;
            }
            if (string.IsNullOrEmpty(eventname))
            {
                return;
            }

            BindingFlags mPropertyFlags = BindingFlags.Instance | BindingFlags.Public | BindingFlags.Static | BindingFlags.NonPublic;
            BindingFlags mFieldFlags = BindingFlags.Static | BindingFlags.NonPublic;
            Type controlType = typeof(System.Windows.Forms.Control);
            PropertyInfo propertyInfo = controlType.GetProperty("Events", mPropertyFlags);
            EventHandlerList eventHandlerList = (EventHandlerList)propertyInfo.GetValue(control, null);
            FieldInfo fieldInfo = (typeof(System.Windows.Forms.Control)).GetField("Event" + eventname, mFieldFlags);
            Delegate d = eventHandlerList[fieldInfo.GetValue(control)];

            if (d == null)
            {
                return;
            }
            EventInfo eventInfo = controlType.GetEvent(eventname);

            foreach (Delegate dx in d.GetInvocationList())
            {
                eventInfo.RemoveEventHandler(control, dx);
            }
        }

        private void button46_Click(object sender, EventArgs e)
        {
            //遍歷窗體找某一控件
            //C#遍歷窗體控件
            string find_ctrl = "button15";
            ForeachFormControls(find_ctrl);
        }

        /// <summary>
        /// Winform C#遍歷窗體控件
        /// </summary>
        /// <param name="ctrlName">控件名稱</param>
        public void ForeachFormControls(string ctrlName)
        {
            foreach (Control ctrl in this.Controls)
            {
                if (ctrl is Panel)
                {
                    //相關操作代碼
                    ctrl.BackColor = Color.Aquamarine;
                }
                else if (ctrl is Button)
                {
                    ctrl.ForeColor = Color.RoyalBlue;
                }
                else if (ctrl is TextBox)
                {
                    ctrl.Text = null;
                }

                //根據控件名稱找某個控件
                if (ctrl.Name.Equals(ctrlName))
                {
                    //ctrl.Name = string.Empty;
                    ctrl.BackColor = Color.Red;
                    richTextBox1.Text += "找到控件 : " + ctrlName + "\n";
                }
            }
        }

        private void bt_rtb_info_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Bounds = " + richTextBox1.Bounds.ToString() + "\n";

            richTextBox1.Text += "左上點座標 = (x_st, y_st) = (Left, Top)\n";
            richTextBox1.Text += "x_st = Left = " + richTextBox1.Left.ToString() + "\n";
            richTextBox1.Text += "y_st = Top = " + richTextBox1.Top.ToString() + "\n";

            richTextBox1.Text += "右下點座標 = (x_sp, y_sp) = (x_st + W, y_st + H) = (Right, Bottom)\n";
            richTextBox1.Text += "x_sp = Right = " + richTextBox1.Right.ToString() + "\n";
            richTextBox1.Text += "y_sp = Bottom = " + richTextBox1.Bottom.ToString() + "\n";

            richTextBox1.Text += "BackColor = " + richTextBox1.BackColor.ToString() + "\n";

            richTextBox1.Text += "Size = " + richTextBox1.Size.ToString() + "\n";
            richTextBox1.Text += "ClientSize = " + richTextBox1.ClientSize.ToString() + "\n";
        }

        private void bt_help_Click(object sender, EventArgs e)
        {
            Help.ShowHelp(this, "help.hlp");
        }

        private void bt_about_Click(object sender, EventArgs e)
        {
            // Show About dialog
            AboutForm form = new AboutForm();

            form.ShowDialog();
        }

        //在winform中查找控件
        private Control findControl(Control control, string controlName)
        {
            Control c1;
            foreach (Control c in control.Controls)
            {
                if (c.Name == controlName)
                {
                    return c;
                }
                else if (c.Controls.Count > 0)
                {
                    c1 = findControl(c, controlName);
                    if (c1 != null)
                    {
                        return c1;
                    }
                }
            }
            return null;
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //在winform中查找控件

            //在winform中查找控件

            //調用
            for (int i = 1; i <= 5; i++)
            {
                string _box = "button" + i.ToString();
                Button btn = (Button)this.findControl(this, _box);

                btn.BackColor = Color.Pink;
                //tb.Text = i.ToString();


                richTextBox1.Text += "i = " + i.ToString() + "\n";
            }

        }

        [DllImportAttribute("user32.dll")]
        private extern static bool ReleaseCapture();
        [DllImportAttribute("user32.dll")]
        private extern static int SendMessage(IntPtr handle, int m, int p, int h);

        private void bt_move_form_MouseDown(object sender, MouseEventArgs e)
        {
            //由控件移動窗體
            if (e.Button == MouseButtons.Left)
            {
                this.Cursor = Cursors.SizeAll;
                ReleaseCapture();
                SendMessage(this.Handle, 0xA1, 0x2, 0);
                this.Cursor = Cursors.Default;
            }
        }

        private void bt_move_control_MouseDown(object sender, MouseEventArgs e)
        {
            //控件在窗體內移動
            if (e.Button == MouseButtons.Left)
            {
                this.Cursor = Cursors.SizeAll;
                ReleaseCapture();
                SendMessage(this.bt_move_control.Handle, 0xA1, 0x2, 0); //只有這行不一樣
                this.Cursor = Cursors.Default;
            }


        }

        private void bt_move_form_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "由控件移動窗體\n";
        }

        private void bt_move_control_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "控件在窗體內移動\n";
        }

        private void button33_Click(object sender, EventArgs e)
        {

        }

        private void button34_Click(object sender, EventArgs e)
        {

        }

        private void button47_Click(object sender, EventArgs e)
        {

        }

        private void button48_Click(object sender, EventArgs e)
        {

        }

        private void button49_Click(object sender, EventArgs e)
        {

        }

        private void button50_Click(object sender, EventArgs e)
        {

        }

        /* 找panel1內的控件
        /// <summary>
　　    /// C#遍歷子控件
　　    /// </summary>
　　    /// <param name="ctrlName">控件名稱</param>
　　    public void ForeachPanelControls(string ctrlName)
　　    {
　　　　    foreach (Control ctrl in panel1.Controls)
　　　　    {
　　　　　　    if (ctrl is Button)
　　　　　　    {
　　　　　　　　    if (ctrl.Name.Equals(ctrlName))
　　　　　　　　　　    ctrl.ForeColor = Color.RoyalBlue;
　　　　　　　　    else
　　　　　　　　　　    ctrl.ForeColor = Color.SkyBlue;
　　　　　　    }
　　　　　　    else if (ctrl is TextBox)
　　　　　　    {
　　　　　　　　    if (ctrl.Name.Equals(ctrlName))
　　　　　　　　　　    ctrl.Name = "當前值";
　　　　　　　　    else
　　　　　　　　　　    ctrl.Text = null;
　　　　　　    }
　　　　    }
　　    }
        */

        /* 找chekbox內的控件
        private void ForeachCheckBox(Control ctrls, bool currVal)
        {
            CheckBox cb;
            foreach (Control ctrl in ctrls.Controls)
            {
                if (ctrl is CheckBox)
                {
                    cb = (CheckBox)ctrl;
                    cb.Checked = currVal;
                }
            }
        }
        //same
        private void ForeachCheckBoxes(Control ctrls, bool currVal)
        {
            CheckBox cb;
            foreach (Control ctrl in ctrls.Controls.OfType<CheckBox>())
            {
                cb = (CheckBox)ctrl;
                cb.Checked = currVal;
            }
        }
        */
    }

    class MyRecordControlClass
    {
        //(1).声明结构,只记录窗体和其控件的初始位置和大小。
        public struct controlInfo
        {
            public string name;
            public string text;

            public int index;
            public int x_st;
            public int y_st;
            /*
            public int cx;
            public int cy;
            public int r;
            public int width;
            */
            public int Left;
            public int Top;
            public int Width;
            public int Height;
            public bool enable;
            public bool visible;

        }

        public List<controlInfo> control_data = new List<controlInfo>();

        int ctrlNo = 0;//1;
        //(3). 创建两个函数
        //(3.1)记录窗体和其控件的初始位置和大小,
        int index = 0;
        public void recordAllControls(Control mForm)
        {
            controlInfo ctrl_info;
            //mForm.
            ctrl_info.name = mForm.Name;
            ctrl_info.text = mForm.Text;
            ctrl_info.x_st = mForm.Location.X;
            ctrl_info.y_st = mForm.Location.Y;
            ctrl_info.index = index;
            index++;
            ctrl_info.Left = mForm.Left;
            ctrl_info.Top = mForm.Top;
            ctrl_info.Width = mForm.Width;
            ctrl_info.Height = mForm.Height;
            ctrl_info.enable = mForm.Enabled;
            ctrl_info.visible = mForm.Visible;
            control_data.Add(ctrl_info);   //第一个为"窗体本身",只加入一次即可

            AddControl(mForm);//窗体内其余控件还可能嵌套控件(比如panel),要单独抽出,因为要递归调用
        }

        private void AddControl(Control ctl)
        {
            foreach (Control c in ctl.Controls)
            {  //**放在这里，是先记录控件的子控件，后记录控件本身
                //if (c.Controls.Count > 0)
                //    AddControl(c);//窗体内其余控件还可能嵌套控件(比如panel),要单独抽出,因为要递归调用
                controlInfo ctrl_info;
                ctrl_info.name = c.Name;
                ctrl_info.text = c.Text;
                ctrl_info.x_st = c.Location.X;
                ctrl_info.y_st = c.Location.Y;
                ctrl_info.index = index;
                index++;
                ctrl_info.Left = c.Left;
                ctrl_info.Top = c.Top;
                ctrl_info.Width = c.Width;
                ctrl_info.Height = c.Height;
                ctrl_info.enable = c.Enabled;
                ctrl_info.visible = c.Visible;

                control_data.Add(ctrl_info);

                //**放在这里，是先记录控件本身，后记录控件的子控件
                if (c.Controls.Count > 0)
                {
                    AddControl(c);//窗体内其余控件还可能嵌套控件(比如panel),要单独抽出,因为要递归调用
                }
            }
        }

        //(3.2)控件自适应大小,
        public void controlSizeChange(Control mForm)
        {
            //if (ctrlNo == 0)
            { //*如果在窗体的Form1_Load中，记录控件原始的大小和位置，正常没有问题，但要加入皮肤就会出现问题，因为有些控件如dataGridView的的子控件还没有完成，个数少
                //*要在窗体的Form1_SizeChanged中，第一次改变大小时，记录控件原始的大小和位置,这里所有控件的子控件都已经形成
                controlInfo ctrl_info;
                //cR.Left = mForm.Left; cR.Top = mForm.Top; cR.Width = mForm.Width; cR.Height = mForm.Height;
                ctrl_info.name = mForm.Name;
                ctrl_info.text = mForm.Text;
                ctrl_info.x_st = mForm.Location.X;
                ctrl_info.y_st = mForm.Location.Y;
                ctrl_info.index = index;
                index++;
                ctrl_info.Left = 0;
                ctrl_info.Top = 0;
                ctrl_info.Width = mForm.PreferredSize.Width;
                ctrl_info.Height = mForm.PreferredSize.Height;
                ctrl_info.enable = mForm.Enabled;
                ctrl_info.visible = mForm.Visible;

                control_data.Add(ctrl_info);   //第一个为"窗体本身",只加入一次即可
                AddControl(mForm);//窗体内其余控件可能嵌套其它控件(比如panel),故单独抽出以便递归调用
            }
            float wScale = (float)mForm.Width / (float)control_data[0].Width;//新旧窗体之间的比例，与最早的旧窗体
            float hScale = (float)mForm.Height / (float)control_data[0].Height;//.Height;

            AutoScaleControl(mForm, wScale, hScale);//窗体内其余控件还可能嵌套控件(比如panel),要单独抽出,因为要递归调用
        }

        private void AutoScaleControl(Control ctl, float wScale, float hScale)
        {
            int ctrLeft0, ctrTop0, ctrWidth0, ctrHeight0;
            //int ctrlNo = 1;//第1个是窗体自身的 Left,Top,Width,Height，所以窗体控件从ctrlNo=1开始
            foreach (Control c in ctl.Controls)
            { //**放在这里，是先缩放控件的子控件，后缩放控件本身

                //if (c.Name != "button2")
                //  continue;

                c.Size = new Size(c.Size.Width / 2, c.Size.Height / 2);
                //c.Size.Width = c.Size.Width / 2;
                //c.Size.Height = c.Size.Height / 2;


                /*

                //if (c.Controls.Count > 0)
                //   AutoScaleControl(c, wScale, hScale);//窗体内其余控件还可能嵌套控件(比如panel),要单独抽出,因为要递归调用
                ctrLeft0 = control_data[ctrlNo].Left;
                ctrTop0 = control_data[ctrlNo].Top;
                ctrWidth0 = control_data[ctrlNo].Width;
                ctrHeight0 = control_data[ctrlNo].Height;
                //c.Left = (int)((ctrLeft0 - wLeft0) * wScale) + wLeft1;//新旧控件之间的线性比例
                //c.Top = (int)((ctrTop0 - wTop0) * h) + wTop1;

                //c.Left = (int)((ctrLeft0) * wScale);//新旧控件之间的线性比例。控件位置只相对于窗体，所以不能加 + wLeft1
                //c.Top = (int)((ctrTop0) * hScale);//
                //c.Width = (int)(ctrWidth0 * wScale);//只与最初的大小相关，所以不能与现在的宽度相乘 (int)(c.Width * w);
                //c.Height = (int)(ctrHeight0 * hScale);//
                c.Width = (int)(ctrWidth0/2);//只与最初的大小相关，所以不能与现在的宽度相乘 (int)(c.Width * w);
                c.Height = (int)(ctrHeight0/2);//

                ctrlNo++;//累加序号
                //**放在这里，是先缩放控件本身，后缩放控件的子控件
                //if (c.Controls.Count > 0)
                    //AutoScaleControl(c, wScale, hScale);//窗体内其余控件还可能嵌套控件(比如panel),要单独抽出,因为要递归调用
               */
            }
        }
    }
}
