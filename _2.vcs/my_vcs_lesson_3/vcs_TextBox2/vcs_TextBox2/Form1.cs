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

            //使用 MaskedTextBox ST

            maskedTextBox1.Mask = "00/00/0000";
            maskedTextBox1.ValidatingType = typeof(System.DateTime);

            //使用 MaskedTextBox SP

            //設定 TextBox 屬性 ST
            textBox_property.MaxLength = 3;    //設最多只能輸入3位數
            textBox_property.ReadOnly = false;   //設為唯讀不能輸入, 改了
            textBox_property.TabIndex = 0;     //設為第一個停駐焦點
            textBox_property.Focus();    //將停駐焦點移到txtDegree
            //設定 TextBox 屬性 SP
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
            groupBox1.Size = new Size(W, H);
            groupBox2.Size = new Size(W, H);
            groupBox3.Size = new Size(W, H);
            groupBox4.Size = new Size(W, H);
            groupBox5.Size = new Size(W, H + 100);
            groupBox6.Size = new Size(W, H);
            groupBox7.Size = new Size(W, H);
            groupBox8.Size = new Size(W, H);
            groupBox9.Size = new Size(W, H);
            groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            groupBox3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            groupBox4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            groupBox5.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            groupBox6.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            groupBox7.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            groupBox8.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            groupBox9.Location = new Point(x_st + dx * 1, y_st + dy * 3);

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
            label1.Text = "TextBox只允許僅允許\n數字, Enter, Backspace, +-*/()";


            x_st = 10;
            y_st = 20;
            dx = 60;
            dy = 24;
            textBox_property.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            y_st = 60;
            lb_property0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            lb_property1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            lb_property2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            lb_property3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            lb_property0.Text = "屬性.MaxLength = 3;   //最多只能輸入3位數";
            lb_property1.Text = "屬性.ReadOnly = true; //設為唯讀不能輸入";
            lb_property2.Text = "屬性.TabIndex = 0;    //設為第一個停駐焦點";
            lb_property3.Text = "屬性.Focus();         //將停駐焦點移到此";

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

        private void textBox_check_TextChanged(object sender, EventArgs e)
        {
            try
            {
                // 將使用者輸入的數字轉換成double型別
                if (double.Parse(textBox_check.Text) < 0)
                {
                    // 如果輸入的數值小於0的話，用紅色粗體15點的大小呈現
                    textBox_check.ForeColor = Color.Red;
                    textBox_check.Font = new Font(FontFamily.GenericSansSerif, 13.0F, FontStyle.Bold);
                }
                else
                {
                    // 如果輸入的數值大於0的話，用黑色斜體12點的大小呈現
                    textBox_check.ForeColor = Color.Black;
                    textBox_check.Font = new Font(FontFamily.GenericSansSerif, 13.0F, FontStyle.Italic);
                }
            }
            catch
            {
                // 如果發生錯誤的話，就使用系統色及10點大小的刪除線加底線樣式呈現
                textBox_check.ForeColor = SystemColors.ControlText;
                textBox_check.Font = new Font(FontFamily.GenericSansSerif, 13.0F, FontStyle.Strikeout | FontStyle.Underline);
            }

        }

        private void maskedTextBox1_TypeValidationCompleted(object sender, TypeValidationEventArgs e)
        {
            if (!e.IsValidInput)
            {
                richTextBox1.Text = "資料格式錯誤 ！";
            }
            else
            {
                DateTime userDate = (DateTime)e.ReturnValue;
                if (userDate < DateTime.Now)
                {
                    richTextBox1.Text = "資料格式正確，但值不對 ！";
                    e.Cancel = true;
                }
            }

        }

        private void textBox_only_number_KeyPress(object sender, KeyPressEventArgs e)
        {
            //只允許輸入數字
            /* same
            if ((e.KeyChar != 8 && !char.IsDigit(e.KeyChar)) && e.KeyChar != 13)
            {
                //MessageBox.Show("只允許輸入數字", "操作提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
                e.Handled = true;
            }
            */
            byte asc = Convert.ToByte(e.KeyChar);
            if (asc < 48 || asc > 57)
            {
                e.Handled = true;  //不接受字元
            }
        }

        // 限制textBox中的字符輸入, 用KeyPress事件
        // 僅允許 數字, Enter, Backspace, +-*/()
        private void textBox_only_number2_KeyPress(object sender, KeyPressEventArgs e)
        {
            //如果輸入的不是數字類別，也不是回車鍵、Backspace鍵、+ - * / ( )，則textBox1_KeyPress取消該輸入
            if (!(Char.IsNumber(e.KeyChar)) && e.KeyChar != (char)13 && e.KeyChar != (char)8 && e.KeyChar != (char)40 && e.KeyChar != (char)41 && e.KeyChar != (char)42 && e.KeyChar != (char)43 && e.KeyChar != (char)45 && e.KeyChar != (char)47)
            {
                e.Handled = true;
            }
        }

        private void textBox_only_abc_KeyPress(object sender, KeyPressEventArgs e)
        {
            //只允許輸入小寫英文字母
            if (e.KeyChar < 'a' || e.KeyChar > 'z')
            {
                e.Handled = true;  //不接受字元
            }
        }

        private void textBox_name_KeyPress(object sender, KeyPressEventArgs e)
        {
            //名稱
            int word;
            word = (int)(e.KeyChar);
            if (word < 65 || word > 90) //判斷是否輸入字元為A~Z
            {
                MessageBox.Show("必須輸入A~Z的字元");
                e.Handled = true; ;//不能忽略使用者輸入的字元
                textBox_name.Clear(); //清除文字方塊內容            
            }
        }

        private void textBox_phone_KeyPress(object sender, KeyPressEventArgs e)
        {
            //電話
            int wd;
            wd = (int)(e.KeyChar);
            if (wd < 48 || wd > 57) //判斷是否輸入字元為A~Z
            {
                MessageBox.Show("必須輸入0~9的數字");
                e.Handled = true; ;//不能忽略使用者輸入的字元
            }
        }

        public bool ValidEmailAddress(string emailAddress, out string errorMessage)
        {
            // 確定e-mail address並非空白
            if (emailAddress.Length == 0)
            {
                errorMessage = "請輸入電子郵件信箱，不可以空白";
                return false;
            }

            // 確定電子郵件信箱是否含有1個 "@" 與 "." 字元
            if (emailAddress.IndexOf("@") > -1)
            {
                if (emailAddress.IndexOf(".", emailAddress.IndexOf("@")) > emailAddress.IndexOf("@"))
                {
                    errorMessage = "";
                    return true;
                }
            }

            errorMessage = "無效的電子郵件信箱";
            return false;
        }

        private void textBox_email_Validating(object sender, CancelEventArgs e)
        {
            string errorMsg;

            if (!ValidEmailAddress(textBox_email.Text, out errorMsg))
            {
                // 取消事件，並選取錯誤的文字
                e.Cancel = true;
                textBox_email.Select(0, textBox_email.Text.Length);

                // 秀出錯誤訊息
                richTextBox1.Text += errorMsg + "\n";
            }
        }

        private void textBox_email_Validated(object sender, EventArgs e)
        {
            richTextBox1.Text += "電子郵信箱格式 OK\n";

        }

        // 判斷使用者是否已輸入數字
        private bool nonNumberEntered = false;

        private void textBox_check_numbers_KeyDown(object sender, KeyEventArgs e)
        {
            // 假設使用者已輸入數字
            nonNumberEntered = false;

            // 判斷使用者是否使用鍵盤上頭的數字鍵
            if (e.KeyCode < Keys.D0 || e.KeyCode > Keys.D9)
            {
                // 判斷使用者是否使用數字盤(keypad)輸入數字
                if (e.KeyCode < Keys.NumPad0 || e.KeyCode > Keys.NumPad9)
                {
                    // 判斷使用者是否輸入退後鍵(Backspace)
                    if (e.KeyCode != Keys.Back)
                    {
                        // 因為使用者並沒有輸入數字，因此將之設為true
                        nonNumberEntered = true;
                    }
                }
            }
        }

        private void textBox_check_numbers_KeyPress(object sender, KeyPressEventArgs e)
        {
            // 判斷使用者是否已輸入數字
            if (nonNumberEntered == true)
            {
                // 因為沒有輸入數字，因此該輸入不予顯示，並提示使用者相關的訊息
                e.Handled = true;

                lb_check_numbers.Text = e.KeyChar + " 是不被允許的，" + Environment.NewLine;
                lb_check_numbers.Text += "請輸入數字或是退後鍵修正數字 !!!";
            }
            else
            {
                lb_check_numbers.Text = e.KeyChar + " 是OK的";
            }
        }
    }
}

