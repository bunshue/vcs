using System;
using System.Drawing;
using System.Windows.Forms;
using System.Data;

namespace hisonic.WinForm.HisonicControl.CourseGrid
{
	/// <summary>
	/// TableRowHeaderColumn 的摘要说明。
	/// </summary>
	public class TableRowHeaderColumn  : DataGridTextBoxColumn
	{
		private Color foreColor = SystemColors.WindowText;
		private Color backColor = SystemColors.Window;

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

		protected override void Edit(
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

		protected override void Paint( Graphics g,
			Rectangle bounds,
			CurrencyManager source,
			int rowNum
			)
		{
			base.Paint(g, bounds, source, rowNum);
		}

		protected override void Paint(Graphics g,
			Rectangle bounds,
			CurrencyManager source,
			int rowNum,
			bool alignToRight
			)
		{
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

			if (myBackBrush is SolidBrush)
			{
				((SolidBrush)myBackBrush).Color = backColor;
			}

			if (myForeBrush is SolidBrush)
			{
				// use selected brush
				((SolidBrush)myForeBrush).Color = foreColor;
			}

			base.Paint(g, bounds, source, rowNum, myBackBrush, myForeBrush,
				alignToRight);
		}
	}
}
