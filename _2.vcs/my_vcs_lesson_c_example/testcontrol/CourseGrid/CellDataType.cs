using System;
using System.Data;

namespace hisonic.WinForm.HisonicControl.CourseGrid
{
	// 和课程表CourseTable类相关的单元格的结构
	#region
	public struct CellDataStruct
	{
		public string _Text;
		public object _Data;
		public int    _State;
		public int    _ColNum;
		public int    _RowNum;
		public int    _usedCount;
	}
	#endregion
}
