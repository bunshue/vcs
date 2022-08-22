using System;
using System.Drawing;
using System.Windows.Forms;
using System.Data;
using hisonic.WinForm.HisonicControl;
using System.Collections;

namespace hisonic.WinForm.HisonicControl.CourseGrid
{
	/// <summary>
	/// CourseTable ��ժҪ˵����
	/// ���õ�dataΪ�ṹ�ͱ���,ֵΪobject����.
	/// </summary>
	public class CourseTable
	{
		protected System.Windows.Forms.DataGrid _dataGrid;
		// �α����ݣ���������ݿ��޹أ�
		protected DataSet  courseDataSet;
		// ��ͼ
		private DataView courseView;
		// �α�����
		public int daysPerWeek = 5;
		public int numsPerDay = 10;
		public int numsPerMorning = 1;
		public int numsPerAm = 4;
		public int numsPerPm = 3;
		public int numsPerEvening = 2;
		// ����
		public string[]  columnNames;
		// ��Ԫ����
		public CellDataStruct[,] courseData;
		// ���
		private int rowHeaderWidth = 40;
		private int columnWidth = 60;
		private int rowHeight = 25;
		private DataGridColumnStyle[] columnStyle;
		private DataGridTableStyle tableStyle;
		private Hashtable stateBackColor;
		private Hashtable stateForeColor;
		private bool stateColorEnabled;

		// ���캯��
		#region 

		public CourseTable(System.Windows.Forms.DataGrid grid)
		{
			this.CreateCourseTable(grid);
		}

        /// <summary>
        /// �γ̱��캯�������Կ���ÿ�ܼ����ϿΣ�ÿ������ϣ����磬���磬���ϸ��Լ��ڿ�
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

		// �����α�
		private void CreateCourseTable(System.Windows.Forms.DataGrid grid)
		{
			this._dataGrid = grid;
			grid.ReadOnly = true;

			this.columnNames = new string[daysPerWeek + 2];
			this.courseData = new CellDataStruct[this.daysPerWeek,this.numsPerDay];
			this.columnStyle = new DataGridColumnStyle[this.daysPerWeek + 2];
			this.columnNames[0] = "timeSect";
			this.columnNames[1] = "couseSeq";
			// ������ɫ״̬�� ---- ��ϣ��
			this.GenerateStateColorTable( );
			// �ر�״̬---��ɫ����
			this.stateColorEnabled = false;
			// �����γ̱�
			this.InitCourseTable( );
			// ���ɽ����
			//this.CreateResultTable( );
		}		

		private void InitCourseTable( )
		{
			// ��ʼ���α������ʽ
			this._dataGrid.CaptionForeColor = Color.Black;
			this._dataGrid.CaptionBackColor = Color.Pink;
			this._dataGrid.AllowNavigation = false;
			
			// ����洢�γ̱����ݵ����ݼ�
			this.courseDataSet = new DataSet("Course");
			DataTable table = new DataTable("courseTable");
			DataColumnCollection columns = table.Columns;
			DataColumn column = null;

			column = columns.Add(columnNames[0], typeof(string));
			column = columns.Add(columnNames[1], typeof(string));

			// ���ÿγ̱����ʽ
			DataGridTableStyle dataGridTableStyle = new DataGridTableStyle();
			dataGridTableStyle.MappingName = table.TableName;
			dataGridTableStyle.AllowSorting = false;
			dataGridTableStyle.RowHeadersVisible = false;
			dataGridTableStyle.PreferredRowHeight = this.rowHeight;	
			dataGridTableStyle.GridLineColor = Color.YellowGreen;
			this._dataGrid.TableStyles.Add(dataGridTableStyle);
			GridColumnStylesCollection gcsc = dataGridTableStyle.GridColumnStyles;
			this.tableStyle = dataGridTableStyle;

			// ���ñ���ͷ��Ϣ����ʽ
			DataGridColumnStyle timeSectColumnStyle =  new TableRowHeaderColumn( );
			((TableRowHeaderColumn)timeSectColumnStyle).MappingName="timeSect";		
			((TableRowHeaderColumn)timeSectColumnStyle).Width = this.rowHeaderWidth;
			((TableRowHeaderColumn)timeSectColumnStyle).Alignment = HorizontalAlignment.Center;
			((TableRowHeaderColumn)timeSectColumnStyle).HeaderText = "ʱ��";
			((TableRowHeaderColumn)timeSectColumnStyle).NullText = "";
			((TableRowHeaderColumn)timeSectColumnStyle).BackColor = System.Drawing.SystemColors.Control;
			gcsc.Add(timeSectColumnStyle);
			columnStyle[0] = timeSectColumnStyle;

			DataGridColumnStyle couseSeqColumnStyle =  new TableRowHeaderColumn( );
			((TableRowHeaderColumn)couseSeqColumnStyle).MappingName="couseSeq";		
			((TableRowHeaderColumn)couseSeqColumnStyle).Width = this.rowHeaderWidth;
			((TableRowHeaderColumn)couseSeqColumnStyle).Alignment = HorizontalAlignment.Center;
			((TableRowHeaderColumn)couseSeqColumnStyle).HeaderText = "�ڴ�";
			((TableRowHeaderColumn)couseSeqColumnStyle).NullText = "";
			((TableRowHeaderColumn)couseSeqColumnStyle).BackColor = System.Drawing.SystemColors.Control;
			gcsc.Add(couseSeqColumnStyle);
			columnStyle[1] = couseSeqColumnStyle;

			// ����γ̱�������м�����ʽ
			for(int count=1;count<(daysPerWeek + 1);count++)
			{
				this.columnNames[count + 1] = Enum.GetName(typeof(WeekDays), count);
				column = columns.Add(columnNames[count + 1], typeof(string));
				DataGridColumnStyle temp = new CourseCommonColumn( );
				temp.NullText = "";
				temp.MappingName = columnNames[count + 1];		
				temp.Width = this.columnWidth;
				temp.Alignment = HorizontalAlignment.Center;
				((CourseCommonColumn)temp).BackColor = System.Drawing.SystemColors.Window;
				((CourseCommonColumn)temp).ForeColor = System.Drawing.SystemColors.WindowText;
				((CourseCommonColumn)temp).SelectedBackColor = Color.Peru;
				((CourseCommonColumn)temp).SelectedForeColor = Color.White;
				// ����״̬����
				((CourseCommonColumn)temp).GenerateState(this.numsPerDay);
				// ����ɫ״̬��ֵ
				((CourseCommonColumn)temp).StateBackColorTable = this.stateBackColor;
				((CourseCommonColumn)temp).StateForeColorTable = this.stateForeColor;
				// ��ʼ��״̬
				((CourseCommonColumn)temp).ClearState( );
				((CourseCommonColumn)temp).IsStateToColor = false;
				columnStyle[count + 1] = temp;
				// �����б���
				switch(count)
				{
					case 1:
						temp.HeaderText = "����һ";
						break;
					case 2:
						temp.HeaderText = "���ڶ�";
						break;
					case 3:
						temp.HeaderText = "������";
						break;
					case 4:
						temp.HeaderText = "������";
						break;
					case 5:
						temp.HeaderText = "������";
						break;
					case 6:
						temp.HeaderText = "������";
						break;
					case 7:
						temp.HeaderText = "������";
						break;
					default:
						break;
				}
				gcsc.Add(temp);
			}
			//
			//�������
			for(int y_coord = 0;y_coord < numsPerDay;y_coord ++)
			{
				DataRow row = table.NewRow( );
				for(int x_coord = 2;x_coord < daysPerWeek + 2;x_coord ++)
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
			this.courseView = new DataView( );
			this.courseView.Table = table;
			this._dataGrid.DataSource = this.courseView;

			this.InitSolidText( );
		}

		// ��ʼ���α�ı�ͷ��Ϣ
		private void InitSolidText( )
		{
			int nums = 0;
			int num = this.numsPerMorning;
			for(int c1=0;c1<num;++c1,++nums)
			{
				if(c1 == 0)
				{
					this.SetCellText(0,nums,"����");					
				}
				this.SetCellText(1,nums,(c1 + 1).ToString( ));
			}
			num = this.numsPerAm;
			for(int c1=0;c1<num;++c1,++nums)
			{
				if(c1 == 0)
				{
					this.SetCellText(0,nums,"����");					
				}
				this.SetCellText(1,nums,(c1 + 1).ToString( ));
			}
			num = this.numsPerPm;
			for(int c1=0;c1<num;++c1,++nums)
			{
				if(c1 == 0)
				{
					this.SetCellText(0,nums,"����");					
				}
				this.SetCellText(1,nums,(c1 + 1).ToString( ));
			}
			num = this.numsPerEvening;
			for(int c1=0;c1<num;++c1,++nums)
			{
				if(c1 == 0)
				{
					this.SetCellText(0,nums,"����");					
				}
				this.SetCellText(1,nums,(c1 + 1).ToString( ));
			}
		}
		#endregion

		// ���ñ�ͷ��Ԫ����ı�
		#region

		public void SetCellText(int x_coord, int y_coord, string text)
		{
			if(x_coord < 0 || x_coord > 1)
			{
				return;
			}
			if(y_coord < 0 || y_coord > (this.numsPerDay - 1))
			{
				return;
			}

			this.courseDataSet.Tables["courseTable"].Rows[y_coord][this.columnNames[x_coord]] = text;
		}
		#endregion

		// ���ÿα�γ�
		#region

		public void SetCellData(int x_coord, int y_coord, object data, string courseName)
		{
			if(x_coord < 2 || x_coord > (this.daysPerWeek + 1) )
			{
				return;
			}
			if(y_coord < 0 || y_coord > (this.numsPerDay - 1))
			{
				return;
			}

			this.courseData[x_coord - 2, y_coord]._Data = data;
			this.courseData[x_coord - 2, y_coord]._State = -1;
			this.courseData[x_coord - 2, y_coord]._Text= courseName;
			this.courseDataSet.Tables["courseTable"].Rows[y_coord][this.columnNames[x_coord]] = 
				courseName;
			((CourseCommonColumn)columnStyle[x_coord]).SetGridState(y_coord, -1);
		}
		
		public void SetCellData(int day, int daySect, int lessonNum, object data, string lessonName)
		{
			int[] temp = this.GetCoordFromTime(day, daySect, lessonNum);
			if(temp[0] < 0 || temp[1] <0)
			{
				return;
			}
			this.SetCellData(temp[0], temp[1], data, lessonName);
		}

		// ��״̬�������������
		public void SetCellData(int x_coord, int y_coord, object data, string courseName, int state)
		{
			if(x_coord < 2 || x_coord > (this.daysPerWeek + 1) )
			{
				return;
			}
			if(y_coord < 0 || y_coord > (this.numsPerDay - 1))
			{
				return;
			}

			this.courseData[x_coord - 2, y_coord]._Data = data;
			this.courseData[x_coord - 2, y_coord]._State = state;
			this.courseData[x_coord - 2, y_coord]._Text= courseName;
			this.courseDataSet.Tables["courseTable"].Rows[y_coord][this.columnNames[x_coord]] = 
				courseName;
			((CourseCommonColumn)columnStyle[x_coord]).SetGridState(y_coord, state);
		}

		public void SetCellData(int day, int daySect, int lessonNum, object data,
									string lessonName, int state)
		{
			int[] temp = this.GetCoordFromTime(day, daySect, lessonNum);
			if(temp[0] < 0 || temp[1] <0)
			{
				return;
			}
			this.SetCellData(temp[0], temp[1], data, lessonName, state);
		}

		#endregion

		// ��ÿα�����
		#region

		public object GetCellData(int day, int daySect, int lessonNum)
		{
			
			int[] temp = this.GetCoordFromTime(day, daySect, lessonNum);
			if(temp[0] < 0 || temp[1] <0)
			{
				return null;
			}

			return this.courseData[temp[0] - 2, temp[1]]._Data;
		}

		public object GetCellData(int x_coord, int y_coord)
		{
			if(x_coord < 2 || x_coord > (this.daysPerWeek + 1) )
			{
				return null;
			}
			if(y_coord < 0 || y_coord > (this.numsPerDay - 1))
			{
				return null;
			}
			return this.courseData[x_coord - 2, y_coord]._Data ;
		}

		public CellDataStruct GetCellStruct(int x_coord, int y_coord)
		{
			if(x_coord < 2 || x_coord > (this.daysPerWeek + 1) )
			{
				throw new Exception("��ȡ�ÿα�Ԫ�ṹʱ�ṩ���кŲ���ȷ");
			}
			if(y_coord < 0 || y_coord > (this.numsPerDay - 1))
			{
				throw new Exception("��ȡ�ÿα�Ԫ�ṹʱ�ṩ���кŲ���ȷ");
			}
			return this.courseData[x_coord - 2, y_coord];
		}

		public CellDataStruct GetCellStruct(int day, int daySect, int lessonNum)
		{
			int[] temp = this.GetCoordFromTime(day, daySect, lessonNum);
			if(temp[0] < 0 || temp[1] <0)
			{
				throw new Exception("��ȡ�ÿα�Ԫ�ṹʱ�ṩ��ʱ�����ݲ���ȷ");
			}

			return this.courseData[temp[0] - 2, temp[1]];
		}

		#endregion

		// ��տγ̱�����
		#region

		public void ClearCourseData( )
		{
			DataTable table = this.courseDataSet.Tables["courseTable"];
			for(int y_coord = 0;y_coord < numsPerDay;y_coord ++)
			{
				DataRow row = table.Rows[y_coord];
				for(int x_coord = 2;x_coord < daysPerWeek + 2;x_coord ++)
				{
					row[x_coord] = string.Empty;
					this.courseData[x_coord - 2,y_coord]._Data = null;
					this.courseData[x_coord - 2,y_coord]._State = -1;
					this.courseData[x_coord - 2,y_coord]._Text = string.Empty;
				}
			}
			for(int i=2;i<=this.columnStyle.GetUpperBound(0);i++)
			{
				((CourseCommonColumn)columnStyle[i]).ClearState( );
			}
		}

		#endregion

		// ɾ���α�γ�
		#region

		public void DelCellData(int x_coord, int y_coord)
		{
			if(x_coord < 2 || x_coord > (this.daysPerWeek + 1) )
			{
				return;
			}
			if(y_coord < 0 || y_coord > (this.numsPerDay - 1))
			{
				return;
			}

			this.courseData[x_coord - 2, y_coord]._Data = null;
			this.courseData[x_coord - 2, y_coord]._State = -1;
			this.courseData[x_coord - 2, y_coord]._Text = string.Empty;
			this.courseDataSet.Tables["courseTable"].Rows[y_coord][this.columnNames[x_coord]] = string.Empty;
			((CourseCommonColumn)columnStyle[x_coord]).SetGridState(y_coord, -1);
		}

		// ɾ���γ�
		public void DelCellData(int day, int daySect, int lessonNum)
		{
			int[] temp = this.GetCoordFromTime(day, daySect, lessonNum);
			if(temp[0] < 0 || temp[1] <0)
			{
				return;
			}
			this.DelCellData(temp[0], temp[1]);
		}

		#endregion

		// ������ʽ
		#region

		public void SetRowHeaderWidth(int width)
		{
			if(this.columnStyle.Length == 0)
			{
				return;
			}
			((TableRowHeaderColumn)columnStyle[0]).Width = width;
			((TableRowHeaderColumn)columnStyle[1]).Width = width;
		}

		public void SetColumnWidth(int width)
		{
			if(this.columnStyle.Length == 0)
			{
				return;
			}
			for(int i=2;i<=this.columnStyle.GetUpperBound(0);i++)
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
			if(this.columnStyle.Length == 0)
			{
				return;
			}
			for(int i=2;i<=this.columnStyle.GetUpperBound(0);i++)
			{
				((CourseCommonColumn)columnStyle[i]).ForeColor = color;
			}
		}

		public void SetBackColor(Color color)
		{
			if(this.columnStyle.Length == 0)
			{
				return;
			}
			for(int i=2;i<=this.columnStyle.GetUpperBound(0);i++)
			{
				((CourseCommonColumn)columnStyle[i]).BackColor = color;
			}
		}

		public void SetSelectedBackColor(Color color)
		{
			if(this.columnStyle.Length == 0)
			{
				return;
			}
			for(int i=2;i<=this.columnStyle.GetUpperBound(0);i++)
			{
				((CourseCommonColumn)columnStyle[i]).SelectedBackColor = color;
			}
		}

		public void SetSelectedForeColor(Color color)
		{
			if(this.columnStyle.Length == 0)
			{
				return;
			}
			for(int i=2;i<=this.columnStyle.GetUpperBound(0);i++)
			{
				((CourseCommonColumn)columnStyle[i]).SelectedForeColor = color;
			}
		}

		public void SetRowHeaderBackColor(Color color)
		{
			if(this.columnStyle.Length == 0)
			{
				return;
			}
			((TableRowHeaderColumn)columnStyle[0]).BackColor = color;
			((TableRowHeaderColumn)columnStyle[1]).BackColor = color;
		}

		public void SetRowHeaderForeColor(Color color)
		{
			if(this.columnStyle.Length == 0)
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

		// ���ñ�����ʽ
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

		// ѡ��Ԫ��
		#region

		public void SelectCell(int rowNum, int colNum)
		{
			if(rowNum < 0 || colNum < 0)
			{
				return;
			}
			if(colNum > (this.daysPerWeek + 1) || rowNum > (this.numsPerDay - 1))
			{
				return;
			}
			this._dataGrid.CurrentCell = new DataGridCell(rowNum, colNum);
		}

		#endregion

		// ʱ�� -- ���� ת��������
		#region
		// ��ʱ��ת��������
		public int[]  GetCoordFromTime(int day, int daySect, int lessonNum)
		{
			int[] ret = new int[2];
			ret[0] = ret[1] = -1;

			if((day<1 || day>7) || (daySect<0 || daySect>3))
			{
				return ret;
			}
			int x_coord = day + 1;
			int y_coord = -1;
			switch(daySect)
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
			if(x_coord < 2 || x_coord > (this.daysPerWeek + 1) )
			{
				return ret;
			}
			if(y_coord < 0 || y_coord > (this.numsPerDay - 1))
			{
				return ret;
			}
			ret[0] = x_coord;
			ret[1] = y_coord;

			return ret;
		}

		// ������ת����ʱ��
		public int[] GetTimeFromCoord(int x_coord, int y_coord)
		{
			int[] ret = new int[3];
			ret [0] = ret[1] = ret[2] = -1;

			if((x_coord < 2) || (x_coord > this.daysPerWeek + 1) ||
				(y_coord < 0) || (y_coord > this.numsPerDay - 1))
			{
				return ret;
			}
			int day = x_coord - 1;
			y_coord ++;
			// �����Ͽ�ʼ����
			int day_sect = 0;
			int lesson_num = 0;
			int temp = y_coord - this.numsPerMorning;
			// ����
			if(temp <= 0)
			{
				lesson_num = y_coord;
				ret[0] = day;
				ret[1] = day_sect;
				ret[2] = lesson_num;
				return ret;
			}
			day_sect ++;
			temp -= this.numsPerAm;
			// ����
			if(temp <= 0)
			{
				lesson_num = y_coord - this.numsPerMorning;
				ret[0] = day;
				ret[1] = day_sect;
				ret[2] = lesson_num;
				return ret;
			}
			day_sect ++;
			temp -= this.numsPerPm;
			// ����
			if(temp <= 0)
			{
				lesson_num = y_coord - this.numsPerMorning - this.numsPerAm;
				ret[0] = day;
				ret[1] = day_sect;
				ret[2] = lesson_num;
				return ret;
			}
			day_sect ++;
			temp -= this.numsPerPm;
			// ����
			if(temp <= 0)
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

		// ״̬��ɫ����
		#region
		// ����״̬��ɫ��
		private void GenerateStateColorTable( )
		{
			this.stateBackColor = new Hashtable( );
			this.stateForeColor = new Hashtable( );
		}

		// ����״̬��ɫ
		public void SetStateColor(int state, Color backColor, Color foreColor)
		{
			if(state<0)
			{
				return;
			}
			if(this.stateForeColor[state] != null)
			{
				this.stateForeColor.Remove(state);
			}
			if(this.stateBackColor[state] != null)
			{
				this.stateBackColor.Remove(state);
			}
			this.stateForeColor.Add(state, foreColor);
			this.stateBackColor.Add(state, backColor);
		}

		// �Ƴ�״̬��ɫ
		public void RemoveStateColor(int state)
		{
			if(state<0)
			{
				return;
			}
			if(this.stateForeColor[state] != null)
			{
				this.stateForeColor.Remove(state);
			}
			if(this.stateBackColor[state] != null)
			{
				this.stateBackColor.Remove(state);
			}
		}

		// ���״̬��ɫ��
		public void ClearStateColorTable( )
		{
			this.stateBackColor.Clear( );
			this.stateForeColor.Clear( );
		}

		// �����״̬
		public void ClearState(int colNum)
		{
			if(colNum<1 || colNum>(this.daysPerWeek+1))
			{
				return;
			}
			for(int y_coord = 0;y_coord < numsPerDay;y_coord ++)
			{
				this.courseData[colNum,y_coord]._State = -1;
			}
			((CourseCommonColumn)columnStyle[colNum]).ClearState( );
		}

		// �������״̬
		public void ClearAllState( )
		{
			for(int y_coord = 0;y_coord < numsPerDay;y_coord ++)
			{
				for(int x_coord = 2;x_coord < daysPerWeek + 2;x_coord ++)
				{
					this.courseData[x_coord - 2,y_coord]._State = -1;
				}
			}
			for(int i=2;i<=this.columnStyle.GetUpperBound(0);i++)
			{
				((CourseCommonColumn)columnStyle[i]).ClearState( );
			}
		}

		// ���õ�Ԫ��״̬
		public void SetGridCellState(int x_coord, int y_coord, int state)
		{
			if(x_coord < 2 || x_coord > (this.daysPerWeek + 1) )
			{
				return;
			}
			if(y_coord < 0 || y_coord > (this.numsPerDay - 1))
			{
				return;
			}

			this.courseData[x_coord - 2,y_coord]._State = state;
			((CourseCommonColumn)columnStyle[x_coord]).SetGridState(y_coord, state);
		}

		public void SetGridCellState(int day, int day_sect, int lessonNum, int state)
		{
			int[] temp = this.GetCoordFromTime(day, day_sect, lessonNum);
			if(temp[0] < 0 || temp[1] <0)
			{
				return;
			}
			this.SetGridCellState(temp[0], temp[1], state);
		}

		public void EnableStateColor(bool enData)
		{
			for(int i=2;i<=this.columnStyle.GetUpperBound(0);i++)
			{
				((CourseCommonColumn)columnStyle[i]).IsStateToColor = enData;
			}
			this.stateColorEnabled = enData;
		}

		// ����״̬ˢ����ʾ
		public void RefreshDisplayByState(int state)
		{
			int st;
			for(int i=2;i<=this.columnStyle.GetUpperBound(0);i++)
			{
				for(int j=0;j<this.numsPerDay;j++)
				{
					st = ((CourseCommonColumn)columnStyle[i]).GetGridState(j);
					if(st == state)
					{
						Rectangle rect = this._dataGrid.GetCellBounds(j, i);
						this._dataGrid.Invalidate(rect,false);
					}
				}
			}
			this._dataGrid.Update( );
		}

		#endregion

	}
}
