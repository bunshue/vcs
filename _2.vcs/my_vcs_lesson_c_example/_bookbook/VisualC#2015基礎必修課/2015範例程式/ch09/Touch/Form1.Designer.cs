namespace Touch
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
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改
        /// 這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.lblTouch = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // lblTouch
            // 
            this.lblTouch.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.lblTouch.Location = new System.Drawing.Point(54, 45);
            this.lblTouch.Name = "lblTouch";
            this.lblTouch.Size = new System.Drawing.Size(112, 70);
            this.lblTouch.TabIndex = 0;
            this.lblTouch.Text = "label1";
            this.lblTouch.Click += new System.EventHandler(this.lblTouch_Click);
            this.lblTouch.DoubleClick += new System.EventHandler(this.lblTouch_DoubleClick);
            this.lblTouch.MouseClick += new System.Windows.Forms.MouseEventHandler(this.lblTouch_MouseClick);
            this.lblTouch.MouseDown += new System.Windows.Forms.MouseEventHandler(this.lblTouch_MouseDown);
            this.lblTouch.MouseMove += new System.Windows.Forms.MouseEventHandler(this.lblTouch_MouseMove);
            this.lblTouch.MouseUp += new System.Windows.Forms.MouseEventHandler(this.lblTouch_MouseUp);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 261);
            this.Controls.Add(this.lblTouch);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Label lblTouch;
    }
}

