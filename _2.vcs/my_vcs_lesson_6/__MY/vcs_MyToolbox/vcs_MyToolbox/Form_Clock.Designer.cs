namespace vcs_MyToolbox
{
    partial class Form_Clock
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
            this.digitalDisplayControl1 = new Owf.Controls.DigitalDisplayControl();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.SuspendLayout();
            // 
            // digitalDisplayControl1
            // 
            this.digitalDisplayControl1.BackColor = System.Drawing.Color.Transparent;
            this.digitalDisplayControl1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.digitalDisplayControl1.DigitColor = System.Drawing.Color.Purple;
            this.digitalDisplayControl1.DigitText = "88:88:88.88";
            this.digitalDisplayControl1.Location = new System.Drawing.Point(104, 76);
            this.digitalDisplayControl1.Name = "digitalDisplayControl1";
            this.digitalDisplayControl1.Size = new System.Drawing.Size(429, 99);
            this.digitalDisplayControl1.TabIndex = 1;
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Interval = 1000;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // Form_Clock
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(714, 331);
            this.Controls.Add(this.digitalDisplayControl1);
            this.Name = "Form_Clock";
            this.Text = "Form_Clock";
            this.Load += new System.EventHandler(this.Form_Clock_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private Owf.Controls.DigitalDisplayControl digitalDisplayControl1;
        private System.Windows.Forms.Timer timer1;
    }
}