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
            //this.richTextBox1.Text += "父得到信息 : " + form1_data + "\n";
        }

        //使用自己建立的Form2表單
        Form2 f2 = new Form2();     //實體化Form2視窗物件
        Form5 f5 = new Form5();     //實體化Form5視窗物件

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            f2.SetupForm2Data = "父告訴子一件事~~~~~~~";
            f2.setForm2Value();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //f2.StartPosition = FormStartPosition.CenterScreen;      //設定新表單的顯示位置, 居中顯示
            //f2.StartPosition = FormStartPosition.CenterParent;
            f2.StartPosition = FormStartPosition.Manual;
            f2.Location = new Point(this.Location.X + 550, this.Location.Y);
            f2.Owner = this;
            //f2.ShowDialog();
            f2.Show();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            f5.Owner = this;

            DialogResult result = f5.ShowDialog();
            if (result == DialogResult.OK)
            {
                richTextBox1.Text += "你按了 香蕉\n";
            }
            else if (result == DialogResult.Cancel)
            {
                richTextBox1.Text += "你按了 芭樂\n";
            }
            else if (result == DialogResult.Abort)
            {
                richTextBox1.Text += "你按了 紅龍果\n";
            }
            else if (result == DialogResult.Ignore)
            {
                richTextBox1.Text += "你選擇了 " + form1_data + "\n";
            }
            else
            {
                richTextBox1.Text += "你按了 XXXXX\n";
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Form2 f2 = new Form2();//產生Form2的物件，才可以使用它所提供的Method
            //f2.Show();         //不等結束
            //f2.ShowDialog();   //要等結束
            f2.ShowDialog(this); //設定Form2為Form1的上層，並開啟Form2視窗。由於在Form1的程式碼內使用this，所以this為Form1的物件本身

            if (f2.DialogResult == System.Windows.Forms.DialogResult.OK)
            {
                //若使用者在Form2按下了OK，則進入這個判斷式
                richTextBox1.Text += "按下了" + f2.DialogResult.ToString() + "\n";
            }
            else if (f2.DialogResult == System.Windows.Forms.DialogResult.Cancel)
            {
                //若使用者在Form2按下了Cancel或者直接點選X關閉視窗，都會進入這個判斷式
                richTextBox1.Text += "按下了" + f2.DialogResult.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "按下了" + f2.DialogResult.ToString() + "\n";
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
                histoData[i] = (int)(100 * sind(i)) + 100;      //直方圖 只顯示正的數值
            }
            Form4 form4 = new Form4(histoData); //開啟表單 並把資料傳送進去
            form4.Show();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //開啟子表單並傳一張圖過去

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            Form6 f6 = new Form6();
            f6.BackgroundImage = bitmap1;
            f6.ClientSize = new Size(bitmap1.Width, bitmap1.Height);
            f6.Show();
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //截圖傳至新表單 1
            ShowControlImage(this);
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //截圖傳至新表單 2 client area
            using (Bitmap bm = GetFormImageWithoutBorders(this))
            {
                ImageForm frm = new ImageForm();
                frm.BackgroundImage = bm;
                frm.ClientSize = bm.Size;
                frm.ShowDialog();
            }

        }

        private void button11_Click(object sender, EventArgs e)
        {
            //截圖傳至新表單 3
            ShowControlImage(richTextBox1);
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //截圖傳至新表單 4

        }

        private void ShowControlImage(Control ctl)
        {
            using (Bitmap bm = GetControlImage(ctl))
            {
                ImageForm frm = new ImageForm();
                frm.BackgroundImage = bm;
                frm.ClientSize = bm.Size;
                frm.ShowDialog();
            }
        }

        // Return a Bitmap holding an image of the control.
        private Bitmap GetControlImage(Control ctl)
        {
            Bitmap bm = new Bitmap(ctl.Width, ctl.Height);
            ctl.DrawToBitmap(bm, new Rectangle(0, 0, ctl.Width, ctl.Height));
            return bm;
        }

        // Return the form's image without its borders and decorations.
        private Bitmap GetFormImageWithoutBorders(Form frm)
        {
            // Get the form's whole image.
            using (Bitmap whole_form = GetControlImage(frm))
            {
                // See how far the form's upper left corner is
                // from the upper left corner of its client area.
                Point origin = frm.PointToScreen(new Point(0, 0));
                int dx = origin.X - frm.Left;
                int dy = origin.Y - frm.Top;

                // Copy the client area into a new Bitmap.
                int wid = frm.ClientSize.Width;
                int hgt = frm.ClientSize.Height;
                Bitmap bm = new Bitmap(wid, hgt);
                using (Graphics gr = Graphics.FromImage(bm))
                {
                    gr.DrawImage(whole_form, 0, 0, new Rectangle(dx, dy, wid, hgt), GraphicsUnit.Pixel);
                }
                return bm;
            }
        }
    }
}

