namespace vcs_MyClock
{
    partial class Form1
    {
        /// <summary>
        /// 設計工具所需的變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清除任何使用中的資源。
        /// </summary>
        /// <param name="disposing">如果應該處置 Managed 資源則為 true，否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 設計工具產生的程式碼

        /// <summary>
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器
        /// 修改這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.a1Panel1 = new Owf.Controls.A1Panel();
            this.digitalDisplayControl3 = new Owf.Controls.DigitalDisplayControl();
            this.digitalDisplayControl2 = new Owf.Controls.DigitalDisplayControl();
            this.digitalDisplayControl1 = new Owf.Controls.DigitalDisplayControl();
            this.a1Panel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Interval = 1000;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // a1Panel1
            // 
            this.a1Panel1.BorderColor = System.Drawing.Color.Gray;
            this.a1Panel1.Controls.Add(this.digitalDisplayControl3);
            this.a1Panel1.Controls.Add(this.digitalDisplayControl2);
            this.a1Panel1.Controls.Add(this.digitalDisplayControl1);
            this.a1Panel1.GradientEndColor = System.Drawing.Color.Gray;
            this.a1Panel1.GradientStartColor = System.Drawing.Color.White;
            this.a1Panel1.Image = null;
            this.a1Panel1.ImageLocation = new System.Drawing.Point(4, 4);
            this.a1Panel1.Location = new System.Drawing.Point(33, 67);
            this.a1Panel1.Name = "a1Panel1";
            this.a1Panel1.Size = new System.Drawing.Size(400, 400);
            this.a1Panel1.TabIndex = 1;
            // 
            // digitalDisplayControl3
            // 
            this.digitalDisplayControl3.BackColor = System.Drawing.Color.Transparent;
            this.digitalDisplayControl3.DigitColor = System.Drawing.Color.GreenYellow;
            this.digitalDisplayControl3.Location = new System.Drawing.Point(223, 23);
            this.digitalDisplayControl3.Name = "digitalDisplayControl3";
            this.digitalDisplayControl3.Size = new System.Drawing.Size(150, 58);
            this.digitalDisplayControl3.TabIndex = 2;
            // 
            // digitalDisplayControl2
            // 
            this.digitalDisplayControl2.BackColor = System.Drawing.Color.Transparent;
            this.digitalDisplayControl2.DigitColor = System.Drawing.Color.GreenYellow;
            this.digitalDisplayControl2.Location = new System.Drawing.Point(27, 23);
            this.digitalDisplayControl2.Name = "digitalDisplayControl2";
            this.digitalDisplayControl2.Size = new System.Drawing.Size(150, 58);
            this.digitalDisplayControl2.TabIndex = 1;
            // 
            // digitalDisplayControl1
            // 
            this.digitalDisplayControl1.BackColor = System.Drawing.Color.Transparent;
            this.digitalDisplayControl1.DigitColor = System.Drawing.Color.GreenYellow;
            this.digitalDisplayControl1.Location = new System.Drawing.Point(83, 151);
            this.digitalDisplayControl1.Name = "digitalDisplayControl1";
            this.digitalDisplayControl1.Size = new System.Drawing.Size(288, 94);
            this.digitalDisplayControl1.TabIndex = 0;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(873, 549);
            this.Controls.Add(this.a1Panel1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.a1Panel1.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private Owf.Controls.DigitalDisplayControl digitalDisplayControl1;
        private Owf.Controls.A1Panel a1Panel1;
        private System.Windows.Forms.Timer timer1;
        private Owf.Controls.DigitalDisplayControl digitalDisplayControl3;
        private Owf.Controls.DigitalDisplayControl digitalDisplayControl2;
    }
}

