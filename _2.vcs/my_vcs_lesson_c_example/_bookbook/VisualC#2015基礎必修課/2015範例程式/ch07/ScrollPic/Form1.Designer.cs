namespace ScrollPic
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
            this.lblW = new System.Windows.Forms.Label();
            this.lblH = new System.Windows.Forms.Label();
            this.picShow = new System.Windows.Forms.PictureBox();
            this.vsbHeight = new System.Windows.Forms.VScrollBar();
            this.hsbWidth = new System.Windows.Forms.HScrollBar();
            ((System.ComponentModel.ISupportInitialize)(this.picShow)).BeginInit();
            this.SuspendLayout();
            // 
            // lblW
            // 
            this.lblW.AutoSize = true;
            this.lblW.Location = new System.Drawing.Point(225, 239);
            this.lblW.Name = "lblW";
            this.lblW.Size = new System.Drawing.Size(33, 12);
            this.lblW.TabIndex = 14;
            this.lblW.Text = "label2";
            // 
            // lblH
            // 
            this.lblH.AutoSize = true;
            this.lblH.Location = new System.Drawing.Point(224, 208);
            this.lblH.Name = "lblH";
            this.lblH.Size = new System.Drawing.Size(33, 12);
            this.lblH.TabIndex = 13;
            this.lblH.Text = "label1";
            // 
            // picShow
            // 
            this.picShow.Location = new System.Drawing.Point(38, 26);
            this.picShow.Name = "picShow";
            this.picShow.Size = new System.Drawing.Size(180, 180);
            this.picShow.TabIndex = 12;
            this.picShow.TabStop = false;
            // 
            // vsbHeight
            // 
            this.vsbHeight.Location = new System.Drawing.Point(246, 9);
            this.vsbHeight.Name = "vsbHeight";
            this.vsbHeight.Size = new System.Drawing.Size(17, 180);
            this.vsbHeight.TabIndex = 11;
            this.vsbHeight.Scroll += new System.Windows.Forms.ScrollEventHandler(this.vsbHeight_Scroll);
            // 
            // hsbWidth
            // 
            this.hsbWidth.Location = new System.Drawing.Point(21, 226);
            this.hsbWidth.Name = "hsbWidth";
            this.hsbWidth.Size = new System.Drawing.Size(180, 17);
            this.hsbWidth.TabIndex = 10;
            this.hsbWidth.Scroll += new System.Windows.Forms.ScrollEventHandler(this.hsbWidth_Scroll);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 261);
            this.Controls.Add(this.lblW);
            this.Controls.Add(this.lblH);
            this.Controls.Add(this.picShow);
            this.Controls.Add(this.vsbHeight);
            this.Controls.Add(this.hsbWidth);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picShow)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lblW;
        private System.Windows.Forms.Label lblH;
        private System.Windows.Forms.PictureBox picShow;
        private System.Windows.Forms.VScrollBar vsbHeight;
        private System.Windows.Forms.HScrollBar hsbWidth;
    }
}

