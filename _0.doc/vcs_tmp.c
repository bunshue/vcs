

�ۤvø�sbitmap�Ϥ��O�s,�ͦ�ico���Ϊ̹�H
���Ѧ^���@�Ӱ��D���ɭԪ��H��
 

Bitmap bit = new Bitmap(100, 30);
Graphics g = Graphics.FromImage(bit);
SolidBrush sb = new SolidBrush(Color.Blue);
Rectangle rg = new Rectangle(new Point(0, 0), bit.Size);
g.FillRectangle(sb, rg);
g.DrawString("���մ��ը���", this.Font, new SolidBrush(Color.White), new PointF(0, 0));
bit.Save("d://123.bmp");//�O�s�U�ӳo�ӥi�H�ݥͦ����Ϥ� 
                
                

vcs
Form2������Modifiers�n�令Internal, �w�]��private

//char * wday[] = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"};
�b�w�]�����p�U�AC# ����ϥΫ��СA�Y�n�Ϋ��Ъ��ܡA�n�b�sĶ���]�w���ҥ� unsafe �Ҧ��~��C



�@�Ψƥ�d��	WinEventHandler

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
�ھڤ��e����ɮ�

using System.IO;


            StreamReader sr1 = new StreamReader(textBox1.Text);		//�Ы�StreamReader��H
            StreamReader sr2 = new StreamReader(textBox2.Text);		//�Ы�StreamReader��H
            if (object.Equals(sr1.ReadToEnd(), sr2.ReadToEnd()))	//Ū����󤺮e�çP�_
            {
                MessageBox.Show("����ɮ׬ۦP");
            }
            else
            {
                MessageBox.Show("����ɮפ��ۦP");
            }
            
-------------------------------------------------------------------------------------------------------------------------------------
�إ��{���ɮ�

            FolderBrowserDialog P_FolderBrowserDialog = new FolderBrowserDialog();	//��ܸ�Ƨ�
            if (P_FolderBrowserDialog.ShowDialog() == DialogResult.OK)	//��ܸ�Ƨ�
            {
                File.Create(P_FolderBrowserDialog.SelectedPath + "\\" + DateTime.Now.ToString("yyyyMMddhhmmss") + ".txt");//�Ыؤ��
            }


-------------------------------------------------------------------------------------------------------------------------------------
�p��ɶ����j
dtpicker_first dtpicker_second ��DateTimePicker
            MessageBox.Show("���j "+
                DateAndTime.DateDiff(	//�ϥ�DateDiff��k���������j
                DateInterval.Day, dtpicker_first.Value, dtpicker_second.Value,
                FirstDayOfWeek.Sunday, FirstWeekOfYear.Jan1).ToString()+" ��", "���j�ɶ�");






-------------------------------------------------------------------------------------------------------------------------------------
        //�@��@��Ū���¤�r�ɮפ������e
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
�ϥ�MD5�[�K

using System.Security.Cryptography; //for MD5

        public string Encrypt(string strPwd)
        {
            MD5 md5 = new MD5CryptoServiceProvider();   //�Ы�MD5��H
            byte[] data = System.Text.Encoding.Default.GetBytes(strPwd);//�N�r��s�X���@��Byte�ǦC
            byte[] md5data = md5.ComputeHash(data);//�p��dataByte��Hash��
            md5.Clear();    //�M��MD5��H
            string str = "";//�w�q�@���ܶq�A�ΨӰO���[�K�᪺�K�X
            for (int i = 0; i < md5data.Length - 1; i++)//�M��byte�Ʋ�
            {
                str += md5data[i].ToString("x").PadLeft(2, '0');//��M���쪺Byte�i��[�K
            }
            return str;//��^�o�쪺�[�K�r��
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string P_str_Code = "ABCDEFG";
            richTextBox1.Text += "�ϥ�MD5�[�K�᪺���G���G" + Encrypt(P_str_Code) + "\n";
        }






-------------------------------------------------------------------------------------------------------------------------------------
�p��GB MB KB

        const int GB = 1024 * 1024 * 1024;//�w�qGB���p��`�q
        const int MB = 1024 * 1024;//�w�qMBW���p��`�q
        const int KB = 1024;//�w�qKB���p��`�q
        public string ByteConversionGBMBKB(Int64 KSize)
        {
            if (KSize / GB >= 1)
                return (Math.Round(KSize / (float)GB, 2)).ToString() + "GB";
            else if (KSize / MB >= 1)
                return (Math.Round(KSize / (float)MB, 2)).ToString() + "MB";
            else if (KSize / KB >= 1)
                return (Math.Round(KSize / (float)KB, 2)).ToString() + "KB";
            else
                return KSize.ToString() + "Byte";//���Byte��
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += ByteConversionGBMBKB(Convert.ToInt64(textBox1.Text)) + "\n";
        }






-------------------------------------------------------------------------------------------------------------------------------------

�{���u��P�ɹB��@��  �bForm1_Load�[�J:

        private void Form1_Load(object sender, EventArgs e)
        {
            bool Exist;//�w�q�@��bool�ܶq �ΨӪ�ܬO�_�w�g�B��
            //�Ы�Mutex������H
            System.Threading.Mutex newMutex = new System.Threading.Mutex(true, "�Ȥ@��", out Exist);
            if (Exist)//�p�G�S���B��
            {
                newMutex.ReleaseMutex();//�B��s���^
            }
            else
            {
                MessageBox.Show("���{���@���u��B��@�ӹ�ҡI", "����", MessageBoxButtons.OK, MessageBoxIcon.Information);//�u�X���ܫH��
                this.Close();//������e���^
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





