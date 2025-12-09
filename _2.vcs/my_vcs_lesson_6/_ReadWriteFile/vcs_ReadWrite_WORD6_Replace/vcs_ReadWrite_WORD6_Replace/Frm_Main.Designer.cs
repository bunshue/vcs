namespace vcs_ReadWrite_WORD6_Replace
{
    partial class Form1
    {
        /// <summary>
        /// 必需的設計器變量。
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

        #region Windows 窗體設計器生成的代碼

        /// <summary>
        /// 設計器支持所需的方法 - 不要
        /// 使用代碼編輯器修改此方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.btn_Display = new System.Windows.Forms.Button();
            this.txt_Replace = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.txt_Find = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.txt_path = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.btn_Begin = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.btn_Display);
            this.groupBox1.Controls.Add(this.txt_Replace);
            this.groupBox1.Controls.Add(this.label4);
            this.groupBox1.Controls.Add(this.txt_Find);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Controls.Add(this.txt_path);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Controls.Add(this.btn_Begin);
            this.groupBox1.Location = new System.Drawing.Point(12, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(438, 149);
            this.groupBox1.TabIndex = 7;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "替換Word文檔中的字符串";
            // 
            // btn_Display
            // 
            this.btn_Display.Enabled = false;
            this.btn_Display.Location = new System.Drawing.Point(216, 113);
            this.btn_Display.Name = "btn_Display";
            this.btn_Display.Size = new System.Drawing.Size(105, 23);
            this.btn_Display.TabIndex = 15;
            this.btn_Display.Text = "顯示文件";
            this.btn_Display.UseVisualStyleBackColor = true;
            this.btn_Display.Click += new System.EventHandler(this.btn_Display_Click);
            // 
            // txt_Replace
            // 
            this.txt_Replace.Location = new System.Drawing.Point(266, 70);
            this.txt_Replace.Name = "txt_Replace";
            this.txt_Replace.ReadOnly = true;
            this.txt_Replace.Size = new System.Drawing.Size(72, 22);
            this.txt_Replace.TabIndex = 13;
            this.txt_Replace.Text = "lion-mouse";
            this.txt_Replace.TextChanged += new System.EventHandler(this.txt_Replace_TextChanged);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(192, 74);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(77, 12);
            this.label4.TabIndex = 14;
            this.label4.Text = "替換為字符：";
            // 
            // txt_Find
            // 
            this.txt_Find.Location = new System.Drawing.Point(104, 70);
            this.txt_Find.Name = "txt_Find";
            this.txt_Find.ReadOnly = true;
            this.txt_Find.Size = new System.Drawing.Size(72, 22);
            this.txt_Find.TabIndex = 8;
            this.txt_Find.Text = "字幕";
            this.txt_Find.TextChanged += new System.EventHandler(this.txt_Find_TextChanged);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(41, 74);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(65, 12);
            this.label2.TabIndex = 9;
            this.label2.Text = "查找字符：";
            // 
            // txt_path
            // 
            this.txt_path.Location = new System.Drawing.Point(105, 31);
            this.txt_path.Name = "txt_path";
            this.txt_path.ReadOnly = true;
            this.txt_path.Size = new System.Drawing.Size(311, 22);
            this.txt_path.TabIndex = 2;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(21, 34);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(89, 12);
            this.label1.TabIndex = 3;
            this.label1.Text = "打開文檔位置：";
            // 
            // btn_Begin
            // 
            this.btn_Begin.Enabled = false;
            this.btn_Begin.Location = new System.Drawing.Point(61, 113);
            this.btn_Begin.Name = "btn_Begin";
            this.btn_Begin.Size = new System.Drawing.Size(105, 23);
            this.btn_Begin.TabIndex = 0;
            this.btn_Begin.Text = "開始替換";
            this.btn_Begin.UseVisualStyleBackColor = true;
            this.btn_Begin.Click += new System.EventHandler(this.btn_Begin_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(12, 167);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(438, 382);
            this.richTextBox1.TabIndex = 8;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(558, 572);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox1);
            this.Name = "Form1";
            this.Text = "批量替換Word文檔中指定的字符串";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox txt_path;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button btn_Begin;
        private System.Windows.Forms.TextBox txt_Replace;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox txt_Find;
        private System.Windows.Forms.Button btn_Display;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}
