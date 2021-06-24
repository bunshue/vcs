namespace _14._5_1
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
            this.components = new System.ComponentModel.Container();
            this.heroLabel = new System.Windows.Forms.Label();
            this.monsterLabel = new System.Windows.Forms.Label();
            this.defenseButton = new System.Windows.Forms.Button();
            this.dodgeButton = new System.Windows.Forms.Button();
            this.attackButton = new System.Windows.Forms.Button();
            this.powerButton = new System.Windows.Forms.Button();
            this.logList = new System.Windows.Forms.ListBox();
            this.logLabel = new System.Windows.Forms.Label();
            this.notifyIcon1 = new System.Windows.Forms.NotifyIcon(this.components);
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.SuspendLayout();
            // 
            // heroLabel
            // 
            this.heroLabel.AutoSize = true;
            this.heroLabel.Location = new System.Drawing.Point(12, 9);
            this.heroLabel.Name = "heroLabel";
            this.heroLabel.Size = new System.Drawing.Size(56, 12);
            this.heroLabel.TabIndex = 0;
            this.heroLabel.Text = "勇者狀態:";
            // 
            // monsterLabel
            // 
            this.monsterLabel.AutoSize = true;
            this.monsterLabel.Location = new System.Drawing.Point(243, 9);
            this.monsterLabel.Name = "monsterLabel";
            this.monsterLabel.Size = new System.Drawing.Size(56, 12);
            this.monsterLabel.TabIndex = 1;
            this.monsterLabel.Text = "怪物狀態:";
            // 
            // defenseButton
            // 
            this.defenseButton.Location = new System.Drawing.Point(14, 75);
            this.defenseButton.Name = "defenseButton";
            this.defenseButton.Size = new System.Drawing.Size(75, 23);
            this.defenseButton.TabIndex = 2;
            this.defenseButton.Text = "防禦";
            this.defenseButton.UseVisualStyleBackColor = true;
            this.defenseButton.Click += new System.EventHandler(this.defenseButton_Click);
            // 
            // dodgeButton
            // 
            this.dodgeButton.Location = new System.Drawing.Point(14, 104);
            this.dodgeButton.Name = "dodgeButton";
            this.dodgeButton.Size = new System.Drawing.Size(75, 23);
            this.dodgeButton.TabIndex = 3;
            this.dodgeButton.Text = "閃躲";
            this.dodgeButton.UseVisualStyleBackColor = true;
            this.dodgeButton.Click += new System.EventHandler(this.dodgeButton_Click);
            // 
            // attackButton
            // 
            this.attackButton.Location = new System.Drawing.Point(243, 75);
            this.attackButton.Name = "attackButton";
            this.attackButton.Size = new System.Drawing.Size(75, 23);
            this.attackButton.TabIndex = 4;
            this.attackButton.Text = "一般攻擊";
            this.attackButton.UseVisualStyleBackColor = true;
            this.attackButton.Click += new System.EventHandler(this.attackButton_Click);
            // 
            // powerButton
            // 
            this.powerButton.Location = new System.Drawing.Point(243, 104);
            this.powerButton.Name = "powerButton";
            this.powerButton.Size = new System.Drawing.Size(75, 23);
            this.powerButton.TabIndex = 5;
            this.powerButton.Text = "強力攻擊";
            this.powerButton.UseVisualStyleBackColor = true;
            this.powerButton.Click += new System.EventHandler(this.powerButton_Click);
            // 
            // logList
            // 
            this.logList.FormattingEnabled = true;
            this.logList.ItemHeight = 12;
            this.logList.Location = new System.Drawing.Point(12, 145);
            this.logList.Name = "logList";
            this.logList.Size = new System.Drawing.Size(306, 316);
            this.logList.TabIndex = 6;
            // 
            // logLabel
            // 
            this.logLabel.AutoSize = true;
            this.logLabel.Location = new System.Drawing.Point(12, 130);
            this.logLabel.Name = "logLabel";
            this.logLabel.Size = new System.Drawing.Size(56, 12);
            this.logLabel.TabIndex = 7;
            this.logLabel.Text = "戰鬥歷程:";
            // 
            // notifyIcon1
            // 
            this.notifyIcon1.Text = "notifyIcon1";
            this.notifyIcon1.Visible = true;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(334, 6);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(329, 455);
            this.richTextBox1.TabIndex = 8;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(675, 476);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.logLabel);
            this.Controls.Add(this.logList);
            this.Controls.Add(this.powerButton);
            this.Controls.Add(this.attackButton);
            this.Controls.Add(this.dodgeButton);
            this.Controls.Add(this.defenseButton);
            this.Controls.Add(this.monsterLabel);
            this.Controls.Add(this.heroLabel);
            this.Name = "Form1";
            this.Text = "勇者怪物戰鬥遊戲";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label heroLabel;
        private System.Windows.Forms.Label monsterLabel;
        private System.Windows.Forms.Button defenseButton;
        private System.Windows.Forms.Button dodgeButton;
        private System.Windows.Forms.Button attackButton;
        private System.Windows.Forms.Button powerButton;
        private System.Windows.Forms.ListBox logList;
        private System.Windows.Forms.Label logLabel;
        private System.Windows.Forms.NotifyIcon notifyIcon1;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

