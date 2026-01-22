namespace vcs_ClockA
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
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改這個方法的內容。
        ///
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.timeGroup = new System.Windows.Forms.GroupBox();
            this.timeOption1 = new System.Windows.Forms.RadioButton();
            this.timeOption2 = new System.Windows.Forms.RadioButton();
            this.timeOption3 = new System.Windows.Forms.RadioButton();
            this.clockText = new System.Windows.Forms.TextBox();
            this.startButton = new System.Windows.Forms.Button();
            this.progressBar1 = new System.Windows.Forms.ProgressBar();
            this.timeGroup.SuspendLayout();
            this.SuspendLayout();
            // 
            // timer1
            // 
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // timeGroup
            // 
            this.timeGroup.Controls.Add(this.timeOption1);
            this.timeGroup.Controls.Add(this.timeOption2);
            this.timeGroup.Controls.Add(this.timeOption3);
            this.timeGroup.Location = new System.Drawing.Point(12, 12);
            this.timeGroup.Name = "timeGroup";
            this.timeGroup.Size = new System.Drawing.Size(113, 93);
            this.timeGroup.TabIndex = 1;
            this.timeGroup.TabStop = false;
            this.timeGroup.Text = "倒數時間長短";
            // 
            // timeOption1
            // 
            this.timeOption1.AutoSize = true;
            this.timeOption1.Location = new System.Drawing.Point(6, 21);
            this.timeOption1.Name = "timeOption1";
            this.timeOption1.Size = new System.Drawing.Size(59, 16);
            this.timeOption1.TabIndex = 10;
            this.timeOption1.Text = "五分鐘";
            this.timeOption1.UseVisualStyleBackColor = true;
            this.timeOption1.CheckedChanged += new System.EventHandler(this.radioButton_CheckedChanged);
            // 
            // timeOption2
            // 
            this.timeOption2.AutoSize = true;
            this.timeOption2.Location = new System.Drawing.Point(6, 43);
            this.timeOption2.Name = "timeOption2";
            this.timeOption2.Size = new System.Drawing.Size(59, 16);
            this.timeOption2.TabIndex = 8;
            this.timeOption2.Text = "三分鐘";
            this.timeOption2.UseVisualStyleBackColor = true;
            this.timeOption2.CheckedChanged += new System.EventHandler(this.radioButton_CheckedChanged);
            // 
            // timeOption3
            // 
            this.timeOption3.AutoSize = true;
            this.timeOption3.Checked = true;
            this.timeOption3.Location = new System.Drawing.Point(6, 65);
            this.timeOption3.Name = "timeOption3";
            this.timeOption3.Size = new System.Drawing.Size(59, 16);
            this.timeOption3.TabIndex = 9;
            this.timeOption3.TabStop = true;
            this.timeOption3.Text = "一分鐘";
            this.timeOption3.UseVisualStyleBackColor = true;
            this.timeOption3.CheckedChanged += new System.EventHandler(this.radioButton_CheckedChanged);
            // 
            // clockText
            // 
            this.clockText.Location = new System.Drawing.Point(12, 111);
            this.clockText.Name = "clockText";
            this.clockText.Size = new System.Drawing.Size(75, 22);
            this.clockText.TabIndex = 2;
            // 
            // startButton
            // 
            this.startButton.Location = new System.Drawing.Point(188, 12);
            this.startButton.Name = "startButton";
            this.startButton.Size = new System.Drawing.Size(69, 88);
            this.startButton.TabIndex = 3;
            this.startButton.Text = "開始倒數";
            this.startButton.UseVisualStyleBackColor = true;
            this.startButton.Click += new System.EventHandler(this.startButton_Click);
            // 
            // progressBar1
            // 
            this.progressBar1.Location = new System.Drawing.Point(93, 111);
            this.progressBar1.Name = "progressBar1";
            this.progressBar1.Size = new System.Drawing.Size(226, 23);
            this.progressBar1.TabIndex = 4;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(614, 470);
            this.Controls.Add(this.progressBar1);
            this.Controls.Add(this.startButton);
            this.Controls.Add(this.clockText);
            this.Controls.Add(this.timeGroup);
            this.Name = "Form1";
            this.Text = "倒數計時器";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.timeGroup.ResumeLayout(false);
            this.timeGroup.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.GroupBox timeGroup;
        private System.Windows.Forms.TextBox clockText;
        private System.Windows.Forms.Button startButton;
        private System.Windows.Forms.ProgressBar progressBar1;
        private System.Windows.Forms.RadioButton timeOption1;
        private System.Windows.Forms.RadioButton timeOption2;
        private System.Windows.Forms.RadioButton timeOption3;










    }
}

