using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Button2
{
    public partial class Form1 : Form
    {
        public enum SwitchState
        {
            On,
            Off
        }

        private SwitchState _state;
        public SwitchState State
        {
            get
            {
                return _state;
            }
            set
            {
                if (_state == value)
                    return;
                _state = value;
                AdjustOnOffButton();
            }
        }

        private void AdjustOnOffButton()
        {
            switch (State)
            {
                case SwitchState.On:
                    OnOffButton.Dock = DockStyle.Top;
                    break;
                case SwitchState.Off:
                    OnOffButton.Dock = DockStyle.Bottom;
                    break;
                default:
                    break;
            }
        }

        public void Toggle()
        {
            State = State == SwitchState.On ? SwitchState.Off : SwitchState.On;
        }

        public Form1()
        {
            InitializeComponent();
            State = SwitchState.Off;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();            
        }

        void show_item_location()
        {
            //button1.BackgroundImage = new Bitmap(@"D:\_git\vcs\_1.data\______test_files1\__pic\_logo\csharp-programming_210700275.jpg.ashx.jpg");
            //button1.BackgroundImageLayout = ImageLayout.None;
            button1.Image = new Bitmap(@"D:\_git\vcs\_1.data\______test_files1\__pic\_logo\csharp-programming_210700275.jpg.ashx.jpg");
            //button1.ImageAlign = ContentAlignment.BottomRight;

            button6.Image = new Bitmap(@"D:\_git\vcs\_1.data\______test_files1\__pic\_logo\csharp-programming_210700275.jpg.ashx.jpg");
            button6.ImageAlign = ContentAlignment.MiddleCenter;
            button6.MouseMove += new MouseEventHandler(button6_MouseMove);
            button6.MouseLeave += new EventHandler(button6_MouseLeave);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //this.Size = new Size(1220, 800);
            this.Text = "vcs_Button2";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void button6_MouseMove(object sender, MouseEventArgs e)
        {
            button6.ImageAlign = ContentAlignment.MiddleLeft;
        }

        void button6_MouseLeave(object sender, EventArgs e)
        {
            button6.ImageAlign = ContentAlignment.MiddleCenter;
        }

        private void OnOffButton_Click(object sender, EventArgs e)
        {
            Toggle();
        }

        private void Form1_SizeChanged(object sender, EventArgs e)
        {
            OnOffButton.Height = this.Height / 2;
        }

        private void bt1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Button變大\n";
            bt2.Size = new Size(bt2.Size.Width + 5, bt2.Size.Height + 5);
        }

        private void bt2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Button變大變小\n";
            bt2.Size = new Size(bt2.Size.Width + 5, bt2.Size.Height + 5);
        }

        private void bt3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Button變小\n";
            bt2.Size = new Size(bt2.Size.Width - 5, bt2.Size.Height - 5);
        }

        //在Button上畫圖
        private void button2_Paint(object sender, PaintEventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_貓咪\cat1.png";
            Bitmap bmp;//實例Bitmap對像
            bmp = new Bitmap(filename);
            Graphics g = e.Graphics;
            TextureBrush myBrush = new TextureBrush(bmp);
            g.FillRectangle(myBrush, this.ClientRectangle);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "在Button上畫圖\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            MessageBox.Show("你按了快捷键 Alt + F\n只要在Text改 快捷鍵 (&F) 即可");
        }

        //6060

        ContentAlignment image_align = ContentAlignment.TopLeft;
        private void button5_Click(object sender, EventArgs e)
        {
            if (image_align == ContentAlignment.TopLeft)
            {
                //     內容垂直靠上對齊，且水平置中對齊。
                image_align = ContentAlignment.TopCenter;
                button1.ImageAlign = image_align;
            }
            else if (image_align == ContentAlignment.TopCenter)
            {
                //     內容垂直靠上對齊，且水平靠右對齊。
                image_align = ContentAlignment.TopRight;
                button1.ImageAlign = image_align;
            }
            else if (image_align == ContentAlignment.TopRight)
            {
                //     內容垂直居中對齊，且水平靠左對齊。
                image_align = ContentAlignment.MiddleLeft;
                button1.ImageAlign = image_align;
            }
            else if (image_align == ContentAlignment.MiddleLeft)
            {
                //     內容垂直居中對齊，且水平置中對齊。
                image_align = ContentAlignment.MiddleCenter;
                button1.ImageAlign = image_align;
            }
            else if (image_align == ContentAlignment.MiddleCenter)
            {
                //     內容垂直居中對齊，且水平置中對齊。
                image_align = ContentAlignment.MiddleRight;
                button1.ImageAlign = image_align;
            }
            else if (image_align == ContentAlignment.MiddleRight)
            {
                //     內容垂直靠下對齊，且水平靠左對齊。
                image_align = ContentAlignment.BottomLeft;
                button1.ImageAlign = image_align;
            }
            else if (image_align == ContentAlignment.BottomLeft)
            {
                //     內容垂直靠下對齊，且水平置中對齊。
                image_align = ContentAlignment.BottomCenter;
                button1.ImageAlign = image_align;
            }
            else if (image_align == ContentAlignment.BottomCenter)
            {
                //     內容垂直靠下對齊，且水平靠右對齊。
                image_align = ContentAlignment.BottomRight;
                button1.ImageAlign = image_align;
            }
            else if (image_align == ContentAlignment.BottomRight)
            {
                //     內容垂直靠上對齊，且水平靠左對齊。
                image_align = ContentAlignment.TopLeft;
                button1.ImageAlign = image_align;
            }
            else
            {
                richTextBox1.Text += "XXXXXXXXXXXXXXXXXXX\n";
            }
        }

        //------------------------------------------------------------  // 60個

        int cnt = 0;
        private void button8_Click(object sender, EventArgs e)
        {
            //設定按鈕樣式 FlatStyle
            if (cnt == 0)
            {
                button8.FlatStyle = FlatStyle.Flat;
                button8.Text = "Flat";
            }
            else if (cnt == 1)
            {
                button8.FlatStyle = FlatStyle.Popup;
                button8.Text = "Popup";
            }
            else if (cnt == 2)
            {
                button8.FlatStyle = FlatStyle.Standard;
                button8.Text = "Standard";
            }
            else if (cnt == 3)
            {
                button8.FlatStyle = FlatStyle.System;
                button8.Text = "System";
            }
            cnt++;
            if (cnt > 3)
            {
                cnt = 0;
            }
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

