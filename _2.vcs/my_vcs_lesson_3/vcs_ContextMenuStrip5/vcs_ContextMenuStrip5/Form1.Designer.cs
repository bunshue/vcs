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
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.contextMenuStrip2 = new System.Windows.Forms.ContextMenuStrip(this.components);
            this.toolStripMenuItem1 = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem2 = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem3 = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem4 = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem5 = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem6 = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem7 = new System.Windows.Forms.ToolStripMenuItem();
            this.button1 = new System.Windows.Forms.Button();
            this.bt_clear = new System.Windows.Forms.Button();
            this.label_description = new System.Windows.Forms.Label();
            this.contextMenuStrip1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.contextMenuStrip2.SuspendLayout();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(18, 14);
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
            this.contextMenuStrip1.Size = new System.Drawing.Size(155, 98);
            // 
            // ToolStripMenuItem_A
            // 
            this.ToolStripMenuItem_A.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.ToolStripMenuItem_Aa,
            this.ToolStripMenuItem_Ab,
            this.ToolStripMenuItem_Ac,
            this.ToolStripMenuItem_Ad});
            this.ToolStripMenuItem_A.Name = "ToolStripMenuItem_A";
            this.ToolStripMenuItem_A.Size = new System.Drawing.Size(154, 22);
            this.ToolStripMenuItem_A.Text = "表單右鍵選單A";
            // 
            // ToolStripMenuItem_Aa
            // 
            this.ToolStripMenuItem_Aa.Name = "ToolStripMenuItem_Aa";
            this.ToolStripMenuItem_Aa.Size = new System.Drawing.Size(162, 22);
            this.ToolStripMenuItem_Aa.Text = "表單右鍵選單aa";
            this.ToolStripMenuItem_Aa.Click += new System.EventHandler(this.ToolStripMenuItem_AA_Click);
            // 
            // ToolStripMenuItem_Ab
            // 
            this.ToolStripMenuItem_Ab.Name = "ToolStripMenuItem_Ab";
            this.ToolStripMenuItem_Ab.Size = new System.Drawing.Size(162, 22);
            this.ToolStripMenuItem_Ab.Text = "表單右鍵選單bb";
            this.ToolStripMenuItem_Ab.Click += new System.EventHandler(this.ToolStripMenuItem_AA_Click);
            // 
            // ToolStripMenuItem_Ac
            // 
            this.ToolStripMenuItem_Ac.Name = "ToolStripMenuItem_Ac";
            this.ToolStripMenuItem_Ac.Size = new System.Drawing.Size(162, 22);
            this.ToolStripMenuItem_Ac.Text = "表單右鍵選單cc";
            this.ToolStripMenuItem_Ac.Click += new System.EventHandler(this.ToolStripMenuItem_AA_Click);
            // 
            // ToolStripMenuItem_Ad
            // 
            this.ToolStripMenuItem_Ad.Name = "ToolStripMenuItem_Ad";
            this.ToolStripMenuItem_Ad.Size = new System.Drawing.Size(162, 22);
            this.ToolStripMenuItem_Ad.Text = "表單右鍵選單dd";
            this.ToolStripMenuItem_Ad.Click += new System.EventHandler(this.ToolStripMenuItem_AA_Click);
            // 
            // ToolStripMenuItem_B
            // 
            this.ToolStripMenuItem_B.Name = "ToolStripMenuItem_B";
            this.ToolStripMenuItem_B.Size = new System.Drawing.Size(154, 22);
            this.ToolStripMenuItem_B.Text = "表單右鍵選單B";
            this.ToolStripMenuItem_B.Click += new System.EventHandler(this.ToolStripMenuItem_B_Click);
            // 
            // ToolStripMenuItem_C
            // 
            this.ToolStripMenuItem_C.Name = "ToolStripMenuItem_C";
            this.ToolStripMenuItem_C.Size = new System.Drawing.Size(154, 22);
            this.ToolStripMenuItem_C.Text = "表單右鍵選單C";
            this.ToolStripMenuItem_C.Click += new System.EventHandler(this.ToolStripMenuItem_C_Click);
            // 
            // toolStripSeparator1
            // 
            this.toolStripSeparator1.Name = "toolStripSeparator1";
            this.toolStripSeparator1.Size = new System.Drawing.Size(103, 6);
            // 
            // ToolStripMenuItem_Exit
            // 
            this.ToolStripMenuItem_Exit.Name = "ToolStripMenuItem_Exit";
            this.ToolStripMenuItem_Exit.Size = new System.Drawing.Size(106, 22);
            this.ToolStripMenuItem_Exit.Text = "E&xit";
            this.ToolStripMenuItem_Exit.Click += new System.EventHandler(this.ToolStripMenuItem_Exit_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(810, 24);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 2;
            this.richTextBox1.Text = "";
            // 
            // pictureBox1
            // 
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox1.Location = new System.Drawing.Point(12, 55);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(305, 400);
            this.pictureBox1.TabIndex = 3;
            this.pictureBox1.TabStop = false;
            // 
            // contextMenuStrip2
            // 
            this.contextMenuStrip2.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripMenuItem1,
            this.toolStripMenuItem2,
            this.toolStripMenuItem3,
            this.toolStripMenuItem4,
            this.toolStripMenuItem5,
            this.toolStripMenuItem6,
            this.toolStripMenuItem7});
            this.contextMenuStrip2.Name = "contextMenuStrip1";
            this.contextMenuStrip2.Size = new System.Drawing.Size(233, 158);
            // 
            // toolStripMenuItem1
            // 
            this.toolStripMenuItem1.Name = "toolStripMenuItem1";
            this.toolStripMenuItem1.Size = new System.Drawing.Size(232, 22);
            this.toolStripMenuItem1.Text = "pictureBox右鍵選單_放大";
            this.toolStripMenuItem1.Click += new System.EventHandler(this.toolStripMenuItem1_Click);
            // 
            // toolStripMenuItem2
            // 
            this.toolStripMenuItem2.Name = "toolStripMenuItem2";
            this.toolStripMenuItem2.Size = new System.Drawing.Size(232, 22);
            this.toolStripMenuItem2.Text = "pictureBox右鍵選單_縮小";
            this.toolStripMenuItem2.Click += new System.EventHandler(this.toolStripMenuItem2_Click);
            // 
            // toolStripMenuItem3
            // 
            this.toolStripMenuItem3.Name = "toolStripMenuItem3";
            this.toolStripMenuItem3.Size = new System.Drawing.Size(232, 22);
            this.toolStripMenuItem3.Text = "pictureBox右鍵選單_全螢幕";
            this.toolStripMenuItem3.Click += new System.EventHandler(this.toolStripMenuItem3_Click);
            // 
            // toolStripMenuItem4
            // 
            this.toolStripMenuItem4.Name = "toolStripMenuItem4";
            this.toolStripMenuItem4.Size = new System.Drawing.Size(232, 22);
            this.toolStripMenuItem4.Text = "pictureBox右鍵選單_複製到...";
            this.toolStripMenuItem4.Click += new System.EventHandler(this.toolStripMenuItem4_Click);
            // 
            // toolStripMenuItem5
            // 
            this.toolStripMenuItem5.Name = "toolStripMenuItem5";
            this.toolStripMenuItem5.Size = new System.Drawing.Size(232, 22);
            this.toolStripMenuItem5.Text = "pictureBox右鍵選單_移動到...";
            this.toolStripMenuItem5.Click += new System.EventHandler(this.toolStripMenuItem5_Click);
            // 
            // toolStripMenuItem6
            // 
            this.toolStripMenuItem6.Name = "toolStripMenuItem6";
            this.toolStripMenuItem6.Size = new System.Drawing.Size(232, 22);
            this.toolStripMenuItem6.Text = "pictureBox右鍵選單_刪除";
            this.toolStripMenuItem6.Click += new System.EventHandler(this.toolStripMenuItem6_Click);
            // 
            // toolStripMenuItem7
            // 
            this.toolStripMenuItem7.Name = "toolStripMenuItem7";
            this.toolStripMenuItem7.Size = new System.Drawing.Size(119, 22);
            this.toolStripMenuItem7.Text = "離開";
            this.toolStripMenuItem7.Click += new System.EventHandler(this.toolStripMenuItem7_Click);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(607, 24);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(135, 64);
            this.button1.TabIndex = 4;
            this.button1.Text = "按Button出現ContextMenuStrip";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(831, 44);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(60, 32);
            this.bt_clear.TabIndex = 37;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // label_description
            // 
            this.label_description.AutoSize = true;
            this.label_description.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label_description.Location = new System.Drawing.Point(347, 14);
            this.label_description.Name = "label_description";
            this.label_description.Size = new System.Drawing.Size(52, 21);
            this.label_description.TabIndex = 38;
            this.label_description.Text = "說明";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(940, 642);
            this.Controls.Add(this.label_description);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.contextMenuStrip1.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.contextMenuStrip2.ResumeLayout(false);
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
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.ContextMenuStrip contextMenuStrip2;
        private System.Windows.Forms.ToolStripMenuItem toolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem toolStripMenuItem2;
        private System.Windows.Forms.ToolStripMenuItem toolStripMenuItem3;
        private System.Windows.Forms.ToolStripMenuItem toolStripMenuItem4;
        private System.Windows.Forms.ToolStripMenuItem toolStripMenuItem5;
        private System.Windows.Forms.ToolStripMenuItem toolStripMenuItem6;
        private System.Windows.Forms.ToolStripMenuItem toolStripMenuItem7;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.Label label_description;
    }
}

