namespace Tester
{
	partial class PriceDemo
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
			this.label1 = new System.Windows.Forms.Label();
			this.a1Panel1 = new Owf.Controls.A1Panel();
			this.digitalDisplayControl1 = new Owf.Controls.DigitalDisplayControl();
			this.label2 = new System.Windows.Forms.Label();
			this.a1Panel1.SuspendLayout();
			this.SuspendLayout();
			// 
			// label1
			// 
			this.label1.BackColor = System.Drawing.Color.Transparent;
			this.label1.Font = new System.Drawing.Font("Times New Roman", 50F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.label1.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(192)))), ((int)(((byte)(128)))));
			this.label1.Location = new System.Drawing.Point(3, 3);
			this.label1.Name = "label1";
			this.label1.Size = new System.Drawing.Size(51, 73);
			this.label1.TabIndex = 1;
			this.label1.Text = "$";
			// 
			// a1Panel1
			// 
			this.a1Panel1.BorderColor = System.Drawing.SystemColors.HighlightText;
			this.a1Panel1.BorderWidth = 2;
			this.a1Panel1.Controls.Add(this.digitalDisplayControl1);
			this.a1Panel1.Controls.Add(this.label1);
			this.a1Panel1.GradientEndColor = System.Drawing.Color.DimGray;
			this.a1Panel1.GradientStartColor = System.Drawing.Color.Black;
			this.a1Panel1.Image = null;
			this.a1Panel1.ImageLocation = new System.Drawing.Point(4, 4);
			this.a1Panel1.Location = new System.Drawing.Point(42, 71);
			this.a1Panel1.Name = "a1Panel1";
			this.a1Panel1.RoundCornerRadius = 29;
			this.a1Panel1.ShadowOffSet = 12;
			this.a1Panel1.Size = new System.Drawing.Size(327, 99);
			this.a1Panel1.TabIndex = 2;
			// 
			// digitalDisplayControl1
			// 
			this.digitalDisplayControl1.BackColor = System.Drawing.Color.Transparent;
			this.digitalDisplayControl1.DigitColor = System.Drawing.Color.GreenYellow;
			this.digitalDisplayControl1.DigitText = "17866.99";
			this.digitalDisplayControl1.Location = new System.Drawing.Point(57, 8);
			this.digitalDisplayControl1.Name = "digitalDisplayControl1";
			this.digitalDisplayControl1.Size = new System.Drawing.Size(197, 70);
			this.digitalDisplayControl1.TabIndex = 0;
			// 
			// label2
			// 
			this.label2.AutoSize = true;
			this.label2.BackColor = System.Drawing.Color.Transparent;
			this.label2.Font = new System.Drawing.Font("Perpetua Titling MT", 20F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.label2.Location = new System.Drawing.Point(61, 25);
			this.label2.Name = "label2";
			this.label2.Size = new System.Drawing.Size(299, 32);
			this.label2.TabIndex = 1;
			this.label2.Text = "This months sale:";
			// 
			// PriceDemo
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.BackColor = System.Drawing.SystemColors.ControlLightLight;
			this.ClientSize = new System.Drawing.Size(426, 251);
			this.Controls.Add(this.a1Panel1);
			this.Controls.Add(this.label2);
			this.Name = "PriceDemo";
			this.Text = "Price Demo";
			this.a1Panel1.ResumeLayout(false);
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.Label label1;
		private Owf.Controls.A1Panel a1Panel1;
		private Owf.Controls.DigitalDisplayControl digitalDisplayControl1;
		private System.Windows.Forms.Label label2;
	}
}