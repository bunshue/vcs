

自己繪製bitmap圖片保存,生成ico文件或者對象
今天回答一個問題的時候的隨筆
 

Bitmap bit = new Bitmap(100, 30);
Graphics g = Graphics.FromImage(bit);
SolidBrush sb = new SolidBrush(Color.Blue);
Rectangle rg = new Rectangle(new Point(0, 0), bit.Size);
g.FillRectangle(sb, rg);
g.DrawString("測試測試呵呵", this.Font, new SolidBrush(Color.White), new PointF(0, 0));
bit.Save("d://123.bmp");//保存下來這個可以看生成的圖片 
                
                

vcs
Form2的元件的Modifiers要改成Internal, 預設為private

//char * wday[] = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"};
在預設的情況下，C# 不能使用指標，若要用指標的話，要在編譯器設定中啟用 unsafe 模式才行。



共用事件範例	WinEventHandler

            Color cl = Color.Red;
            panel1.BackColor = cl;
            richTextBox1.Text += cl.R.ToString() + "," + cl.G.ToString() + "," + cl.B.ToString() + "\n";
            //txtColor.Text = ColorTranslator.ToHtml(cl).ToString();

            byte Alpha = 0xff;
            byte Red = 0x00;
            byte Green = 0xff;
            byte Blue = 0x00;

            Color cc = Color.FromArgb(Alpha, Red, Green, Blue);
            panel1.BackColor = cc;
            richTextBox1.Text += cl.R.ToString() + "," + cl.G.ToString() + "," + cl.B.ToString() + "\n";



-------------------------------------------------------------------------------------------------------------------------------------
根據內容比對檔案

using System.IO;


            StreamReader sr1 = new StreamReader(textBox1.Text);		//創建StreamReader對象
            StreamReader sr2 = new StreamReader(textBox2.Text);		//創建StreamReader對象
            if (object.Equals(sr1.ReadToEnd(), sr2.ReadToEnd()))	//讀取文件內容並判斷
            {
                MessageBox.Show("兩個檔案相同");
            }
            else
            {
                MessageBox.Show("兩個檔案不相同");
            }
            
-------------------------------------------------------------------------------------------------------------------------------------
建立臨時檔案

            FolderBrowserDialog P_FolderBrowserDialog = new FolderBrowserDialog();	//選擇資料夾
            if (P_FolderBrowserDialog.ShowDialog() == DialogResult.OK)	//選擇資料夾
            {
                File.Create(P_FolderBrowserDialog.SelectedPath + "\\" + DateTime.Now.ToString("yyyyMMddhhmmss") + ".txt");//創建文件
            }


-------------------------------------------------------------------------------------------------------------------------------------
計算時間間隔
dtpicker_first dtpicker_second 為DateTimePicker
            MessageBox.Show("間隔 "+
                DateAndTime.DateDiff(	//使用DateDiff方法獲取日期間隔
                DateInterval.Day, dtpicker_first.Value, dtpicker_second.Value,
                FirstDayOfWeek.Sunday, FirstWeekOfYear.Jan1).ToString()+" 天", "間隔時間");






-------------------------------------------------------------------------------------------------------------------------------------
        //一行一行讀取純文字檔案中的內容
        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                openFileDialog1.ShowDialog();
                textBox1.Text = openFileDialog1.FileName;
                StreamReader SReader = new StreamReader(textBox1.Text, Encoding.Default);
                string strLine = string.Empty;
                while ((strLine = SReader.ReadLine()) != null)
                {
                    textBox2.Text += strLine + Environment.NewLine;
                }
            }
            catch { }
        }





-------------------------------------------------------------------------------------------------------------------------------------
使用MD5加密

using System.Security.Cryptography; //for MD5

        public string Encrypt(string strPwd)
        {
            MD5 md5 = new MD5CryptoServiceProvider();   //創建MD5對象
            byte[] data = System.Text.Encoding.Default.GetBytes(strPwd);//將字串編碼為一個Byte序列
            byte[] md5data = md5.ComputeHash(data);//計算dataByte的Hash值
            md5.Clear();    //清空MD5對象
            string str = "";//定義一個變量，用來記錄加密後的密碼
            for (int i = 0; i < md5data.Length - 1; i++)//遍歷byte數組
            {
                str += md5data[i].ToString("x").PadLeft(2, '0');//對遍歷到的Byte進行加密
            }
            return str;//返回得到的加密字串
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string P_str_Code = "ABCDEFG";
            richTextBox1.Text += "使用MD5加密後的結果為：" + Encrypt(P_str_Code) + "\n";
        }






-------------------------------------------------------------------------------------------------------------------------------------
計算GB MB KB

        const int GB = 1024 * 1024 * 1024;//定義GB的計算常量
        const int MB = 1024 * 1024;//定義MBW的計算常量
        const int KB = 1024;//定義KB的計算常量
        public string ByteConversionGBMBKB(Int64 KSize)
        {
            if (KSize / GB >= 1)
                return (Math.Round(KSize / (float)GB, 2)).ToString() + "GB";
            else if (KSize / MB >= 1)
                return (Math.Round(KSize / (float)MB, 2)).ToString() + "MB";
            else if (KSize / KB >= 1)
                return (Math.Round(KSize / (float)KB, 2)).ToString() + "KB";
            else
                return KSize.ToString() + "Byte";//顯示Byte值
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += ByteConversionGBMBKB(Convert.ToInt64(textBox1.Text)) + "\n";
        }






-------------------------------------------------------------------------------------------------------------------------------------

程式只能同時運行一個  在Form1_Load加入:

        private void Form1_Load(object sender, EventArgs e)
        {
            bool Exist;//定義一個bool變量 用來表示是否已經運行
            //創建Mutex互斥對象
            System.Threading.Mutex newMutex = new System.Threading.Mutex(true, "僅一次", out Exist);
            if (Exist)//如果沒有運行
            {
                newMutex.ReleaseMutex();//運行新窗体
            }
            else
            {
                MessageBox.Show("本程式一次只能運行一個實例！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);//彈出提示信息
                this.Close();//關閉當前窗体
            }

        }
        






-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------








-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------








-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------








-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------










-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------









-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------









-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------








-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------





