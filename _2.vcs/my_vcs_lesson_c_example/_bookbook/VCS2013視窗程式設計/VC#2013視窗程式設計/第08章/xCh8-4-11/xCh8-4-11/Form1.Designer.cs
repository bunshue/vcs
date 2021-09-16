namespace xCh8_4_11
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
            this.dataGridView1 = new System.Windows.Forms.DataGridView();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.dataGridView2 = new System.Windows.Forms.DataGridView();
            this.訂單識別碼DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.員工識別碼DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.客戶識別碼DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.訂單日期DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.出貨日期DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.貨運公司識別碼DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.收貨人名稱DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.交貨地址DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.運送縣市DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.運送國家地區DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.運送郵遞區號DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.shipCountryRegionDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.運費DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.稅款DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.付款類型DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.付款日期DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.附註DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.稅率DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.課稅狀態DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.狀態識別碼DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.訂單BindingSource = new System.Windows.Forms.BindingSource(this.components);
            this.北風DataSet = new xCh8_4_11.北風DataSet();
            this.訂單TableAdapter = new xCh8_4_11.北風DataSetTableAdapters.訂單TableAdapter();
            this.訂單訂單詳細資料BindingSource = new System.Windows.Forms.BindingSource(this.components);
            this.訂單詳細資料TableAdapter = new xCh8_4_11.北風DataSetTableAdapters.訂單詳細資料TableAdapter();
            this.識別碼DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.訂單識別碼DataGridViewTextBoxColumn1 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.產品識別碼DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.數量DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.單價DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.折扣DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.狀態識別碼DataGridViewTextBoxColumn1 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.配置的日期DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.採購單識別碼DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.庫存識別碼DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.訂單BindingSource)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.北風DataSet)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.訂單訂單詳細資料BindingSource)).BeginInit();
            this.SuspendLayout();
            // 
            // dataGridView1
            // 
            this.dataGridView1.AutoGenerateColumns = false;
            this.dataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView1.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.訂單識別碼DataGridViewTextBoxColumn,
            this.員工識別碼DataGridViewTextBoxColumn,
            this.客戶識別碼DataGridViewTextBoxColumn,
            this.訂單日期DataGridViewTextBoxColumn,
            this.出貨日期DataGridViewTextBoxColumn,
            this.貨運公司識別碼DataGridViewTextBoxColumn,
            this.收貨人名稱DataGridViewTextBoxColumn,
            this.交貨地址DataGridViewTextBoxColumn,
            this.運送縣市DataGridViewTextBoxColumn,
            this.運送國家地區DataGridViewTextBoxColumn,
            this.運送郵遞區號DataGridViewTextBoxColumn,
            this.shipCountryRegionDataGridViewTextBoxColumn,
            this.運費DataGridViewTextBoxColumn,
            this.稅款DataGridViewTextBoxColumn,
            this.付款類型DataGridViewTextBoxColumn,
            this.付款日期DataGridViewTextBoxColumn,
            this.附註DataGridViewTextBoxColumn,
            this.稅率DataGridViewTextBoxColumn,
            this.課稅狀態DataGridViewTextBoxColumn,
            this.狀態識別碼DataGridViewTextBoxColumn});
            this.dataGridView1.DataSource = this.訂單BindingSource;
            this.dataGridView1.Location = new System.Drawing.Point(22, 26);
            this.dataGridView1.Name = "dataGridView1";
            this.dataGridView1.RowTemplate.Height = 25;
            this.dataGridView1.Size = new System.Drawing.Size(513, 150);
            this.dataGridView1.TabIndex = 0;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(19, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(77, 14);
            this.label1.TabIndex = 1;
            this.label1.Text = "訂單主檔：";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(19, 188);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(77, 14);
            this.label2.TabIndex = 2;
            this.label2.Text = "訂單明細：";
            // 
            // dataGridView2
            // 
            this.dataGridView2.AutoGenerateColumns = false;
            this.dataGridView2.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView2.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.識別碼DataGridViewTextBoxColumn,
            this.訂單識別碼DataGridViewTextBoxColumn1,
            this.產品識別碼DataGridViewTextBoxColumn,
            this.數量DataGridViewTextBoxColumn,
            this.單價DataGridViewTextBoxColumn,
            this.折扣DataGridViewTextBoxColumn,
            this.狀態識別碼DataGridViewTextBoxColumn1,
            this.配置的日期DataGridViewTextBoxColumn,
            this.採購單識別碼DataGridViewTextBoxColumn,
            this.庫存識別碼DataGridViewTextBoxColumn});
            this.dataGridView2.DataSource = this.訂單訂單詳細資料BindingSource;
            this.dataGridView2.Location = new System.Drawing.Point(22, 205);
            this.dataGridView2.Name = "dataGridView2";
            this.dataGridView2.RowTemplate.Height = 25;
            this.dataGridView2.Size = new System.Drawing.Size(513, 150);
            this.dataGridView2.TabIndex = 3;
            // 
            // 訂單識別碼DataGridViewTextBoxColumn
            // 
            this.訂單識別碼DataGridViewTextBoxColumn.DataPropertyName = "訂單識別碼";
            this.訂單識別碼DataGridViewTextBoxColumn.HeaderText = "訂單識別碼";
            this.訂單識別碼DataGridViewTextBoxColumn.Name = "訂單識別碼DataGridViewTextBoxColumn";
            // 
            // 員工識別碼DataGridViewTextBoxColumn
            // 
            this.員工識別碼DataGridViewTextBoxColumn.DataPropertyName = "員工識別碼";
            this.員工識別碼DataGridViewTextBoxColumn.HeaderText = "員工識別碼";
            this.員工識別碼DataGridViewTextBoxColumn.Name = "員工識別碼DataGridViewTextBoxColumn";
            // 
            // 客戶識別碼DataGridViewTextBoxColumn
            // 
            this.客戶識別碼DataGridViewTextBoxColumn.DataPropertyName = "客戶識別碼";
            this.客戶識別碼DataGridViewTextBoxColumn.HeaderText = "客戶識別碼";
            this.客戶識別碼DataGridViewTextBoxColumn.Name = "客戶識別碼DataGridViewTextBoxColumn";
            // 
            // 訂單日期DataGridViewTextBoxColumn
            // 
            this.訂單日期DataGridViewTextBoxColumn.DataPropertyName = "訂單日期";
            this.訂單日期DataGridViewTextBoxColumn.HeaderText = "訂單日期";
            this.訂單日期DataGridViewTextBoxColumn.Name = "訂單日期DataGridViewTextBoxColumn";
            // 
            // 出貨日期DataGridViewTextBoxColumn
            // 
            this.出貨日期DataGridViewTextBoxColumn.DataPropertyName = "出貨日期";
            this.出貨日期DataGridViewTextBoxColumn.HeaderText = "出貨日期";
            this.出貨日期DataGridViewTextBoxColumn.Name = "出貨日期DataGridViewTextBoxColumn";
            // 
            // 貨運公司識別碼DataGridViewTextBoxColumn
            // 
            this.貨運公司識別碼DataGridViewTextBoxColumn.DataPropertyName = "貨運公司識別碼";
            this.貨運公司識別碼DataGridViewTextBoxColumn.HeaderText = "貨運公司識別碼";
            this.貨運公司識別碼DataGridViewTextBoxColumn.Name = "貨運公司識別碼DataGridViewTextBoxColumn";
            // 
            // 收貨人名稱DataGridViewTextBoxColumn
            // 
            this.收貨人名稱DataGridViewTextBoxColumn.DataPropertyName = "收貨人名稱";
            this.收貨人名稱DataGridViewTextBoxColumn.HeaderText = "收貨人名稱";
            this.收貨人名稱DataGridViewTextBoxColumn.Name = "收貨人名稱DataGridViewTextBoxColumn";
            // 
            // 交貨地址DataGridViewTextBoxColumn
            // 
            this.交貨地址DataGridViewTextBoxColumn.DataPropertyName = "交貨地址";
            this.交貨地址DataGridViewTextBoxColumn.HeaderText = "交貨地址";
            this.交貨地址DataGridViewTextBoxColumn.Name = "交貨地址DataGridViewTextBoxColumn";
            // 
            // 運送縣市DataGridViewTextBoxColumn
            // 
            this.運送縣市DataGridViewTextBoxColumn.DataPropertyName = "運送縣/市";
            this.運送縣市DataGridViewTextBoxColumn.HeaderText = "運送縣/市";
            this.運送縣市DataGridViewTextBoxColumn.Name = "運送縣市DataGridViewTextBoxColumn";
            // 
            // 運送國家地區DataGridViewTextBoxColumn
            // 
            this.運送國家地區DataGridViewTextBoxColumn.DataPropertyName = "運送國家/地區";
            this.運送國家地區DataGridViewTextBoxColumn.HeaderText = "運送國家/地區";
            this.運送國家地區DataGridViewTextBoxColumn.Name = "運送國家地區DataGridViewTextBoxColumn";
            // 
            // 運送郵遞區號DataGridViewTextBoxColumn
            // 
            this.運送郵遞區號DataGridViewTextBoxColumn.DataPropertyName = "運送郵遞區號";
            this.運送郵遞區號DataGridViewTextBoxColumn.HeaderText = "運送郵遞區號";
            this.運送郵遞區號DataGridViewTextBoxColumn.Name = "運送郵遞區號DataGridViewTextBoxColumn";
            // 
            // shipCountryRegionDataGridViewTextBoxColumn
            // 
            this.shipCountryRegionDataGridViewTextBoxColumn.DataPropertyName = "Ship Country/Region";
            this.shipCountryRegionDataGridViewTextBoxColumn.HeaderText = "Ship Country/Region";
            this.shipCountryRegionDataGridViewTextBoxColumn.Name = "shipCountryRegionDataGridViewTextBoxColumn";
            // 
            // 運費DataGridViewTextBoxColumn
            // 
            this.運費DataGridViewTextBoxColumn.DataPropertyName = "運費";
            this.運費DataGridViewTextBoxColumn.HeaderText = "運費";
            this.運費DataGridViewTextBoxColumn.Name = "運費DataGridViewTextBoxColumn";
            // 
            // 稅款DataGridViewTextBoxColumn
            // 
            this.稅款DataGridViewTextBoxColumn.DataPropertyName = "稅款";
            this.稅款DataGridViewTextBoxColumn.HeaderText = "稅款";
            this.稅款DataGridViewTextBoxColumn.Name = "稅款DataGridViewTextBoxColumn";
            // 
            // 付款類型DataGridViewTextBoxColumn
            // 
            this.付款類型DataGridViewTextBoxColumn.DataPropertyName = "付款類型";
            this.付款類型DataGridViewTextBoxColumn.HeaderText = "付款類型";
            this.付款類型DataGridViewTextBoxColumn.Name = "付款類型DataGridViewTextBoxColumn";
            // 
            // 付款日期DataGridViewTextBoxColumn
            // 
            this.付款日期DataGridViewTextBoxColumn.DataPropertyName = "付款日期";
            this.付款日期DataGridViewTextBoxColumn.HeaderText = "付款日期";
            this.付款日期DataGridViewTextBoxColumn.Name = "付款日期DataGridViewTextBoxColumn";
            // 
            // 附註DataGridViewTextBoxColumn
            // 
            this.附註DataGridViewTextBoxColumn.DataPropertyName = "附註";
            this.附註DataGridViewTextBoxColumn.HeaderText = "附註";
            this.附註DataGridViewTextBoxColumn.Name = "附註DataGridViewTextBoxColumn";
            // 
            // 稅率DataGridViewTextBoxColumn
            // 
            this.稅率DataGridViewTextBoxColumn.DataPropertyName = "稅率";
            this.稅率DataGridViewTextBoxColumn.HeaderText = "稅率";
            this.稅率DataGridViewTextBoxColumn.Name = "稅率DataGridViewTextBoxColumn";
            // 
            // 課稅狀態DataGridViewTextBoxColumn
            // 
            this.課稅狀態DataGridViewTextBoxColumn.DataPropertyName = "課稅狀態";
            this.課稅狀態DataGridViewTextBoxColumn.HeaderText = "課稅狀態";
            this.課稅狀態DataGridViewTextBoxColumn.Name = "課稅狀態DataGridViewTextBoxColumn";
            // 
            // 狀態識別碼DataGridViewTextBoxColumn
            // 
            this.狀態識別碼DataGridViewTextBoxColumn.DataPropertyName = "狀態識別碼";
            this.狀態識別碼DataGridViewTextBoxColumn.HeaderText = "狀態識別碼";
            this.狀態識別碼DataGridViewTextBoxColumn.Name = "狀態識別碼DataGridViewTextBoxColumn";
            // 
            // 訂單BindingSource
            // 
            this.訂單BindingSource.DataMember = "訂單";
            this.訂單BindingSource.DataSource = this.北風DataSet;
            // 
            // 北風DataSet
            // 
            this.北風DataSet.DataSetName = "北風DataSet";
            this.北風DataSet.SchemaSerializationMode = System.Data.SchemaSerializationMode.IncludeSchema;
            // 
            // 訂單TableAdapter
            // 
            this.訂單TableAdapter.ClearBeforeFill = true;
            // 
            // 訂單訂單詳細資料BindingSource
            // 
            this.訂單訂單詳細資料BindingSource.DataMember = "訂單_訂單詳細資料";
            this.訂單訂單詳細資料BindingSource.DataSource = this.訂單BindingSource;
            // 
            // 訂單詳細資料TableAdapter
            // 
            this.訂單詳細資料TableAdapter.ClearBeforeFill = true;
            // 
            // 識別碼DataGridViewTextBoxColumn
            // 
            this.識別碼DataGridViewTextBoxColumn.DataPropertyName = "識別碼";
            this.識別碼DataGridViewTextBoxColumn.HeaderText = "識別碼";
            this.識別碼DataGridViewTextBoxColumn.Name = "識別碼DataGridViewTextBoxColumn";
            // 
            // 訂單識別碼DataGridViewTextBoxColumn1
            // 
            this.訂單識別碼DataGridViewTextBoxColumn1.DataPropertyName = "訂單識別碼";
            this.訂單識別碼DataGridViewTextBoxColumn1.HeaderText = "訂單識別碼";
            this.訂單識別碼DataGridViewTextBoxColumn1.Name = "訂單識別碼DataGridViewTextBoxColumn1";
            // 
            // 產品識別碼DataGridViewTextBoxColumn
            // 
            this.產品識別碼DataGridViewTextBoxColumn.DataPropertyName = "產品識別碼";
            this.產品識別碼DataGridViewTextBoxColumn.HeaderText = "產品識別碼";
            this.產品識別碼DataGridViewTextBoxColumn.Name = "產品識別碼DataGridViewTextBoxColumn";
            // 
            // 數量DataGridViewTextBoxColumn
            // 
            this.數量DataGridViewTextBoxColumn.DataPropertyName = "數量";
            this.數量DataGridViewTextBoxColumn.HeaderText = "數量";
            this.數量DataGridViewTextBoxColumn.Name = "數量DataGridViewTextBoxColumn";
            // 
            // 單價DataGridViewTextBoxColumn
            // 
            this.單價DataGridViewTextBoxColumn.DataPropertyName = "單價";
            this.單價DataGridViewTextBoxColumn.HeaderText = "單價";
            this.單價DataGridViewTextBoxColumn.Name = "單價DataGridViewTextBoxColumn";
            // 
            // 折扣DataGridViewTextBoxColumn
            // 
            this.折扣DataGridViewTextBoxColumn.DataPropertyName = "折扣";
            this.折扣DataGridViewTextBoxColumn.HeaderText = "折扣";
            this.折扣DataGridViewTextBoxColumn.Name = "折扣DataGridViewTextBoxColumn";
            // 
            // 狀態識別碼DataGridViewTextBoxColumn1
            // 
            this.狀態識別碼DataGridViewTextBoxColumn1.DataPropertyName = "狀態識別碼";
            this.狀態識別碼DataGridViewTextBoxColumn1.HeaderText = "狀態識別碼";
            this.狀態識別碼DataGridViewTextBoxColumn1.Name = "狀態識別碼DataGridViewTextBoxColumn1";
            // 
            // 配置的日期DataGridViewTextBoxColumn
            // 
            this.配置的日期DataGridViewTextBoxColumn.DataPropertyName = "配置的日期";
            this.配置的日期DataGridViewTextBoxColumn.HeaderText = "配置的日期";
            this.配置的日期DataGridViewTextBoxColumn.Name = "配置的日期DataGridViewTextBoxColumn";
            // 
            // 採購單識別碼DataGridViewTextBoxColumn
            // 
            this.採購單識別碼DataGridViewTextBoxColumn.DataPropertyName = "採購單識別碼";
            this.採購單識別碼DataGridViewTextBoxColumn.HeaderText = "採購單識別碼";
            this.採購單識別碼DataGridViewTextBoxColumn.Name = "採購單識別碼DataGridViewTextBoxColumn";
            // 
            // 庫存識別碼DataGridViewTextBoxColumn
            // 
            this.庫存識別碼DataGridViewTextBoxColumn.DataPropertyName = "庫存識別碼";
            this.庫存識別碼DataGridViewTextBoxColumn.HeaderText = "庫存識別碼";
            this.庫存識別碼DataGridViewTextBoxColumn.Name = "庫存識別碼DataGridViewTextBoxColumn";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(557, 369);
            this.Controls.Add(this.dataGridView2);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.dataGridView1);
            this.Name = "Form1";
            this.Text = "關聯式資料表";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.訂單BindingSource)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.北風DataSet)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.訂單訂單詳細資料BindingSource)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DataGridView dataGridView1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.DataGridView dataGridView2;
        private 北風DataSet 北風DataSet;
        private System.Windows.Forms.BindingSource 訂單BindingSource;
        private 北風DataSetTableAdapters.訂單TableAdapter 訂單TableAdapter;
        private System.Windows.Forms.DataGridViewTextBoxColumn 訂單識別碼DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 員工識別碼DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 客戶識別碼DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 訂單日期DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 出貨日期DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 貨運公司識別碼DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 收貨人名稱DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 交貨地址DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 運送縣市DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 運送國家地區DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 運送郵遞區號DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn shipCountryRegionDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 運費DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 稅款DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 付款類型DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 付款日期DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 附註DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 稅率DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 課稅狀態DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 狀態識別碼DataGridViewTextBoxColumn;
        private System.Windows.Forms.BindingSource 訂單訂單詳細資料BindingSource;
        private 北風DataSetTableAdapters.訂單詳細資料TableAdapter 訂單詳細資料TableAdapter;
        private System.Windows.Forms.DataGridViewTextBoxColumn 識別碼DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 訂單識別碼DataGridViewTextBoxColumn1;
        private System.Windows.Forms.DataGridViewTextBoxColumn 產品識別碼DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 數量DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 單價DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 折扣DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 狀態識別碼DataGridViewTextBoxColumn1;
        private System.Windows.Forms.DataGridViewTextBoxColumn 配置的日期DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 採購單識別碼DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 庫存識別碼DataGridViewTextBoxColumn;

    }
}

