namespace vcs_programming
{
    partial class ScoreFile
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.txtName = new System.Windows.Forms.TextBox();
            this.txtChinese = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.txtMath = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.btn_input = new System.Windows.Forms.Button();
            this.txtOutput = new System.Windows.Forms.TextBox();
            this.lblCounter = new System.Windows.Forms.Label();
            this.btn_read = new System.Windows.Forms.Button();
            this.btn_save = new System.Windows.Forms.Button();
            this.sfdSave = new System.Windows.Forms.SaveFileDialog();
            this.ofdOpen = new System.Windows.Forms.OpenFileDialog();
            this.btn_b_read = new System.Windows.Forms.Button();
            this.btn_b_save = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(21, 23);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(40, 16);
            this.label1.TabIndex = 0;
            this.label1.Text = "姓名";
            // 
            // txtName
            // 
            this.txtName.Location = new System.Drawing.Point(67, 12);
            this.txtName.Name = "txtName";
            this.txtName.Size = new System.Drawing.Size(100, 27);
            this.txtName.TabIndex = 1;
            // 
            // txtChinese
            // 
            this.txtChinese.Location = new System.Drawing.Point(67, 45);
            this.txtChinese.Name = "txtChinese";
            this.txtChinese.Size = new System.Drawing.Size(100, 27);
            this.txtChinese.TabIndex = 3;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(21, 56);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(40, 16);
            this.label2.TabIndex = 2;
            this.label2.Text = "國文";
            // 
            // txtMath
            // 
            this.txtMath.Location = new System.Drawing.Point(67, 78);
            this.txtMath.Name = "txtMath";
            this.txtMath.Size = new System.Drawing.Size(100, 27);
            this.txtMath.TabIndex = 5;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(21, 89);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(40, 16);
            this.label3.TabIndex = 4;
            this.label3.Text = "數學";
            // 
            // btn_input
            // 
            this.btn_input.Location = new System.Drawing.Point(24, 111);
            this.btn_input.Name = "btn_input";
            this.btn_input.Size = new System.Drawing.Size(143, 27);
            this.btn_input.TabIndex = 7;
            this.btn_input.Text = "輸入資料";
            this.btn_input.UseVisualStyleBackColor = true;
            this.btn_input.Click += new System.EventHandler(this.btn_input_Click);
            // 
            // txtOutput
            // 
            this.txtOutput.Location = new System.Drawing.Point(183, 45);
            this.txtOutput.Multiline = true;
            this.txtOutput.Name = "txtOutput";
            this.txtOutput.ReadOnly = true;
            this.txtOutput.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.txtOutput.Size = new System.Drawing.Size(225, 232);
            this.txtOutput.TabIndex = 8;
            this.txtOutput.WordWrap = false;
            // 
            // lblCounter
            // 
            this.lblCounter.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblCounter.Location = new System.Drawing.Point(183, 15);
            this.lblCounter.Name = "lblCounter";
            this.lblCounter.Size = new System.Drawing.Size(225, 24);
            this.lblCounter.TabIndex = 9;
            this.lblCounter.Text = "共有0人";
            this.lblCounter.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // btn_read
            // 
            this.btn_read.Location = new System.Drawing.Point(24, 217);
            this.btn_read.Name = "btn_read";
            this.btn_read.Size = new System.Drawing.Size(143, 27);
            this.btn_read.TabIndex = 10;
            this.btn_read.Text = "載入資料";
            this.btn_read.UseVisualStyleBackColor = true;
            this.btn_read.Click += new System.EventHandler(this.btn_read_Click);
            // 
            // btn_save
            // 
            this.btn_save.Location = new System.Drawing.Point(24, 250);
            this.btn_save.Name = "btn_save";
            this.btn_save.Size = new System.Drawing.Size(143, 27);
            this.btn_save.TabIndex = 11;
            this.btn_save.Text = "儲存資料";
            this.btn_save.UseVisualStyleBackColor = true;
            this.btn_save.Click += new System.EventHandler(this.btn_save_Click);
            // 
            // sfdSave
            // 
            this.sfdSave.Filter = "文字檔案(*.txt)|*.txt|二元檔案(*.dat)|*.dat|所有檔案(*.*)|*.*";
            this.sfdSave.RestoreDirectory = true;
            // 
            // ofdOpen
            // 
            this.ofdOpen.Filter = "資料檔案(*.txt)|*.txt|二元檔案(*.dat)|*.dat|所有檔案(*.*)|*.*";
            this.ofdOpen.RestoreDirectory = true;
            // 
            // btn_b_read
            // 
            this.btn_b_read.Location = new System.Drawing.Point(24, 283);
            this.btn_b_read.Name = "btn_b_read";
            this.btn_b_read.Size = new System.Drawing.Size(187, 27);
            this.btn_b_read.TabIndex = 12;
            this.btn_b_read.Text = "載入資料(二進位檔案)";
            this.btn_b_read.UseVisualStyleBackColor = true;
            this.btn_b_read.Click += new System.EventHandler(this.btn_b_read_Click);
            // 
            // btn_b_save
            // 
            this.btn_b_save.Location = new System.Drawing.Point(24, 316);
            this.btn_b_save.Name = "btn_b_save";
            this.btn_b_save.Size = new System.Drawing.Size(191, 27);
            this.btn_b_save.TabIndex = 13;
            this.btn_b_save.Text = "儲存資料(二進位檔案)";
            this.btn_b_save.UseVisualStyleBackColor = true;
            this.btn_b_save.Click += new System.EventHandler(this.btn_b_save_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(414, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(655, 561);
            this.richTextBox1.TabIndex = 14;
            this.richTextBox1.Text = "";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(265, 283);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(143, 27);
            this.button1.TabIndex = 15;
            this.button1.Text = "清除資料";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // ScoreFile
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1081, 585);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.btn_b_save);
            this.Controls.Add(this.btn_b_read);
            this.Controls.Add(this.btn_save);
            this.Controls.Add(this.btn_read);
            this.Controls.Add(this.lblCounter);
            this.Controls.Add(this.txtOutput);
            this.Controls.Add(this.btn_input);
            this.Controls.Add(this.txtMath);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.txtChinese);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.txtName);
            this.Controls.Add(this.label1);
            this.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Margin = new System.Windows.Forms.Padding(4);
            this.Name = "ScoreFile";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "成績存檔讀取";
            this.Load += new System.EventHandler(this.ScoreFile_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txtName;
        private System.Windows.Forms.TextBox txtChinese;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox txtMath;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Button btn_input;
        private System.Windows.Forms.TextBox txtOutput;
        private System.Windows.Forms.Label lblCounter;
        private System.Windows.Forms.Button btn_read;
        private System.Windows.Forms.Button btn_save;
        private System.Windows.Forms.SaveFileDialog sfdSave;
        private System.Windows.Forms.OpenFileDialog ofdOpen;
        private System.Windows.Forms.Button btn_b_read;
        private System.Windows.Forms.Button btn_b_save;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button1;
    }
}