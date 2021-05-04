namespace MouseDrag
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
            this.picCat = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.picCat)).BeginInit();
            this.SuspendLayout();
            // 
            // picCat
            // 
            this.picCat.Location = new System.Drawing.Point(112, 100);
            this.picCat.Name = "picCat";
            this.picCat.Size = new System.Drawing.Size(60, 60);
            this.picCat.TabIndex = 3;
            this.picCat.TabStop = false;
            this.picCat.MouseDown += new System.Windows.Forms.MouseEventHandler(this.picCat_MouseDown);
            this.picCat.MouseEnter += new System.EventHandler(this.picCat_MouseEnter);
            this.picCat.MouseLeave += new System.EventHandler(this.picCat_MouseLeave);
            this.picCat.MouseMove += new System.Windows.Forms.MouseEventHandler(this.picCat_MouseMove);
            this.picCat.MouseUp += new System.Windows.Forms.MouseEventHandler(this.picCat_MouseUp);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 261);
            this.Controls.Add(this.picCat);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picCat)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox picCat;
    }
}

