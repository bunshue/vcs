namespace DataViewDemo1
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
            this.label1 = new System.Windows.Forms.Label();
            this.dataGridView1 = new System.Windows.Forms.DataGridView();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.btnOk = new System.Windows.Forms.Button();
            this.rdbChi = new System.Windows.Forms.RadioButton();
            this.rdbEng = new System.Windows.Forms.RadioButton();
            this.rdbMath = new System.Windows.Forms.RadioButton();
            this.rdbDesc = new System.Windows.Forms.RadioButton();
            this.rdbAsc = new System.Windows.Forms.RadioButton();
            this.txtFilter = new System.Windows.Forms.TextBox();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).BeginInit();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 13.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(134, 45);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(274, 24);
            this.label1.TabIndex = 0;
            this.label1.Text = "碁峰大學資管甲班成績單";
            // 
            // dataGridView1
            // 
            this.dataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView1.Location = new System.Drawing.Point(29, 93);
            this.dataGridView1.Name = "dataGridView1";
            this.dataGridView1.RowTemplate.Height = 27;
            this.dataGridView1.Size = new System.Drawing.Size(528, 220);
            this.dataGridView1.TabIndex = 1;
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.rdbMath);
            this.groupBox1.Controls.Add(this.rdbEng);
            this.groupBox1.Controls.Add(this.rdbChi);
            this.groupBox1.Location = new System.Drawing.Point(588, 95);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(93, 113);
            this.groupBox1.TabIndex = 2;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "排序欄位";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.rdbAsc);
            this.groupBox2.Controls.Add(this.rdbDesc);
            this.groupBox2.Location = new System.Drawing.Point(702, 95);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(93, 113);
            this.groupBox2.TabIndex = 2;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "排序方式";
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.txtFilter);
            this.groupBox3.Location = new System.Drawing.Point(588, 240);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(207, 75);
            this.groupBox3.TabIndex = 2;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "篩選條件式";
            // 
            // btnOk
            // 
            this.btnOk.Location = new System.Drawing.Point(702, 45);
            this.btnOk.Name = "btnOk";
            this.btnOk.Size = new System.Drawing.Size(93, 30);
            this.btnOk.TabIndex = 3;
            this.btnOk.Text = "確定";
            this.btnOk.UseVisualStyleBackColor = true;
            this.btnOk.Click += new System.EventHandler(this.btnOk_Click);
            // 
            // rdbChi
            // 
            this.rdbChi.AutoSize = true;
            this.rdbChi.Location = new System.Drawing.Point(7, 25);
            this.rdbChi.Name = "rdbChi";
            this.rdbChi.Size = new System.Drawing.Size(58, 19);
            this.rdbChi.TabIndex = 0;
            this.rdbChi.TabStop = true;
            this.rdbChi.Text = "國文";
            this.rdbChi.UseVisualStyleBackColor = true;
            // 
            // rdbEng
            // 
            this.rdbEng.AutoSize = true;
            this.rdbEng.Location = new System.Drawing.Point(7, 51);
            this.rdbEng.Name = "rdbEng";
            this.rdbEng.Size = new System.Drawing.Size(58, 19);
            this.rdbEng.TabIndex = 1;
            this.rdbEng.TabStop = true;
            this.rdbEng.Text = "英文";
            this.rdbEng.UseVisualStyleBackColor = true;
            // 
            // rdbMath
            // 
            this.rdbMath.AutoSize = true;
            this.rdbMath.Location = new System.Drawing.Point(7, 77);
            this.rdbMath.Name = "rdbMath";
            this.rdbMath.Size = new System.Drawing.Size(58, 19);
            this.rdbMath.TabIndex = 2;
            this.rdbMath.TabStop = true;
            this.rdbMath.Text = "數學";
            this.rdbMath.UseVisualStyleBackColor = true;
            // 
            // rdbDesc
            // 
            this.rdbDesc.AutoSize = true;
            this.rdbDesc.Location = new System.Drawing.Point(7, 25);
            this.rdbDesc.Name = "rdbDesc";
            this.rdbDesc.Size = new System.Drawing.Size(58, 19);
            this.rdbDesc.TabIndex = 0;
            this.rdbDesc.TabStop = true;
            this.rdbDesc.Text = "遞增";
            this.rdbDesc.UseVisualStyleBackColor = true;
            // 
            // rdbAsc
            // 
            this.rdbAsc.AutoSize = true;
            this.rdbAsc.Location = new System.Drawing.Point(7, 50);
            this.rdbAsc.Name = "rdbAsc";
            this.rdbAsc.Size = new System.Drawing.Size(58, 19);
            this.rdbAsc.TabIndex = 1;
            this.rdbAsc.TabStop = true;
            this.rdbAsc.Text = "遞減";
            this.rdbAsc.UseVisualStyleBackColor = true;
            // 
            // txtFilter
            // 
            this.txtFilter.Location = new System.Drawing.Point(19, 30);
            this.txtFilter.Name = "txtFilter";
            this.txtFilter.Size = new System.Drawing.Size(182, 25);
            this.txtFilter.TabIndex = 0;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(807, 340);
            this.Controls.Add(this.btnOk);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox3);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.dataGridView1);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).EndInit();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.groupBox3.ResumeLayout(false);
            this.groupBox3.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.DataGridView dataGridView1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.RadioButton rdbMath;
        private System.Windows.Forms.RadioButton rdbEng;
        private System.Windows.Forms.RadioButton rdbChi;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.RadioButton rdbAsc;
        private System.Windows.Forms.RadioButton rdbDesc;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.TextBox txtFilter;
        private System.Windows.Forms.Button btnOk;
    }
}

