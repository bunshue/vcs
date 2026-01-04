namespace vcs_ContextMenuStrip5
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
            this.label1 = new System.Windows.Forms.Label();
            this.contextMenuStrip1 = new System.Windows.Forms.ContextMenuStrip(this.components);
            this.ToolStripMenuItem_A = new System.Windows.Forms.ToolStripMenuItem();
            this.ToolStripMenuItem_Aa = new System.Windows.Forms.ToolStripMenuItem();
            this.ToolStripMenuItem_Ab = new System.Windows.Forms.ToolStripMenuItem();
            this.ToolStripMenuItem_Ac = new System.Windows.Forms.ToolStripMenuItem();
            this.ToolStripMenuItem_Ad = new System.Windows.Forms.ToolStripMenuItem();
            this.ToolStripMenuItem_B = new System.Windows.Forms.ToolStripMenuItem();
            this.ToolStripMenuItem_C = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripSeparator1 = new System.Windows.Forms.ToolStripSeparator();
            this.ToolStripMenuItem_Exit = new System.Windows.Forms.ToolStripMenuItem();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.contextMenuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(20, 20);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(299, 21);
            this.label1.TabIndex = 0;
            this.label1.Text = "滑鼠右鍵選單  contextMenuStrip1";
            // 
            // contextMenuStrip1
            // 
            this.contextMenuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.ToolStripMenuItem_A,
            this.ToolStripMenuItem_B,
            this.ToolStripMenuItem_C,
            this.toolStripSeparator1,
            this.ToolStripMenuItem_Exit});
            this.contextMenuStrip1.Name = "contextMenuStrip1";
            this.contextMenuStrip1.Size = new System.Drawing.Size(153, 120);
            // 
            // ToolStripMenuItem_A
            // 
            this.ToolStripMenuItem_A.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.ToolStripMenuItem_Aa,
            this.ToolStripMenuItem_Ab,
            this.ToolStripMenuItem_Ac,
            this.ToolStripMenuItem_Ad});
            this.ToolStripMenuItem_A.Name = "ToolStripMenuItem_A";
            this.ToolStripMenuItem_A.Size = new System.Drawing.Size(152, 22);
            this.ToolStripMenuItem_A.Text = "AAAA";
            // 
            // ToolStripMenuItem_Aa
            // 
            this.ToolStripMenuItem_Aa.Name = "ToolStripMenuItem_Aa";
            this.ToolStripMenuItem_Aa.Size = new System.Drawing.Size(152, 22);
            this.ToolStripMenuItem_Aa.Text = "aaaa";
            this.ToolStripMenuItem_Aa.Click += new System.EventHandler(this.ToolStripMenuItem_AA_Click);
            // 
            // ToolStripMenuItem_Ab
            // 
            this.ToolStripMenuItem_Ab.Name = "ToolStripMenuItem_Ab";
            this.ToolStripMenuItem_Ab.Size = new System.Drawing.Size(152, 22);
            this.ToolStripMenuItem_Ab.Text = "bbbb";
            this.ToolStripMenuItem_Ab.Click += new System.EventHandler(this.ToolStripMenuItem_AA_Click);
            // 
            // ToolStripMenuItem_Ac
            // 
            this.ToolStripMenuItem_Ac.Name = "ToolStripMenuItem_Ac";
            this.ToolStripMenuItem_Ac.Size = new System.Drawing.Size(152, 22);
            this.ToolStripMenuItem_Ac.Text = "cccc";
            this.ToolStripMenuItem_Ac.Click += new System.EventHandler(this.ToolStripMenuItem_AA_Click);
            // 
            // ToolStripMenuItem_Ad
            // 
            this.ToolStripMenuItem_Ad.Name = "ToolStripMenuItem_Ad";
            this.ToolStripMenuItem_Ad.Size = new System.Drawing.Size(152, 22);
            this.ToolStripMenuItem_Ad.Text = "dddd";
            this.ToolStripMenuItem_Ad.Click += new System.EventHandler(this.ToolStripMenuItem_AA_Click);
            // 
            // ToolStripMenuItem_B
            // 
            this.ToolStripMenuItem_B.Name = "ToolStripMenuItem_B";
            this.ToolStripMenuItem_B.Size = new System.Drawing.Size(152, 22);
            this.ToolStripMenuItem_B.Text = "&BBBB";
            this.ToolStripMenuItem_B.Click += new System.EventHandler(this.ToolStripMenuItem_B_Click);
            // 
            // ToolStripMenuItem_C
            // 
            this.ToolStripMenuItem_C.Name = "ToolStripMenuItem_C";
            this.ToolStripMenuItem_C.Size = new System.Drawing.Size(152, 22);
            this.ToolStripMenuItem_C.Text = "&CCCC";
            this.ToolStripMenuItem_C.Click += new System.EventHandler(this.ToolStripMenuItem_C_Click);
            // 
            // toolStripSeparator1
            // 
            this.toolStripSeparator1.Name = "toolStripSeparator1";
            this.toolStripSeparator1.Size = new System.Drawing.Size(149, 6);
            // 
            // ToolStripMenuItem_Exit
            // 
            this.ToolStripMenuItem_Exit.Name = "ToolStripMenuItem_Exit";
            this.ToolStripMenuItem_Exit.Size = new System.Drawing.Size(152, 22);
            this.ToolStripMenuItem_Exit.Text = "E&xit";
            this.ToolStripMenuItem_Exit.Click += new System.EventHandler(this.ToolStripMenuItem_Exit_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(455, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(270, 533);
            this.richTextBox1.TabIndex = 2;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(737, 557);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.contextMenuStrip1.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.ContextMenuStrip contextMenuStrip1;
        private System.Windows.Forms.ToolStripMenuItem ToolStripMenuItem_A;
        private System.Windows.Forms.ToolStripMenuItem ToolStripMenuItem_Aa;
        private System.Windows.Forms.ToolStripMenuItem ToolStripMenuItem_Ab;
        private System.Windows.Forms.ToolStripMenuItem ToolStripMenuItem_Ac;
        private System.Windows.Forms.ToolStripMenuItem ToolStripMenuItem_Ad;
        private System.Windows.Forms.ToolStripMenuItem ToolStripMenuItem_B;
        private System.Windows.Forms.ToolStripMenuItem ToolStripMenuItem_C;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator1;
        private System.Windows.Forms.ToolStripMenuItem ToolStripMenuItem_Exit;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

