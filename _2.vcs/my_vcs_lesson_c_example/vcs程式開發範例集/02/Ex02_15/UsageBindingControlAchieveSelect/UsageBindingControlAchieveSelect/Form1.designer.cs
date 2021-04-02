namespace UsageBindingControlAchieveSelect
{
    partial class Form1
    {
        /// <summary>
        /// 必需的設計器變數。
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

        #region Windows 視窗設計器產生的代碼

        /// <summary>
        /// 設計器支援所需的方法 - 不要
        /// 使用代碼編輯器修改此方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.listBox1 = new System.Windows.Forms.ListBox();
            this.tbLandBindingSource = new System.Windows.Forms.BindingSource(this.components);
            this.db_02_1DataSet = new UsageBindingControlAchieveSelect.db_02_1DataSet();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.textBox2 = new System.Windows.Forms.TextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.tb_LandTableAdapter = new UsageBindingControlAchieveSelect.db_02_1DataSetTableAdapters.tb_LandTableAdapter();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.tbLandBindingSource)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.db_02_1DataSet)).BeginInit();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.listBox1);
            this.groupBox1.Location = new System.Drawing.Point(9, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(97, 132);
            this.groupBox1.TabIndex = 0;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "地名：";
            // 
            // listBox1
            // 
            this.listBox1.DataSource = this.db_02_1DataSet;
            this.listBox1.DisplayMember = "tb_Land.depname";
            this.listBox1.FormattingEnabled = true;
            this.listBox1.ItemHeight = 12;
            this.listBox1.Location = new System.Drawing.Point(6, 20);
            this.listBox1.Name = "listBox1";
            this.listBox1.Size = new System.Drawing.Size(82, 100);
            this.listBox1.TabIndex = 0;
            this.listBox1.ValueMember = "tb_Land.depname";
            this.listBox1.SelectedIndexChanged += new System.EventHandler(this.listBox1_SelectedIndexChanged_1);
            // 
            // tbLandBindingSource
            // 
            this.tbLandBindingSource.DataMember = "tb_Land";
            this.tbLandBindingSource.DataSource = this.db_02_1DataSet;
            // 
            // db_02_1DataSet
            // 
            this.db_02_1DataSet.DataSetName = "db_02_1DataSet";
            this.db_02_1DataSet.SchemaSerializationMode = System.Data.SchemaSerializationMode.IncludeSchema;
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(164, 27);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(100, 22);
            this.textBox1.TabIndex = 1;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(117, 30);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(41, 12);
            this.label1.TabIndex = 2;
            this.label1.Text = "姓名：";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(117, 70);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(41, 12);
            this.label2.TabIndex = 3;
            this.label2.Text = "地址：";
            // 
            // textBox2
            // 
            this.textBox2.Location = new System.Drawing.Point(164, 70);
            this.textBox2.Name = "textBox2";
            this.textBox2.Size = new System.Drawing.Size(100, 22);
            this.textBox2.TabIndex = 4;
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(119, 109);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 5;
            this.button1.Text = "確定(&D)";
            this.button1.UseVisualStyleBackColor = true;
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(202, 109);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(75, 23);
            this.button2.TabIndex = 6;
            this.button2.Text = "取消(&E)";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // tb_LandTableAdapter
            // 
            this.tb_LandTableAdapter.ClearBeforeFill = true;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(314, 152);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.textBox2);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.groupBox1);
            this.Name = "Form1";
            this.Text = "藉由綁定控制元件完成資料選擇登入";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.tbLandBindingSource)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.db_02_1DataSet)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox textBox2;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.ListBox listBox1;
        private db_02_1DataSet db_02_1DataSet;
        private System.Windows.Forms.BindingSource tbLandBindingSource;
        private UsageBindingControlAchieveSelect.db_02_1DataSetTableAdapters.tb_LandTableAdapter tb_LandTableAdapter;
    }
}

