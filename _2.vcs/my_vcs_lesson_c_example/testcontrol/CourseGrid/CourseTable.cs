using System;
using System.Drawing;
using System.Windows.Forms;
using System.Data;
using hisonic.WinForm.HisonicControl;
using System.Collections;

namespace hisonic.WinForm.HisonicControl.CourseGrid
{
    /// <summary>
    /// CourseTable 的摘要說明。
    /// 內置的data為結構型變量,值為object類型.
    /// </summary>
    public class CourseTable
    {
        protected System.Windows.Forms.DataGrid _dataGrid;
        // 課表數據，與外界數據庫無關；
        protected DataSet courseDataSet;
        // 視圖
        private DataView courseView;
        // 課表數據
        public int daysPerWeek = 5;
        public int numsPerDay = 10;
        public int numsPerMorning = 1;
        public int numsPerAm = 4;
        public int numsPerPm = 3;
        public int numsPerEvening = 2;
        // 列名
        public string[] columnNames;
        // 單元數據
        public CellDataStruct[,] courseData;
        // 外觀
        private int rowHeaderWidth = 40;
        private int columnWidth = 60;
        private int rowHeight = 25;
        private DataGridColumnStyle[] columnStyle;
        private DataGridTableStyle tableStyle;
        private Hashtable stateBackColor;
        private Hashtable stateForeColor;
        private bool stateColorEnabled;

        // 構造函數
        #region

        public CourseTable(System.Windows.Forms.DataGrid grid)
        {
            this.CreateCourseTable(grid);
        }

        /// <summary>
        /// 課程表構造函數，可以控制每周幾天上課，每天分早上，上午，下午，晚上各自幾節課
        /// </summary>
        /// <param name="grid"></param>
        /// <param name="dayPerWeek"></param>
        /// <param name="numPerMorning"></param>
        /// <param name="numPerAm"></param>
        /// <param name="numPerPm"></param>
        /// <param name="numPerEvening"></param>
        public CourseTable(System.Windows.Forms.DataGrid grid, int dayPerWeek,
                            int numPerMorning, int numPerAm, int numPerPm,
                            int numPerEvening)
        {
            this.daysPerWeek = dayPerWeek;
            this.numsPerMorning = numPerMorning;
            this.numsPerAm = numPerAm;
            this.numsPerPm = numPerPm;
            this.numsPerEvening = numPerEvening;
            this.numsPerDay = numPerMorning + numPerAm + numPerPm + numPerEvening;

            this.CreateCourseTable(grid);
        }

        public CourseTable(System.Windows.Forms.DataGrid grid, int dayPerWeek,
            int numPerMorning, int numPerAm, int numPerPm,
            int numPerEvening, int rowHeadWidth, int rowHeigh, int colWidth)
        {
            this.daysPerWeek = dayPerWeek;
            this.numsPerMorning = numPerMorning;
            this.numsPerAm = numPerAm;
            this.numsPerPm = numPerPm;
            this.numsPerEvening = numPerEvening;
            this.numsPerDay = numPerMorning + numPerAm + numPerPm + numPerEvening;

            this.rowHeaderWidth = rowHeadWidth;
            this.rowHeight = rowHeigh;
            this.columnWidth = colWidth;

            this.CreateCourseTable(grid);
        }

        public CourseTable(System.Windows.Forms.DataGrid grid,
            int rowHeadWidth, int rowHeigh, int colWidth)
        {
            this.rowHeaderWidth = rowHeadWidth;
            this.rowHeight = rowHeigh;
            this.columnWidth = colWidth;

            this.CreateCourseTable(grid);
        }

        // 創建課表
        private void CreateCourseTable(System.Windows.Forms.DataGrid grid)
        {
            this._dataGrid = grid;
            grid.ReadOnly = true;

            this.columnNames = new string[daysPerWeek + 2];
            this.courseData = new CellDataStruct[this.daysPerWeek, this.numsPerDay];
            this.columnStyle = new DataGridColumnStyle[this.daysPerWeek + 2];
            this.columnNames[0] = "timeSect";
            this.columnNames[1] = "couseSeq";
            // 生成顏色狀態表 ---- 哈希表
            this.GenerateStateColorTable();
            // 關閉狀態---顏色功能
            this.stateColorEnabled = false;
            // 創建課程表
            this.InitCourseTable();
            // 生成結果表
            //this.CreateResultTable( );
        }

        private void InitCourseTable()
        {
            // 初始化課表標題樣式
            this._dataGrid.CaptionForeColor = Color.Black;
            this._dataGrid.CaptionBackColor = Color.Pink;
            this._dataGrid.AllowNavigation = false;

            // 構造存儲課程表數據的數據集
            this.courseDataSet = new DataSet("Course");
            DataTable table = new DataTable("courseTable");
            DataColumnCollection columns = table.Columns;
            DataColumn column = null;

            column = columns.Add(columnNames[0], typeof(string));
            column = columns.Add(columnNames[1], typeof(string));

            // 設置課程表的樣式
            DataGridTableStyle dataGridTableStyle = new DataGridTableStyle();
            dataGridTableStyle.MappingName = table.TableName;
            dataGridTableStyle.AllowSorting = false;
            dataGridTableStyle.RowHeadersVisible = false;
            dataGridTableStyle.PreferredRowHeight = this.rowHeight;
            dataGridTableStyle.GridLineColor = Color.YellowGreen;
            this._dataGrid.TableStyles.Add(dataGridTableStyle);
            GridColumnStylesCollection gcsc = dataGridTableStyle.GridColumnStyles;
            this.tableStyle = dataGridTableStyle;

            // 設置標行頭信息的樣式
            DataGridColumnStyle timeSectColumnStyle = new TableRowHeaderColumn();
            ((TableRowHeaderColumn)timeSectColumnStyle).MappingName = "timeSect";
            ((TableRowHeaderColumn)timeSectColumnStyle).Width = this.rowHeaderWidth;
            ((TableRowHeaderColumn)timeSectColumnStyle).Alignment = HorizontalAlignment.Center;
            ((TableRowHeaderColumn)timeSectColumnStyle).HeaderText = "時段";
            ((TableRowHeaderColumn)timeSectColumnStyle).NullText = "";
            ((TableRowHeaderColumn)timeSectColumnStyle).BackColor = System.Drawing.SystemColors.Control;
            gcsc.Add(timeSectColumnStyle);
            columnStyle[0] = timeSectColumnStyle;

            DataGridColumnStyle couseSeqColumnStyle = new TableRowHeaderColumn();
            ((TableRowHeaderColumn)couseSeqColumnStyle).MappingName = "couseSeq";
            ((TableRowHeaderColumn)couseSeqColumnStyle).Width = this.rowHeaderWidth;
            ((TableRowHeaderColumn)couseSeqColumnStyle).Alignment = HorizontalAlignment.Center;
            ((TableRowHeaderColumn)couseSeqColumnStyle).HeaderText = "節次";
            ((TableRowHeaderColumn)couseSeqColumnStyle).NullText = "";
            ((TableRowHeaderColumn)couseSeqColumnStyle).BackColor = System.Drawing.SystemColors.Control;
            gcsc.Add(couseSeqColumnStyle);
            columnStyle[1] = couseSeqColumnStyle;

            // 構造課程表的數據列及其樣式
            for (int count = 1; count < (daysPerWeek + 1); count++)
            {
                this.columnNames[count + 1] = Enum.GetName(typeof(WeekDays), count);
                column = columns.Add(columnNames[count + 1], typeof(string));
                DataGridColumnStyle temp = new CourseCommonColumn();
                temp.NullText = "";
                temp.MappingName = columnNames[count + 1];
                temp.Width = this.columnWidth;
                temp.Alignment = HorizontalAlignment.Center;
                ((CourseCommonColumn)temp).BackColor = System.Drawing.SystemColors.Window;
                ((CourseCommonColumn)temp).ForeColor = System.Drawing.SystemColors.WindowText;
                ((CourseCommonColumn)temp).SelectedBackColor = Color.Peru;
                ((CourseCommonColumn)temp).SelectedForeColor = Color.White;
                // 生成狀態數組
                ((CourseCommonColumn)temp).GenerateState(this.numsPerDay);
                // 給顏色狀態表賦值
                ((CourseCommonColumn)temp).StateBackColorTable = this.stateBackColor;
                ((CourseCommonColumn)temp).StateForeColorTable = this.stateForeColor;
                // 初始化狀態
                ((CourseCommonColumn)temp).ClearState();
                ((CourseCommonColumn)temp).IsStateToColor = false;
                columnStyle[count + 1] = temp;
                // 設置列標題
                switch (count)
                {
                    case 1:
                        temp.HeaderText = "星期一";
                        break;
                    case 2:
                        temp.HeaderText = "星期二";
                        break;
                    case 3:
                        temp.HeaderText = "星期三";
                        break;
                    case 4:
                        temp.HeaderText = "星期四";
                        break;
                    case 5:
                        temp.HeaderText = "星期五";
                        break;
                    case 6:
                        temp.HeaderText = "星期六";
                        break;
                    case 7:
                        temp.HeaderText = "星期日";
                        break;
                    default:
                        break;
                }
                gcsc.Add(temp);
            }
            //
            //添加數據
            for (int y_coord = 0; y_coord < numsPerDay; y_coord++)
            {
                DataRow row = table.NewRow();
                for (int x_coord = 2; x_coord < daysPerWeek + 2; x_coord++)
                {
                    row[x_coord] = string.Empty;
                    this.courseData[x_coord - 2, y_coord]._Data = null;
                    this.courseData[x_coord - 2, y_coord]._State = -1;
                    this.courseData[x_coord - 2, y_coord]._Text = string.Empty;
                    this.courseData[x_coord - 2, y_coord]._ColNum = x_coord;
                    this.courseData[x_coord - 2, y_coord]._RowNum = y_coord;
                }
                table.Rows.Add(row);
            }
            //
            this.courseDataSet.Tables.Add(table);
            this.courseView = new DataView();
            this.courseView.Table = table;
            this._dataGrid.DataSource = this.courseView;

            this.InitSolidText();
        }

        // 初始化課表的表頭信息
        private void InitSolidText()
        {
            int nums = 0;
            int num = this.numsPerMorning;
            for (int c1 = 0; c1 < num; ++c1, ++nums)
            {
                if (c1 == 0)
                {
                    this.SetCellText(0, nums, "早上");
                }
                this.SetCellText(1, nums, (c1 + 1).ToString());
            }
            num = this.numsPerAm;
            for (int c1 = 0; c1 < num; ++c1, ++nums)
            {
                if (c1 == 0)
                {
                    this.SetCellText(0, nums, "上午");
                }
                this.SetCellText(1, nums, (c1 + 1).ToString());
            }
            num = this.numsPerPm;
            for (int c1 = 0; c1 < num; ++c1, ++nums)
            {
                if (c1 == 0)
                {
                    this.SetCellText(0, nums, "下午");
                }
                this.SetCellText(1, nums, (c1 + 1).ToString());
            }
            num = this.numsPerEvening;
            for (int c1 = 0; c1 < num; ++c1, ++nums)
            {
                if (c1 == 0)
                {
                    this.SetCellText(0, nums, "晚上");
                }
                this.SetCellText(1, nums, (c1 + 1).ToString());
            }
        }
        #endregion

        // 設置表頭單元格的文本
        #region

        public void SetCellText(int x_coord, int y_coord, string text)
        {
            if (x_coord < 0 || x_coord > 1)
            {
                return;
            }
            if (y_coord < 0 || y_coord > (this.numsPerDay - 1))
            {
                return;
            }

            this.courseDataSet.Tables["courseTable"].Rows[y_coord][this.columnNames[x_coord]] = text;
        }
        #endregion

        // 設置課表課程
        #region

        public void SetCellData(int x_coord, int y_coord, object data, string courseName)
        {
            if (x_coord < 2 || x_coord > (this.daysPerWeek + 1))
            {
                return;
            }
            if (y_coord < 0 || y_coord > (this.numsPerDay - 1))
            {
                return;
            }

            this.courseData[x_coord - 2, y_coord]._Data = data;
            this.courseData[x_coord - 2, y_coord]._State = -1;
            this.courseData[x_coord - 2, y_coord]._Text = courseName;
            this.courseDataSet.Tables["courseTable"].Rows[y_coord][this.columnNames[x_coord]] =
                courseName;
            ((CourseCommonColumn)columnStyle[x_coord]).SetGridState(y_coord, -1);
        }

        public void SetCellData(int day, int daySect, int lessonNum, object data, string lessonName)
        {
            int[] temp = this.GetCoordFromTime(day, daySect, lessonNum);
            if (temp[0] < 0 || temp[1] < 0)
            {
                return;
            }
            this.SetCellData(temp[0], temp[1], data, lessonName);
        }

        // 帶狀態參數的數據添加
        public void SetCellData(int x_coord, int y_coord, object data, string courseName, int state)
        {
            if (x_coord < 2 || x_coord > (this.daysPerWeek + 1))
            {
                return;
            }
            if (y_coord < 0 || y_coord > (this.numsPerDay - 1))
            {
                return;
            }

            this.courseData[x_coord - 2, y_coord]._Data = data;
            this.courseData[x_coord - 2, y_coord]._State = state;
            this.courseData[x_coord - 2, y_coord]._Text = courseName;
            this.courseDataSet.Tables["courseTable"].Rows[y_coord][this.columnNames[x_coord]] =
                courseName;
            ((CourseCommonColumn)columnStyle[x_coord]).SetGridState(y_coord, state);
        }

        public void SetCellData(int day, int daySect, int lessonNum, object data,
                                    string lessonName, int state)
        {
            int[] temp = this.GetCoordFromTime(day, daySect, lessonNum);
            if (temp[0] < 0 || temp[1] < 0)
            {
                return;
            }
            this.SetCellData(temp[0], temp[1], data, lessonName, state);
        }

        #endregion

        // 獲得課表數據
        #region

        public object GetCellData(int day, int daySect, int lessonNum)
        {

            int[] temp = this.GetCoordFromTime(day, daySect, lessonNum);
            if (temp[0] < 0 || temp[1] < 0)
            {
                return null;
            }

            return this.courseData[temp[0] - 2, temp[1]]._Data;
        }

        public object GetCellData(int x_coord, int y_coord)
        {
            if (x_coord < 2 || x_coord > (this.daysPerWeek + 1))
            {
                return null;
            }
            if (y_coord < 0 || y_coord > (this.numsPerDay - 1))
            {
                return null;
            }
            return this.courseData[x_coord - 2, y_coord]._Data;
        }

        public CellDataStruct GetCellStruct(int x_coord, int y_coord)
        {
            if (x_coord < 2 || x_coord > (this.daysPerWeek + 1))
            {
                throw new Exception("在取得課表單元結構時提供的行號不正確");
            }
            if (y_coord < 0 || y_coord > (this.numsPerDay - 1))
            {
                throw new Exception("在取得課表單元結構時提供的列號不正確");
            }
            return this.courseData[x_coord - 2, y_coord];
        }

        public CellDataStruct GetCellStruct(int day, int daySect, int lessonNum)
        {
            int[] temp = this.GetCoordFromTime(day, daySect, lessonNum);
            if (temp[0] < 0 || temp[1] < 0)
            {
                throw new Exception("在取得課表單元結構時提供的時間數據不正確");
            }

            return this.courseData[temp[0] - 2, temp[1]];
        }

        #endregion

        // 清空課程表數據
        #region

        public void ClearCourseData()
        {
            DataTable table = this.courseDataSet.Tables["courseTable"];
            for (int y_coord = 0; y_coord < numsPerDay; y_coord++)
            {
                DataRow row = table.Rows[y_coord];
                for (int x_coord = 2; x_coord < daysPerWeek + 2; x_coord++)
                {
                    row[x_coord] = string.Empty;
                    this.courseData[x_coord - 2, y_coord]._Data = null;
                    this.courseData[x_coord - 2, y_coord]._State = -1;
                    this.courseData[x_coord - 2, y_coord]._Text = string.Empty;
                }
            }
            for (int i = 2; i <= this.columnStyle.GetUpperBound(0); i++)
            {
                ((CourseCommonColumn)columnStyle[i]).ClearState();
            }
        }

        #endregion

        // 刪除課表課程
        #region

        public void DelCellData(int x_coord, int y_coord)
        {
            if (x_coord < 2 || x_coord > (this.daysPerWeek + 1))
            {
                return;
            }
            if (y_coord < 0 || y_coord > (this.numsPerDay - 1))
            {
                return;
            }

            this.courseData[x_coord - 2, y_coord]._Data = null;
            this.courseData[x_coord - 2, y_coord]._State = -1;
            this.courseData[x_coord - 2, y_coord]._Text = string.Empty;
            this.courseDataSet.Tables["courseTable"].Rows[y_coord][this.columnNames[x_coord]] = string.Empty;
            ((CourseCommonColumn)columnStyle[x_coord]).SetGridState(y_coord, -1);
        }

        // 刪除課程
        public void DelCellData(int day, int daySect, int lessonNum)
        {
            int[] temp = this.GetCoordFromTime(day, daySect, lessonNum);
            if (temp[0] < 0 || temp[1] < 0)
            {
                return;
            }
            this.DelCellData(temp[0], temp[1]);
        }

        #endregion

        // 設置樣式
        #region

        public void SetRowHeaderWidth(int width)
        {
            if (this.columnStyle.Length == 0)
            {
                return;
            }
            ((TableRowHeaderColumn)columnStyle[0]).Width = width;
            ((TableRowHeaderColumn)columnStyle[1]).Width = width;
        }

        public void SetColumnWidth(int width)
        {
            if (this.columnStyle.Length == 0)
            {
                return;
            }
            for (int i = 2; i <= this.columnStyle.GetUpperBound(0); i++)
            {
                ((CourseCommonColumn)columnStyle[i]).Width = width;
            }
        }

        public bool CaptionVisible
        {
            set
            {
                this._dataGrid.CaptionVisible = value;
            }
            get
            {
                return this._dataGrid.CaptionVisible;
            }
        }

        public void SetForeColor(Color color)
        {
            if (this.columnStyle.Length == 0)
            {
                return;
            }
            for (int i = 2; i <= this.columnStyle.GetUpperBound(0); i++)
            {
                ((CourseCommonColumn)columnStyle[i]).ForeColor = color;
            }
        }

        public void SetBackColor(Color color)
        {
            if (this.columnStyle.Length == 0)
            {
                return;
            }
            for (int i = 2; i <= this.columnStyle.GetUpperBound(0); i++)
            {
                ((CourseCommonColumn)columnStyle[i]).BackColor = color;
            }
        }

        public void SetSelectedBackColor(Color color)
        {
            if (this.columnStyle.Length == 0)
            {
                return;
            }
            for (int i = 2; i <= this.columnStyle.GetUpperBound(0); i++)
            {
                ((CourseCommonColumn)columnStyle[i]).SelectedBackColor = color;
            }
        }

        public void SetSelectedForeColor(Color color)
        {
            if (this.columnStyle.Length == 0)
            {
                return;
            }
            for (int i = 2; i <= this.columnStyle.GetUpperBound(0); i++)
            {
                ((CourseCommonColumn)columnStyle[i]).SelectedForeColor = color;
            }
        }

        public void SetRowHeaderBackColor(Color color)
        {
            if (this.columnStyle.Length == 0)
            {
                return;
            }
            ((TableRowHeaderColumn)columnStyle[0]).BackColor = color;
            ((TableRowHeaderColumn)columnStyle[1]).BackColor = color;
        }

        public void SetRowHeaderForeColor(Color color)
        {
            if (this.columnStyle.Length == 0)
            {
                return;
            }
            ((TableRowHeaderColumn)columnStyle[0]).ForeColor = color;
            ((TableRowHeaderColumn)columnStyle[1]).ForeColor = color;
        }

        public void SetGridLineColor(Color color)
        {
            this.tableStyle.GridLineColor = color;
        }

        public void SetCaptionText(string text)
        {
            this._dataGrid.CaptionText = text;
        }

        #endregion

        // 設置標題樣式
        #region

        public Color CaptionBackColor
        {
            set
            {
                this._dataGrid.CaptionBackColor = value;
            }
            get
            {
                return this._dataGrid.CaptionBackColor;
            }
        }

        public Color CaptionForeColor
        {
            set
            {
                this._dataGrid.CaptionForeColor = value;
            }
            get
            {
                return this._dataGrid.CaptionForeColor;
            }
        }

        #endregion

        // 選擇單元格
        #region

        public void SelectCell(int rowNum, int colNum)
        {
            if (rowNum < 0 || colNum < 0)
            {
                return;
            }
            if (colNum > (this.daysPerWeek + 1) || rowNum > (this.numsPerDay - 1))
            {
                return;
            }
            this._dataGrid.CurrentCell = new DataGridCell(rowNum, colNum);
        }

        #endregion

        // 時間 -- 坐標 轉換函數。
        #region
        // 把時間轉換成坐標
        public int[] GetCoordFromTime(int day, int daySect, int lessonNum)
        {
            int[] ret = new int[2];
            ret[0] = ret[1] = -1;

            if ((day < 1 || day > 7) || (daySect < 0 || daySect > 3))
            {
                return ret;
            }
            int x_coord = day + 1;
            int y_coord = -1;
            switch (daySect)
            {
                case 0:
                    //y_coord = 0;
                    y_coord += lessonNum;
                    break;
                case 1:
                    //y_coord = 0;
                    y_coord += this.numsPerMorning;
                    y_coord += lessonNum;
                    break;
                case 2:
                    //y_coord = 0;
                    y_coord += this.numsPerMorning;
                    y_coord += this.numsPerAm;
                    y_coord += lessonNum;
                    break;
                case 3:
                    //y_coord = 0;
                    y_coord += this.numsPerMorning;
                    y_coord += this.numsPerAm;
                    y_coord += this.numsPerPm;
                    y_coord += lessonNum;
                    break;
                default:
                    break;
            }
            if (x_coord < 2 || x_coord > (this.daysPerWeek + 1))
            {
                return ret;
            }
            if (y_coord < 0 || y_coord > (this.numsPerDay - 1))
            {
                return ret;
            }
            ret[0] = x_coord;
            ret[1] = y_coord;

            return ret;
        }

        // 把坐標轉換成時間
        public int[] GetTimeFromCoord(int x_coord, int y_coord)
        {
            int[] ret = new int[3];
            ret[0] = ret[1] = ret[2] = -1;

            if ((x_coord < 2) || (x_coord > this.daysPerWeek + 1) ||
                (y_coord < 0) || (y_coord > this.numsPerDay - 1))
            {
                return ret;
            }
            int day = x_coord - 1;
            y_coord++;
            // 從早上開始假設
            int day_sect = 0;
            int lesson_num = 0;
            int temp = y_coord - this.numsPerMorning;
            // 早上
            if (temp <= 0)
            {
                lesson_num = y_coord;
                ret[0] = day;
                ret[1] = day_sect;
                ret[2] = lesson_num;
                return ret;
            }
            day_sect++;
            temp -= this.numsPerAm;
            // 上午
            if (temp <= 0)
            {
                lesson_num = y_coord - this.numsPerMorning;
                ret[0] = day;
                ret[1] = day_sect;
                ret[2] = lesson_num;
                return ret;
            }
            day_sect++;
            temp -= this.numsPerPm;
            // 下午
            if (temp <= 0)
            {
                lesson_num = y_coord - this.numsPerMorning - this.numsPerAm;
                ret[0] = day;
                ret[1] = day_sect;
                ret[2] = lesson_num;
                return ret;
            }
            day_sect++;
            temp -= this.numsPerPm;
            // 晚上
            if (temp <= 0)
            {
                lesson_num = y_coord - this.numsPerMorning - this.numsPerAm - this.numsPerPm;
                ret[0] = day;
                ret[1] = day_sect;
                ret[2] = lesson_num;
                return ret;
            }
            return ret;
        }
        #endregion

        // 狀態顏色控制
        #region
        // 生成狀態顏色表
        private void GenerateStateColorTable()
        {
            this.stateBackColor = new Hashtable();
            this.stateForeColor = new Hashtable();
        }

        // 設置狀態顏色
        public void SetStateColor(int state, Color backColor, Color foreColor)
        {
            if (state < 0)
            {
                return;
            }
            if (this.stateForeColor[state] != null)
            {
                this.stateForeColor.Remove(state);
            }
            if (this.stateBackColor[state] != null)
            {
                this.stateBackColor.Remove(state);
            }
            this.stateForeColor.Add(state, foreColor);
            this.stateBackColor.Add(state, backColor);
        }

        // 移除狀態顏色
        public void RemoveStateColor(int state)
        {
            if (state < 0)
            {
                return;
            }
            if (this.stateForeColor[state] != null)
            {
                this.stateForeColor.Remove(state);
            }
            if (this.stateBackColor[state] != null)
            {
                this.stateBackColor.Remove(state);
            }
        }

        // 清空狀態顏色表
        public void ClearStateColorTable()
        {
            this.stateBackColor.Clear();
            this.stateForeColor.Clear();
        }

        // 清除列狀態
        public void ClearState(int colNum)
        {
            if (colNum < 1 || colNum > (this.daysPerWeek + 1))
            {
                return;
            }
            for (int y_coord = 0; y_coord < numsPerDay; y_coord++)
            {
                this.courseData[colNum, y_coord]._State = -1;
            }
            ((CourseCommonColumn)columnStyle[colNum]).ClearState();
        }

        // 清除所有狀態
        public void ClearAllState()
        {
            for (int y_coord = 0; y_coord < numsPerDay; y_coord++)
            {
                for (int x_coord = 2; x_coord < daysPerWeek + 2; x_coord++)
                {
                    this.courseData[x_coord - 2, y_coord]._State = -1;
                }
            }
            for (int i = 2; i <= this.columnStyle.GetUpperBound(0); i++)
            {
                ((CourseCommonColumn)columnStyle[i]).ClearState();
            }
        }

        // 設置單元格狀態
        public void SetGridCellState(int x_coord, int y_coord, int state)
        {
            if (x_coord < 2 || x_coord > (this.daysPerWeek + 1))
            {
                return;
            }
            if (y_coord < 0 || y_coord > (this.numsPerDay - 1))
            {
                return;
            }

            this.courseData[x_coord - 2, y_coord]._State = state;
            ((CourseCommonColumn)columnStyle[x_coord]).SetGridState(y_coord, state);
        }

        public void SetGridCellState(int day, int day_sect, int lessonNum, int state)
        {
            int[] temp = this.GetCoordFromTime(day, day_sect, lessonNum);
            if (temp[0] < 0 || temp[1] < 0)
            {
                return;
            }
            this.SetGridCellState(temp[0], temp[1], state);
        }

        public void EnableStateColor(bool enData)
        {
            for (int i = 2; i <= this.columnStyle.GetUpperBound(0); i++)
            {
                ((CourseCommonColumn)columnStyle[i]).IsStateToColor = enData;
            }
            this.stateColorEnabled = enData;
        }

        // 根據狀態刷新顯示
        public void RefreshDisplayByState(int state)
        {
            int st;
            for (int i = 2; i <= this.columnStyle.GetUpperBound(0); i++)
            {
                for (int j = 0; j < this.numsPerDay; j++)
                {
                    st = ((CourseCommonColumn)columnStyle[i]).GetGridState(j);
                    if (st == state)
                    {
                        Rectangle rect = this._dataGrid.GetCellBounds(j, i);
                        this._dataGrid.Invalidate(rect, false);
                    }
                }
            }
            this._dataGrid.Update();
        }

        #endregion

    }
}
