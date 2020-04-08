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
		private System.Windows.Forms.Button btnClose;
		private System.Windows.Forms.MonthCalendar MyCalendar;
		private System.Windows.Forms.PictureBox PicMoon;
		private System.Windows.Forms.Button btnToDay;
		private System.Windows.Forms.Label lblAge;
		private System.ComponentModel.IContainer components = null;

		//Variables for Moon program
		private double ip;
        private RichTextBox richTextBox1;
        private MonthCalendar monthCalendar1;
        private Button button1;
        private Button button2;
        private Button button3;
		private double ag;

		public frmMoon()
		{
			InitializeComponent();
		}

		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		protected override void Dispose( bool disposing )
		{
			if( disposing )
			{
				if (components != null) 
				{
					components.Dispose();
				}
			}
			base.Dispose( disposing );
		}

		#region Windows Form Designer generated code
		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(frmMoon));
            this.btnToDay = new System.Windows.Forms.Button();
            this.btnClose = new System.Windows.Forms.Button();
            this.MyCalendar = new System.Windows.Forms.MonthCalendar();
            this.lblAge = new System.Windows.Forms.Label();
            this.PicMoon = new System.Windows.Forms.PictureBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.monthCalendar1 = new System.Windows.Forms.MonthCalendar();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
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
            // btnClose
            // 
            this.btnClose.Font = new System.Drawing.Font("Tahoma", 8.25F);
            this.btnClose.ImeMode = System.Windows.Forms.ImeMode.NoControl;
            this.btnClose.Location = new System.Drawing.Point(368, 203);
            this.btnClose.Name = "btnClose";
            this.btnClose.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.btnClose.Size = new System.Drawing.Size(75, 28);
            this.btnClose.TabIndex = 4;
            this.btnClose.Text = "Close";
            this.btnClose.Click += new System.EventHandler(this.btnClose_Click);
            // 
            // MyCalendar
            // 
            this.MyCalendar.ImeMode = System.Windows.Forms.ImeMode.NoControl;
            this.MyCalendar.Location = new System.Drawing.Point(188, 9);
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
            this.PicMoon.Size = new System.Drawing.Size(155, 179);
            this.PicMoon.TabIndex = 13;
            this.PicMoon.TabStop = false;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(499, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(254, 258);
            this.richTextBox1.TabIndex = 14;
            this.richTextBox1.Text = "";
            // 
            // monthCalendar1
            // 
            this.monthCalendar1.Location = new System.Drawing.Point(16, 248);
            this.monthCalendar1.Name = "monthCalendar1";
            this.monthCalendar1.TabIndex = 15;
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("Tahoma", 8.25F);
            this.button1.ImeMode = System.Windows.Forms.ImeMode.NoControl;
            this.button1.Location = new System.Drawing.Point(293, 302);
            this.button1.Name = "button1";
            this.button1.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.button1.Size = new System.Drawing.Size(75, 28);
            this.button1.TabIndex = 16;
            this.button1.Text = "tmp1";
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Font = new System.Drawing.Font("Tahoma", 8.25F);
            this.button2.ImeMode = System.Windows.Forms.ImeMode.NoControl;
            this.button2.Location = new System.Drawing.Point(293, 373);
            this.button2.Name = "button2";
            this.button2.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.button2.Size = new System.Drawing.Size(75, 28);
            this.button2.TabIndex = 17;
            this.button2.Text = "clear draw";
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button3
            // 
            this.button3.Font = new System.Drawing.Font("Tahoma", 8.25F);
            this.button3.ImeMode = System.Windows.Forms.ImeMode.NoControl;
            this.button3.Location = new System.Drawing.Point(499, 276);
            this.button3.Name = "button3";
            this.button3.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.button3.Size = new System.Drawing.Size(75, 28);
            this.button3.TabIndex = 18;
            this.button3.Text = "clear";
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // frmMoon
            // 
            this.AutoScaleBaseSize = new System.Drawing.Size(5, 15);
            this.ClientSize = new System.Drawing.Size(765, 437);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.monthCalendar1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.PicMoon);
            this.Controls.Add(this.lblAge);
            this.Controls.Add(this.MyCalendar);
            this.Controls.Add(this.btnClose);
            this.Controls.Add(this.btnToDay);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.Fixed3D;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximizeBox = false;
            this.Name = "frmMoon";
            this.ShowInTaskbar = false;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "*Moon Phase*";
            this.Load += new System.EventHandler(this.frmMoon_Load);
            ((System.ComponentModel.ISupportInitialize)(this.PicMoon)).EndInit();
            this.ResumeLayout(false);

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
            richTextBox1.Text += "MoonAge d = " + d.ToString() + ", m = " + m.ToString() + ", y = " + y.ToString() + "\n";
			int j = JulianDate(d, m, y);
			//Calculate the approximate phase of the moon
			ip = (j + 4.867) / 29.53059;
			ip = ip - Math.Floor(ip);
			//After several trials I've seen to add the following lines, 
			//which gave the result was not bad
			if(ip < 0.5)
				ag = ip * 29.53059 + 29.53059 / 2;
			else
				ag = ip * 29.53059 - 29.53059 / 2;
			// Moon's age in days
			ag = Math.Floor(ag) + 1;
            richTextBox1.Text += "MoonAge ag = " + ag.ToString() + "\n";
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
			if(PicMoon.Image != null)
			{
				PicMoon.Image = null;
			}
		}

		private void DrawMoon()
		{
			int Xpos, Ypos, Rpos;
			int Xpos1, Xpos2;
			double Phase;
            richTextBox1.Text += "ip = " + ip.ToString() + "\n";
			Phase = ip;

			// Width of 'ImageToDraw' Object = Width of 'PicMoon' control
			int PageWidth = PicMoon.Width;
			// Height of 'ImageToDraw' Object = Height of 'PicMoon' control
			int PageHeight = PicMoon.Height;
			// Initiate 'ImageToDraw' Object with size = size of control 'PicMoon' control
			Bitmap ImageToDraw = new Bitmap(PageWidth, PageHeight);
			// Create graphics object for alteration.
			Graphics newGraphics = Graphics.FromImage(ImageToDraw);

			Pen PenB = new Pen(Color.Black); // For darkness part of the moon
			Pen PenW = new Pen(Color.White); // For the lighted part of the moon

			for (Ypos=0; Ypos<= 45; Ypos++)
			{
				Xpos = (int)(Math.Sqrt(45*45 - Ypos*Ypos));
                // Draw darkness part of the moon
				Point pB1 = new Point(90-Xpos, Ypos+90);
				Point pB2 = new Point(Xpos+90, Ypos+90);
				Point pB3 = new Point(90-Xpos, 90-Ypos);
				Point pB4 = new Point(Xpos+90, 90-Ypos);
				newGraphics.DrawLine(PenB, pB1, pB2); 
				newGraphics.DrawLine(PenB, pB3, pB4); 
				// Determine the edges of the lighted part of the moon
				Rpos = 2 * Xpos;
				if (Phase < 0.5)
				{
					Xpos1 = - Xpos;
					Xpos2 = (int)(Rpos - 2*Phase*Rpos - Xpos);
				}
				else
				{
					Xpos1 = Xpos;
					Xpos2 = (int)(Xpos - 2*Phase*Rpos + Rpos);
				}
				// Draw the lighted part of the moon
				Point pW1 = new Point(Xpos1+90, 90-Ypos);
				Point pW2 = new Point(Xpos2+90, 90-Ypos);
				Point pW3 = new Point(Xpos1+90, Ypos+90);
				Point pW4 = new Point(Xpos2+90, Ypos+90);
				newGraphics.DrawLine(PenW, pW1, pW2);
				newGraphics.DrawLine(PenW, pW3, pW4);
			}
			// Display the bitmap in the picture box.
			PicMoon.Image = ImageToDraw;
			// Release graphics object
			PenB.Dispose();
			PenW.Dispose();
			newGraphics.Dispose();
			ImageToDraw = null;
		}

		private void YourChoice()
		{
			//user select date from MonthCalendar control
			int Aday, Amonth, Ayear;
			Aday = this.MyCalendar.SelectionStart.Day;
			Amonth = this.MyCalendar.SelectionStart.Month;
			Ayear = this.MyCalendar.SelectionStart.Year;
            richTextBox1.Text += "Aday = " + Aday.ToString() + ", Amonth = " + Amonth.ToString() + ", Ayear = " + Ayear.ToString() + "\n";
 			this.MoonAge(Aday, Amonth, Ayear);
		}

		private void ShowMoon()
		{
            richTextBox1.Text += "ShowMoon 111\n";
			//draw moon and print age in selected days
			this.YourChoice(); //select date
            richTextBox1.Text += "ShowMoon 222\n";
			this.ClearDraw(); //clear PicMoon PictureBox
            richTextBox1.Text += "ShowMoon 333\n";
			this.DrawMoon(); //draw the moon
            richTextBox1.Text += "ShowMoon 444\n";
			this.PrintAge(); //print age of moon in days
		}

		private void frmMoon_Load(object sender, System.EventArgs e)
		{
			this.ShowMoon(); 
		}

		private void MyCalendar_DateChanged(object sender, System.Windows.Forms.DateRangeEventArgs e)
		{
            richTextBox1.Text += "MyCalendar_DateChanged \n";
			this.ShowMoon(); 
		}

		private void btnToDay_Click(object sender, System.EventArgs e)
		{
			//set the date of today
			this.MyCalendar.SetDate(this.MyCalendar.TodayDate.Date);
		}

		private void btnClose_Click(object sender, System.EventArgs e)
		{
			Application.Exit();
		}

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Date : " + this.MyCalendar.TodayDate.Date.ToString() + "\n";

        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.ClearDraw(); //clear PicMoon PictureBox

        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }
	}
}
