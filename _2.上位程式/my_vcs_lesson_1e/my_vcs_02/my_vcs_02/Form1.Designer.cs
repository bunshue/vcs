namespace my_vcs_02
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.button1 = new System.Windows.Forms.Button();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.textBox2 = new System.Windows.Forms.TextBox();
            this.button2 = new System.Windows.Forms.Button();
            this.folderBrowserDialog1 = new System.Windows.Forms.FolderBrowserDialog();
            this.label1 = new System.Windows.Forms.Label();
            this.textBox3 = new System.Windows.Forms.TextBox();
            this.button3 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.button6 = new System.Windows.Forms.Button();
            this.OpenComPortButton = new System.Windows.Forms.Button();
            this.button7 = new System.Windows.Forms.Button();
            this.SelectFile = new System.Windows.Forms.Button();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.label2 = new System.Windows.Forms.Label();
            this.button8 = new System.Windows.Forms.Button();
            this.label3 = new System.Windows.Forms.Label();
            this.button9 = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(40, 40);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(89, 35);
            this.button1.TabIndex = 0;
            this.button1.Text = "SelectDirectory";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(134, 40);
            this.textBox1.Multiline = true;
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(307, 33);
            this.textBox1.TabIndex = 6;
            // 
            // textBox2
            // 
            this.textBox2.Location = new System.Drawing.Point(40, 81);
            this.textBox2.Multiline = true;
            this.textBox2.Name = "textBox2";
            this.textBox2.Size = new System.Drawing.Size(496, 364);
            this.textBox2.TabIndex = 2;
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(40, 451);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(125, 37);
            this.button2.TabIndex = 3;
            this.button2.Text = "GetFileNames";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(581, 51);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(69, 12);
            this.label1.TabIndex = 7;
            this.label1.Text = "Folder name :";
            // 
            // textBox3
            // 
            this.textBox3.Location = new System.Drawing.Point(656, 41);
            this.textBox3.Multiline = true;
            this.textBox3.Name = "textBox3";
            this.textBox3.Size = new System.Drawing.Size(251, 34);
            this.textBox3.TabIndex = 8;
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(584, 91);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(141, 37);
            this.button3.TabIndex = 9;
            this.button3.Text = "CreateFolder";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(766, 91);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(141, 37);
            this.button4.TabIndex = 10;
            this.button4.Text = "DeleteFolder";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(583, 153);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(138, 33);
            this.button5.TabIndex = 11;
            this.button5.Text = "GetCruuentSystemDir";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // button6
            // 
            this.button6.Location = new System.Drawing.Point(765, 153);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(141, 33);
            this.button6.TabIndex = 12;
            this.button6.Text = "GetCurrentDirectory";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
            // 
            // OpenComPortButton
            // 
            this.OpenComPortButton.Location = new System.Drawing.Point(583, 207);
            this.OpenComPortButton.Name = "OpenComPortButton";
            this.OpenComPortButton.Size = new System.Drawing.Size(138, 40);
            this.OpenComPortButton.TabIndex = 0;
            this.OpenComPortButton.Text = "COM Close";
            this.OpenComPortButton.UseVisualStyleBackColor = true;
            this.OpenComPortButton.Click += new System.EventHandler(this.OpenComPortButton_Click);
            // 
            // button7
            // 
            this.button7.CausesValidation = false;
            this.button7.Location = new System.Drawing.Point(583, 282);
            this.button7.Name = "button7";
            this.button7.Size = new System.Drawing.Size(138, 40);
            this.button7.TabIndex = 13;
            this.button7.Text = "TestNetworkConnection";
            this.button7.UseVisualStyleBackColor = true;
            this.button7.Click += new System.EventHandler(this.button7_Click);
            // 
            // SelectFile
            // 
            this.SelectFile.Image = global::my_vcs_02.Properties.Resources._1431440286_folder_open;
            this.SelectFile.Location = new System.Drawing.Point(583, 359);
            this.SelectFile.Name = "SelectFile";
            this.SelectFile.Size = new System.Drawing.Size(126, 86);
            this.SelectFile.TabIndex = 14;
            this.SelectFile.UseVisualStyleBackColor = true;
            this.SelectFile.Click += new System.EventHandler(this.SelectFile_Click);
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(728, 396);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(0, 12);
            this.label2.TabIndex = 15;
            // 
            // button8
            // 
            this.button8.Location = new System.Drawing.Point(447, 41);
            this.button8.Name = "button8";
            this.button8.Size = new System.Drawing.Size(89, 35);
            this.button8.TabIndex = 16;
            this.button8.Text = "OpenDirectory";
            this.button8.UseVisualStyleBackColor = true;
            this.button8.Click += new System.EventHandler(this.button8_Click);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label3.Location = new System.Drawing.Point(588, 454);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(319, 24);
            this.label3.TabIndex = 17;
            this.label3.Text = "這也是Button，只是改了Image";
            // 
            // button9
            // 
            this.button9.BackColor = System.Drawing.Color.Red;
            this.button9.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button9.Location = new System.Drawing.Point(766, 294);
            this.button9.Name = "button9";
            this.button9.Size = new System.Drawing.Size(128, 77);
            this.button9.TabIndex = 18;
            this.button9.Text = "說明";
            this.button9.UseVisualStyleBackColor = false;
            this.button9.Click += new System.EventHandler(this.button9_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(962, 520);
            this.Controls.Add(this.button9);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.button8);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.SelectFile);
            this.Controls.Add(this.button7);
            this.Controls.Add(this.OpenComPortButton);
            this.Controls.Add(this.button6);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.textBox3);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.textBox2);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.button1);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "Form1";
            this.Text = "my_vcs_02";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button button1;
        public System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.TextBox textBox2;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.FolderBrowserDialog folderBrowserDialog1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox textBox3;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.Button OpenComPortButton;
        private System.Windows.Forms.Button button7;
        private System.Windows.Forms.Button SelectFile;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button button8;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Button button9;
    }
}

