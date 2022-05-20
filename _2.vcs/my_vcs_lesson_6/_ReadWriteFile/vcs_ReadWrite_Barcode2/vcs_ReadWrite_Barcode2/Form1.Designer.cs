namespace vcs_ReadWrite_Barcode2
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
            this.Creat2DOfHaveLogoBtn = new System.Windows.Forms.Button();
            this.barCodeImg = new System.Windows.Forms.PictureBox();
            this.label3 = new System.Windows.Forms.Label();
            this.Read2DBtn = new System.Windows.Forms.Button();
            this.Read1DBtn = new System.Windows.Forms.Button();
            this.OpenImgBtn = new System.Windows.Forms.Button();
            this.ImgPathTxt = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.Create2DBtn = new System.Windows.Forms.Button();
            this.ContentTxt = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.Create1DBtn = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            ((System.ComponentModel.ISupportInitialize)(this.barCodeImg)).BeginInit();
            this.SuspendLayout();
            // 
            // Creat2DOfHaveLogoBtn
            // 
            this.Creat2DOfHaveLogoBtn.Location = new System.Drawing.Point(416, 101);
            this.Creat2DOfHaveLogoBtn.Name = "Creat2DOfHaveLogoBtn";
            this.Creat2DOfHaveLogoBtn.Size = new System.Drawing.Size(121, 23);
            this.Creat2DOfHaveLogoBtn.TabIndex = 23;
            this.Creat2DOfHaveLogoBtn.Text = "生成带Logo二维码";
            this.Creat2DOfHaveLogoBtn.UseVisualStyleBackColor = true;
            this.Creat2DOfHaveLogoBtn.Click += new System.EventHandler(this.Creat2DOfHaveLogoBtn_Click);
            // 
            // barCodeImg
            // 
            this.barCodeImg.Location = new System.Drawing.Point(14, 101);
            this.barCodeImg.Name = "barCodeImg";
            this.barCodeImg.Size = new System.Drawing.Size(340, 223);
            this.barCodeImg.TabIndex = 22;
            this.barCodeImg.TabStop = false;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 86);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(41, 12);
            this.label3.TabIndex = 21;
            this.label3.Text = "图片：";
            // 
            // Read2DBtn
            // 
            this.Read2DBtn.Location = new System.Drawing.Point(462, 49);
            this.Read2DBtn.Name = "Read2DBtn";
            this.Read2DBtn.Size = new System.Drawing.Size(75, 23);
            this.Read2DBtn.TabIndex = 20;
            this.Read2DBtn.Text = "读取二维码";
            this.Read2DBtn.UseVisualStyleBackColor = true;
            this.Read2DBtn.Click += new System.EventHandler(this.Read2DBtn_Click);
            // 
            // Read1DBtn
            // 
            this.Read1DBtn.Location = new System.Drawing.Point(363, 49);
            this.Read1DBtn.Name = "Read1DBtn";
            this.Read1DBtn.Size = new System.Drawing.Size(75, 23);
            this.Read1DBtn.TabIndex = 19;
            this.Read1DBtn.Text = "读取一维码";
            this.Read1DBtn.UseVisualStyleBackColor = true;
            this.Read1DBtn.Click += new System.EventHandler(this.Read1DBtn_Click);
            // 
            // OpenImgBtn
            // 
            this.OpenImgBtn.Location = new System.Drawing.Point(274, 49);
            this.OpenImgBtn.Name = "OpenImgBtn";
            this.OpenImgBtn.Size = new System.Drawing.Size(66, 23);
            this.OpenImgBtn.TabIndex = 18;
            this.OpenImgBtn.Text = "打开图片";
            this.OpenImgBtn.UseVisualStyleBackColor = true;
            this.OpenImgBtn.Click += new System.EventHandler(this.OpenImgBtn_Click);
            // 
            // ImgPathTxt
            // 
            this.ImgPathTxt.Location = new System.Drawing.Point(71, 51);
            this.ImgPathTxt.Name = "ImgPathTxt";
            this.ImgPathTxt.ReadOnly = true;
            this.ImgPathTxt.Size = new System.Drawing.Size(197, 22);
            this.ImgPathTxt.TabIndex = 17;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 57);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(65, 12);
            this.label2.TabIndex = 16;
            this.label2.Text = "图片路径：";
            // 
            // Create2DBtn
            // 
            this.Create2DBtn.Location = new System.Drawing.Point(463, 22);
            this.Create2DBtn.Name = "Create2DBtn";
            this.Create2DBtn.Size = new System.Drawing.Size(75, 23);
            this.Create2DBtn.TabIndex = 15;
            this.Create2DBtn.Text = "生成二维码";
            this.Create2DBtn.UseVisualStyleBackColor = true;
            this.Create2DBtn.Click += new System.EventHandler(this.Create2DBtn_Click);
            // 
            // ContentTxt
            // 
            this.ContentTxt.Location = new System.Drawing.Point(71, 22);
            this.ContentTxt.Name = "ContentTxt";
            this.ContentTxt.Size = new System.Drawing.Size(269, 22);
            this.ContentTxt.TabIndex = 14;
            this.ContentTxt.Text = "9787302380979";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 27);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(65, 12);
            this.label1.TabIndex = 13;
            this.label1.Text = "条码内容：";
            // 
            // Create1DBtn
            // 
            this.Create1DBtn.Location = new System.Drawing.Point(363, 22);
            this.Create1DBtn.Name = "Create1DBtn";
            this.Create1DBtn.Size = new System.Drawing.Size(75, 23);
            this.Create1DBtn.TabIndex = 12;
            this.Create1DBtn.Text = "生成一维码";
            this.Create1DBtn.UseVisualStyleBackColor = true;
            this.Create1DBtn.Click += new System.EventHandler(this.Create1DBtn_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(567, 22);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(373, 596);
            this.richTextBox1.TabIndex = 24;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(952, 630);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.Creat2DOfHaveLogoBtn);
            this.Controls.Add(this.barCodeImg);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.Read2DBtn);
            this.Controls.Add(this.Read1DBtn);
            this.Controls.Add(this.OpenImgBtn);
            this.Controls.Add(this.ImgPathTxt);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.Create2DBtn);
            this.Controls.Add(this.ContentTxt);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.Create1DBtn);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.barCodeImg)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button Creat2DOfHaveLogoBtn;
        private System.Windows.Forms.PictureBox barCodeImg;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Button Read2DBtn;
        private System.Windows.Forms.Button Read1DBtn;
        private System.Windows.Forms.Button OpenImgBtn;
        private System.Windows.Forms.TextBox ImgPathTxt;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button Create2DBtn;
        private System.Windows.Forms.TextBox ContentTxt;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button Create1DBtn;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

