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
            show_item_location();
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
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
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            pictureBox1.Size = new Size(500, 300);
            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            richTextBox1.Size = new Size(500, 690 - 310);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0 + 310);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(960, 750);
            this.Text = "vcs_FormSendData";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            f2.SetupForm2Data = "父告訴子一件事~~~~~~~";
            f2.setForm2Value();
        }

        //------------------------------------------------------------  # 60個

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

        //------------------------------------------------------------  # 60個

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

        //------------------------------------------------------------  # 60個

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

        //------------------------------------------------------------  # 60個

        private void button5_Click(object sender, EventArgs e)
        {
            //開啟新表單, 並傳遞資料
            string data = "This is a lion-mouse.";

            if (string.IsNullOrEmpty(data))
            {
                MessageBox.Show("資料不能空白，請重新輸入");
                return;
            }

            Form7 f7 = new Form7(data);
            //f7.Show();
            //this.Hide();//隱藏窗體

            //子表單關閉時 回傳給父表單訊息
            if (f7.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "子表單回傳 OK\n";
            }
            else
            {
                richTextBox1.Text += "子表單回傳 Cancel\n";
            }
        }

        //------------------------------------------------------------  # 60個

        private Form3 frm3 = null;
        private void button6_Click(object sender, EventArgs e)
        {
            //Form1之 button6的「Modifiers」屬性變更為“public”，以供Form3存取。
            //將Form1傳入Form3中
            frm3 = new Form3(this);
            //frm3.ShowDialog();
            frm3.Show();
        }

        //------------------------------------------------------------  # 60個

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

        //------------------------------------------------------------  # 60個

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

        //------------------------------------------------------------  # 60個

        private void button9_Click(object sender, EventArgs e)
        {
            //截圖傳至新表單 1
            ShowControlImage(this);

            ShowControlImage(button6);
        }

        private void ShowControlImage(Control ctl)
        {
            Bitmap bm = GetControlImage(ctl);
            Form8_NewPicture frm = new Form8_NewPicture();
            frm.BackgroundImage = bm;
            frm.ClientSize = bm.Size;
            frm.ShowDialog();
        }

        // Return a Bitmap holding an image of the control.
        private Bitmap GetControlImage(Control ctl)
        {
            Bitmap bm = new Bitmap(ctl.Width, ctl.Height);
            ctl.DrawToBitmap(bm, new Rectangle(0, 0, ctl.Width, ctl.Height));
            return bm;
        }

        //------------------------------------------------------------  # 60個

        private void button10_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button11_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button12_Click(object sender, EventArgs e)
        {
            //傳圖至新表單

            string filename = @"D:\_git\vcs\_1.data\______test_files1\bear.jpg";
            Bitmap bm = (Bitmap)Bitmap.FromFile(filename);

            Form8_NewPicture frm = new Form8_NewPicture();
            frm.BackgroundImage = bm;
            frm.ClientSize = bm.Size;
            frm.ShowDialog();
        }

        //------------------------------------------------------------  # 60個

        private void button13_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button14_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button15_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button16_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button17_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button18_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button19_Click(object sender, EventArgs e)
        {

        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個



/*

frm.DrawToBitmap(whole_form, new Rectangle(0, 0, frm.Width, frm.Height));

Point origin = frm.PointToScreen(new Point(0, 0));

*/
