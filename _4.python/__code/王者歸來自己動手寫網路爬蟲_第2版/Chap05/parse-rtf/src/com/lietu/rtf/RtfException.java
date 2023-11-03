package com.lietu.rtf;

public class RtfException extends Exception
{

	/**
	 * 
	 */
	private static final long serialVersionUID = 3207207603259198102L;

	// ----------------------------------------------------------------------
	/// <summary>Creates a new instance.</summary>
	public RtfException()
	{
	} // RtfException

	// ----------------------------------------------------------------------
	/// <summary>Creates a new instance with the given message.</summary>
	/// <param name="message">the message to display</param>
	public RtfException( String message )
		
	{
		super( message );
	} // RtfException

	// ----------------------------------------------------------------------
	/// <summary>Creates a new instance with the given message, based on the given cause.</summary>
	/// <param name="message">the message to display</param>
	/// <param name="cause">the original cause for this exception</param>
	public RtfException( String message, Exception cause )			
	{
		super( message, cause );
	} // RtfException

	// ----------------------------------------------------------------------
	/// <summary>Serialization support.</summary>
	/// <param name="info">the info to use for serialization</param>
	/// <param name="context">the context to use for serialization</param>


} // class RtfException

