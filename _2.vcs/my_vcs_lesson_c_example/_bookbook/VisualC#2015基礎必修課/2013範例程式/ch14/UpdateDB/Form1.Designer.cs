namespace UpdateDB
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
            System.Windows.Forms.Label 員工編號Label;
            System.Windows.Forms.Label 姓名Label;
            System.Windows.Forms.Label 性別Label;
            System.Windows.Forms.Label 薪資Label;
            this.dataSetEmployee = new UpdateDB.DataSetEmployee();
            this.員工BindingSource = new System.Windows.Forms.BindingSource(this.components);
            this.員工TableAdapter = new UpdateDB.DataSetEmployeeTableAdapters.員工TableAdapter();
            this.tableAdapterManager = new UpdateDB.DataSetEmployeeTableAdapters.TableAdapterManager();
            this.員工BindingNavigator = new System.Windows.Forms.BindingNavigator(this.components);
            this.bindingNavigatorMoveFirstItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorMovePreviousItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorSeparator = new System.Windows.Forms.ToolStripSeparator();
            this.bindingNavigatorPositionItem = new System.Windows.Forms.ToolStripTextBox();
            this.bindingNavigatorCountItem = new System.Windows.Forms.ToolStripLabel();
            this.bindingNavigatorSeparator1 = new System.Windows.Forms.ToolStripSeparator();
            this.bindingNavigatorMoveNextItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorMoveLastItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorSeparator2 = new System.Windows.Forms.ToolStripSeparator();
            this.bindingNavigatorAddNewItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorDeleteItem = new System.Windows.Forms.ToolStripButton();
            this.員工BindingNavigatorSaveItem = new System.Windows.Forms.ToolStripButton();
            this.員工編號TextBox = new System.Windows.Forms.TextBox();
            this.姓名TextBox = new System.Windows.Forms.TextBox();
            this.性別TextBox = new System.Windows.Forms.TextBox();
            this.薪資TextBox = new System.Windows.Forms.TextBox();
            員工編號Label = new System.Windows.Forms.Label();
            姓名Label = new System.Windows.Forms.Label();
            性別Label = new System.Windows.Forms.Label();
            薪資Label = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.dataSetEmployee)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.員工BindingSource)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.員工BindingNavigator)).BeginInit();
            this.員工BindingNavigator.SuspendLayout();
            this.SuspendLayout();
            // 
            // dataSetEmployee
            // 
            this.dataSetEmployee.DataSetName = "DataSetEmployee";
            this.dataSetEmployee.SchemaSerializationMode = System.Data.SchemaSerializationMode.IncludeSchema;
            // 
            // 員工BindingSource
            // 
            this.員工BindingSource.DataMember = "員工";
            this.員工BindingSource.DataSource = this.dataSetEmployee;
            // 
            // 員工TableAdapter
            // 
            this.員工TableAdapter.ClearBeforeFill = true;
            // 
            // tableAdapterManager
            // 
            this.tableAdapterManager.BackupDataSetBeforeUpdate = false;
            this.tableAdapterManager.UpdateOrder = UpdateDB.DataSetEmployeeTableAdapters.TableAdapterManager.UpdateOrderOption.InsertUpdateDelete;
            this.tableAdapterManager.員工TableAdapter = this.員工TableAdapter;
            // 
            // 員工BindingNavigator
            // 
            this.員工BindingNavigator.AddNewItem = this.bindingNavigatorAddNewItem;
            this.員工BindingNavigator.BindingSource = this.員工BindingSource;
            this.員工BindingNavigator.CountItem = this.bindingNavigatorCountItem;
            this.員工BindingNavigator.DeleteItem = this.bindingNavigatorDeleteItem;
            this.員工BindingNavigator.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
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
            this.bindingNavigatorDeleteItem,
            this.員工BindingNavigatorSaveItem});
            this.員工BindingNavigator.Location = new System.Drawing.Point(0, 0);
            this.員工BindingNavigator.MoveFirstItem = this.bindingNavigatorMoveFirstItem;
            this.員工BindingNavigator.MoveLastItem = this.bindingNavigatorMoveLastItem;
            this.員工BindingNavigator.MoveNextItem = this.bindingNavigatorMoveNextItem;
            this.員工BindingNavigator.MovePreviousItem = this.bindingNavigatorMovePreviousItem;
            this.員工BindingNavigator.Name = "員工BindingNavigator";
            this.員工BindingNavigator.PositionItem = this.bindingNavigatorPositionItem;
            this.員工BindingNavigator.Size = new System.Drawing.Size(342, 25);
            this.員工BindingNavigator.TabIndex = 0;
            this.員工BindingNavigator.Text = "bindingNavigator1";
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
            this.bindingNavigatorPositionItem.Size = new System.Drawing.Size(50, 23);
            this.bindingNavigatorPositionItem.Text = "0";
            this.bindingNavigatorPositionItem.ToolTipText = "目前的位置";
            // 
            // bindingNavigatorCountItem
            // 
            this.bindingNavigatorCountItem.Name = "bindingNavigatorCountItem";
            this.bindingNavigatorCountItem.Size = new System.Drawing.Size(27, 15);
            this.bindingNavigatorCountItem.Text = "/{0}";
            this.bindingNavigatorCountItem.ToolTipText = "項目總數";
            // 
            // bindingNavigatorSeparator1
            // 
            this.bindingNavigatorSeparator1.Name = "bindingNavigatorSeparator";
            this.bindingNavigatorSeparator1.Size = new System.Drawing.Size(6, 6);
            // 
            // bindingNavigatorMoveNextItem
            // 
            this.bindingNavigatorMoveNextItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.bindingNavigatorMoveNextItem.Image = ((System.Drawing.Image)(resources.GetObject("bindingNavigatorMoveNextItem.Image")));
            this.bindingNavigatorMoveNextItem.Name = "bindingNavigatorMoveNextItem";
            this.bindingNavigatorMoveNextItem.RightToLeftAutoMirrorImage = true;
            this.bindingNavigatorMoveNextItem.Size = new System.Drawing.Size(23, 20);
            this.bindingNavigatorMoveNextItem.Text = "移到下一個";
            // 
            // bindingNavigatorMoveLastItem
            // 
            this.bindingNavigatorMoveLastItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.bindingNavigatorMoveLastItem.Image = ((System.Drawing.Image)(resources.GetObject("bindingNavigatorMoveLastItem.Image")));
            this.bindingNavigatorMoveLastItem.Name = "bindingNavigatorMoveLastItem";
            this.bindingNavigatorMoveLastItem.RightToLeftAutoMirrorImage = true;
            this.bindingNavigatorMoveLastItem.Size = new System.Drawing.Size(23, 20);
            this.bindingNavigatorMoveLastItem.Text = "移到最後面";
            // 
            // bindingNavigatorSeparator2
            // 
            this.bindingNavigatorSeparator2.Name = "bindingNavigatorSeparator";
            this.bindingNavigatorSeparator2.Size = new System.Drawing.Size(6, 6);
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
            // bindingNavigatorDeleteItem
            // 
            this.bindingNavigatorDeleteItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.bindingNavigatorDeleteItem.Image = ((System.Drawing.Image)(resources.GetObject("bindingNavigatorDeleteItem.Image")));
            this.bindingNavigatorDeleteItem.Name = "bindingNavigatorDeleteItem";
            this.bindingNavigatorDeleteItem.RightToLeftAutoMirrorImage = true;
            this.bindingNavigatorDeleteItem.Size = new System.Drawing.Size(23, 20);
            this.bindingNavigatorDeleteItem.Text = "刪除";
            // 
            // 員工BindingNavigatorSaveItem
            // 
            this.員工BindingNavigatorSaveItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.員工BindingNavigatorSaveItem.Image = ((System.Drawing.Image)(resources.GetObject("員工BindingNavigatorSaveItem.Image")));
            this.員工BindingNavigatorSaveItem.Name = "員工BindingNavigatorSaveItem";
            this.員工BindingNavigatorSaveItem.Size = new System.Drawing.Size(23, 23);
            this.員工BindingNavigatorSaveItem.Text = "儲存資料";
            this.員工BindingNavigatorSaveItem.Click += new System.EventHandler(this.員工BindingNavigatorSaveItem_Click);
            // 
            // 員工編號Label
            // 
            員工編號Label.AutoSize = true;
            員工編號Label.Location = new System.Drawing.Point(54, 79);
            員工編號Label.Name = "員工編號Label";
            員工編號Label.Size = new System.Drawing.Size(71, 15);
            員工編號Label.TabIndex = 1;
            員工編號Label.Text = "員工編號:";
            // 
            // 員工編號TextBox
            // 
            this.員工編號TextBox.DataBindings.Add(new System.Windows.Forms.Binding("Text", this.員工BindingSource, "員工編號", true));
            this.員工編號TextBox.Location = new System.Drawing.Point(131, 76);
            this.員工編號TextBox.Name = "員工編號TextBox";
            this.員工編號TextBox.Size = new System.Drawing.Size(100, 25);
            this.員工編號TextBox.TabIndex = 2;
            // 
            // 姓名Label
            // 
            姓名Label.AutoSize = true;
            姓名Label.Location = new System.Drawing.Point(54, 110);
            姓名Label.Name = "姓名Label";
            姓名Label.Size = new System.Drawing.Size(41, 15);
            姓名Label.TabIndex = 3;
            姓名Label.Text = "姓名:";
            // 
            // 姓名TextBox
            // 
            this.姓名TextBox.DataBindings.Add(new System.Windows.Forms.Binding("Text", this.員工BindingSource, "姓名", true));
            this.姓名TextBox.Location = new System.Drawing.Point(131, 107);
            this.姓名TextBox.Name = "姓名TextBox";
            this.姓名TextBox.Size = new System.Drawing.Size(100, 25);
            this.姓名TextBox.TabIndex = 4;
            // 
            // 性別Label
            // 
            性別Label.AutoSize = true;
            性別Label.Location = new System.Drawing.Point(54, 141);
            性別Label.Name = "性別Label";
            性別Label.Size = new System.Drawing.Size(41, 15);
            性別Label.TabIndex = 5;
            性別Label.Text = "性別:";
            // 
            // 性別TextBox
            // 
            this.性別TextBox.DataBindings.Add(new System.Windows.Forms.Binding("Text", this.員工BindingSource, "性別", true));
            this.性別TextBox.Location = new System.Drawing.Point(131, 138);
            this.性別TextBox.Name = "性別TextBox";
            this.性別TextBox.Size = new System.Drawing.Size(100, 25);
            this.性別TextBox.TabIndex = 6;
            // 
            // 薪資Label
            // 
            薪資Label.AutoSize = true;
            薪資Label.Location = new System.Drawing.Point(54, 172);
            薪資Label.Name = "薪資Label";
            薪資Label.Size = new System.Drawing.Size(41, 15);
            薪資Label.TabIndex = 7;
            薪資Label.Text = "薪資:";
            // 
            // 薪資TextBox
            // 
            this.薪資TextBox.DataBindings.Add(new System.Windows.Forms.Binding("Text", this.員工BindingSource, "薪資", true));
            this.薪資TextBox.Location = new System.Drawing.Point(131, 169);
            this.薪資TextBox.Name = "薪資TextBox";
            this.薪資TextBox.Size = new System.Drawing.Size(100, 25);
            this.薪資TextBox.TabIndex = 8;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(342, 233);
            this.Controls.Add(員工編號Label);
            this.Controls.Add(this.員工編號TextBox);
            this.Controls.Add(姓名Label);
            this.Controls.Add(this.姓名TextBox);
            this.Controls.Add(性別Label);
            this.Controls.Add(this.性別TextBox);
            this.Controls.Add(薪資Label);
            this.Controls.Add(this.薪資TextBox);
            this.Controls.Add(this.員工BindingNavigator);
            this.Font = new System.Drawing.Font("新細明體", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.Name = "Form1";
            this.Text = "員工資料管理";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dataSetEmployee)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.員工BindingSource)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.員工BindingNavigator)).EndInit();
            this.員工BindingNavigator.ResumeLayout(false);
            this.員工BindingNavigator.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private DataSetEmployee dataSetEmployee;
        private System.Windows.Forms.BindingSource 員工BindingSource;
        private DataSetEmployeeTableAdapters.員工TableAdapter 員工TableAdapter;
        private DataSetEmployeeTableAdapters.TableAdapterManager tableAdapterManager;
        private System.Windows.Forms.BindingNavigator 員工BindingNavigator;
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
        private System.Windows.Forms.ToolStripButton 員工BindingNavigatorSaveItem;
        private System.Windows.Forms.TextBox 員工編號TextBox;
        private System.Windows.Forms.TextBox 姓名TextBox;
        private System.Windows.Forms.TextBox 性別TextBox;
        private System.Windows.Forms.TextBox 薪資TextBox;
    }
}

