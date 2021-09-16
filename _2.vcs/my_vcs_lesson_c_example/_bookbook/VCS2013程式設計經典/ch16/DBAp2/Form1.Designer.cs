namespace DBAp2
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
            this.bindingSource1 = new System.Windows.Forms.BindingSource(this.components);
            this.ch16DBDataSet = new DBAp2.ch16DBDataSet();
            this.產品資料TableAdapter = new DBAp2.ch16DBDataSetTableAdapters.產品資料TableAdapter();
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.巡覽ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.第一筆ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.上一筆ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.下一筆ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.最末筆ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.編輯ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.新增ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.刪除ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.更新ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.tsmShow = new System.Windows.Forms.ToolStripMenuItem();
            this.chkIsSupply = new System.Windows.Forms.CheckBox();
            this.dtpDate = new System.Windows.Forms.DateTimePicker();
            this.txtSpecial = new System.Windows.Forms.TextBox();
            this.txtPrice = new System.Windows.Forms.TextBox();
            this.txtName = new System.Windows.Forms.TextBox();
            this.txtId = new System.Windows.Forms.TextBox();
            this.label6 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.產品資料BindingSource = new System.Windows.Forms.BindingSource(this.components);
            ((System.ComponentModel.ISupportInitialize)(this.bindingSource1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.ch16DBDataSet)).BeginInit();
            this.menuStrip1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.產品資料BindingSource)).BeginInit();
            this.SuspendLayout();
            // 
            // ch16DBDataSet
            // 
            this.ch16DBDataSet.DataSetName = "ch16DBDataSet";
            this.ch16DBDataSet.SchemaSerializationMode = System.Data.SchemaSerializationMode.IncludeSchema;
            // 
            // 產品資料TableAdapter
            // 
            this.產品資料TableAdapter.ClearBeforeFill = true;
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.巡覽ToolStripMenuItem,
            this.編輯ToolStripMenuItem,
            this.tsmShow});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Padding = new System.Windows.Forms.Padding(4, 2, 0, 2);
            this.menuStrip1.Size = new System.Drawing.Size(241, 24);
            this.menuStrip1.TabIndex = 30;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // 巡覽ToolStripMenuItem
            // 
            this.巡覽ToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.第一筆ToolStripMenuItem,
            this.上一筆ToolStripMenuItem,
            this.下一筆ToolStripMenuItem,
            this.最末筆ToolStripMenuItem});
            this.巡覽ToolStripMenuItem.Name = "巡覽ToolStripMenuItem";
            this.巡覽ToolStripMenuItem.Size = new System.Drawing.Size(43, 20);
            this.巡覽ToolStripMenuItem.Text = "巡覽";
            // 
            // 第一筆ToolStripMenuItem
            // 
            this.第一筆ToolStripMenuItem.Name = "第一筆ToolStripMenuItem";
            this.第一筆ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.第一筆ToolStripMenuItem.Text = "第一筆";
            this.第一筆ToolStripMenuItem.Click += new System.EventHandler(this.第一筆ToolStripMenuItem_Click);
            // 
            // 上一筆ToolStripMenuItem
            // 
            this.上一筆ToolStripMenuItem.Name = "上一筆ToolStripMenuItem";
            this.上一筆ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.上一筆ToolStripMenuItem.Text = "上一筆";
            this.上一筆ToolStripMenuItem.Click += new System.EventHandler(this.上一筆ToolStripMenuItem_Click);
            // 
            // 下一筆ToolStripMenuItem
            // 
            this.下一筆ToolStripMenuItem.Name = "下一筆ToolStripMenuItem";
            this.下一筆ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.下一筆ToolStripMenuItem.Text = "下一筆";
            this.下一筆ToolStripMenuItem.Click += new System.EventHandler(this.下一筆ToolStripMenuItem_Click);
            // 
            // 最末筆ToolStripMenuItem
            // 
            this.最末筆ToolStripMenuItem.Name = "最末筆ToolStripMenuItem";
            this.最末筆ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.最末筆ToolStripMenuItem.Text = "最末筆";
            this.最末筆ToolStripMenuItem.Click += new System.EventHandler(this.最末筆ToolStripMenuItem_Click);
            // 
            // 編輯ToolStripMenuItem
            // 
            this.編輯ToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.新增ToolStripMenuItem,
            this.刪除ToolStripMenuItem,
            this.更新ToolStripMenuItem});
            this.編輯ToolStripMenuItem.Name = "編輯ToolStripMenuItem";
            this.編輯ToolStripMenuItem.Size = new System.Drawing.Size(43, 20);
            this.編輯ToolStripMenuItem.Text = "編輯";
            // 
            // 新增ToolStripMenuItem
            // 
            this.新增ToolStripMenuItem.Name = "新增ToolStripMenuItem";
            this.新增ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.新增ToolStripMenuItem.Text = "新增";
            this.新增ToolStripMenuItem.Click += new System.EventHandler(this.新增ToolStripMenuItem_Click);
            // 
            // 刪除ToolStripMenuItem
            // 
            this.刪除ToolStripMenuItem.Name = "刪除ToolStripMenuItem";
            this.刪除ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.刪除ToolStripMenuItem.Text = "刪除";
            this.刪除ToolStripMenuItem.Click += new System.EventHandler(this.刪除ToolStripMenuItem_Click);
            // 
            // 更新ToolStripMenuItem
            // 
            this.更新ToolStripMenuItem.Name = "更新ToolStripMenuItem";
            this.更新ToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.更新ToolStripMenuItem.Text = "更新";
            this.更新ToolStripMenuItem.Click += new System.EventHandler(this.更新ToolStripMenuItem_Click);
            // 
            // tsmShow
            // 
            this.tsmShow.Name = "tsmShow";
            this.tsmShow.Size = new System.Drawing.Size(133, 20);
            this.tsmShow.Text = "toolStripMenuItem1";
            // 
            // chkIsSupply
            // 
            this.chkIsSupply.AutoSize = true;
            this.chkIsSupply.DataBindings.Add(new System.Windows.Forms.Binding("Checked", this.產品資料BindingSource, "是否供貨", true));
            this.chkIsSupply.Location = new System.Drawing.Point(80, 199);
            this.chkIsSupply.Margin = new System.Windows.Forms.Padding(2);
            this.chkIsSupply.Name = "chkIsSupply";
            this.chkIsSupply.Size = new System.Drawing.Size(15, 14);
            this.chkIsSupply.TabIndex = 42;
            this.chkIsSupply.UseVisualStyleBackColor = true;
            // 
            // dtpDate
            // 
            this.dtpDate.DataBindings.Add(new System.Windows.Forms.Binding("Value", this.產品資料BindingSource, "上架日期", true));
            this.dtpDate.Location = new System.Drawing.Point(80, 157);
            this.dtpDate.Margin = new System.Windows.Forms.Padding(2);
            this.dtpDate.Name = "dtpDate";
            this.dtpDate.Size = new System.Drawing.Size(118, 22);
            this.dtpDate.TabIndex = 41;
            // 
            // txtSpecial
            // 
            this.txtSpecial.DataBindings.Add(new System.Windows.Forms.Binding("Text", this.產品資料BindingSource, "特價", true));
            this.txtSpecial.Location = new System.Drawing.Point(80, 232);
            this.txtSpecial.Margin = new System.Windows.Forms.Padding(2);
            this.txtSpecial.Name = "txtSpecial";
            this.txtSpecial.Size = new System.Drawing.Size(76, 22);
            this.txtSpecial.TabIndex = 38;
            // 
            // txtPrice
            // 
            this.txtPrice.DataBindings.Add(new System.Windows.Forms.Binding("Text", this.產品資料BindingSource, "單價", true));
            this.txtPrice.Location = new System.Drawing.Point(80, 125);
            this.txtPrice.Margin = new System.Windows.Forms.Padding(2);
            this.txtPrice.Name = "txtPrice";
            this.txtPrice.Size = new System.Drawing.Size(76, 22);
            this.txtPrice.TabIndex = 37;
            // 
            // txtName
            // 
            this.txtName.DataBindings.Add(new System.Windows.Forms.Binding("Text", this.產品資料BindingSource, "品名", true));
            this.txtName.Location = new System.Drawing.Point(80, 89);
            this.txtName.Margin = new System.Windows.Forms.Padding(2);
            this.txtName.Name = "txtName";
            this.txtName.Size = new System.Drawing.Size(136, 22);
            this.txtName.TabIndex = 40;
            // 
            // txtId
            // 
            this.txtId.DataBindings.Add(new System.Windows.Forms.Binding("Text", this.產品資料BindingSource, "產品編號", true));
            this.txtId.Location = new System.Drawing.Point(80, 53);
            this.txtId.Margin = new System.Windows.Forms.Padding(2);
            this.txtId.Name = "txtId";
            this.txtId.Size = new System.Drawing.Size(76, 22);
            this.txtId.TabIndex = 39;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(48, 234);
            this.label6.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(29, 12);
            this.label6.TabIndex = 33;
            this.label6.Text = "特價";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(26, 199);
            this.label5.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(53, 12);
            this.label5.TabIndex = 32;
            this.label5.Text = "是否供貨";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(26, 163);
            this.label4.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(53, 12);
            this.label4.TabIndex = 31;
            this.label4.Text = "上架日期";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(48, 127);
            this.label3.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(29, 12);
            this.label3.TabIndex = 36;
            this.label3.Text = "單價";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(48, 91);
            this.label2.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(29, 12);
            this.label2.TabIndex = 35;
            this.label2.Text = "品名";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(26, 55);
            this.label1.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(53, 12);
            this.label1.TabIndex = 34;
            this.label1.Text = "產品編號";
            // 
            // 產品資料BindingSource
            // 
            this.產品資料BindingSource.DataMember = "產品資料";
            this.產品資料BindingSource.DataSource = this.ch16DBDataSet;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(241, 274);
            this.Controls.Add(this.menuStrip1);
            this.Controls.Add(this.chkIsSupply);
            this.Controls.Add(this.dtpDate);
            this.Controls.Add(this.txtSpecial);
            this.Controls.Add(this.txtPrice);
            this.Controls.Add(this.txtName);
            this.Controls.Add(this.txtId);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.bindingSource1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.ch16DBDataSet)).EndInit();
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.產品資料BindingSource)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.BindingSource bindingSource1;
        private ch16DBDataSet ch16DBDataSet;
        private ch16DBDataSetTableAdapters.產品資料TableAdapter 產品資料TableAdapter;
        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem 巡覽ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 第一筆ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 上一筆ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 下一筆ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 最末筆ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 編輯ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 新增ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 刪除ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 更新ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem tsmShow;
        private System.Windows.Forms.CheckBox chkIsSupply;
        private System.Windows.Forms.DateTimePicker dtpDate;
        private System.Windows.Forms.TextBox txtSpecial;
        private System.Windows.Forms.TextBox txtPrice;
        private System.Windows.Forms.TextBox txtName;
        private System.Windows.Forms.TextBox txtId;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.BindingSource 產品資料BindingSource;
    }
}

