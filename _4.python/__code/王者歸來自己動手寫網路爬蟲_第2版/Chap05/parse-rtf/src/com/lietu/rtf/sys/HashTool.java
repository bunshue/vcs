package com.lietu.rtf.sys;

// ------------------------------------------------------------------------
/// <summary>
/// Some hash utility methods for collections.
/// </summary>

public final class HashTool
{

	// ----------------------------------------------------------------------
	public static int AddHashCode( int hash, Object obj )
	{
		int combinedHash = obj != null ? obj.hashCode(): 0;
		if ( hash != 0 ) // perform this check to prevent FxCop warning 'op could overflow'
		{
			combinedHash += hash * 31;
		}
		return combinedHash;
	} // AddHashCode

	// ----------------------------------------------------------------------
	public static int AddHashCode( int hash, int objHash )
	{
		int combinedHash = objHash;
		if ( hash != 0 ) // perform this check to prevent FxCop warning 'op could overflow'
		{
			combinedHash += hash * 31;
		}
		return combinedHash;
	} // AddHashCode

} // class HashTool
