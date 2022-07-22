using System;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Collections;
using System.ComponentModel;
using System.Windows.Forms;
using System.Data;

namespace MoonPhase
{
    /// <summary>
    /// Summary description for Form1.
    /// </summary>
    public class frmMoon : System.Windows.Forms.Form
    {
        private System.Windows.Forms.MonthCalendar MyCalendar;
        private System.Windows.Forms.PictureBox PicMoon;
        private System.Windows.Forms.Button btnToDay;
        private System.Windows.Forms.Label lblAge;
        private System.ComponentModel.IContainer components = null;

        //Variables for Moon program
        private double ip;
        private TextBox textBox1;
        private Button button1;
        private RichTextBox richTextBox1;
        private double ag;

        public frmMoon()
        {
            InitializeComponent();
        }

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                if (components != null)
                {
                    components.Dispose();
                }
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code
        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.btnToDay = new System.Windows.Forms.Button();
            this.MyCalendar = new System.Windows.Forms.MonthCalendar();
            this.lblAge = new System.Windows.Forms.Label();
            this.PicMoon = new System.Windows.Forms.PictureBox();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            ((System.ComponentModel.ISupportInitialize)(this.PicMoon)).BeginInit();
            this.SuspendLayout();
            // 
            // btnToDay
            // 
            this.btnToDay.Font = new System.Drawing.Font("Tahoma", 8.25F);
            this.btnToDay.ImeMode = System.Windows.Forms.ImeMode.NoControl;
            this.btnToDay.Location = new System.Drawing.Point(188, 203);
            this.btnToDay.Name = "btnToDay";
            this.btnToDay.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.btnToDay.Size = new System.Drawing.Size(75, 28);
            this.btnToDay.TabIndex = 2;
            this.btnToDay.Text = "Moon today";
            this.btnToDay.Click += new System.EventHandler(this.btnToDay_Click);
            // 
            // MyCalendar
            // 
            this.MyCalendar.ImeMode = System.Windows.Forms.ImeMode.NoControl;
            this.MyCalendar.Location = new System.Drawing.Point(264, 9);
            this.MyCalendar.Name = "MyCalendar";
            this.MyCalendar.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.MyCalendar.TabIndex = 11;
            this.MyCalendar.DateChanged += new System.Windows.Forms.DateRangeEventHandler(this.MyCalendar_DateChanged);
            // 
            // lblAge
            // 
            this.lblAge.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblAge.Font = new System.Drawing.Font("Tahoma", 9.75F);
            this.lblAge.ImeMode = System.Windows.Forms.ImeMode.NoControl;
            this.lblAge.Location = new System.Drawing.Point(16, 203);
            this.lblAge.Name = "lblAge";
            this.lblAge.Size = new System.Drawing.Size(155, 28);
            this.lblAge.TabIndex = 12;
            this.lblAge.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // PicMoon
            // 
            this.PicMoon.BackColor = System.Drawing.Color.Navy;
            this.PicMoon.ImeMode = System.Windows.Forms.ImeMode.NoControl;
            this.PicMoon.Location = new System.Drawing.Point(16, 9);
            this.PicMoon.Name = "PicMoon";
            this.PicMoon.Size = new System.Drawing.Size(180, 180);
            this.PicMoon.TabIndex = 13;
            this.PicMoon.TabStop = false;
            // 
            // textBox1
            // 
            this.textBox1.Font = new System.Drawing.Font("�s�ө���", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.textBox1.Location = new System.Drawing.Point(16, 260);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(155, 33);
            this.textBox1.TabIndex = 14;
            this.textBox1.Text = "2006/03/11";
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("Tahoma", 8.25F);
            this.button1.ImeMode = System.Windows.Forms.ImeMode.NoControl;
            this.button1.Location = new System.Drawing.Point(188, 260);
            this.button1.Name = "button1";
            this.button1.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.button1.Size = new System.Drawing.Size(75, 28);
            this.button1.TabIndex = 15;
            this.button1.Text = "OK";
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(511, 9);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(371, 485);
            this.richTextBox1.TabIndex = 16;
            this.richTextBox1.Text = "";
            // 
            // frmMoon
            // 
            this.AutoScaleBaseSize = new System.Drawing.Size(5, 15);
            this.ClientSize = new System.Drawing.Size(894, 506);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.PicMoon);
            this.Controls.Add(this.lblAge);
            this.Controls.Add(this.MyCalendar);
            this.Controls.Add(this.btnToDay);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.Fixed3D;
            this.MaximizeBox = false;
            this.Name = "frmMoon";
            this.ShowInTaskbar = false;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "���";
            this.Load += new System.EventHandler(this.frmMoon_Load);
            ((System.ComponentModel.ISupportInitialize)(this.PicMoon)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }
        #endregion

        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.Run(new frmMoon());
        }

        private int JulianDate(int d, int m, int y)
        {
            int mm, yy;
            int k1, k2, k3;
            int j;

            yy = y - (int)((12 - m) / 10);
            mm = m + 9;
            if (mm >= 12)
            {
                mm = mm - 12;
            }
            k1 = (int)(365.25 * (yy + 4712));
            k2 = (int)(30.6001 * mm + 0.5);
            k3 = (int)((int)((yy / 100) + 49) * 0.75) - 38;
            // 'j' for dates in Julian calendar:
            j = k1 + k2 + d + 59;
            if (j > 2299160)
            {
                // For Gregorian calendar:
                j = j - k3;  // 'j' is the Julian date at 12h UT (Universal Time)
            }
            return j;
        }

        private double MoonAge(int d, int m, int y)
        {
            int j = JulianDate(d, m, y);
            //Calculate the approximate phase of the moon
            ip = (j + 4.867) / 29.53059;
            ip = ip - Math.Floor(ip);
            //After several trials I've seen to add the following lines, 
            //which gave the result was not bad
            if (ip < 0.5)
                ag = ip * 29.53059 + 29.53059 / 2;
            else
                ag = ip * 29.53059 - 29.53059 / 2;
            // Moon's age in days
            ag = Math.Floor(ag) + 1;
            return ag;
        }

        private void PrintAge()
        {
            string theAge = "Moon age";

            theAge = theAge + " " + ":" + " " + ag.ToString();

            if (ag == 1)
                theAge = theAge + " " + "day";
            else
                theAge = theAge + " " + "days";

            this.lblAge.Text = theAge;
        }

        public void ClearDraw()
        {
            if (PicMoon.Image != null)
            {
                PicMoon.Image = null;
            }
        }

        private void DrawMoon()
        {
            richTextBox1.Text += "DrawMoon\n";
            int Xpos, Ypos, Rpos;
            int Xpos1, Xpos2;
            double Phase;

            Phase = ip;

            // Width of 'bitmap1' Object = Width of 'PicMoon' control
            int PageWidth = PicMoon.Width;
            // Height of 'bitmap1' Object = Height of 'PicMoon' control
            int PageHeight = PicMoon.Height;
            // Initiate 'bitmap1' Object with size = size of control 'PicMoon' control
            Bitmap bitmap1 = new Bitmap(PageWidth, PageHeight);
            // Create graphics object for alteration.
            Graphics g = Graphics.FromImage(bitmap1);

            Pen PenB = new Pen(Color.Black); // For darkness part of the moon
            Pen PenW = new Pen(Color.White); // For the lighted part of the moon

            for (Ypos = 0; Ypos <= 45; Ypos++)
            {
                Xpos = (int)(Math.Sqrt(45 * 45 - Ypos * Ypos));
                // Draw darkness part of the moon
                Point pB1 = new Point(90 - Xpos, Ypos + 90);
                Point pB2 = new Point(Xpos + 90, Ypos + 90);
                Point pB3 = new Point(90 - Xpos, 90 - Ypos);
                Point pB4 = new Point(Xpos + 90, 90 - Ypos);
                g.DrawLine(PenB, pB1, pB2);
                g.DrawLine(PenB, pB3, pB4);
                // Determine the edges of the lighted part of the moon
                Rpos = 2 * Xpos;
                if (Phase < 0.5)
                {
                    Xpos1 = -Xpos;
                    Xpos2 = (int)(Rpos - 2 * Phase * Rpos - Xpos);
                }
                else
                {
                    Xpos1 = Xpos;
                    Xpos2 = (int)(Xpos - 2 * Phase * Rpos + Rpos);
                }
                // Draw the lighted part of the moon
                Point pW1 = new Point(Xpos1 + 90, 90 - Ypos);
                Point pW2 = new Point(Xpos2 + 90, 90 - Ypos);
                Point pW3 = new Point(Xpos1 + 90, Ypos + 90);
                Point pW4 = new Point(Xpos2 + 90, Ypos + 90);
                g.DrawLine(PenW, pW1, pW2);
                g.DrawLine(PenW, pW3, pW4);
            }

            // Display the bitmap in the picture box.
            PicMoon.Image = bitmap1;

            // Release graphics object
            PenB.Dispose();
            PenW.Dispose();
            g.Dispose();
            bitmap1 = null;
        }

        private void YourChoice()
        {
            //user select date from MonthCalendar control
            int Aday, Amonth, Ayear;
            Aday = this.MyCalendar.SelectionStart.Day;
            Amonth = this.MyCalendar.SelectionStart.Month;
            Ayear = this.MyCalendar.SelectionStart.Year;
            this.MoonAge(Aday, Amonth, Ayear);
        }

        private void ShowMoon()
        {
            richTextBox1.Text += "ShowMoon\n";
            //draw moon and print age in selected days
            this.YourChoice(); //select date
            this.ClearDraw(); //clear PicMoon PictureBox
            this.DrawMoon(); //draw the moon
            this.PrintAge(); //print age of moon in days
        }

        private void frmMoon_Load(object sender, System.EventArgs e)
        {
            this.ShowMoon();
        }

        private void MyCalendar_DateChanged(object sender, System.Windows.Forms.DateRangeEventArgs e)
        {
            this.ShowMoon();
        }

        private void btnToDay_Click(object sender, System.EventArgs e)
        {
            //set the date of today
            this.MyCalendar.SetDate(this.MyCalendar.TodayDate.Date);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            DateTime dt = DateTime.Now;
            bool conversionSuccessful = DateTime.TryParse(textBox1.Text, out dt);    //out������
            if (conversionSuccessful == true)
            {
                richTextBox1.Text += "�o��DateTime��ơG " + dt.ToString() + "\n";
                this.MyCalendar.SetDate(dt);

            }
            else
            {
                richTextBox1.Text += "DateTime.TryParse ����\n";
            }
        }
    }
}

