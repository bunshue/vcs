namespace xCh8_6_1_11
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
            Microsoft.Reporting.WinForms.ReportDataSource reportDataSource1 = new Microsoft.Reporting.WinForms.ReportDataSource();
            this.reportViewer1 = new Microsoft.Reporting.WinForms.ReportViewer();
            this.NorthwindDataSet = new xCh8_6_1_11.NorthwindDataSet();
            this.員工BindingSource = new System.Windows.Forms.BindingSource(this.components);
            this.員工TableAdapter = new xCh8_6_1_11.NorthwindDataSetTableAdapters.員工TableAdapter();
            ((System.ComponentModel.ISupportInitialize)(this.NorthwindDataSet)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.員工BindingSource)).BeginInit();
            this.SuspendLayout();
            // 
            // reportViewer1
            // 
            reportDataSource1.Name = "DataSet1";
            reportDataSource1.Value = this.員工BindingSource;
            this.reportViewer1.LocalReport.DataSources.Add(reportDataSource1);
            this.reportViewer1.LocalReport.ReportEmbeddedResource = "xCh21_6_1_11.Report1.rdlc";
            this.reportViewer1.Location = new System.Drawing.Point(0, 0);
            this.reportViewer1.Name = "reportViewer1";
            this.reportViewer1.Size = new System.Drawing.Size(396, 246);
            this.reportViewer1.TabIndex = 0;
            // 
            // NorthwindDataSet
            // 
            this.NorthwindDataSet.DataSetName = "NorthwindDataSet";
            this.NorthwindDataSet.SchemaSerializationMode = System.Data.SchemaSerializationMode.IncludeSchema;
            // 
            // 員工BindingSource
            // 
            this.員工BindingSource.DataMember = "員工";
            this.員工BindingSource.DataSource = this.NorthwindDataSet;
            // 
            // 員工TableAdapter
            // 
            this.員工TableAdapter.ClearBeforeFill = true;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(404, 260);
            this.Controls.Add(this.reportViewer1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.NorthwindDataSet)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.員工BindingSource)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private Microsoft.Reporting.WinForms.ReportViewer reportViewer1;
        private System.Windows.Forms.BindingSource 員工BindingSource;
        private NorthwindDataSet NorthwindDataSet;
        private NorthwindDataSetTableAdapters.員工TableAdapter 員工TableAdapter;
    }
}

