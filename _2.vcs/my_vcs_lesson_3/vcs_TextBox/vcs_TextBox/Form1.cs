using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_TextBox
{
    public partial class Form1 : Form
    {
        TextBox RightKeyCarte;//聲明一個自定義類CustomTextBoxGroup的對象
        TextBox NoStiky = new CustomTextBoxGroup3();//聲明一個自定義類CustomTextBoxGroup的對象

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            textBox1.ShortcutsEnabled = false;   // 不啟用快速鍵, 限制 TextBox 上不使用快速鍵與滑鼠右鍵表單
            textBox_use_scrollbar.ScrollBars = ScrollBars.Both;

            // Register the TextChanged event handler.
            textBox2.TextChanged += textBox2_TextChanged;
            textBox2.Multiline = true;
            textBox2.ScrollBars = ScrollBars.None;

            // Make the TextBox fit its initial text.
            AutoSizeTextBox(textBox2);

            this.AcceptButton = button5;            //在表單按enter就執行button5按鈕的動作

            //製作一個加上底線的TextBox  在文字框下劃一條底線
            TextBox goal = new CustomTextBoxGroup();//定義一個TextBox對像goal
            goal.Parent = this;//獲取或設置自定義TextBox控件的父容器
            goal.Text = "在文字框下劃一條底線";
            goal.Size = new Size(200, 40);
            goal.BackColor = Color.Pink;
            goal.Location = new Point(470, 500);
            this.Controls.Add(goal);//向窗體中添加自定義TextBox控件goal

            this.RightKeyCarte = new CustomTextBoxGroup2();//實例化該類的對象
            this.RightKeyCarte.Parent = this; //設定自定義控件的父容器為當前窗口
            RightKeyCarte.Text = "禁止使用滑鼠右鍵";
            RightKeyCarte.Location = new Point(470, 550);

            this.Controls.Add(this.RightKeyCarte);//在當前窗體中添加自定義控件

            lb_CustomTextBoxGroup3.Location = new Point(12, 650);
            this.NoStiky.Parent = this;//設定自定義控件的父容器為當前窗口
            NoStiky.Location = new Point(12, 650 + 30);
            this.Controls.Add(this.NoStiky);//在當前窗體中添加自定義控件

            textBox10.GotFocus += new EventHandler(textBox10_GotFocus);
            textBox10.LostFocus += new EventHandler(textBox10_LostFocus);
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            int W = 300;
            int H = 160;

            groupBox1.Size = new Size(W, H);
            groupBox4.Size = new Size(W, H);
            groupBox6.Size = new Size(W, H);
            groupBox8.Size = new Size(W, H * 2 / 3);

            groupBox1.Location = new Point(x_st + dx * 3 + 100, y_st + dy * 0);
            groupBox8.Location = new Point(x_st + dx * 5 + 0, y_st + dy * 0);

            groupBox4.Location = new Point(x_st + dx * 3 + 100, y_st + dy * 2 + 50);
            groupBox6.Location = new Point(x_st + dx * 5 + 0, y_st + dy * 2 + 50);

            richTextBox2.Size = new Size(400, 300);
            richTextBox2.Location = new Point(x_st + dx * 3 + 100, y_st + dy * 4 + 50 * 2);
            bt_clear.Location = new Point(richTextBox2.Location.X + richTextBox2.Size.Width - bt_clear.Size.Width, richTextBox2.Location.Y + richTextBox2.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1420, 800);
            this.Text = "vcs_TextBox";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox2.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            // 限制 TextBox只能輸入十六進位碼、Backspace、Enter
            // e.KeyChar == (Char)48 ~ 57 -----> 0~9
            // e.KeyChar == (Char)8 -----------> Backspace
            // e.KeyChar == (Char)13-----------> Enter            
            if ((e.KeyChar >= (Char)48 && e.KeyChar <= (Char)57) || ((e.KeyChar >= 'A') && (e.KeyChar <= 'F')) || ((e.KeyChar >= 'a') && (e.KeyChar <= 'f')) || (e.KeyChar == (Char)13) || (e.KeyChar == (Char)8))
            {
                e.Handled = false;  //未處理, 表示要顯示出來
            }
            else
            {
                e.Handled = true;   //已處理, 表示不顯示出來
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox1.Text.Length <= 0)
            {
                label2.Text = "未輸入數字";
            }
            else
            {
                string input = textBox1.Text; ;
                double output = 0;
                byte value = 0;
                for (int i = 0; i < input.Length; i++)
                {
                    if ((input[i] >= (Char)48 && input[i] <= (Char)57))
                    {
                        value = (byte)(input[i] - 48);

                    }
                    else if ((input[i] >= 'A') && (input[i] <= 'F'))
                    {
                        value = (byte)(input[i] - 'A' + 10);
                    }
                    else if ((input[i] >= 'a') && (input[i] <= 'f'))
                    {
                        value = (byte)(input[i] - 'a' + 10);
                    }
                    output = output * 16 + value;
                    //MessageBox.Show("data : " + input[i] + " value : " + value);
                }
                label2.Text = "結果：" + output.ToString();
            }
        }

        //------------------------------------------------------------  # 60個

        // Make the TextBox fit its new contents.
        private void textBox2_TextChanged(object sender, EventArgs e)
        {
            AutoSizeTextBox(sender as TextBox);
        }

        // Make the TextBox fit its contents.
        private void AutoSizeTextBox(TextBox txt)
        {
            const int x_margin = 0;
            const int y_margin = 2;
            Size size = TextRenderer.MeasureText(txt.Text, txt.Font);
            txt.ClientSize =
                new Size(size.Width + x_margin, size.Height + y_margin);
        }

        //登入
        private void button5_Click(object sender, EventArgs e)
        {
            string Username;
            string Password;
            Username = tb_id.Text;	        //取得textBox的內容為名字
            Password = tb_password.Text;	//取得textBox的內容為密碼
            if (Username == "root" && Password == "123456")
                MessageBox.Show("您是合法的使用者！！");
            else
                MessageBox.Show("滾蛋！！！！");
        }

        private void button6_Click(object sender, EventArgs e)
        {
            tb_id.Clear();
            tb_password.Text = "";
        }

        //拖曳文字內容到其他TextBox ST
        //須設定 textBox7.AllowDrop = true;
        private void textBox6_MouseMove(object sender, MouseEventArgs e)
        {
            if ((e.Button & MouseButtons.Left) == MouseButtons.Left)    //是否按下滑鼠左鍵
            {
                this.Cursor = new Cursor("../../arrow.cur");    //設置滑鼠鼠標樣式
                //拖曳文字
                DragDropEffects dropEffect = this.textBox6.DoDragDrop(this.textBox6.Text, DragDropEffects.Copy | DragDropEffects.Link);
            }
        }

        private void textBox7_DragDrop(object sender, DragEventArgs e)
        {
            textBox7.Text += e.Data.GetData(DataFormats.Text).ToString();//显示拖放文本
        }

        private void textBox7_DragEnter(object sender, DragEventArgs e)
        {
            e.Effect = DragDropEffects.Copy;//设置复制操作
        }
        //拖曳文字內容到其他TextBox SP

        private void textBox9_Enter(object sender, EventArgs e)
        {
            // 如果使用者利用Tab鍵移到textBox9物件時，
            // 更換前景與背景顏色
            if (textBox9.Text != String.Empty)
            {
                textBox9.ForeColor = Color.Red;
                textBox9.BackColor = Color.Black;
                // 移動插入點(selection pointer)到最後
                textBox9.Select(textBox9.Text.Length, 0);
            }
        }

        private void textBox9_Leave(object sender, EventArgs e)
        {
            // 如果使用者利用Tab鍵離開textBox9物件時，
            // 更換前景與背景色
            textBox9.ForeColor = Color.Black;
            textBox9.BackColor = Color.White;
            textBox9.Select(0, 0);
        }

        private void textBox10_GotFocus(object sender, EventArgs e)
        {
            // 如果使用者利用Tab鍵移到textBox10物件時，
            // 更換前景與背景顏色
            if (textBox10.Text != String.Empty)
            {
                textBox10.ForeColor = Color.Red;
                textBox10.BackColor = Color.Black;
                // 移動插入點(selection pointer)到最後
                textBox10.Select(textBox10.Text.Length, 0);
            }
        }

        private void textBox10_LostFocus(object sender, EventArgs e)
        {
            // 如果使用者利用Tab鍵離開textBox10物件時，
            // 更換前景與背景色
            textBox10.ForeColor = Color.Black;
            textBox10.BackColor = Color.White;
            textBox10.Select(0, 0);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //設定多行TextBox
            textBox_multiline.Multiline = true;
            textBox_multiline.ScrollBars = ScrollBars.Vertical;
            textBox_multiline.AcceptsReturn = true;

            Size aSize = new Size(120, 150);
            textBox_multiline.Size = aSize;

            textBox_multiline.Focus();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            int i = 0;
            foreach (string line in textBox_multiline.Lines)
            {
                i++;
            }
            richTextBox2.Text += "共有 " + i + " 列文字：" + textBox_multiline.Text + "\n";
        }
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


/*
        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            // 限制 TextBox只能輸入十六進位碼、Backspace、Enter
            // e.KeyChar == (Char)48 ~ 57 -----> 0~9
            // e.KeyChar == (Char)8 -----------> Backspace
            // e.KeyChar == (Char)13-----------> Enter            
            if ((e.KeyChar >= (Char)48 && e.KeyChar <= (Char)57) || ((e.KeyChar >= 'A') && (e.KeyChar <= 'F')) || ((e.KeyChar >= 'a') && (e.KeyChar <= 'f')) || (e.KeyChar == (Char)13) || (e.KeyChar == (Char)8))
            {
                e.Handled = false;
            }
            else
            {
                e.Handled = true;
            }
        }

        private void textBox5_KeyPress(object sender, KeyPressEventArgs e)
        {
            // 限制 TextBox只能輸入十進位碼、Backspace、Enter
            // e.KeyChar == (Char)48 ~ 57 -----> 0~9
            // e.KeyChar == (Char)8 -----------> Backspace
            // e.KeyChar == (Char)13-----------> Enter            
            if ((e.KeyChar >= (Char)48 && e.KeyChar <= (Char)57) || (e.KeyChar == (Char)13) || (e.KeyChar == (Char)8))
            {
                e.Handled = false;
            }
            else
            {
                e.Handled = true;
            }
        }
        

textBox 的 KeyPress

        private void textBox2_KeyPress(object sender, KeyPressEventArgs e)
        {
            if ((e.KeyChar < 48 || e.KeyChar > 57) && e.KeyChar != 8 && e.KeyChar != 13)
            {
                e.Handled = true;
            }
            else if (e.KeyChar == 13)
            {
                int textSize = int.Parse(textBox2.Text);
                //ApplyTextSize(textSize);

                e.Handled = true;
                this.richTextBox1.Focus();
            }
        }

 C# 限定textbox只能輸入數字 
 
        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (((int)e.KeyChar < 48 | (int)e.KeyChar > 57) & (int)e.KeyChar != 8)
            {
                e.Handled = true;
            }
        }



//------------------------------------------------------------  # 60個

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == (Char)Keys.Return)						//如果按下回车键
            {
                if (textBox1.Text.Length > 8)							//如果位数大于8
                {
                    textBox1.Text = textBox1.Text.Substring(0, 8);			//获取前8位数
                }
                else
                {
                    int j = 8 - textBox1.Text.Length;						//确定增加的位数
                    for (int i = 0; i < j; i++)
                    {
                        textBox1.Text = "0" + textBox1.Text;
                    }
                }
            }
        }



KeyPress 之 e.Handled的意義

private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
{
    if (e.KeyChar == (Char)48 || e.KeyChar == (Char)49 ||
        e.KeyChar == (Char)50 || e.KeyChar == (Char)51 ||
        e.KeyChar == (Char)52 || e.KeyChar == (Char)53 ||
        e.KeyChar == (Char)54 || e.KeyChar == (Char)55 ||
        e.KeyChar == (Char)56 || e.KeyChar == (Char)57 ||
        e.KeyChar == (Char)8  || e.KeyChar == (Char)46)
    {
        e.Handled = false;  //允許textBox1物件接受按鍵
    }
    else
    {
        e.Handled = true;   //不允許textBox1物件接受按鍵
    }
	
	if (e.KeyChar == (char)8) //允许输入回退键
	{
		e.Handled = false;
	}
	else
	{
		e.Handled = true;//为true时表示已经处理了事件（即不处理当前键盘事件  不接受）
	}
}

//------------------------------------------------------------  # 60個

private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
{
	if (!(e.KeyChar >= '0' && e.KeyChar <= '9'))
	{
		e.Handled = true;
	}
}
說明：這裡的textBox1，會排除0~9以外的文字，換句話說就是只顯示數字

//------------------------------------------------------------  # 60個

*/


