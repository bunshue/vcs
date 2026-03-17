namespace vcs_SqlConnection5
{
    partial class frmMain
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
            this.button1 = new System.Windows.Forms.Button();
            this.dataGridView1 = new System.Windows.Forms.DataGridView();
            this.btnAdd = new System.Windows.Forms.Button();
            this.txtName = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.txtMsg = new System.Windows.Forms.TextBox();
            this.txtPrice = new System.Windows.Forms.TextBox();
            this.txtName2 = new System.Windows.Forms.TextBox();
            this.cboCategoryId = new System.Windows.Forms.ComboBox();
            this.label4 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.button6 = new System.Windows.Forms.Button();
            this.dataGridView2 = new System.Windows.Forms.DataGridView();
            this.dataGridView3 = new System.Windows.Forms.DataGridView();
            this.lb_dgv1 = new System.Windows.Forms.Label();
            this.lb_dgv2 = new System.Windows.Forms.Label();
            this.lb_dgv3 = new System.Windows.Forms.Label();
            this.dataGridView4 = new System.Windows.Forms.DataGridView();
            this.button2 = new System.Windows.Forms.Button();
            this.bt_clear = new System.Windows.Forms.Button();
            this.lb_dgv4 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView3)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView4)).BeginInit();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(232, 11);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(100, 100);
            this.button1.TabIndex = 3;
            this.button1.Text = "兩個表單";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // dataGridView1
            // 
            this.dataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView1.Location = new System.Drawing.Point(12, 36);
            this.dataGridView1.Name = "dataGridView1";
            this.dataGridView1.RowTemplate.Height = 24;
            this.dataGridView1.Size = new System.Drawing.Size(100, 100);
            this.dataGridView1.TabIndex = 16;
            this.dataGridView1.Click += new System.EventHandler(this.dataGridView1_Click);
            // 
            // btnAdd
            // 
            this.btnAdd.Location = new System.Drawing.Point(412, 162);
            this.btnAdd.Name = "btnAdd";
            this.btnAdd.Size = new System.Drawing.Size(100, 100);
            this.btnAdd.TabIndex = 13;
            this.btnAdd.Text = "新增\r\n修改\r\n刪除";
            this.btnAdd.UseVisualStyleBackColor = true;
            this.btnAdd.Click += new System.EventHandler(this.btnAdd_Click);
            // 
            // txtName
            // 
            this.txtName.Location = new System.Drawing.Point(306, 177);
            this.txtName.Name = "txtName";
            this.txtName.Size = new System.Drawing.Size(100, 23);
            this.txtName.TabIndex = 12;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(233, 180);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(59, 13);
            this.label1.TabIndex = 11;
            this.label1.Text = "類別名稱";
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(118, 315);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 19;
            this.richTextBox1.Text = "";
            // 
            // txtMsg
            // 
            this.txtMsg.Location = new System.Drawing.Point(298, 445);
            this.txtMsg.Name = "txtMsg";
            this.txtMsg.Size = new System.Drawing.Size(121, 23);
            this.txtMsg.TabIndex = 27;
            // 
            // txtPrice
            // 
            this.txtPrice.Location = new System.Drawing.Point(298, 399);
            this.txtPrice.Name = "txtPrice";
            this.txtPrice.Size = new System.Drawing.Size(121, 23);
            this.txtPrice.TabIndex = 26;
            // 
            // txtName2
            // 
            this.txtName2.Location = new System.Drawing.Point(298, 353);
            this.txtName2.Name = "txtName2";
            this.txtName2.Size = new System.Drawing.Size(121, 23);
            this.txtName2.TabIndex = 25;
            // 
            // cboCategoryId
            // 
            this.cboCategoryId.FormattingEnabled = true;
            this.cboCategoryId.Location = new System.Drawing.Point(298, 309);
            this.cboCategoryId.Name = "cboCategoryId";
            this.cboCategoryId.Size = new System.Drawing.Size(202, 21);
            this.cboCategoryId.TabIndex = 24;
            this.cboCategoryId.SelectedIndexChanged += new System.EventHandler(this.cboCategoryId_SelectedIndexChanged);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(233, 447);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(33, 13);
            this.label4.TabIndex = 23;
            this.label4.Text = "說明";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(233, 402);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(33, 13);
            this.label3.TabIndex = 22;
            this.label3.Text = "單價";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(233, 357);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(33, 13);
            this.label2.TabIndex = 21;
            this.label2.Text = "品名";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(233, 312);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(59, 13);
            this.label5.TabIndex = 20;
            this.label5.Text = "類別編號";
            // 
            // button6
            // 
            this.button6.Location = new System.Drawing.Point(425, 357);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(100, 100);
            this.button6.TabIndex = 28;
            this.button6.Text = "新增\r\n修改\r\n刪除\r\n";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
            // 
            // dataGridView2
            // 
            this.dataGridView2.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView2.Location = new System.Drawing.Point(8, 178);
            this.dataGridView2.Name = "dataGridView2";
            this.dataGridView2.RowTemplate.Height = 24;
            this.dataGridView2.Size = new System.Drawing.Size(100, 100);
            this.dataGridView2.TabIndex = 31;
            // 
            // dataGridView3
            // 
            this.dataGridView3.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView3.Location = new System.Drawing.Point(8, 315);
            this.dataGridView3.Name = "dataGridView3";
            this.dataGridView3.RowTemplate.Height = 24;
            this.dataGridView3.Size = new System.Drawing.Size(100, 100);
            this.dataGridView3.TabIndex = 32;
            // 
            // lb_dgv1
            // 
            this.lb_dgv1.AutoSize = true;
            this.lb_dgv1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_dgv1.Location = new System.Drawing.Point(9, 11);
            this.lb_dgv1.Name = "lb_dgv1";
            this.lb_dgv1.Size = new System.Drawing.Size(86, 19);
            this.lb_dgv1.TabIndex = 33;
            this.lb_dgv1.Text = "DGV名稱";
            // 
            // lb_dgv2
            // 
            this.lb_dgv2.AutoSize = true;
            this.lb_dgv2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_dgv2.Location = new System.Drawing.Point(9, 149);
            this.lb_dgv2.Name = "lb_dgv2";
            this.lb_dgv2.Size = new System.Drawing.Size(86, 19);
            this.lb_dgv2.TabIndex = 34;
            this.lb_dgv2.Text = "DGV名稱";
            // 
            // lb_dgv3
            // 
            this.lb_dgv3.AutoSize = true;
            this.lb_dgv3.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_dgv3.Location = new System.Drawing.Point(8, 287);
            this.lb_dgv3.Name = "lb_dgv3";
            this.lb_dgv3.Size = new System.Drawing.Size(86, 19);
            this.lb_dgv3.TabIndex = 35;
            this.lb_dgv3.Text = "DGV名稱";
            // 
            // dataGridView4
            // 
            this.dataGridView4.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView4.Location = new System.Drawing.Point(118, 36);
            this.dataGridView4.Name = "dataGridView4";
            this.dataGridView4.RowTemplate.Height = 24;
            this.dataGridView4.Size = new System.Drawing.Size(100, 100);
            this.dataGridView4.TabIndex = 36;
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(338, 11);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(100, 100);
            this.button2.TabIndex = 38;
            this.button2.Text = "產品類別管理\r\n產品資料管理\r\n產品關聯查詢";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(133, 328);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(69, 32);
            this.bt_clear.TabIndex = 39;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // lb_dgv4
            // 
            this.lb_dgv4.AutoSize = true;
            this.lb_dgv4.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_dgv4.Location = new System.Drawing.Point(116, 11);
            this.lb_dgv4.Name = "lb_dgv4";
            this.lb_dgv4.Size = new System.Drawing.Size(86, 19);
            this.lb_dgv4.TabIndex = 40;
            this.lb_dgv4.Text = "DGV名稱";
            // 
            // frmMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(601, 493);
            this.Controls.Add(this.lb_dgv4);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.dataGridView4);
            this.Controls.Add(this.lb_dgv3);
            this.Controls.Add(this.lb_dgv2);
            this.Controls.Add(this.lb_dgv1);
            this.Controls.Add(this.dataGridView3);
            this.Controls.Add(this.dataGridView2);
            this.Controls.Add(this.button6);
            this.Controls.Add(this.txtMsg);
            this.Controls.Add(this.txtPrice);
            this.Controls.Add(this.txtName2);
            this.Controls.Add(this.cboCategoryId);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.dataGridView1);
            this.Controls.Add(this.btnAdd);
            this.Controls.Add(this.txtName);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.button1);
            this.Font = new System.Drawing.Font("新細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Name = "frmMain";
            this.Load += new System.EventHandler(this.frmMain_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView3)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView4)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.DataGridView dataGridView1;
        private System.Windows.Forms.Button btnAdd;
        private System.Windows.Forms.TextBox txtName;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.TextBox txtMsg;
        private System.Windows.Forms.TextBox txtPrice;
        private System.Windows.Forms.TextBox txtName2;
        private System.Windows.Forms.ComboBox cboCategoryId;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.DataGridView dataGridView2;
        private System.Windows.Forms.DataGridView dataGridView3;
        private System.Windows.Forms.Label lb_dgv1;
        private System.Windows.Forms.Label lb_dgv2;
        private System.Windows.Forms.Label lb_dgv3;
        private System.Windows.Forms.DataGridView dataGridView4;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.Label lb_dgv4;
    }
}