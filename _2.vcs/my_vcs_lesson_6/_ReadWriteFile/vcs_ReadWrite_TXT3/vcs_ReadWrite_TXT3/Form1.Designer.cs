namespace vcs_ReadWrite_TXT3
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
            this.DataGridView3 = new System.Windows.Forms.DataGridView();
            this.DataGridView2 = new System.Windows.Forms.DataGridView();
            this.DataGridView1 = new System.Windows.Forms.DataGridView();
            this.btnParseTextFiles = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            ((System.ComponentModel.ISupportInitialize)(this.DataGridView3)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.DataGridView2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.DataGridView1)).BeginInit();
            this.SuspendLayout();
            // 
            // DataGridView3
            // 
            this.DataGridView3.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.DataGridView3.ColumnHeadersHeight = 32;
            this.DataGridView3.Location = new System.Drawing.Point(11, 319);
            this.DataGridView3.Margin = new System.Windows.Forms.Padding(2);
            this.DataGridView3.Name = "DataGridView3";
            this.DataGridView3.RowTemplate.Height = 27;
            this.DataGridView3.Size = new System.Drawing.Size(350, 120);
            this.DataGridView3.TabIndex = 21;
            this.DataGridView3.Text = "DataGridView3";
            // 
            // DataGridView2
            // 
            this.DataGridView2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.DataGridView2.ColumnHeadersHeight = 32;
            this.DataGridView2.Location = new System.Drawing.Point(11, 162);
            this.DataGridView2.Margin = new System.Windows.Forms.Padding(2);
            this.DataGridView2.Name = "DataGridView2";
            this.DataGridView2.RowTemplate.Height = 27;
            this.DataGridView2.Size = new System.Drawing.Size(350, 120);
            this.DataGridView2.TabIndex = 20;
            this.DataGridView2.Text = "DataGridView2";
            // 
            // DataGridView1
            // 
            this.DataGridView1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.DataGridView1.ColumnHeadersHeight = 32;
            this.DataGridView1.Location = new System.Drawing.Point(11, 11);
            this.DataGridView1.Margin = new System.Windows.Forms.Padding(2);
            this.DataGridView1.Name = "DataGridView1";
            this.DataGridView1.RowTemplate.Height = 27;
            this.DataGridView1.Size = new System.Drawing.Size(350, 120);
            this.DataGridView1.TabIndex = 19;
            this.DataGridView1.Text = "DataGridView1";
            // 
            // btnParseTextFiles
            // 
            this.btnParseTextFiles.ImageAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.btnParseTextFiles.Location = new System.Drawing.Point(11, 470);
            this.btnParseTextFiles.Margin = new System.Windows.Forms.Padding(2);
            this.btnParseTextFiles.Name = "btnParseTextFiles";
            this.btnParseTextFiles.Size = new System.Drawing.Size(174, 59);
            this.btnParseTextFiles.TabIndex = 18;
            this.btnParseTextFiles.Text = "將內含多重格式的文本文件顯示在 DataGridView 控件中";
            this.btnParseTextFiles.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btnParseTextFiles.TextImageRelation = System.Windows.Forms.TextImageRelation.TextBeforeImage;
            this.btnParseTextFiles.Click += new System.EventHandler(this.btnParseTextFiles_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(407, 11);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(453, 518);
            this.richTextBox1.TabIndex = 23;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(889, 550);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.DataGridView3);
            this.Controls.Add(this.DataGridView2);
            this.Controls.Add(this.DataGridView1);
            this.Controls.Add(this.btnParseTextFiles);
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "Form1";
            this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Show;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "解析含有多種格式的文本文件";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.DataGridView3)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.DataGridView2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.DataGridView1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        internal System.Windows.Forms.DataGridView DataGridView3;
        internal System.Windows.Forms.DataGridView DataGridView2;
        internal System.Windows.Forms.DataGridView DataGridView1;
        internal System.Windows.Forms.Button btnParseTextFiles;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}
