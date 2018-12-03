



------------------------------------------------------------------------------------------------------------------------


------------------------------------------------------------------------------------------------------------------------






------------------------------------------------------------------------------------------------------------------------


------------------------------------------------------------------------------------------------------------------------






------------------------------------------------------------------------------------------------------------------------


------------------------------------------------------------------------------------------------------------------------



            Pen pen = new Pen(Color.Black, 8);
            pen.EndCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;  //EndCap�]�w �o�䵧�������|�O�ӽb�Y

            g.DrawLine(pen, 50, 400, 50, 100);  //�e�XX�b��y�b
            g.DrawLine(pen, 50, 400, 350, 400);

            pen = new Pen(Color.Blue, 6);   //���s�]�wpp���u���˦�
            //pp.DashStyle = System.Drawing.Drawing2D.DashStyle.Dot; //DashStyle�]�w�u�� �I
            //pp.StartCap = System.Drawing.Drawing2D.LineCap.RoundAnchor; //�]�w�����Y

            pen.EndCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;

            //gg.DrawLine(pp, 50, 50, 250, 250);//�u�e�@��
            g.DrawLines(pen, new Point[] {//�@���e�n�h��
            new Point(70,350),
            new Point(100,280),
            new Point(120,300),
            new Point(200,220),
            new Point(250,260),
            new Point(340,150)});




------------------------------------------------------------------------------------------------------------------------


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



------------------------------------------------------------------------------------------------------------------------


            Point[] pt = new Point[360];    //�@���}�C����360��Point
            int angle;
            int amplitude = 100;
            for (angle = 0; angle < 360; angle += 1)
            {
                pt[angle].X = angle;
                pt[angle].Y = y_positon - (int)(amplitude * Math.Sin(angle*3 * Math.PI / 180));

            }
            g.DrawLines(new Pen(Brushes.Red, 3), pt);


------------------------------------------------------------------------------------------------------------------------



            Point[] arrayPoint = new Point[20];
            p = new Pen(Color.Blue, 5);
            double zz;

            for (int i = 0; i < 20; i++)
            {
                zz = Math.Sin(Math.PI * i * 30 / 180) * 200 + 200;
                arrayPoint[i].X = i * 20;
                arrayPoint[i].Y = (int)zz;
            }
            g.DrawLines(p, arrayPoint);

------------------------------------------------------------------------------------------------------------------------

            SolidBrush brush = new SolidBrush(Color.Blue);
            Font font = new Font("�з���", 20);
            g.DrawString("�Q�n�g����r", font, brush, 20, 20);
            g.DrawString("�Q�n�g����r", font, brush, 50, 50);
            g.DrawString("�Q�n�g����r", font, brush, 80, 80);


------------------------------------------------------------------------------------------------------------------------



            // �H����ø�����i
            Graphics g = this.CreateGraphics();
            Pen p = new Pen(Color.Red, 2);
            int h = 100;
            int y1 = 100;
            double angle, y;
            float tmpy, tmpx;
            for (double x = 0; x <= 360; x++)
            {
                angle = x / 180 * Math.PI;
                y = Convert.ToDouble(y1) + Math.Sin(angle) * h;
                tmpx = Convert.ToSingle(x);
                tmpy = Convert.ToSingle(y);
                g.DrawEllipse(p, tmpx, tmpy, 1, 1); //ø�s������I
            }

            g.DrawEllipse(p, 260, 260, 100, 100); //ø�s������I

            SolidBrush sb = new SolidBrush(Color.Green);
            g.FillEllipse(sb, 360, 360, 100, 100); //ø�s������I

------------------------------------------------------------------------------------------------------------------------

            int[] x = { 0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600 };
            int[] y = { 200, 295, 368, 399, 381, 319, 228, 129, 48, 4, 8, 58, 144, 243, 331, 387, 397, 359, 282, 184, 91 };
            Bitmap bitM = new Bitmap(this.panel1.Width, this.panel1.Height);
            //MessageBox.Show("Width = " + this.panel1.Width + "  Height = " + this.panel1.Height);
            Graphics g = Graphics.FromImage(bitM);
            g.Clear(Color.WhiteSmoke);
            Point[] points = new Point[21];
            Random r = new Random();
            for (int i = 0; i < 21; i++)
            {
                points[i].X = x[i];
                points[i].Y = y[i];
            }
            g.DrawLines(new Pen(Color.FromArgb(r.Next(1, 255), r.Next(1, 255), r.Next(1, 255))), points);  //ø�s��u 
            this.panel1.BackgroundImage = bitM;

------------------------------------------------------------------------------------------------------------------------


            int[] x = { 0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600 };
            int[] y = { 200, 328, 396, 373, 268, 131, 26, 3, 71, 200, 328, 396, 373, 268, 131, 26 };

            for (int i = 0; i < 10; i++)
            {
                Application.DoEvents();
                for (int j = 0; j < 20; j++)
                    System.Threading.Thread.Sleep(1);

                g.DrawLine(Pens.Red, new Point(x[i], 400 - y[i]), new Point(x[i + 1], 400 - y[i + 1]));
            }
            MessageBox.Show("OK");


------------------------------------------------------------

            int[] x = new int[10];
            double[] y = new double[10];
            int[] yy = new int[10];
            //int x[10] = 0;
            //float y[10] = 0;
            for (int i = 0; i < 10; i++)
            {
                x[i] = i * 40;
                y[i] = Math.Sin(x[i] * Math.PI / 180) * 200 + 200;
                yy[i] = (int)y[i];
                richTextBox1.Text += x[i].ToString() + "\t" + y[i].ToString() + "\n";
            }

            Pen greenPen = new Pen(Color.Green, 3); // Create pens.

            // Create points that define curve.
            Point point0 = new Point(x[0], yy[0]);
            Point point1 = new Point(x[1], yy[1]);
            Point point2 = new Point(x[2], yy[2]);
            Point point3 = new Point(x[3], yy[3]);
            Point point4 = new Point(x[4], yy[4]);
            Point point5 = new Point(x[5], yy[5]);
            Point point6 = new Point(x[6], yy[6]);
            Point point7 = new Point(x[7], yy[7]);
            Point point8 = new Point(x[8], yy[8]);
            Point point9 = new Point(x[9], yy[9]);

            Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9 };

            g.DrawCurve(greenPen, curvePoints); //�e���u
            g.DrawLines(greenPen, curvePoints);   //�e���u



-----------------------------------------

            Point[] pt = new Point[360];    //�@���}�C����360��Point
            int angle;
            int amplitude = 100;
            for (angle = 0; angle < 360; angle += 1)
            {
                pt[angle].X = angle;
                pt[angle].Y = (int)(amplitude * Math.Sin(angle * 3 * Math.PI / 180)) + amplitude;

            }
            g.DrawLines(new Pen(Brushes.Red, 3), pt);


		//�P�߶�
            g.DrawString("�o�O�@�զP�߶�", this.Font, Brushes.Black, 10, 20);
            Pen p1 = new Pen(Color.Red);
            Pen p2 = new Pen(Color.Purple);
            Pen p3 = new Pen(Color.Blue);
            Pen p4 = new Pen(Color.Green);
            g.DrawEllipse(p1, 120 - 80, 120 - 80, 80 * 2, 80 * 2);
            g.DrawEllipse(p2, 120 - 60, 120 - 60, 60 * 2, 60 * 2);
            g.DrawEllipse(p3, 120 - 40, 120 - 40, 40 * 2, 40 * 2);
            g.DrawEllipse(p4, 120 - 20, 120 - 20, 20 * 2, 20 * 2);


            //�e���u
            Point[] pts = new Point[5];
            pts[0].X = 10;
            pts[0].Y = 10;
            pts[1].X = 20;
            pts[1].Y = 60;
            pts[2].X = 30;
            pts[2].Y = 10;
            pts[3].X = 40;
            pts[3].Y = 60;
            pts[4].X = 50;
            pts[4].Y = 10;
            g.DrawCurve(new Pen(Color.Black), pts);



            //�e�h��Rectangles
            Rectangle[] R = new Rectangle[25];
            int i;
            for (i = 0; i <= 24; i++)
            {
                //R[i] = new Rectangle(0 + 30 * i, 0 + 30 * i);
                R[i] = new Rectangle(i * 10 , i * 5, i*30, i*15);
            }
            g.DrawRectangles(new Pen(Brushes.Red, 3), R);



XML ����	<!-- --> �����e�C


@"C:\______test_vcs\cat\cat2.png"

Pen blackPen = new Pen(Color.FromArgb(255, 0, 0, 0), 5);



DrawImage(bmp, 0, 0);
DrawImage(bmp, 0, 0); // �b���W��� bmp �O����Ϲ�

this.Refresh() ; //���� Form1_Paint()


Bitmap bmp =new Bitmap(@"D:\bear.jpg");
pictureBox1.SizeMode = pictureBoxSizeMode.AutoSize; //�۰ʽվ�j�p
pictureBox1.Image = bmp; //��ܦb pictureBox1 �Ϥ������

// bmp ���j�p�MpictureBox1 �ۦP
Bitmap bmp = new Bitmap(this.PictureBox1.Width,
this.PictureBox1.Height);
// �H�O����Ϲ� bmp �إ� myDraw �O����e��
Graphics myDraw = Graphics.FromImage(bmp);
MyDraw.Clear(this.pictureBox1.BackColor); //�e���I����
MyDraw.DrawLine(new pen(Color.Red,2),x,y,e.X,e.Y); //�i�Hø�ϤF






ø�s�ϧΪ��󪺤�k

Graphics���OGDI+���ѤU�C��k��ø�s�W�z�M�椤�����ءG 


DrawLines

DrawCurve
DrawClosedCurve


        private void Form1_Resize(object sender, EventArgs e)
        {
            pictureBox1.Width = this.ClientSize.Width - 20;
            pictureBox1.Height = this.ClientSize.Height - 20;
        }

	DrawCircle(200, 200, 100);

        private void DrawCircle(int center_x, int center_y, int radius)
        {
            int linewidth = 5;
            // Create a Graphics object for the Control.
            Graphics g = pictureBox1.CreateGraphics();
            // Create a new pen.
            Pen PenStyle = new Pen(Color.Red, 5);
            // Set the pen's width.
            PenStyle.Width = linewidth;
            // Draw the circle
            g.DrawEllipse(PenStyle, new Rectangle(center_x - radius, center_y - radius, radius * 2, radius * 2));
            //Dispose of the pen.
            PenStyle.Dispose();
        }


	private void DrawPixel(int xx, int yy)
	{
		
	}
	


PictureBoxSizeMode

                case 0: pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize; break;
                case 1: pictureBox1.SizeMode = PictureBoxSizeMode.CenterImage; break;
                case 2: pictureBox1.SizeMode = PictureBoxSizeMode.Normal; break;
                case 3: pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage; break;
                case 4: pictureBox1.SizeMode = PictureBoxSizeMode.Zoom; break;


�إߵe��

Graphics �e�������ܼ�;
�e�������ܼ� = ����W��.CreateGraphics();

�Ҧp�G�b���W�إߵe��g�G
Graphics g;
g = this.CreateGraphics();


�Ҧp�G�b�Ϥ����pictureBox1�W�إߵe��g�G
Graphics g;
g = pictureBox1.CreateGraphics();

�e��Pen����

Pen �e�� = new Pen(�e���C��, �e���ʲ�);
Pen p = new Pen(Color.Blue, 5);
p.Color = Color.Red;
p.Width = 2;

���ꪫ��]���S�B�Ϯ�T�B�᯾H�B���hL�^

�������O
SolidBrush		�إ߳�@�C�⪺����
	SolidBrush sb = new SolidBrush(Color.Red);
	Pen p = new Pen(sb, 2);
TextureBrush		�إߥH�ϧΪ����@�Ϯת�����
	TextureBrush tb = new TextureBrush("bmp1.bmp");
	Pen p = new Pen(tb, 2);
HatchBrush		�إߪ᯾����
	HatchBrush �᯾�����ܼ� = new HatchBrush(�᯾����, �e���C��, �I���C��);
	HatchBrush hb = new HatchBrush(HatchStyle.Wave, Color.Blue, Color.Red);
	Pen p = new Pen(hb, 10);
	(�n���[�J�Gusing System.Drawing.Drawing2D;)
LinearGradienBrush	�إߺ��h����
	LinearGradientBrush ���h�����ܼ� = new LinearGradientBrush(���h�x�ΰϰ�, �e���C��, �I���C��, ���h�ɱר���);
	
	Rectangle rect1 = new Rectangle(0, 0, pictureBox1.Size.Width, pictureBox1.Size.Height);
	LinearGradientBrush lgb = new LinearGradientBrush(rect1, Color.Blue, Color.Red, 90);
	Pen p = new Pen(lgb, 10);
	(�n���[�J�Gusing System.Drawing.Drawing2D;)


Pen �e�� = new Pen(�e���C��, �e���ʲ�);






�]�w�C�⪺��k	�I�s�R�A�禡�GColor.FromArgb()

ex:
Color red= Color.FromArgb(255,0,0)
this.BackColor=Color.White;


Pen�u���@��
Brush���|��

Pen�Ω�i�DGraphics�p��ø�s�u��
Brush�Ω��R�ϰ�

Point���Ϊk
Point b=new Point(20,10);
Point a=new Point();
a.X=20;
a.Y=10;


ø�s��u�A�i�]�wPen��DashStyle�ݩʬ�Dash,Dot,DashDot�Ϊ�DashDotDot��
���ܪ��u���I���Ϊ��A�i�H�]�wStartCap�MEndCap�ݩ�

blackPen.StartCap=LineCap.ArrowAnchor;







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






