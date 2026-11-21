namespace vcs_CompareKatfile
{
    partial class Form1
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.dataGridView1 = new System.Windows.Forms.DataGridView();
            this.colDir1 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Dir2 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.btnCompare = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.bt_clear = new System.Windows.Forms.Button();
            this.richTextBox_katfile1 = new System.Windows.Forms.RichTextBox();
            this.richTextBox_katfile2 = new System.Windows.Forms.RichTextBox();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).BeginInit();
            this.SuspendLayout();
            // 
            // dataGridView1
            // 
            this.dataGridView1.AllowUserToAddRows = false;
            this.dataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView1.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.colDir1,
            this.Dir2});
            this.dataGridView1.Location = new System.Drawing.Point(10, 10);
            this.dataGridView1.Name = "dataGridView1";
            this.dataGridView1.RowTemplate.Height = 24;
            this.dataGridView1.Size = new System.Drawing.Size(100, 100);
            this.dataGridView1.TabIndex = 14;
            // 
            // colDir1
            // 
            this.colDir1.HeaderText = "Directory 1";
            this.colDir1.Name = "colDir1";
            // 
            // Dir2
            // 
            this.Dir2.HeaderText = "Directory 2";
            this.Dir2.Name = "Dir2";
            // 
            // btnCompare
            // 
            this.btnCompare.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnCompare.Location = new System.Drawing.Point(22, 130);
            this.btnCompare.Name = "btnCompare";
            this.btnCompare.Size = new System.Drawing.Size(72, 36);
            this.btnCompare.TabIndex = 11;
            this.btnCompare.Text = "比較";
            this.btnCompare.UseVisualStyleBackColor = true;
            this.btnCompare.Click += new System.EventHandler(this.btnCompare_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.richTextBox1.Location = new System.Drawing.Point(10, 120);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 15;
            this.richTextBox1.Text = "";
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(22, 172);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(72, 36);
            this.bt_clear.TabIndex = 16;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // richTextBox_katfile1
            // 
            this.richTextBox_katfile1.Location = new System.Drawing.Point(120, 10);
            this.richTextBox_katfile1.Name = "richTextBox_katfile1";
            this.richTextBox_katfile1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox_katfile1.TabIndex = 17;
            this.richTextBox_katfile1.Text = resources.GetString("richTextBox_katfile1.Text");
            // 
            // richTextBox_katfile2
            // 
            this.richTextBox_katfile2.Location = new System.Drawing.Point(230, 10);
            this.richTextBox_katfile2.Name = "richTextBox_katfile2";
            this.richTextBox_katfile2.Size = new System.Drawing.Size(100, 100);
            this.richTextBox_katfile2.TabIndex = 18;
            this.richTextBox_katfile2.Text = "\n金梅字型~字之藏.rar\n華康手書風I~妙筆生花.rar\n華康手書風II~字得奇樂.rar\n華康金蝶2010.part01.rar";
            // 
            // Form1
            // 
            this.AcceptButton = this.btnCompare;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(400, 276);
            this.Controls.Add(this.btnCompare);
            this.Controls.Add(this.richTextBox_katfile2);
            this.Controls.Add(this.richTextBox_katfile1);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.dataGridView1);
            this.Name = "Form1";
            this.Text = "vcs_CompareKatfile";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.Resize += new System.EventHandler(this.Form1_Resize);
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        internal System.Windows.Forms.DataGridView dataGridView1;
        internal System.Windows.Forms.DataGridViewTextBoxColumn colDir1;
        internal System.Windows.Forms.DataGridViewTextBoxColumn Dir2;
        internal System.Windows.Forms.Button btnCompare;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.RichTextBox richTextBox_katfile1;
        private System.Windows.Forms.RichTextBox richTextBox_katfile2;
    }
}

