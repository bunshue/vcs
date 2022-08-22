using System;
using System.Drawing;
using System.Windows.Forms;
using System.Data;
using System.Collections;

namespace hisonic.WinForm.HisonicControl.CourseGrid
{
	/// <summary>
	/// CourseCommonColumn ��ժҪ˵����
	/// ����ĳ�����ݵ�������ɫ��ʾ֧�֡�
	/// </summary>
	public class CourseCommonColumn : DataGridTextBoxColumn
	{
		private Color foreColor = SystemColors.WindowText;
		private Color backColor = SystemColors.Window;

		private Color selectedForeColor = SystemColors.HighlightText;
		private Color selectedBackColor = SystemColors.Highlight;

		// �Ƿ�����״̬��ɫ
		private bool isStateToColor = false;
		// ���и��ӵ�״̬����
		private int[] gridState = null;
		// ״̬��ɫ��
		// ��������״ֵ̬������ȡ����ɫ��
		private Hashtable stateBackColorTable = null;
		private Hashtable stateForeColorTable = null;
		// ���е�����
		private int _rowCount;

		public bool IsStateToColor
		{
			set
			{
				if(gridState == null || stateBackColorTable == null || stateForeColorTable == null)
				{
					this.isStateToColor = false;
				}
				else
				{
					this.isStateToColor = value;
				}
			}
		}

		public Hashtable StateBackColorTable
		{
			set
			{
				this.stateBackColorTable = value;
			}
		}

		public Hashtable StateForeColorTable
		{
			set
			{
				this.stateForeColorTable = value;
			}
		}

		public Color ForeColor
		{
			get
			{
				return foreColor;
			}
			set
			{
				foreColor = value;
			}
		}

		public Color BackColor
		{
			get
			{
				return backColor;
			}
			set
			{
				backColor = value;
			}
		}

		public Color SelectedForeColor
		{
			get
			{
				return selectedForeColor;
			}
			set
			{
				selectedForeColor = value;
			}
		}

		public Color SelectedBackColor
		{
			get
			{
				return selectedBackColor;
			}
			set
			{
				selectedBackColor = value;
			}
		}

		/*	protected override void Edit(
				CurrencyManager source,
				int rowNum,
				Rectangle bounds,
				bool readOnly
				)
			{
				EndEdit();
			}

			protected override void Edit(
				CurrencyManager source,
				int rowNum,
				Rectangle bounds,
				bool readOnly,
				string instantText
				)
			{
				EndEdit();
			}

			protected override void Edit(
				CurrencyManager source,
				int rowNum,
				Rectangle bounds,
				bool readOnly,
				string instantText,
				bool cellIsVisible
				)
			{
				EndEdit();
			}
		*/

		protected override void Paint( Graphics g,
			Rectangle bounds,
			CurrencyManager source,
			int rowNum
			)
		{
			if(this.TextBox != null)
			{
				this.TextBox.ForeColor = this.SelectedForeColor;
				this.TextBox.BackColor = this.selectedBackColor;
			}
			base.Paint(g, bounds, source, rowNum);
		}

		protected override void Paint(Graphics g,
			Rectangle bounds,
			CurrencyManager source,
			int rowNum,
			bool alignToRight
			)
		{
			if(this.TextBox != null)
			{
				this.TextBox.ForeColor = this.SelectedForeColor;
				this.TextBox.BackColor = this.selectedBackColor;
			}
			base.Paint(g, bounds, source, rowNum, alignToRight);
		}

		protected override void Paint(Graphics g,
			Rectangle bounds,
			CurrencyManager source,
			int rowNum,
			Brush backBrush,
			Brush foreBrush,
			bool alignToRight
			)
		{
			Brush myBackBrush = (Brush) backBrush.Clone();
			Brush myForeBrush = (Brush) foreBrush.Clone();

			DataGridTableStyle gridTableStyle = this.DataGridTableStyle.DataGrid.TableStyles[0];
			string temp = 
				gridTableStyle.GridColumnStyles[this.DataGridTableStyle.DataGrid.CurrentCell.ColumnNumber].MappingName;
			if (source.Position == rowNum && temp == this.MappingName)
			{
				if (myBackBrush is SolidBrush)
				{
					// use selected brush
					((SolidBrush)myBackBrush).Color = selectedBackColor;
				}

				if (myForeBrush is SolidBrush)
				{
					// use selected brush
					((SolidBrush)myForeBrush).Color = selectedForeColor;
				}
			}
			else
			{
				if(this.isStateToColor == true)
				{
					if (myBackBrush is SolidBrush)
					{
						if(this.stateBackColorTable[this.gridState[rowNum]] != null)
						{
							Color c = (Color) this.stateBackColorTable[this.gridState[rowNum]];
							((SolidBrush)myBackBrush).Color = c;
						}
					}

					if (myForeBrush is SolidBrush)
					{						
						if(this.stateForeColorTable[this.gridState[rowNum]] != null)
						{
							Color c = (Color) this.stateForeColorTable[this.gridState[rowNum]];
							((SolidBrush)myForeBrush).Color = c;
						}
					}
				}
				else
				{
					if (myBackBrush is SolidBrush)
					{
						((SolidBrush)myBackBrush).Color = backColor;
					}

					if (myForeBrush is SolidBrush)
					{
						// use selected brush
						((SolidBrush)myForeBrush).Color = foreColor;
					}
				}				
			}

			if(this.TextBox != null)
			{
				this.TextBox.ForeColor = this.SelectedForeColor;
				this.TextBox.BackColor = this.selectedBackColor;
			}
			base.Paint(g, bounds, source, rowNum, myBackBrush, myForeBrush,
				alignToRight);
		}

		/// <summary>
		/// ���ɱ��е�Ԫ��״̬����
		/// </summary>
		/// <param name="rowCount">�α������</param> 
		public void GenerateState(int rowCount)
		{
			this._rowCount = rowCount;
			this.gridState = new int[rowCount];
		}

		/// <summary>
		/// ���״̬
		/// ״̬ȡ����0��ֵ��0��ʾѡ�У�С��0��ʾ��Ч״̬		/// 
		/// </summary>
		public void ClearState( )
		{
			for(int i=0;i<_rowCount;++i)
			{
				this.gridState[i] = -1;
			}
		}

		/// <summary>
		/// ���õ�Ԫ��״ֵ̬
		/// </summary>
		/// <param name="rowNum">�к�</param>
		/// <param name="state">״ֵ̬</param>
		public void SetGridState(int rowNum, int state)
		{
			if(rowNum<0 || rowNum>(_rowCount-1))
			{
				return;
			}
			this.gridState[rowNum] = state;
		}

		/// <summary>
		/// ��ȡ��Ԫ��״ֵ̬
		/// </summary>
		/// <param name="rowNum">�к�</param>
		/// <returns></returns>
		public int GetGridState(int rowNum)
		{
			return this.gridState[rowNum];
		}
	}
}