using System;
using System.Data;

namespace hisonic.WinForm.HisonicControl.CourseGrid
{
    // 和課程表CourseTable類相關的單元格的結構
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
