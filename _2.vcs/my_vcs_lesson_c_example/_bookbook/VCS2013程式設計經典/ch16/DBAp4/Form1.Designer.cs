namespace DBAp4
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
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.dgDepartment = new System.Windows.Forms.DataGridView();
            this.dgEmployee = new System.Windows.Forms.DataGridView();
            this.myDBDataSet = new DBAp4.MyDBDataSet();
            this.部門BindingSource = new System.Windows.Forms.BindingSource(this.components);
            this.部門TableAdapter = new DBAp4.MyDBDataSetTableAdapters.部門TableAdapter();
            this.部門編號DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.部門名稱DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.部門員工BindingSource = new System.Windows.Forms.BindingSource(this.components);
            this.員工TableAdapter = new DBAp4.MyDBDataSetTableAdapters.員工TableAdapter();
            this.員工編號DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.部門編號DataGridViewTextBoxColumn1 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.姓名DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.電話DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.薪資DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            ((System.ComponentModel.ISupportInitialize)(this.bindingSource1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dgDepartment)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dgEmployee)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.myDBDataSet)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.部門BindingSource)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.部門員工BindingSource)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(23, 19);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(29, 12);
            this.label1.TabIndex = 0;
            this.label1.Text = "部門";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(23, 200);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(29, 12);
            this.label2.TabIndex = 1;
            this.label2.Text = "員工";
            // 
            // dgDepartment
            // 
            this.dgDepartment.AutoGenerateColumns = false;
            this.dgDepartment.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgDepartment.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.部門編號DataGridViewTextBoxColumn,
            this.部門名稱DataGridViewTextBoxColumn});
            this.dgDepartment.DataSource = this.部門BindingSource;
            this.dgDepartment.Location = new System.Drawing.Point(70, 19);
            this.dgDepartment.Name = "dgDepartment";
            this.dgDepartment.RowTemplate.Height = 24;
            this.dgDepartment.Size = new System.Drawing.Size(378, 150);
            this.dgDepartment.TabIndex = 2;
            // 
            // dgEmployee
            // 
            this.dgEmployee.AutoGenerateColumns = false;
            this.dgEmployee.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgEmployee.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.員工編號DataGridViewTextBoxColumn,
            this.部門編號DataGridViewTextBoxColumn1,
            this.姓名DataGridViewTextBoxColumn,
            this.電話DataGridViewTextBoxColumn,
            this.薪資DataGridViewTextBoxColumn});
            this.dgEmployee.DataSource = this.部門員工BindingSource;
            this.dgEmployee.Location = new System.Drawing.Point(70, 200);
            this.dgEmployee.Name = "dgEmployee";
            this.dgEmployee.RowTemplate.Height = 24;
            this.dgEmployee.Size = new System.Drawing.Size(471, 150);
            this.dgEmployee.TabIndex = 3;
            // 
            // myDBDataSet
            // 
            this.myDBDataSet.DataSetName = "MyDBDataSet";
            this.myDBDataSet.SchemaSerializationMode = System.Data.SchemaSerializationMode.IncludeSchema;
            // 
            // 部門BindingSource
            // 
            this.部門BindingSource.DataMember = "部門";
            this.部門BindingSource.DataSource = this.myDBDataSet;
            // 
            // 部門TableAdapter
            // 
            this.部門TableAdapter.ClearBeforeFill = true;
            // 
            // 部門編號DataGridViewTextBoxColumn
            // 
            this.部門編號DataGridViewTextBoxColumn.DataPropertyName = "部門編號";
            this.部門編號DataGridViewTextBoxColumn.HeaderText = "部門編號";
            this.部門編號DataGridViewTextBoxColumn.Name = "部門編號DataGridViewTextBoxColumn";
            this.部門編號DataGridViewTextBoxColumn.ReadOnly = true;
            // 
            // 部門名稱DataGridViewTextBoxColumn
            // 
            this.部門名稱DataGridViewTextBoxColumn.DataPropertyName = "部門名稱";
            this.部門名稱DataGridViewTextBoxColumn.HeaderText = "部門名稱";
            this.部門名稱DataGridViewTextBoxColumn.Name = "部門名稱DataGridViewTextBoxColumn";
            // 
            // 部門員工BindingSource
            // 
            this.部門員工BindingSource.DataMember = "部門_員工";
            this.部門員工BindingSource.DataSource = this.部門BindingSource;
            // 
            // 員工TableAdapter
            // 
            this.員工TableAdapter.ClearBeforeFill = true;
            // 
            // 員工編號DataGridViewTextBoxColumn
            // 
            this.員工編號DataGridViewTextBoxColumn.DataPropertyName = "員工編號";
            this.員工編號DataGridViewTextBoxColumn.HeaderText = "員工編號";
            this.員工編號DataGridViewTextBoxColumn.Name = "員工編號DataGridViewTextBoxColumn";
            // 
            // 部門編號DataGridViewTextBoxColumn1
            // 
            this.部門編號DataGridViewTextBoxColumn1.DataPropertyName = "部門編號";
            this.部門編號DataGridViewTextBoxColumn1.HeaderText = "部門編號";
            this.部門編號DataGridViewTextBoxColumn1.Name = "部門編號DataGridViewTextBoxColumn1";
            // 
            // 姓名DataGridViewTextBoxColumn
            // 
            this.姓名DataGridViewTextBoxColumn.DataPropertyName = "姓名";
            this.姓名DataGridViewTextBoxColumn.HeaderText = "姓名";
            this.姓名DataGridViewTextBoxColumn.Name = "姓名DataGridViewTextBoxColumn";
            // 
            // 電話DataGridViewTextBoxColumn
            // 
            this.電話DataGridViewTextBoxColumn.DataPropertyName = "電話";
            this.電話DataGridViewTextBoxColumn.HeaderText = "電話";
            this.電話DataGridViewTextBoxColumn.Name = "電話DataGridViewTextBoxColumn";
            // 
            // 薪資DataGridViewTextBoxColumn
            // 
            this.薪資DataGridViewTextBoxColumn.DataPropertyName = "薪資";
            this.薪資DataGridViewTextBoxColumn.HeaderText = "薪資";
            this.薪資DataGridViewTextBoxColumn.Name = "薪資DataGridViewTextBoxColumn";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(568, 380);
            this.Controls.Add(this.dgEmployee);
            this.Controls.Add(this.dgDepartment);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.bindingSource1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dgDepartment)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dgEmployee)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.myDBDataSet)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.部門BindingSource)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.部門員工BindingSource)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.BindingSource bindingSource1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.DataGridView dgDepartment;
        private System.Windows.Forms.DataGridView dgEmployee;
        private MyDBDataSet myDBDataSet;
        private System.Windows.Forms.BindingSource 部門BindingSource;
        private MyDBDataSetTableAdapters.部門TableAdapter 部門TableAdapter;
        private System.Windows.Forms.DataGridViewTextBoxColumn 部門編號DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 部門名稱DataGridViewTextBoxColumn;
        private System.Windows.Forms.BindingSource 部門員工BindingSource;
        private MyDBDataSetTableAdapters.員工TableAdapter 員工TableAdapter;
        private System.Windows.Forms.DataGridViewTextBoxColumn 員工編號DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 部門編號DataGridViewTextBoxColumn1;
        private System.Windows.Forms.DataGridViewTextBoxColumn 姓名DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 電話DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 薪資DataGridViewTextBoxColumn;
    }
}

