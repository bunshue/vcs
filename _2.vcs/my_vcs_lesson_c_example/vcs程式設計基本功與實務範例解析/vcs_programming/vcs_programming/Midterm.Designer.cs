namespace vcs_programming
{
    partial class Midterm
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
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.檔案ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.mLoad = new System.Windows.Forms.ToolStripMenuItem();
            this.mSave = new System.Windows.Forms.ToolStripMenuItem();
            this.結束ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.成績處理ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.mSumRank = new System.Windows.Forms.ToolStripMenuItem();
            this.mScoreStatistics = new System.Windows.Forms.ToolStripMenuItem();
            this.lblCounter = new System.Windows.Forms.Label();
            this.txtOutput = new System.Windows.Forms.TextBox();
            this.btn_input = new System.Windows.Forms.Button();
            this.txtMath = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.txtChinese = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.txtName = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.sfdSave = new System.Windows.Forms.SaveFileDialog();
            this.ofdOpen = new System.Windows.Forms.OpenFileDialog();
            this.menuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.檔案ToolStripMenuItem,
            this.成績處理ToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(444, 24);
            this.menuStrip1.TabIndex = 0;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // 檔案ToolStripMenuItem
            // 
            this.檔案ToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mLoad,
            this.mSave,
            this.結束ToolStripMenuItem});
            this.檔案ToolStripMenuItem.Name = "檔案ToolStripMenuItem";
            this.檔案ToolStripMenuItem.Size = new System.Drawing.Size(44, 20);
            this.檔案ToolStripMenuItem.Text = "檔案";
            // 
            // mLoad
            // 
            this.mLoad.Name = "mLoad";
            this.mLoad.Size = new System.Drawing.Size(124, 22);
            this.mLoad.Text = "載入成績";
            this.mLoad.Click += new System.EventHandler(this.mLoad_Click);
            // 
            // mSave
            // 
            this.mSave.Name = "mSave";
            this.mSave.Size = new System.Drawing.Size(124, 22);
            this.mSave.Text = "儲存成績";
            this.mSave.Click += new System.EventHandler(this.mSave_Click);
            // 
            // 結束ToolStripMenuItem
            // 
            this.結束ToolStripMenuItem.Name = "結束ToolStripMenuItem";
            this.結束ToolStripMenuItem.Size = new System.Drawing.Size(124, 22);
            this.結束ToolStripMenuItem.Text = "結束";
            this.結束ToolStripMenuItem.Click += new System.EventHandler(this.結束ToolStripMenuItem_Click);
            // 
            // 成績處理ToolStripMenuItem
            // 
            this.成績處理ToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mSumRank,
            this.mScoreStatistics});
            this.成績處理ToolStripMenuItem.Name = "成績處理ToolStripMenuItem";
            this.成績處理ToolStripMenuItem.Size = new System.Drawing.Size(68, 20);
            this.成績處理ToolStripMenuItem.Text = "成績處理";
            // 
            // mSumRank
            // 
            this.mSumRank.Name = "mSumRank";
            this.mSumRank.Size = new System.Drawing.Size(136, 22);
            this.mSumRank.Text = "總分與名次";
            this.mSumRank.Click += new System.EventHandler(this.mSumRank_Click);
            // 
            // mScoreStatistics
            // 
            this.mScoreStatistics.Name = "mScoreStatistics";
            this.mScoreStatistics.Size = new System.Drawing.Size(136, 22);
            this.mScoreStatistics.Text = "分數統計";
            this.mScoreStatistics.Click += new System.EventHandler(this.mScoreStatistics_Click);
            // 
            // lblCounter
            // 
            this.lblCounter.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblCounter.Location = new System.Drawing.Point(12, 42);
            this.lblCounter.Name = "lblCounter";
            this.lblCounter.Size = new System.Drawing.Size(255, 24);
            this.lblCounter.TabIndex = 20;
            this.lblCounter.Text = "共有0人";
            this.lblCounter.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // txtOutput
            // 
            this.txtOutput.Location = new System.Drawing.Point(12, 72);
            this.txtOutput.Multiline = true;
            this.txtOutput.Name = "txtOutput";
            this.txtOutput.ReadOnly = true;
            this.txtOutput.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.txtOutput.Size = new System.Drawing.Size(255, 244);
            this.txtOutput.TabIndex = 19;
            this.txtOutput.WordWrap = false;
            // 
            // btn_input
            // 
            this.btn_input.Location = new System.Drawing.Point(285, 150);
            this.btn_input.Name = "btn_input";
            this.btn_input.Size = new System.Drawing.Size(143, 27);
            this.btn_input.TabIndex = 4;
            this.btn_input.Text = "輸入資料";
            this.btn_input.UseVisualStyleBackColor = true;
            this.btn_input.Click += new System.EventHandler(this.btn_input_Click);
            // 
            // txtMath
            // 
            this.txtMath.Location = new System.Drawing.Point(328, 117);
            this.txtMath.Name = "txtMath";
            this.txtMath.Size = new System.Drawing.Size(100, 27);
            this.txtMath.TabIndex = 3;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(282, 128);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(40, 16);
            this.label3.TabIndex = 25;
            this.label3.Text = "數學";
            // 
            // txtChinese
            // 
            this.txtChinese.Location = new System.Drawing.Point(328, 84);
            this.txtChinese.Name = "txtChinese";
            this.txtChinese.Size = new System.Drawing.Size(100, 27);
            this.txtChinese.TabIndex = 2;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(282, 95);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(40, 16);
            this.label2.TabIndex = 23;
            this.label2.Text = "國文";
            // 
            // txtName
            // 
            this.txtName.Location = new System.Drawing.Point(328, 51);
            this.txtName.Name = "txtName";
            this.txtName.Size = new System.Drawing.Size(100, 27);
            this.txtName.TabIndex = 1;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(282, 62);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(40, 16);
            this.label1.TabIndex = 21;
            this.label1.Text = "姓名";
            // 
            // sfdSave
            // 
            this.sfdSave.Filter = "資料檔案(*.txt)|*.txt|二元檔案(*.dat)|*.dat|所有檔案(*.*)|*.*";
            this.sfdSave.RestoreDirectory = true;
            // 
            // ofdOpen
            // 
            this.ofdOpen.Filter = "資料檔案(*.txt)|*.txt|二元檔案(*.dat)|*.dat|所有檔案(*.*)|*.*";
            this.ofdOpen.RestoreDirectory = true;
            // 
            // Midterm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(444, 338);
            this.Controls.Add(this.btn_input);
            this.Controls.Add(this.txtMath);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.txtChinese);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.txtName);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.lblCounter);
            this.Controls.Add(this.txtOutput);
            this.Controls.Add(this.menuStrip1);
            this.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.MainMenuStrip = this.menuStrip1;
            this.Margin = new System.Windows.Forms.Padding(4);
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "Midterm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Midterm";
            this.Load += new System.EventHandler(this.Midterm_Load);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem 檔案ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem mLoad;
        private System.Windows.Forms.ToolStripMenuItem 成績處理ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem mSave;
        private System.Windows.Forms.ToolStripMenuItem 結束ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem mSumRank;
        private System.Windows.Forms.ToolStripMenuItem mScoreStatistics;
        private System.Windows.Forms.Label lblCounter;
        private System.Windows.Forms.TextBox txtOutput;
        private System.Windows.Forms.Button btn_input;
        private System.Windows.Forms.TextBox txtMath;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox txtChinese;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox txtName;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.SaveFileDialog sfdSave;
        private System.Windows.Forms.OpenFileDialog ofdOpen;
    }
}