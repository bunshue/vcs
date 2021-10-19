namespace EX30
{
    partial class Form1
    {
        /// <summary>
        /// 必需的设计器变量。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的资源。
        /// </summary>
        /// <param name="disposing">如果应释放托管资源，为 true；否则为 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 窗体设计器生成的代码

        /// <summary>
        /// 设计器支持所需的方法 - 不要
        /// 使用代码编辑器修改此方法的内容。
        /// </summary>
        private void InitializeComponent()
        {
            this.Create1DBtn = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.ContentTxt = new System.Windows.Forms.TextBox();
            this.Create2DBtn = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.ImgPathTxt = new System.Windows.Forms.TextBox();
            this.OpenImgBtn = new System.Windows.Forms.Button();
            this.Read1DBtn = new System.Windows.Forms.Button();
            this.Read2DBtn = new System.Windows.Forms.Button();
            this.label3 = new System.Windows.Forms.Label();
            this.barCodeImg = new System.Windows.Forms.PictureBox();
            this.Creat2DOfHaveLogoBtn = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.barCodeImg)).BeginInit();
            this.SuspendLayout();
            // 
            // Create1DBtn
            // 
            this.Create1DBtn.Location = new System.Drawing.Point(357, 12);
            this.Create1DBtn.Name = "Create1DBtn";
            this.Create1DBtn.Size = new System.Drawing.Size(75, 23);
            this.Create1DBtn.TabIndex = 0;
            this.Create1DBtn.Text = "生成一维码";
            this.Create1DBtn.UseVisualStyleBackColor = true;
            this.Create1DBtn.Click += new System.EventHandler(this.Create1DBtn_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(6, 17);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(65, 12);
            this.label1.TabIndex = 1;
            this.label1.Text = "条码内容：";
            // 
            // ContentTxt
            // 
            this.ContentTxt.Location = new System.Drawing.Point(65, 12);
            this.ContentTxt.Name = "ContentTxt";
            this.ContentTxt.Size = new System.Drawing.Size(269, 22);
            this.ContentTxt.TabIndex = 2;
            this.ContentTxt.Text = "9787302380979";
            // 
            // Create2DBtn
            // 
            this.Create2DBtn.Location = new System.Drawing.Point(457, 12);
            this.Create2DBtn.Name = "Create2DBtn";
            this.Create2DBtn.Size = new System.Drawing.Size(75, 23);
            this.Create2DBtn.TabIndex = 3;
            this.Create2DBtn.Text = "生成二维码";
            this.Create2DBtn.UseVisualStyleBackColor = true;
            this.Create2DBtn.Click += new System.EventHandler(this.Create2DBtn_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(6, 47);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(65, 12);
            this.label2.TabIndex = 4;
            this.label2.Text = "图片路径：";
            // 
            // ImgPathTxt
            // 
            this.ImgPathTxt.Location = new System.Drawing.Point(65, 41);
            this.ImgPathTxt.Name = "ImgPathTxt";
            this.ImgPathTxt.ReadOnly = true;
            this.ImgPathTxt.Size = new System.Drawing.Size(197, 22);
            this.ImgPathTxt.TabIndex = 5;
            // 
            // OpenImgBtn
            // 
            this.OpenImgBtn.Location = new System.Drawing.Point(268, 39);
            this.OpenImgBtn.Name = "OpenImgBtn";
            this.OpenImgBtn.Size = new System.Drawing.Size(66, 23);
            this.OpenImgBtn.TabIndex = 6;
            this.OpenImgBtn.Text = "打开图片";
            this.OpenImgBtn.UseVisualStyleBackColor = true;
            this.OpenImgBtn.Click += new System.EventHandler(this.OpenImgBtn_Click);
            // 
            // Read1DBtn
            // 
            this.Read1DBtn.Location = new System.Drawing.Point(357, 39);
            this.Read1DBtn.Name = "Read1DBtn";
            this.Read1DBtn.Size = new System.Drawing.Size(75, 23);
            this.Read1DBtn.TabIndex = 7;
            this.Read1DBtn.Text = "读取一维码";
            this.Read1DBtn.UseVisualStyleBackColor = true;
            this.Read1DBtn.Click += new System.EventHandler(this.Read1DBtn_Click);
            // 
            // Read2DBtn
            // 
            this.Read2DBtn.Location = new System.Drawing.Point(456, 39);
            this.Read2DBtn.Name = "Read2DBtn";
            this.Read2DBtn.Size = new System.Drawing.Size(75, 23);
            this.Read2DBtn.TabIndex = 8;
            this.Read2DBtn.Text = "读取二维码";
            this.Read2DBtn.UseVisualStyleBackColor = true;
            this.Read2DBtn.Click += new System.EventHandler(this.Read2DBtn_Click);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(6, 76);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(41, 12);
            this.label3.TabIndex = 9;
            this.label3.Text = "图片：";
            // 
            // barCodeImg
            // 
            this.barCodeImg.Location = new System.Drawing.Point(8, 91);
            this.barCodeImg.Name = "barCodeImg";
            this.barCodeImg.Size = new System.Drawing.Size(340, 223);
            this.barCodeImg.TabIndex = 10;
            this.barCodeImg.TabStop = false;
            // 
            // Creat2DOfHaveLogoBtn
            // 
            this.Creat2DOfHaveLogoBtn.Location = new System.Drawing.Point(410, 91);
            this.Creat2DOfHaveLogoBtn.Name = "Creat2DOfHaveLogoBtn";
            this.Creat2DOfHaveLogoBtn.Size = new System.Drawing.Size(121, 23);
            this.Creat2DOfHaveLogoBtn.TabIndex = 11;
            this.Creat2DOfHaveLogoBtn.Text = "生成带Logo二维码";
            this.Creat2DOfHaveLogoBtn.UseVisualStyleBackColor = true;
            this.Creat2DOfHaveLogoBtn.Click += new System.EventHandler(this.Creat2DOfHaveLogoBtn_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(821, 550);
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
            this.Text = "条形码";
            ((System.ComponentModel.ISupportInitialize)(this.barCodeImg)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button Create1DBtn;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox ContentTxt;
        private System.Windows.Forms.Button Create2DBtn;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox ImgPathTxt;
        private System.Windows.Forms.Button OpenImgBtn;
        private System.Windows.Forms.Button Read1DBtn;
        private System.Windows.Forms.Button Read2DBtn;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.PictureBox barCodeImg;
        private System.Windows.Forms.Button Creat2DOfHaveLogoBtn;

    }
}

