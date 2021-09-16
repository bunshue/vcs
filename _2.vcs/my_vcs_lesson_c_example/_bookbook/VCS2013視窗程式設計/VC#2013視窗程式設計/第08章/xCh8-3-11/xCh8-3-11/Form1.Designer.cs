namespace xCh8_3_11
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.bindingSource1 = new System.Windows.Forms.BindingSource(this.components);
            this.北風DataSet = new xCh8_3_11.北風DataSet();
            this.dataGridView1 = new System.Windows.Forms.DataGridView();
            this.識別碼DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.公司DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.姓氏DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.名字DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.電子郵件地址DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.職稱DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.商務電話DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.住家電話DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.行動電話DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.傳真號碼DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.地址DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.市鎮DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.縣市DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.郵遞區號DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.國家地區DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.網頁DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.附註DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.附件DataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.員工BindingSource = new System.Windows.Forms.BindingSource(this.components);
            this.員工TableAdapter = new xCh8_3_11.北風DataSetTableAdapters.員工TableAdapter();
            this.bindingNavigator1 = new System.Windows.Forms.BindingNavigator(this.components);
            this.bindingNavigatorAddNewItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorCountItem = new System.Windows.Forms.ToolStripLabel();
            this.bindingNavigatorDeleteItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorMoveFirstItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorMovePreviousItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorSeparator = new System.Windows.Forms.ToolStripSeparator();
            this.bindingNavigatorPositionItem = new System.Windows.Forms.ToolStripTextBox();
            this.bindingNavigatorSeparator1 = new System.Windows.Forms.ToolStripSeparator();
            this.bindingNavigatorMoveNextItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorMoveLastItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorSeparator2 = new System.Windows.Forms.ToolStripSeparator();
            ((System.ComponentModel.ISupportInitialize)(this.bindingSource1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.北風DataSet)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.員工BindingSource)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.bindingNavigator1)).BeginInit();
            this.bindingNavigator1.SuspendLayout();
            this.SuspendLayout();
            // 
            // bindingSource1
            // 
            this.bindingSource1.DataSource = this.北風DataSet;
            this.bindingSource1.Position = 0;
            // 
            // 北風DataSet
            // 
            this.北風DataSet.DataSetName = "北風DataSet";
            this.北風DataSet.SchemaSerializationMode = System.Data.SchemaSerializationMode.IncludeSchema;
            // 
            // dataGridView1
            // 
            this.dataGridView1.AutoGenerateColumns = false;
            this.dataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView1.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.識別碼DataGridViewTextBoxColumn,
            this.公司DataGridViewTextBoxColumn,
            this.姓氏DataGridViewTextBoxColumn,
            this.名字DataGridViewTextBoxColumn,
            this.電子郵件地址DataGridViewTextBoxColumn,
            this.職稱DataGridViewTextBoxColumn,
            this.商務電話DataGridViewTextBoxColumn,
            this.住家電話DataGridViewTextBoxColumn,
            this.行動電話DataGridViewTextBoxColumn,
            this.傳真號碼DataGridViewTextBoxColumn,
            this.地址DataGridViewTextBoxColumn,
            this.市鎮DataGridViewTextBoxColumn,
            this.縣市DataGridViewTextBoxColumn,
            this.郵遞區號DataGridViewTextBoxColumn,
            this.國家地區DataGridViewTextBoxColumn,
            this.網頁DataGridViewTextBoxColumn,
            this.附註DataGridViewTextBoxColumn,
            this.附件DataGridViewTextBoxColumn});
            this.dataGridView1.DataSource = this.員工BindingSource;
            this.dataGridView1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.dataGridView1.Location = new System.Drawing.Point(0, 0);
            this.dataGridView1.Name = "dataGridView1";
            this.dataGridView1.RowTemplate.Height = 25;
            this.dataGridView1.Size = new System.Drawing.Size(513, 260);
            this.dataGridView1.TabIndex = 0;
            // 
            // 識別碼DataGridViewTextBoxColumn
            // 
            this.識別碼DataGridViewTextBoxColumn.DataPropertyName = "識別碼";
            this.識別碼DataGridViewTextBoxColumn.HeaderText = "識別碼";
            this.識別碼DataGridViewTextBoxColumn.Name = "識別碼DataGridViewTextBoxColumn";
            // 
            // 公司DataGridViewTextBoxColumn
            // 
            this.公司DataGridViewTextBoxColumn.DataPropertyName = "公司";
            this.公司DataGridViewTextBoxColumn.HeaderText = "公司";
            this.公司DataGridViewTextBoxColumn.Name = "公司DataGridViewTextBoxColumn";
            // 
            // 姓氏DataGridViewTextBoxColumn
            // 
            this.姓氏DataGridViewTextBoxColumn.DataPropertyName = "姓氏";
            this.姓氏DataGridViewTextBoxColumn.HeaderText = "姓氏";
            this.姓氏DataGridViewTextBoxColumn.Name = "姓氏DataGridViewTextBoxColumn";
            // 
            // 名字DataGridViewTextBoxColumn
            // 
            this.名字DataGridViewTextBoxColumn.DataPropertyName = "名字";
            this.名字DataGridViewTextBoxColumn.HeaderText = "名字";
            this.名字DataGridViewTextBoxColumn.Name = "名字DataGridViewTextBoxColumn";
            // 
            // 電子郵件地址DataGridViewTextBoxColumn
            // 
            this.電子郵件地址DataGridViewTextBoxColumn.DataPropertyName = "電子郵件地址";
            this.電子郵件地址DataGridViewTextBoxColumn.HeaderText = "電子郵件地址";
            this.電子郵件地址DataGridViewTextBoxColumn.Name = "電子郵件地址DataGridViewTextBoxColumn";
            // 
            // 職稱DataGridViewTextBoxColumn
            // 
            this.職稱DataGridViewTextBoxColumn.DataPropertyName = "職稱";
            this.職稱DataGridViewTextBoxColumn.HeaderText = "職稱";
            this.職稱DataGridViewTextBoxColumn.Name = "職稱DataGridViewTextBoxColumn";
            // 
            // 商務電話DataGridViewTextBoxColumn
            // 
            this.商務電話DataGridViewTextBoxColumn.DataPropertyName = "商務電話";
            this.商務電話DataGridViewTextBoxColumn.HeaderText = "商務電話";
            this.商務電話DataGridViewTextBoxColumn.Name = "商務電話DataGridViewTextBoxColumn";
            // 
            // 住家電話DataGridViewTextBoxColumn
            // 
            this.住家電話DataGridViewTextBoxColumn.DataPropertyName = "住家電話";
            this.住家電話DataGridViewTextBoxColumn.HeaderText = "住家電話";
            this.住家電話DataGridViewTextBoxColumn.Name = "住家電話DataGridViewTextBoxColumn";
            // 
            // 行動電話DataGridViewTextBoxColumn
            // 
            this.行動電話DataGridViewTextBoxColumn.DataPropertyName = "行動電話";
            this.行動電話DataGridViewTextBoxColumn.HeaderText = "行動電話";
            this.行動電話DataGridViewTextBoxColumn.Name = "行動電話DataGridViewTextBoxColumn";
            // 
            // 傳真號碼DataGridViewTextBoxColumn
            // 
            this.傳真號碼DataGridViewTextBoxColumn.DataPropertyName = "傳真號碼";
            this.傳真號碼DataGridViewTextBoxColumn.HeaderText = "傳真號碼";
            this.傳真號碼DataGridViewTextBoxColumn.Name = "傳真號碼DataGridViewTextBoxColumn";
            // 
            // 地址DataGridViewTextBoxColumn
            // 
            this.地址DataGridViewTextBoxColumn.DataPropertyName = "地址";
            this.地址DataGridViewTextBoxColumn.HeaderText = "地址";
            this.地址DataGridViewTextBoxColumn.Name = "地址DataGridViewTextBoxColumn";
            // 
            // 市鎮DataGridViewTextBoxColumn
            // 
            this.市鎮DataGridViewTextBoxColumn.DataPropertyName = "市/鎮";
            this.市鎮DataGridViewTextBoxColumn.HeaderText = "市/鎮";
            this.市鎮DataGridViewTextBoxColumn.Name = "市鎮DataGridViewTextBoxColumn";
            // 
            // 縣市DataGridViewTextBoxColumn
            // 
            this.縣市DataGridViewTextBoxColumn.DataPropertyName = "縣/市";
            this.縣市DataGridViewTextBoxColumn.HeaderText = "縣/市";
            this.縣市DataGridViewTextBoxColumn.Name = "縣市DataGridViewTextBoxColumn";
            // 
            // 郵遞區號DataGridViewTextBoxColumn
            // 
            this.郵遞區號DataGridViewTextBoxColumn.DataPropertyName = "郵遞區號";
            this.郵遞區號DataGridViewTextBoxColumn.HeaderText = "郵遞區號";
            this.郵遞區號DataGridViewTextBoxColumn.Name = "郵遞區號DataGridViewTextBoxColumn";
            // 
            // 國家地區DataGridViewTextBoxColumn
            // 
            this.國家地區DataGridViewTextBoxColumn.DataPropertyName = "國家/地區";
            this.國家地區DataGridViewTextBoxColumn.HeaderText = "國家/地區";
            this.國家地區DataGridViewTextBoxColumn.Name = "國家地區DataGridViewTextBoxColumn";
            // 
            // 網頁DataGridViewTextBoxColumn
            // 
            this.網頁DataGridViewTextBoxColumn.DataPropertyName = "網頁";
            this.網頁DataGridViewTextBoxColumn.HeaderText = "網頁";
            this.網頁DataGridViewTextBoxColumn.Name = "網頁DataGridViewTextBoxColumn";
            // 
            // 附註DataGridViewTextBoxColumn
            // 
            this.附註DataGridViewTextBoxColumn.DataPropertyName = "附註";
            this.附註DataGridViewTextBoxColumn.HeaderText = "附註";
            this.附註DataGridViewTextBoxColumn.Name = "附註DataGridViewTextBoxColumn";
            // 
            // 附件DataGridViewTextBoxColumn
            // 
            this.附件DataGridViewTextBoxColumn.DataPropertyName = "附件";
            this.附件DataGridViewTextBoxColumn.HeaderText = "附件";
            this.附件DataGridViewTextBoxColumn.Name = "附件DataGridViewTextBoxColumn";
            // 
            // 員工BindingSource
            // 
            this.員工BindingSource.DataMember = "員工";
            this.員工BindingSource.DataSource = this.bindingSource1;
            // 
            // 員工TableAdapter
            // 
            this.員工TableAdapter.ClearBeforeFill = true;
            // 
            // bindingNavigator1
            // 
            this.bindingNavigator1.AddNewItem = this.bindingNavigatorAddNewItem;
            this.bindingNavigator1.BindingSource = this.員工BindingSource;
            this.bindingNavigator1.CountItem = this.bindingNavigatorCountItem;
            this.bindingNavigator1.DeleteItem = this.bindingNavigatorDeleteItem;
            this.bindingNavigator1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.bindingNavigatorMoveFirstItem,
            this.bindingNavigatorMovePreviousItem,
            this.bindingNavigatorSeparator,
            this.bindingNavigatorPositionItem,
            this.bindingNavigatorCountItem,
            this.bindingNavigatorSeparator1,
            this.bindingNavigatorMoveNextItem,
            this.bindingNavigatorMoveLastItem,
            this.bindingNavigatorSeparator2,
            this.bindingNavigatorAddNewItem,
            this.bindingNavigatorDeleteItem});
            this.bindingNavigator1.Location = new System.Drawing.Point(0, 0);
            this.bindingNavigator1.MoveFirstItem = this.bindingNavigatorMoveFirstItem;
            this.bindingNavigator1.MoveLastItem = this.bindingNavigatorMoveLastItem;
            this.bindingNavigator1.MoveNextItem = this.bindingNavigatorMoveNextItem;
            this.bindingNavigator1.MovePreviousItem = this.bindingNavigatorMovePreviousItem;
            this.bindingNavigator1.Name = "bindingNavigator1";
            this.bindingNavigator1.PositionItem = this.bindingNavigatorPositionItem;
            this.bindingNavigator1.Size = new System.Drawing.Size(513, 25);
            this.bindingNavigator1.TabIndex = 1;
            this.bindingNavigator1.Text = "bindingNavigator1";
            // 
            // bindingNavigatorAddNewItem
            // 
            this.bindingNavigatorAddNewItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.bindingNavigatorAddNewItem.Image = ((System.Drawing.Image)(resources.GetObject("bindingNavigatorAddNewItem.Image")));
            this.bindingNavigatorAddNewItem.Name = "bindingNavigatorAddNewItem";
            this.bindingNavigatorAddNewItem.RightToLeftAutoMirrorImage = true;
            this.bindingNavigatorAddNewItem.Size = new System.Drawing.Size(23, 22);
            this.bindingNavigatorAddNewItem.Text = "加入新的";
            // 
            // bindingNavigatorCountItem
            // 
            this.bindingNavigatorCountItem.Name = "bindingNavigatorCountItem";
            this.bindingNavigatorCountItem.Size = new System.Drawing.Size(30, 22);
            this.bindingNavigatorCountItem.Text = "/{0}";
            this.bindingNavigatorCountItem.ToolTipText = "項目總數";
            // 
            // bindingNavigatorDeleteItem
            // 
            this.bindingNavigatorDeleteItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.bindingNavigatorDeleteItem.Image = ((System.Drawing.Image)(resources.GetObject("bindingNavigatorDeleteItem.Image")));
            this.bindingNavigatorDeleteItem.Name = "bindingNavigatorDeleteItem";
            this.bindingNavigatorDeleteItem.RightToLeftAutoMirrorImage = true;
            this.bindingNavigatorDeleteItem.Size = new System.Drawing.Size(23, 22);
            this.bindingNavigatorDeleteItem.Text = "刪除";
            // 
            // bindingNavigatorMoveFirstItem
            // 
            this.bindingNavigatorMoveFirstItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.bindingNavigatorMoveFirstItem.Image = ((System.Drawing.Image)(resources.GetObject("bindingNavigatorMoveFirstItem.Image")));
            this.bindingNavigatorMoveFirstItem.Name = "bindingNavigatorMoveFirstItem";
            this.bindingNavigatorMoveFirstItem.RightToLeftAutoMirrorImage = true;
            this.bindingNavigatorMoveFirstItem.Size = new System.Drawing.Size(23, 22);
            this.bindingNavigatorMoveFirstItem.Text = "移到最前面";
            // 
            // bindingNavigatorMovePreviousItem
            // 
            this.bindingNavigatorMovePreviousItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.bindingNavigatorMovePreviousItem.Image = ((System.Drawing.Image)(resources.GetObject("bindingNavigatorMovePreviousItem.Image")));
            this.bindingNavigatorMovePreviousItem.Name = "bindingNavigatorMovePreviousItem";
            this.bindingNavigatorMovePreviousItem.RightToLeftAutoMirrorImage = true;
            this.bindingNavigatorMovePreviousItem.Size = new System.Drawing.Size(23, 22);
            this.bindingNavigatorMovePreviousItem.Text = "移到上一個";
            // 
            // bindingNavigatorSeparator
            // 
            this.bindingNavigatorSeparator.Name = "bindingNavigatorSeparator";
            this.bindingNavigatorSeparator.Size = new System.Drawing.Size(6, 25);
            // 
            // bindingNavigatorPositionItem
            // 
            this.bindingNavigatorPositionItem.AccessibleName = "位置";
            this.bindingNavigatorPositionItem.AutoSize = false;
            this.bindingNavigatorPositionItem.Name = "bindingNavigatorPositionItem";
            this.bindingNavigatorPositionItem.Size = new System.Drawing.Size(50, 25);
            this.bindingNavigatorPositionItem.Text = "0";
            this.bindingNavigatorPositionItem.ToolTipText = "目前的位置";
            // 
            // bindingNavigatorSeparator1
            // 
            this.bindingNavigatorSeparator1.Name = "bindingNavigatorSeparator1";
            this.bindingNavigatorSeparator1.Size = new System.Drawing.Size(6, 25);
            // 
            // bindingNavigatorMoveNextItem
            // 
            this.bindingNavigatorMoveNextItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.bindingNavigatorMoveNextItem.Image = ((System.Drawing.Image)(resources.GetObject("bindingNavigatorMoveNextItem.Image")));
            this.bindingNavigatorMoveNextItem.Name = "bindingNavigatorMoveNextItem";
            this.bindingNavigatorMoveNextItem.RightToLeftAutoMirrorImage = true;
            this.bindingNavigatorMoveNextItem.Size = new System.Drawing.Size(23, 22);
            this.bindingNavigatorMoveNextItem.Text = "移到下一個";
            // 
            // bindingNavigatorMoveLastItem
            // 
            this.bindingNavigatorMoveLastItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.bindingNavigatorMoveLastItem.Image = ((System.Drawing.Image)(resources.GetObject("bindingNavigatorMoveLastItem.Image")));
            this.bindingNavigatorMoveLastItem.Name = "bindingNavigatorMoveLastItem";
            this.bindingNavigatorMoveLastItem.RightToLeftAutoMirrorImage = true;
            this.bindingNavigatorMoveLastItem.Size = new System.Drawing.Size(23, 22);
            this.bindingNavigatorMoveLastItem.Text = "移到最後面";
            // 
            // bindingNavigatorSeparator2
            // 
            this.bindingNavigatorSeparator2.Name = "bindingNavigatorSeparator2";
            this.bindingNavigatorSeparator2.Size = new System.Drawing.Size(6, 25);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(513, 260);
            this.Controls.Add(this.bindingNavigator1);
            this.Controls.Add(this.dataGridView1);
            this.Name = "Form1";
            this.Text = "資料控制項間的關係範例";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.bindingSource1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.北風DataSet)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.員工BindingSource)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.bindingNavigator1)).EndInit();
            this.bindingNavigator1.ResumeLayout(false);
            this.bindingNavigator1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.BindingSource bindingSource1;
        private 北風DataSet 北風DataSet;
        private System.Windows.Forms.DataGridView dataGridView1;
        private System.Windows.Forms.BindingSource 員工BindingSource;
        private 北風DataSetTableAdapters.員工TableAdapter 員工TableAdapter;
        private System.Windows.Forms.DataGridViewTextBoxColumn 識別碼DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 公司DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 姓氏DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 名字DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 電子郵件地址DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 職稱DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 商務電話DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 住家電話DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 行動電話DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 傳真號碼DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 地址DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 市鎮DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 縣市DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 郵遞區號DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 國家地區DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 網頁DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 附註DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn 附件DataGridViewTextBoxColumn;
        private System.Windows.Forms.BindingNavigator bindingNavigator1;
        private System.Windows.Forms.ToolStripButton bindingNavigatorAddNewItem;
        private System.Windows.Forms.ToolStripLabel bindingNavigatorCountItem;
        private System.Windows.Forms.ToolStripButton bindingNavigatorDeleteItem;
        private System.Windows.Forms.ToolStripButton bindingNavigatorMoveFirstItem;
        private System.Windows.Forms.ToolStripButton bindingNavigatorMovePreviousItem;
        private System.Windows.Forms.ToolStripSeparator bindingNavigatorSeparator;
        private System.Windows.Forms.ToolStripTextBox bindingNavigatorPositionItem;
        private System.Windows.Forms.ToolStripSeparator bindingNavigatorSeparator1;
        private System.Windows.Forms.ToolStripButton bindingNavigatorMoveNextItem;
        private System.Windows.Forms.ToolStripButton bindingNavigatorMoveLastItem;
        private System.Windows.Forms.ToolStripSeparator bindingNavigatorSeparator2;
    }
}

