using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Text.RegularExpressions;

namespace vcs_test_all_00_Control
{
    public partial class Form1 : Form
    {
        // The small and large button sizes.
        private Size SmallSize, LargeSize;
        private Font SmallFont, LargeFont;

        //移動控件 ST
        Point CPoint;//記錄滑鼠游標在父容器中的初始位置
        bool isDown = false;//判斷是否可以移動文字
        int tem_x = 0;//記錄滑鼠游標移動文字後的X位置
        int tem_y = 0;//記錄滑鼠游標移動文字後的Y位置

        int W = 0;
        int H = 0;
        //移動控件 SP

        public Form1()
        {
            InitializeComponent();

            //不同Button共用一個事件
            button6.Click += new EventHandler(button6_Click);//按下button6觸發button1_Click
            button7.Click += new EventHandler(button6_Click);//按下button7觸發button1_Click
            button8.Click += new EventHandler(button6_Click);//按下button8觸發button1_Click
            button9.Click += new EventHandler(button6_Click);//按下button9觸發button1_Click

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //移動控件 ST
            W = this.ClientSize.Width;
            H = this.ClientSize.Height - 100;
            //移動控件 SP
        }

        //移動控件 ST
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
        //移動控件 SP

        private void Form1_Load(object sender, EventArgs e)
        {
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
            MessageBox.Show(str);  //顯示結果

            // Set the small and large sizes.
            SmallSize = flp1.Size;
            LargeSize = new Size(
                (int)(1.5 * flp1.Size.Width),
                (int)(1.5 * flp1.Size.Height));

            SmallFont = flp1.Font;
            LargeFont = new Font(
                SmallFont.FontFamily,
                SmallFont.Size * 1.5f,
                FontStyle.Bold);

            lb_checkbox_CheckState.Text = "";

            // Give this button's image a transparent background.
            MakeButtonTransparent(button35);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();
        }

        // 做出 去背景 的效果
        // Give the button a transparent background.
        private void MakeButtonTransparent(Button btn)
        {
            Bitmap bm = (Bitmap)btn.Image;
            bm.MakeTransparent(bm.GetPixel(0, 0));
            //btn.Image = bm;   comment also OK
        }

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
                richTextBox1.LoadFile("C:\\______test_files\\__RW\\_rtf\\VS2013Express.rtf");
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
            button13.ClientSize = new Size(
                preferredSize.Width + (textPadding * 2),
                preferredSize.Height + (textPadding * 2));
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
            if (parent.Text == name) return parent;

            // Recursively search the parent's children.
            foreach (Control ctl in parent.Controls)
            {
                richTextBox1.Text += "檢查\t" + ctl.Name + "\t" + ctl.Text + "\n";
                Control found = FindControl(ctl, name);
                if (found != null)
                    return found;
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
            if (IgnoreCheckChangeEvents) return;

            if (chkMeals.CheckState == CheckState.Indeterminate)
                chkMeals.CheckState = CheckState.Unchecked;

            CheckBox[] meal_boxes = { chkBreakfast, chkLunch, chkDinner };
            IgnoreCheckChangeEvents = true;
            foreach (CheckBox chk in meal_boxes)
                chk.Checked = chkMeals.Checked;
            IgnoreCheckChangeEvents = false;
        }

        // The user changed a meal type selection.
        // Update the chkMeals CheckBox.
        private void chkMealType_CheckedChanged(object sender, EventArgs e)
        {
            if (IgnoreCheckChangeEvents) return;

            // See how many meals are selected.
            int num_selected = 0;
            CheckBox[] meal_boxes = { chkBreakfast, chkLunch, chkDinner };
            foreach (CheckBox chk in meal_boxes)
                if (chk.Checked) num_selected++;

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
                Close();
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            // Start the fade out Timer.
            timer1.Enabled = true;

            // Only allow close after fading is done.
            e.Cancel = (Opacity > 0);
        }

        // Validate a required field. Return true if the field is valid.
        private bool RequiredFieldIsBlank(ErrorProvider err, TextBox txt)
        {
            if (txt.Text.Length > 0)
            {
                // Clear the error.
                err.SetError(txt, "");
                return false;
            }
            else
            {
                // Set the error.
                err.SetError(txt, CamelCaseToWords(txt.Name) + " must not be blank.");
                return true;
            }
        }

        // Split a string in camelCase, removing the prefix.
        private string CamelCaseToWords(string input)
        {
            // Insert a space in front of each capital letter.
            string result = "";
            foreach (char ch in input.ToCharArray())
            {
                if (char.IsUpper(ch)) result += " ";
                result += ch;
            }

            // Find the first space and remove everything before it.
            return result.Substring(result.IndexOf(" ") + 1);
        }

        // Validate the ID code.
        private void textBox1_Validating(object sender, CancelEventArgs e)
        {
            // Check for missing value.
            if (RequiredFieldIsBlank(errorProvider1, textBox1))
            {
                e.Cancel = true;
                return;
            }

            // Check for correct format.

            //Regex regex = new Regex(@"^(\d{5}|\d{5}-\d{4})$");    //5數 或 5數-4數
            Regex regex = new Regex(@"^[A-Z]{1}[0-9]{9}$");         //1英9數

            if (regex.IsMatch(textBox1.Text))
            {
                // Clear the error.
                errorProvider1.SetError(textBox1, "OK");
            }
            else
            {
                // Set the error.
                errorProvider1.SetError(textBox1, "台灣身份證字號格式 1英9數");
                e.Cancel = true;
            }

        }

        // Validate fields.
        private void textBox2_Validating(object sender, CancelEventArgs e)
        {
            TextBox txt = sender as TextBox;
            e.Cancel = RequiredFieldIsBlank(errorProvider1, txt);
        }

        // Validate a required field. Return true if the field is valid.

        //RequiredFieldIsBlank   same
        private bool ValidateRequiredField(ErrorProvider err, TextBox txt)
        {
            if (txt.Text.Length > 0)
            {
                // Clear the error.
                err.SetError(txt, "");
                return false;
            }
            else
            {
                // Set the error.
                err.SetError(txt, CamelCaseToWords(txt.Name) + " must not be blank.");
                return true;
            }
        }

        // Validate the ID code
        private void ValidateIDCode(ErrorProvider err, TextBox txt)
        {
            // Check for missing value.
            if (ValidateRequiredField(err, txt)) return;

            // Check for correct format.

            //Regex regex = new Regex(@"^(\d{5}|\d{5}-\d{4})$");    //5數 或 5數-4數
            Regex regex = new Regex(@"^[A-Z]{1}[0-9]{9}$");         //1英9數
            if (regex.IsMatch(txt.Text))
            {
                // Clear the error.
                errorProvider1.SetError(txt, "");
            }
            else
            {
                // Set the error.
                errorProvider1.SetError(txt, "ZIP code must have format ##### or #####-####.");
            }
        }

        private void button33_Click(object sender, EventArgs e)
        {
            //richTextBox1.Text += "你按了OK\n";
            // Validate all fields.
            ValidateIDCode(errorProvider1, textBox1);
            ValidateRequiredField(errorProvider1, textBox2);

            // See if any field has an error message.
            foreach (Control ctl in Controls)
            {
                if (errorProvider1.GetError(ctl) != "")
                {
                    MessageBox.Show(errorProvider1.GetError(ctl));
                    return;
                }
            }

            richTextBox1.Text += "資料正確\nID:\t" + textBox1.Text + "\nName:\t" + textBox2.Text + "\n";

        }

        private void button34_Click(object sender, EventArgs e)
        {
            this.Close();
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

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
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

        private void button37_Click(object sender, EventArgs e)
        {
            // Show About dialog
            AboutForm form = new AboutForm();

            form.ShowDialog();
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
                    AddControl(c);//窗体内其余控件还可能嵌套控件(比如panel),要单独抽出,因为要递归调用
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
