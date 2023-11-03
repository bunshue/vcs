package com.lietu.rtf.interpreter;

import java.io.IOException;
import java.util.ArrayList;

import com.lietu.rtf.IRtfGroup;
import com.lietu.rtf.IRtfInterpreter;
import com.lietu.rtf.IRtfInterpreterListener;
import com.lietu.rtf.RtfVisualBreakKind;
import com.lietu.rtf.RtfVisualImageFormat;
import com.lietu.rtf.RtfVisualSpecialCharKind;

public abstract class RtfInterpreterBase implements IRtfInterpreter
{

	// ----------------------------------------------------------------------
	protected RtfInterpreterBase(
		 IRtfInterpreterListener... listeners
	) throws Exception
	{
		if ( listeners != null )
		{
			for ( IRtfInterpreterListener listener : listeners )
			{
				AddInterpreterListener( listener );
			}
		}
	} // RtfInterpreterBase

	// ----------------------------------------------------------------------
	public void AddInterpreterListener( IRtfInterpreterListener listener ) throws Exception
	{
		if ( listener == null )
		{
			throw new Exception( "listener" );
		}
		if ( this.listeners == null )
		{
			this.listeners = new ArrayList<IRtfInterpreterListener>();
		}
		if ( !this.listeners.contains( listener ) )
		{
			this.listeners.add( listener );
		}
	} // AddInterpreterListener

	// ----------------------------------------------------------------------
	public void RemoveInterpreterListener( IRtfInterpreterListener listener )
	{
		try {
			if ( listener == null )
			{
				throw new Exception( "listener" );
			}
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		if ( this.listeners != null )
		{
			if ( this.listeners.contains( listener ) )
			{
				this.listeners.remove( listener );
			}
			if ( this.listeners.isEmpty() )
			{
				this.listeners = null;
			}
		}
	} // RemoveInterpreterListener

	// ----------------------------------------------------------------------
	public void Interpret( IRtfGroup rtfDocument ) throws Exception
	{
		try {
			if ( rtfDocument == null )
			{
				throw new Exception( "rtfDocument" );
			}
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		DoInterpret( rtfDocument );
	} // Interpret

	// ----------------------------------------------------------------------
	protected abstract void DoInterpret( IRtfGroup rtfDocument ) throws Exception;

	// ----------------------------------------------------------------------
	protected void NotifyBeginDocument() throws IOException
	{
		if ( this.listeners != null )
		{
			for ( IRtfInterpreterListener listener : this.listeners )
			{
				listener.BeginDocument( this.context );
			}
		}
	} // NotifyBeginDocument

	protected void NotifyInsertText( String text ) throws Exception
	{
		if ( this.listeners != null )
		{
			for ( IRtfInterpreterListener listener : this.listeners )
			{
				listener.InsertText( this.context, text );
			}
		}
	} // NotifyInsertText

	// ----------------------------------------------------------------------
	protected void NotifyInsertSpecialChar( RtfVisualSpecialCharKind kind ) throws Exception
	{
		if ( this.listeners != null )
		{
			for ( IRtfInterpreterListener listener : this.listeners )
			{
				listener.InsertSpecialChar( this.context, kind );
			}
		}
	} // NotifyInsertSpecialChar

	// ----------------------------------------------------------------------
	protected void NotifyInsertBreak( RtfVisualBreakKind kind ) throws Exception
	{
		if ( this.listeners != null )
		{
			for ( IRtfInterpreterListener listener : this.listeners )
			{
				listener.InsertBreak( this.context, kind );
			}
		}
	} // NotifyInsertBreak

	// ----------------------------------------------------------------------
	protected void NotifyInsertImage( RtfVisualImageFormat format,
		int width, int height, int desiredWidth, int desiredHeight,
		int scaleWidthPercent, int scaleHeightPercent, String imageDataHex
	) throws Exception
	{
		if ( this.listeners != null )
		{
			for ( IRtfInterpreterListener listener : this.listeners )
			{
				listener.InsertImage(
					this.context,
					format,
					width,
					height,
					desiredWidth,
					desiredHeight,
					scaleWidthPercent,
					scaleHeightPercent,
					imageDataHex );
			}
		}
	} // NotifyInsertImage

	// ----------------------------------------------------------------------
	protected void NotifyEndDocument() throws Exception
	{
		if ( this.listeners != null )
		{
			for ( IRtfInterpreterListener listener : this.listeners )
			{
				listener.EndDocument( this.context );
			}
		}
	} // NotifyEndDocument

	// ----------------------------------------------------------------------
	protected RtfInterpreterContext getContext()
	{
		 return context;
	} // Context

	// ----------------------------------------------------------------------
	// members
	private  RtfInterpreterContext context = new RtfInterpreterContext();
	private ArrayList<IRtfInterpreterListener> listeners;

} // class RtfInterpreterBase

