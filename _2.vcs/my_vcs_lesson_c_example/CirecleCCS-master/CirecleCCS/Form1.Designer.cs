namespace CirecleCCS
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
        /// 设计器支持所需的方法 - 不要修改
        /// 使用代码编辑器修改此方法的内容。
        /// </summary>
        private void InitializeComponent()
        {
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.label_xval = new System.Windows.Forms.Label();
            this.label_yval = new System.Windows.Forms.Label();
            this.labelccsX = new System.Windows.Forms.Label();
            this.label_CcsY = new System.Windows.Forms.Label();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox1
            // 
            this.pictureBox1.BackColor = System.Drawing.Color.Black;
            this.pictureBox1.Location = new System.Drawing.Point(12, 12);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(541, 417);
            this.pictureBox1.TabIndex = 0;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.Paint += new System.Windows.Forms.PaintEventHandler(this.pictureBox1_Paint);
            this.pictureBox1.MouseDown += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseDown);
            this.pictureBox1.MouseMove += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseMove);
            this.pictureBox1.MouseUp += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseUp);
            // 
            // label_xval
            // 
            this.label_xval.AutoSize = true;
            this.label_xval.Font = new System.Drawing.Font("Courier New", 9F);
            this.label_xval.Location = new System.Drawing.Point(830, 9);
            this.label_xval.Name = "label_xval";
            this.label_xval.Size = new System.Drawing.Size(35, 15);
            this.label_xval.TabIndex = 3;
            this.label_xval.Text = "XVal";
            // 
            // label_yval
            // 
            this.label_yval.AutoSize = true;
            this.label_yval.Font = new System.Drawing.Font("Courier New", 9F);
            this.label_yval.Location = new System.Drawing.Point(830, 35);
            this.label_yval.Name = "label_yval";
            this.label_yval.Size = new System.Drawing.Size(35, 15);
            this.label_yval.TabIndex = 3;
            this.label_yval.Text = "YVal";
            // 
            // labelccsX
            // 
            this.labelccsX.AutoSize = true;
            this.labelccsX.Font = new System.Drawing.Font("Courier New", 9F);
            this.labelccsX.Location = new System.Drawing.Point(830, 60);
            this.labelccsX.Name = "labelccsX";
            this.labelccsX.Size = new System.Drawing.Size(35, 15);
            this.labelccsX.TabIndex = 3;
            this.labelccsX.Text = "CcsX";
            // 
            // label_CcsY
            // 
            this.label_CcsY.AutoSize = true;
            this.label_CcsY.Font = new System.Drawing.Font("Courier New", 9F);
            this.label_CcsY.Location = new System.Drawing.Point(830, 86);
            this.label_CcsY.Name = "label_CcsY";
            this.label_CcsY.Size = new System.Drawing.Size(35, 15);
            this.label_CcsY.TabIndex = 3;
            this.label_CcsY.Text = "CcsY";
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(821, 161);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(333, 412);
            this.richTextBox1.TabIndex = 4;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1166, 586);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.label_CcsY);
            this.Controls.Add(this.labelccsX);
            this.Controls.Add(this.label_yval);
            this.Controls.Add(this.label_xval);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Label label_xval;
        private System.Windows.Forms.Label label_yval;
        private System.Windows.Forms.Label labelccsX;
        private System.Windows.Forms.Label label_CcsY;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

