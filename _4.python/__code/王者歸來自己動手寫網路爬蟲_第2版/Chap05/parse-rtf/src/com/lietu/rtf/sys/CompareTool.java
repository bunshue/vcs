package com.lietu.rtf.sys;
	public final class CompareTool
	{

		// ----------------------------------------------------------------------
		public static boolean AreEqual( Object left, Object right )
		{
			return left == right || ( left != null && left.equals( right ) );
		} // AreEqual

	} // class CompareTool

