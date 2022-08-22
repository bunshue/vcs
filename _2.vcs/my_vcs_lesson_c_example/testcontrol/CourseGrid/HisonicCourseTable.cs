using System;
using System.Drawing;
using System.Windows.Forms;
using System.Data;
using hisonic.WinForm.HisonicControl;
using System.Collections;

namespace hisonic.WinForm.HisonicControl.CourseGrid
{
	/// <summary>
	/// 1��HisonicCourseTable���ڿα�ĵ�Ԫ����ֻ���DataRow[]
	///		�������ݵĿγ̱��ࡣ
	/// 2����DataRow[]�������������:
	///		dayColumn, daySectColumn, lessonNumColumn,
	///		�е�������ʹ��֮ǰ���뱻���á�
	/// 3���ÿγ̱���Ժ����ݿ�α���ϵ��һ��,������ݼ�����
	///		resultData��
	///	4���ÿγ̱��ѡ�пγ̿�����ͻ������ɫ��ʾ��
	/// </summary>
	public class HisonicCourseTable : CourseTable
	{
		// ��ϵ��ʵ�����ݿ�����ݼ�.��Ҫ��縳ֵ���滻��
		private DataSet resultData;	
		private string resultTableName;
		private string dayColumnName;
		private string daySectColumnName;
		private string lessonNumColumnName;
		private string weekStateColumnName;

		// ͻ����ʾѡ�пγ̵���ɫ
		private Color currCourseForeColor;
		private Color currCourseBackColor;
		private int currState;

		/// <summary>
		/// ���캯��
		/// </summary>
		#region

		public HisonicCourseTable(System.Windows.Forms.DataGrid grid) : 
			base(grid)
		{
			InitVars( );
			CreateResultTable( );
		}

		public HisonicCourseTable(System.Windows.Forms.DataGrid grid, int dayPerWeek,
			int numPerMorning, int numPerAm, int numPerPm,
			int numPerEvening) : 
			base(grid, dayPerWeek, numPerMorning, numPerAm, numPerPm, numPerEvening)
		{
			InitVars( );
			CreateResultTable( );
		}

		public HisonicCourseTable(System.Windows.Forms.DataGrid grid, int dayPerWeek,
			int numPerMorning, int numPerAm, int numPerPm,
			int numPerEvening, int rowHeadWidth, int rowHeigh, int colWidth) :
			base(grid, dayPerWeek, numPerMorning, numPerAm, numPerPm,
					numPerEvening, rowHeadWidth, rowHeigh, colWidth)
		{
			InitVars( );
			CreateResultTable( );
		}

		public HisonicCourseTable(System.Windows.Forms.DataGrid grid,
			int rowHeadWidth, int rowHeigh, int colWidth) :
			base(grid, rowHeadWidth, rowHeigh, colWidth)
		{
			InitVars( );
			CreateResultTable( );
		}

		private void InitVars( )
		{
			this.currCourseBackColor = Color.FromArgb(190, 200, 220);
			this.currCourseForeColor = SystemColors.WindowText;
			this.currState = -1;
		}

		// �������ݼ�
		private void CreateResultTable( )
		{
			this.resultData = new DataSet( );
			DataTable table = new DataTable("resultDataTable");
			this.resultTableName = "resultDataTable";
			DataColumnCollection columns = table.Columns;
			DataColumn column = columns.Add("currs_id", typeof(int));
			column.AllowDBNull = false;
			column.AutoIncrement = true;
			table.PrimaryKey = new DataColumn[]{ columns["currs_id"] };

			column = columns.Add("curr_id", typeof(int));
			column.AllowDBNull = false;
			column = columns.Add("user_id", typeof(int));
			column.AllowDBNull = false;
			column = columns.Add("user_dep_id", typeof(int));
			column.AllowDBNull = false;

			column = columns.Add("currs_week",typeof(int));
			column.AllowDBNull = false;
			this.dayColumnName = "currs_week";
			column = columns.Add("currs_day_sect",typeof(int));
			column.AllowDBNull = false;
			this.daySectColumnName = "currs_day_sect";
			column = columns.Add("currs_num",typeof(int));
			column.AllowDBNull = false;
			this.lessonNumColumnName = "currs_num";
			column = columns.Add("week_state",typeof(int));
			column.AllowDBNull = false;
			this.weekStateColumnName = "week_state";
			column = columns.Add("group_tag",typeof(int));
			column.AllowDBNull = false;

			this.resultData.Tables.Add(table);
		}

		#endregion

		// �α����ݴ���
		#region

		/// <summary>
		/// ���ÿα����ݼ�
		/// </summary>
		/// <param name="data">���ݼ�</param>
		public void SetResultData(DataSet data, string tableName)
		{			
			this.resultData = data;
			this.resultTableName = tableName;
		}

		/// <summary>
		/// ���ý�����ݱ��ʱ���ֶ�����
		/// </summary>
		/// <param name="colDayName">���ڼ��ֶ���</param>
		/// <param name="colSectName">ʱ���ֶ���</param>
		/// <param name="colNumName">�ڴ��ֶ���</param>
		public void SetResultTableColumn(string colDayName, string colSectName,
			string colNumName, string colWeekName)
		{
			this.dayColumnName = colDayName;
			this.daySectColumnName = colSectName;
			this.lessonNumColumnName = colNumName;
			this.weekStateColumnName = colWeekName;
		}

		/// <summary>
		///  �α����ݼ���
		/// </summary>
		public DataSet ResultData
		{
			get
			{
				return this.resultData;
			}
		}

		#endregion

		// ֧���м������ݴ���
		#region

		/// <summary>
		/// ���ĳ��λ���ܲ����ſ�(�Ƿ�Ϊ��)��
		/// </summary>
		/// <param name="x_coord">�к�</param>
		/// <param name="y_coord">�к�</param>
		/// <returns></returns>
		public bool PositionIsEmpty(int x_coord, int y_coord)
		{
			if(this.GetCellData(x_coord, y_coord) == null)
			{
				return true;
			}
			else
			{
				return false;
			}
		}

		/// <summary>
		///  ���ĳ��λ���ܲ����ſ�(�Ƿ�Ϊ��)��
		/// </summary>
		/// <param name="day">���ڼ�</param>
		/// <param name="day_sect">ʱ��</param>
		/// <param name="lessonNum">�ڴ�</param>
		/// <returns></returns>
		public bool PositionIsEmpty(int day, int day_sect, int lessonNum)
		{
			if(this.GetCellData(day, day_sect, lessonNum) == null)
			{
				return true;
			}
			else
			{
				return false;
			}
		}

		/// <summary>
		/// ɾ�����ӵ������С�
		/// </summary>
		/// <param name="x_coord">��</param>
		/// <param name="y_coord">��</param>
		public void DelCellRows(int x_coord, int y_coord)
		{
			CellDataStruct os = this.GetCellStruct(x_coord, y_coord);
			if(os._Data != null)
			{
				DataRow[] orow = (DataRow[])os._Data;
				foreach(DataRow row in orow)
				{
					row.Delete( );
				}
				if(orow.Length == 0)
				{
					os._Data = null;
				}
			}
			this.DelCellData(x_coord, y_coord);
		}

		public void DelCellRows(int day, int day_sect, int lessonNum)
		{
			int[] coord = this.GetCoordFromTime(day, day_sect, lessonNum);
			this.DelCellRows(coord[0], coord[1]);
		}

		/// <summary>
		/// �������������
		/// </summary>
		public void ClearAllRows( )
		{
			foreach(CellDataStruct cds in this.courseData)
			{
				if(cds._Data != null)
				{
					DataRow[] rows = (DataRow[])cds._Data;
					foreach(DataRow row in rows)
					{
						row.Delete( );
					}					
					this.DelCellData(cds._ColNum, cds._RowNum);
				}				
			}
		}

		/// <summary>
		/// ����ʽ�����õ�Ԫ���м�����
		/// </summary>
		/// <param name="x_coord">��</param>
		/// <param name="y_coord">��</param>
		/// <param name="row">������</param>
		/// <param name="textFieldName">�ı��ֶ���</param>
		/// <param name="stateFieldName">״̬�ֶ���</param>
		public void SetCellRows(int x_coord, int y_coord, DataRow row, 
			string textFieldName, string stateFieldName)
		{
			if(x_coord < 2 || x_coord > (this.daysPerWeek + 1) )
			{
				return;
			}
			if(y_coord < 0 || y_coord > (this.numsPerDay - 1))
			{
				return;
			}
			int[] time = this.GetTimeFromCoord(x_coord, y_coord);
			DataRow[] rows = new DataRow[]{ row };
			row[this.dayColumnName] = time[0];
			row[this.daySectColumnName] = time[1];
			row[this.lessonNumColumnName] = time[2];
			object oldData = this.GetCellData(x_coord, y_coord);
			if(oldData != null)
			{
				DataRow[] orows = (DataRow[])oldData;
				foreach(DataRow or in orows)
				{
					or.Delete( );
				}
			}
			int weekState = (int)row[this.weekStateColumnName];
			string text = (string)row[textFieldName];
			if(weekState > 0)
			{
				text += weekState;
			}
			this.SetCellData(x_coord, y_coord, rows, text, (int)row[stateFieldName]);
		}

		/// <summary>
		/// ����ʽ�����õ�Ԫ���м�����.
		/// </summary>
		/// <param name="day">���ڼ�</param>
		/// <param name="day_sect">ʱ��</param>
		/// <param name="lessonNum">�ڴ�</param>
		/// <param name="row">������</param>
		/// <param name="textFieldName">�ı��ֶ�����</param>
		/// <param name="stateFieldName">״̬�ֶ�����</param>
		public void SetCellRows(int day, int day_sect, int lessonNum, DataRow row, 
			string textFieldName, string stateFieldName)
		{
			int[] coord = this.GetCoordFromTime(day, day_sect, lessonNum);
			this.SetCellRows(coord[0], coord[1], row, textFieldName, stateFieldName);
		}

		/// <summary>
		/// ���ʽ�����õ�Ԫ��������м������ݡ�
		/// </summary>
		/// <param name="x_coord">��</param>
		/// <param name="y_coord">��</param>
		/// <param name="row">������</param>
		/// <param name="textFieldName">�ı��ֶ�����</param>
		/// <param name="stateFieldName">״̬�ֶ�����</param>
		/// <param name="replaceText">���Ե����Ƿ��滻�ı�</param>
		public void AddCellRows(int x_coord, int y_coord, DataRow row, 
			string textFieldName, string stateFieldName, bool replaceText)
		{
			if(x_coord < 2 || x_coord > (this.daysPerWeek + 1) )
			{
				return;
			}
			if(y_coord < 0 || y_coord > (this.numsPerDay - 1))
			{
				return;
			}
			int[] time = this.GetTimeFromCoord(x_coord, y_coord);
			DataRow[] rows = new DataRow[]{ row };
			row[this.dayColumnName] = time[0];
			row[this.daySectColumnName] = time[1];
			row[this.lessonNumColumnName] = time[2];
			object oldData = this.GetCellData(x_coord, y_coord);
			DataRow[] nrows;
			string text = string.Empty;
			if(oldData != null)
			{
				DataRow[] orows = (DataRow[])oldData;
				nrows = new DataRow[orows.Length + 1];
				for(int i=0;i<orows.Length;i++)
				{
					nrows[i] = orows[i];
					if(replaceText == false)
					{
						text += (string)orows[i][textFieldName];
					}
				}
				nrows[orows.Length] = row;
				if(replaceText == false)
				{
					text += (string)row[textFieldName];
				}
				else
				{
					text = (string)row[textFieldName];
				}
			}
			else
			{
				nrows = new DataRow[]{ row };
				text = (string)row[textFieldName];
			}
			int weekState = (int)row[this.weekStateColumnName];
			if(weekState > 0)
			{
				text += weekState;
			}
			this.SetCellData(x_coord, y_coord, nrows, 
				text, (int)row[stateFieldName]); 
			text = string.Empty;
		}

		/// <summary>
		/// ���ʽ�����õ�Ԫ��������м������ݡ�
		/// </summary>
		/// <param name="day">���ڼ�</param>
		/// <param name="day_sect">ʱ��</param>
		/// <param name="lessonNum">�ڴ�</param>
		/// <param name="row">������</param>
		/// <param name="textFieldName">�ı��ֶ�</param>
		/// <param name="stateFieldName">״̬�ֶ�</param>
		/// <param name="replaceText">���Ե����Ƿ��滻�ı�</param>
		public void AddCellRows(int day, int day_sect, int lessonNum, DataRow row, 
			string textFieldName, string stateFieldName, bool replaceText)
		{
			int[] coord = this.GetCoordFromTime(day, day_sect, lessonNum);
			this.AddCellRows(coord[0], coord[1], row, textFieldName, stateFieldName, replaceText);
		}

		/// <summary>
		/// ����������Ԫ��.���ݱ�����DataRow[]����.
		/// </summary>
		/// <param name="old_x">ԭʼ��</param>
		/// <param name="old_y">ԭʼ��</param>
		/// <param name="new_x">����</param>
		/// <param name="new_y">����</param>
		public void ExChangeDataPosition(int old_x, int old_y, int new_x, int new_y)
		{
			if(old_x == new_x && old_y == new_y)
			{
				return;
			}
			if(old_x < 2 || old_x > (this.daysPerWeek + 1) )
			{
				return;
			}
			if(old_y < 0 || old_y > (this.numsPerDay - 1))
			{
				return;
			}
			if(new_x < 2 || new_x > (this.daysPerWeek + 1) )
			{
				return;
			}
			if(new_y < 0 || new_y > (this.numsPerDay - 1))
			{
				return;
			}
			CellDataStruct os = this.GetCellStruct(old_x, old_y);
			CellDataStruct ns = this.GetCellStruct(new_x, new_y);
			int[] oTime = this.GetTimeFromCoord(old_x, old_y);
			int[] nTime = this.GetTimeFromCoord(new_x, new_y);

			// �޸�ʱ��
			if(os._Data != null)
			{
				DataRow[] orow = (DataRow[])os._Data;
				foreach(DataRow row in orow)
				{
					row[this.dayColumnName] = nTime[0];
					row[this.daySectColumnName] = nTime[1];
					row[this.lessonNumColumnName] = nTime[2];					
				}				
			}
			// ���°���λ��
			this.DelCellData(old_x, old_y);			
			this.SetCellData(old_x, old_y, ns._Data, ns._Text);
			this.SetGridCellState(old_x, old_y, ns._State);

			// �޸�ʱ��
			if(ns._Data != null)
			{
				DataRow[] nrow = (DataRow[])ns._Data;			
				foreach(DataRow row in nrow)
				{
					row[this.dayColumnName] = oTime[0];
					row[this.daySectColumnName] = oTime[1];
					row[this.lessonNumColumnName] = oTime[2];
				}				
			}
			// �޸�ʱ��
			this.DelCellData(new_x, new_y);			
			this.SetCellData(new_x, new_y, os._Data, os._Text);
			this.SetGridCellState(new_x, new_y, os._State);
		}

		#endregion

		// ��ɫ������ѡ�еĿγ���ɫ����ͻ����ʾ��
		#region

		public void SelectCellByCourse(int state)
		{
			if(state < 0)
			{
				return;
			}
			this.ClearStateColorTable( );
			this.SetStateColor(state, this.currCourseBackColor, this.currCourseForeColor);
			this.RefreshDisplayByState(state);
			if(this.currState>0)
			{
				this.RefreshDisplayByState(this.currState);
			}
			this.currState = state;
		}

		public void RefreshCurrStateDisplay( )
		{
			if(this.currState < 0)
			{
				return;
			}
			this.RefreshDisplayByState(this.currState);
		}

		#endregion

		// ������ʾ--- ��ʾresultTable�пγ̵�����
		#region

		public void DisplayData(string textFieldName, string stateFieldName, bool replaceText)
		{
			this.ClearCourseData( );
			DataTable table = this.resultData.Tables[this.resultTableName];
			int day, day_sect, lessonNum;
			string text = string.Empty;
			foreach(DataRow row in table.Rows)
			{
				day = (int)row[this.dayColumnName];
				day_sect = (int)row[this.daySectColumnName];
				lessonNum = (int)row[this.lessonNumColumnName];
				object data = this.GetCellData(day, day_sect, lessonNum);
				DataRow[] rows;
				if(data == null)
				{
					rows = new DataRow[]{ row };
					text += row[textFieldName];
				}
				else
				{
					DataRow[] orows = (DataRow[])data;
					rows = new DataRow[orows.Length + 1];
					for(int i=0;i<orows.Length;i++)
					{
						rows[i] = orows[i];
						if(replaceText == false)
						{
							text += (string)orows[i][textFieldName];
						}
					}
					rows[orows.Length] = row;
					if(replaceText == false)
					{
						text += (string)row[textFieldName];
					}
					else
					{
						text = (string)row[textFieldName];
					}
				}
				int weekState = (int)row[this.weekStateColumnName];
				if(weekState > 0)
				{
					text += weekState;
				}
				this.SetCellData(day, day_sect, lessonNum, rows, 
					text, (int)row[stateFieldName]); 
				text = string.Empty;
			}
		}
		#endregion
	}
}
