namespace vcs_MyEditor
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
            this.fontDialog1 = new System.Windows.Forms.FontDialog();
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.mFile = new System.Windows.Forms.ToolStripMenuItem();
            this.mOpen = new System.Windows.Forms.ToolStripMenuItem();
            this.mSave = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripSeparator2 = new System.Windows.Forms.ToolStripSeparator();
            this.mExit = new System.Windows.Forms.ToolStripMenuItem();
            this.mEdit = new System.Windows.Forms.ToolStripMenuItem();
            this.mUndo = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripSeparator3 = new System.Windows.Forms.ToolStripSeparator();
            this.mCut = new System.Windows.Forms.ToolStripMenuItem();
            this.mCopy = new System.Windows.Forms.ToolStripMenuItem();
            this.mPaste = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripSeparator4 = new System.Windows.Forms.ToolStripSeparator();
            this.mSelectAll = new System.Windows.Forms.ToolStripMenuItem();
            this.mSetting = new System.Windows.Forms.ToolStripMenuItem();
            this.mFont = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripSeparator1 = new System.Windows.Forms.ToolStripSeparator();
            this.mColor = new System.Windows.Forms.ToolStripMenuItem();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.colorDialog1 = new System.Windows.Forms.ColorDialog();
            this.saveFileDialog1 = new System.Windows.Forms.SaveFileDialog();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.menuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mFile,
            this.mEdit,
            this.mSetting});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(941, 24);
            this.menuStrip1.TabIndex = 1;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // mFile
            // 
            this.mFile.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mOpen,
            this.mSave,
            this.toolStripSeparator2,
            this.mExit});
            this.mFile.Name = "mFile";
            this.mFile.Size = new System.Drawing.Size(44, 20);
            this.mFile.Text = "檔案";
            // 
            // mOpen
            // 
            this.mOpen.Name = "mOpen";
            this.mOpen.Size = new System.Drawing.Size(152, 22);
            this.mOpen.Text = "開檔";
            this.mOpen.Click += new System.EventHandler(this.mOpen_Click);
            // 
            // mSave
            // 
            this.mSave.Name = "mSave";
            this.mSave.Size = new System.Drawing.Size(152, 22);
            this.mSave.Text = "存檔";
            this.mSave.Click += new System.EventHandler(this.mSave_Click);
            // 
            // toolStripSeparator2
            // 
            this.toolStripSeparator2.Name = "toolStripSeparator2";
            this.toolStripSeparator2.Size = new System.Drawing.Size(97, 6);
            // 
            // mExit
            // 
            this.mExit.Name = "mExit";
            this.mExit.Size = new System.Drawing.Size(152, 22);
            this.mExit.Text = "結束";
            this.mExit.Click += new System.EventHandler(this.mExit_Click);
            // 
            // mEdit
            // 
            this.mEdit.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mUndo,
            this.toolStripSeparator3,
            this.mCut,
            this.mCopy,
            this.mPaste,
            this.toolStripSeparator4,
            this.mSelectAll});
            this.mEdit.Name = "mEdit";
            this.mEdit.Size = new System.Drawing.Size(44, 20);
            this.mEdit.Text = "編輯";
            // 
            // mUndo
            // 
            this.mUndo.Name = "mUndo";
            this.mUndo.Size = new System.Drawing.Size(152, 22);
            this.mUndo.Text = "復原";
            this.mUndo.Click += new System.EventHandler(this.mUndo_Click);
            // 
            // toolStripSeparator3
            // 
            this.toolStripSeparator3.Name = "toolStripSeparator3";
            this.toolStripSeparator3.Size = new System.Drawing.Size(97, 6);
            // 
            // mCut
            // 
            this.mCut.Name = "mCut";
            this.mCut.Size = new System.Drawing.Size(152, 22);
            this.mCut.Text = "剪下";
            this.mCut.Click += new System.EventHandler(this.mCut_Click);
            // 
            // mCopy
            // 
            this.mCopy.Name = "mCopy";
            this.mCopy.Size = new System.Drawing.Size(152, 22);
            this.mCopy.Text = "複製";
            this.mCopy.Click += new System.EventHandler(this.mCopy_Click);
            // 
            // mPaste
            // 
            this.mPaste.Name = "mPaste";
            this.mPaste.Size = new System.Drawing.Size(152, 22);
            this.mPaste.Text = "貼上";
            this.mPaste.Click += new System.EventHandler(this.mPaste_Click);
            // 
            // toolStripSeparator4
            // 
            this.toolStripSeparator4.Name = "toolStripSeparator4";
            this.toolStripSeparator4.Size = new System.Drawing.Size(97, 6);
            // 
            // mSelectAll
            // 
            this.mSelectAll.Name = "mSelectAll";
            this.mSelectAll.Size = new System.Drawing.Size(152, 22);
            this.mSelectAll.Text = "全選";
            this.mSelectAll.Click += new System.EventHandler(this.mSelectAll_Click);
            // 
            // mSetting
            // 
            this.mSetting.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mFont,
            this.toolStripSeparator1,
            this.mColor});
            this.mSetting.Name = "mSetting";
            this.mSetting.Size = new System.Drawing.Size(44, 20);
            this.mSetting.Text = "設定";
            // 
            // mFont
            // 
            this.mFont.Name = "mFont";
            this.mFont.Size = new System.Drawing.Size(152, 22);
            this.mFont.Text = "字型";
            this.mFont.Click += new System.EventHandler(this.mFont_Click);
            // 
            // toolStripSeparator1
            // 
            this.toolStripSeparator1.Name = "toolStripSeparator1";
            this.toolStripSeparator1.Size = new System.Drawing.Size(97, 6);
            // 
            // mColor
            // 
            this.mColor.Name = "mColor";
            this.mColor.Size = new System.Drawing.Size(152, 22);
            this.mColor.Text = "顏色";
            this.mColor.Click += new System.EventHandler(this.mColor_Click);
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            this.openFileDialog1.Filter = "文字檔(*.txt)|*.txt|RTF檔(*.rtf)|*.rtf";
            this.openFileDialog1.RestoreDirectory = true;
            // 
            // saveFileDialog1
            // 
            this.saveFileDialog1.Filter = "文字檔(*.txt)|*.txt|RTF檔(*.rtf)|*.rtf";
            this.saveFileDialog1.RestoreDirectory = true;
            // 
            // richTextBox1
            // 
            this.richTextBox1.BackColor = System.Drawing.SystemColors.Window;
            this.richTextBox1.Location = new System.Drawing.Point(0, 27);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(552, 375);
            this.richTextBox1.TabIndex = 2;
            this.richTextBox1.Text = "";
            this.richTextBox1.WordWrap = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(941, 620);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.menuStrip1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.Resize += new System.EventHandler(this.Form1_Resize);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.FontDialog fontDialog1;
        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem mFile;
        private System.Windows.Forms.ToolStripMenuItem mOpen;
        private System.Windows.Forms.ToolStripMenuItem mSave;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator2;
        private System.Windows.Forms.ToolStripMenuItem mExit;
        private System.Windows.Forms.ToolStripMenuItem mEdit;
        private System.Windows.Forms.ToolStripMenuItem mUndo;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator3;
        private System.Windows.Forms.ToolStripMenuItem mCut;
        private System.Windows.Forms.ToolStripMenuItem mCopy;
        private System.Windows.Forms.ToolStripMenuItem mPaste;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator4;
        private System.Windows.Forms.ToolStripMenuItem mSelectAll;
        private System.Windows.Forms.ToolStripMenuItem mSetting;
        private System.Windows.Forms.ToolStripMenuItem mFont;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator1;
        private System.Windows.Forms.ToolStripMenuItem mColor;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.ColorDialog colorDialog1;
        private System.Windows.Forms.SaveFileDialog saveFileDialog1;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

