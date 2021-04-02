namespace AptitudeFluctuateWidget
{
    partial class frmMain
    {
        /// <summary>
        /// 必需的設計器變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的資源。
        /// </summary>
        /// <param name="disposing">如果應釋放托管資源，為 true；否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 視窗設計器產生的代碼

        /// <summary>
        /// 設計器支援所需的方法 - 不要
        /// 使用代碼編輯器修改此方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(frmMain));
            this.imageList1 = new System.Windows.Forms.ImageList(this.components);
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.button6 = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // imageList1
            // 
            this.imageList1.ImageStream = ((System.Windows.Forms.ImageListStreamer)(resources.GetObject("imageList1.ImageStream")));
            this.imageList1.TransparentColor = System.Drawing.Color.Transparent;
            this.imageList1.Images.SetKeyName(0, "121.gif");
            this.imageList1.Images.SetKeyName(1, "11.bmp");
            this.imageList1.Images.SetKeyName(2, "97.bmp");
            this.imageList1.Images.SetKeyName(3, "70.bmp");
            this.imageList1.Images.SetKeyName(4, "64.bmp");
            this.imageList1.Images.SetKeyName(5, "103.bmp");
            // 
            // button1
            // 
            this.button1.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.button1.ImageAlign = System.Drawing.ContentAlignment.TopCenter;
            this.button1.ImageIndex = 2;
            this.button1.ImageList = this.imageList1;
            this.button1.Location = new System.Drawing.Point(244, 125);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(109, 104);
            this.button1.TabIndex = 0;
            this.button1.Text = "用戶設置";
            this.button1.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            this.button1.UseVisualStyleBackColor = true;
            // 
            // button2
            // 
            this.button2.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.button2.ImageAlign = System.Drawing.ContentAlignment.TopCenter;
            this.button2.ImageIndex = 3;
            this.button2.ImageList = this.imageList1;
            this.button2.Location = new System.Drawing.Point(12, 122);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(109, 107);
            this.button2.TabIndex = 1;
            this.button2.Text = "報表打印";
            this.button2.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            this.button2.UseVisualStyleBackColor = true;
            // 
            // button4
            // 
            this.button4.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.button4.ImageIndex = 1;
            this.button4.ImageList = this.imageList1;
            this.button4.Location = new System.Drawing.Point(241, 12);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(117, 104);
            this.button4.TabIndex = 3;
            this.button4.Text = "系統設置";
            this.button4.TextAlign = System.Drawing.ContentAlignment.TopCenter;
            this.button4.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageAboveText;
            this.button4.UseVisualStyleBackColor = true;
            // 
            // button3
            // 
            this.button3.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.button3.ImageAlign = System.Drawing.ContentAlignment.TopCenter;
            this.button3.ImageIndex = 0;
            this.button3.ImageList = this.imageList1;
            this.button3.Location = new System.Drawing.Point(12, 12);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(108, 104);
            this.button3.TabIndex = 2;
            this.button3.Text = "目錄查詢";
            this.button3.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageAboveText;
            this.button3.UseVisualStyleBackColor = true;
            // 
            // button5
            // 
            this.button5.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.button5.ImageAlign = System.Drawing.ContentAlignment.TopCenter;
            this.button5.ImageIndex = 4;
            this.button5.ImageList = this.imageList1;
            this.button5.Location = new System.Drawing.Point(127, 122);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(106, 107);
            this.button5.TabIndex = 4;
            this.button5.Text = "數據錄入";
            this.button5.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            this.button5.UseVisualStyleBackColor = true;
            // 
            // button6
            // 
            this.button6.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.button6.ImageAlign = System.Drawing.ContentAlignment.TopCenter;
            this.button6.ImageIndex = 5;
            this.button6.ImageList = this.imageList1;
            this.button6.Location = new System.Drawing.Point(127, 12);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(108, 104);
            this.button6.TabIndex = 5;
            this.button6.Text = "月底統計";
            this.button6.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            this.button6.UseVisualStyleBackColor = true;
            // 
            // frmMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.Control;
            this.ClientSize = new System.Drawing.Size(365, 238);
            this.Controls.Add(this.button6);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Name = "frmMain";
            this.Text = "財務憑證管理系統";
            this.Load += new System.EventHandler(this.frmMain_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ImageList imageList1;
        public System.Windows.Forms.Button button1;
        public System.Windows.Forms.Button button2;
        public System.Windows.Forms.Button button3;
        public System.Windows.Forms.Button button4;
        public System.Windows.Forms.Button button5;
        public System.Windows.Forms.Button button6;
    }
}