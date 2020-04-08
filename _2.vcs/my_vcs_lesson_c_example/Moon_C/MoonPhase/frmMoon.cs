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
			System.Resources.ResourceManager resources = new System.Resources.ResourceManager(typeof(frmMoon));
			this.btnToDay = new System.Windows.Forms.Button();
			this.btnClose = new System.Windows.Forms.Button();
			this.MyCalendar = new System.Windows.Forms.MonthCalendar();
			this.lblAge = new System.Windows.Forms.Label();
			this.PicMoon = new System.Windows.Forms.PictureBox();
			this.SuspendLayout();
			// 
			// btnToDay
			// 
			this.btnToDay.Font = new System.Drawing.Font("Tahoma", 8.25F);
			this.btnToDay.ImeMode = System.Windows.Forms.ImeMode.NoControl;
			this.btnToDay.Location = new System.Drawing.Point(188, 176);
			this.btnToDay.Name = "btnToDay";
			this.btnToDay.RightToLeft = System.Windows.Forms.RightToLeft.No;
			this.btnToDay.Size = new System.Drawing.Size(75, 24);
			this.btnToDay.TabIndex = 2;
			this.btnToDay.Text = "Moon today";
			this.btnToDay.Click += new System.EventHandler(this.btnToDay_Click);
			// 
			// btnClose
			// 
			this.btnClose.Font = new System.Drawing.Font("Tahoma", 8.25F);
			this.btnClose.ImeMode = System.Windows.Forms.ImeMode.NoControl;
			this.btnClose.Location = new System.Drawing.Point(368, 176);
			this.btnClose.Name = "btnClose";
			this.btnClose.RightToLeft = System.Windows.Forms.RightToLeft.No;
			this.btnClose.Size = new System.Drawing.Size(75, 24);
			this.btnClose.TabIndex = 4;
			this.btnClose.Text = "Close";
			this.btnClose.Click += new System.EventHandler(this.btnClose_Click);
			// 
			// MyCalendar
			// 
			this.MyCalendar.ImeMode = System.Windows.Forms.ImeMode.NoControl;
			this.MyCalendar.Location = new System.Drawing.Point(188, 8);
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
			this.lblAge.Location = new System.Drawing.Point(16, 176);
			this.lblAge.Name = "lblAge";
			this.lblAge.Size = new System.Drawing.Size(155, 24);
			this.lblAge.TabIndex = 12;
			this.lblAge.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// PicMoon
			// 
			this.PicMoon.BackColor = System.Drawing.Color.Navy;
			this.PicMoon.ImeMode = System.Windows.Forms.ImeMode.NoControl;
			this.PicMoon.Location = new System.Drawing.Point(16, 8);
			this.PicMoon.Name = "PicMoon";
			this.PicMoon.Size = new System.Drawing.Size(155, 155);
			this.PicMoon.TabIndex = 13;
			this.PicMoon.TabStop = false;
			// 
			// frmMoon
			// 
			this.AutoScaleBaseSize = new System.Drawing.Size(5, 13);
			this.ClientSize = new System.Drawing.Size(455, 214);
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
			this.MoonAge(Aday, Amonth, Ayear);
		}

		private void ShowMoon()
		{
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

		private void btnClose_Click(object sender, System.EventArgs e)
		{
			Application.Exit();
		}
	}
}
