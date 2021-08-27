namespace Tester
{
	partial class ClockDemo
	{
		/// <summary>
		/// Required designer variable.
		/// </summary>
		private System.ComponentModel.IContainer components = null;

		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		/// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
		protected override void Dispose(bool disposing)
		{
			if (disposing && (components != null))
			{
				components.Dispose();
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
			this.components = new System.ComponentModel.Container();
			this.a1Panel2 = new Owf.Controls.A1Panel();
			this.digitalDisplayControl1 = new Owf.Controls.DigitalDisplayControl();
			this.timer1 = new System.Windows.Forms.Timer(this.components);
			this.a1Panel2.SuspendLayout();
			this.SuspendLayout();
			// 
			// a1Panel2
			// 
			this.a1Panel2.BorderColor = System.Drawing.SystemColors.HighlightText;
			this.a1Panel2.BorderWidth = 2;
			this.a1Panel2.Controls.Add(this.digitalDisplayControl1);
			this.a1Panel2.GradientEndColor = System.Drawing.Color.Silver;
			this.a1Panel2.GradientStartColor = System.Drawing.Color.Silver;
			this.a1Panel2.Image = null;
			this.a1Panel2.ImageLocation = new System.Drawing.Point(4, 4);
			this.a1Panel2.Location = new System.Drawing.Point(82, 86);
			this.a1Panel2.Name = "a1Panel2";
			this.a1Panel2.RoundCornerRadius = 29;
			this.a1Panel2.ShadowOffSet = 12;
			this.a1Panel2.Size = new System.Drawing.Size(304, 117);
			this.a1Panel2.TabIndex = 3;
			// 
			// digitalDisplayControl1
			// 
			this.digitalDisplayControl1.BackColor = System.Drawing.Color.Transparent;
			this.digitalDisplayControl1.DigitColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
			this.digitalDisplayControl1.DigitText = "00:00:00";
			this.digitalDisplayControl1.Location = new System.Drawing.Point(17, 15);
			this.digitalDisplayControl1.Name = "digitalDisplayControl1";
			this.digitalDisplayControl1.Size = new System.Drawing.Size(257, 70);
			this.digitalDisplayControl1.TabIndex = 1;
			// 
			// timer1
			// 
			this.timer1.Enabled = true;
			this.timer1.Interval = 1000;
			this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
			// 
			// ClockDemo
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.BackColor = System.Drawing.SystemColors.ControlLightLight;
			this.ClientSize = new System.Drawing.Size(468, 289);
			this.Controls.Add(this.a1Panel2);
			this.Name = "ClockDemo";
			this.Text = "ClockDemo";
			this.Load += new System.EventHandler(this.ClockDemo_Load);
			this.a1Panel2.ResumeLayout(false);
			this.ResumeLayout(false);

		}

		#endregion

		private Owf.Controls.A1Panel a1Panel2;
		private Owf.Controls.DigitalDisplayControl digitalDisplayControl1;
		private System.Windows.Forms.Timer timer1;
	}
}