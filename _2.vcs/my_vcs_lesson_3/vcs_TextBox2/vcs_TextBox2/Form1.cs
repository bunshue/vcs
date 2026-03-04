using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_TextBox2
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

            //設定 TextBox 之 自動完成字串
            //設定自定義來源字串
            AutoCompleteStringCollection source = new AutoCompleteStringCollection();
            source.AddRange(new string[]
            {
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December"
            });
            tb_auto_complete1.AutoCompleteMode = AutoCompleteMode.SuggestAppend;
            //tb_auto_complete1.AutoCompleteMode = AutoCompleteMode.Suggest;
            tb_auto_complete1.AutoCompleteSource = AutoCompleteSource.CustomSource;
            tb_auto_complete1.AutoCompleteCustomSource = source;


            tb_auto_complete2.AutoCompleteMode = AutoCompleteMode.SuggestAppend;
            tb_auto_complete2.AutoCompleteSource = AutoCompleteSource.HistoryList;

            //限制輸入 ST
            textBox0.TextChanged += new EventHandler(textBox0_TextChanged);
            textBox0.KeyPress += new KeyPressEventHandler(textBox0_KeyPress);
            textBox1.TextChanged += new EventHandler(textBox1_TextChanged);
            textBox1.KeyPress += new KeyPressEventHandler(textBox1_KeyPress);
            textBox2.TextChanged += new EventHandler(textBox2_TextChanged);
            textBox2.KeyPress += new KeyPressEventHandler(textBox2_KeyPress);
            textBox0.Text = "";
            textBox1.Text = "0";
            textBox2.Text = "0";
            textBox3.Text = "0";
            textBox3.ReadOnly = true;
            //限制輸入 SP
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;
            int W = 300;
            int H = 160;

            //button
            x_st = 10;
            y_st = 10;
            dx = W + 10;
            dy = H + 10;

            groupBox0.Size = new Size(W, H);
            groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox1.Size = new Size(W, H);
            groupBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            richTextBox1.Size = new Size(300, 340);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            x_st = 10;
            y_st = 20;
            dx = 60;
            dy = 36;
            label0a.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            label1a.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            label2a.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            label3a.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            textBox0.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            textBox1.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            textBox2.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            textBox3.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            label0b.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            label1b.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            label2b.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            label3b.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            label0b.Text = "限制 1英5數";
            label1b.Text = "限制 數字";
            label2b.Text = "限制 數字";
            label3b.Text = "";


            this.Size = new Size(1380, 800);
            this.Text = "vcs_TextBox";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void textBox0_TextChanged(object sender, EventArgs e)
        {
            int Loc = textBox0.SelectionStart;   　 // 儲存目前游標位置       
            // 當字母轉成大寫指定給textBox0.Text時游標移到字串最後
            textBox0.Text = textBox0.Text.ToUpper();
            textBox0.SelectionStart = Loc;　　　　　// 將游標還原到原來位置
        }

        private void textBox0_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (textBox0.Text.Length < 6)//檢查輸入的產品編號長度是否超過六個字元
            {
                if (textBox0.SelectionStart == 0)//檢查輸入的第一個字元是否為字母
                {   //將輸入的字母轉成大寫
                    string S = e.KeyChar.ToString().ToUpper();
                    if (S.CompareTo("A") < 0 || S.CompareTo("Z") > 0)
                    {
                        // 若輸入的第一個字元不是字母,取消輸入字元不顯示,游標停在原處
                        e.Handled = true;
                    }
                }
                else　// 若輸入的字元是第2個(含)以後的字元執行此段程式碼
                {
                    if (e.KeyChar.CompareTo('0') < 0 || e.KeyChar.CompareTo('9') > 0)
                    {
                        if (e.KeyChar != '\b')//若輸入的字元非數字且不是倒退鍵
                        {
                            e.Handled = true;//取消輸入字元不顯示,游標停在原處
                        }
                    }
                }
            }
            else　　//若輸的字元的長度超過6個字元執行此區段程式碼
            {
                if (e.KeyChar != '\b')//若是倒退鍵,取消輸入字元不顯示,游標停在原處
                {
                    e.Handled = true;
                }
            }
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            try
            {
                int price = int.Parse(textBox1.Text);
                int qty = int.Parse(textBox2.Text);
                textBox3.Text = (price * qty).ToString();
            }
            catch//若輸入的資料有誤執行此空區段程式碼,不處理所發生的錯誤
            { }
        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            //若輸入的字元是非數字且不是倒退鍵 
            if ((e.KeyChar < '0' || e.KeyChar > '9') && (e.KeyChar != '\b'))
            {
                e.Handled = true;  //取消輸入字元不顯示,游標停在原處　             
            }
        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {
            try
            {
                int price = int.Parse(textBox1.Text);
                int qty = int.Parse(textBox2.Text);
                textBox3.Text = (price * qty).ToString();
            }
            catch
            { }
        }

        private void textBox2_KeyPress(object sender, KeyPressEventArgs e)
        {
            if ((e.KeyChar < '0' || e.KeyChar > '9') && (e.KeyChar != '\b'))
            {
                e.Handled = true;
            }
        }
    }
}
