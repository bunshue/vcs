package com.lietu.rtf.parser;

import java.io.IOException;
import java.util.ArrayList;

import com.lietu.rtf.IRtfParser;
import com.lietu.rtf.IRtfParserListener;
import com.lietu.rtf.IRtfSource;
import com.lietu.rtf.IRtfTag;
import com.lietu.rtf.IRtfText;
import com.lietu.rtf.RtfException;


	public abstract class RtfParserBase implements IRtfParser
	{

		// ----------------------------------------------------------------------
		protected RtfParserBase()
		{
		} // RtfParserBase

		// ----------------------------------------------------------------------
		protected RtfParserBase( IRtfParserListener[] listeners ) throws Exception
		{
			if ( listeners != null )
			{
				for ( IRtfParserListener listener : listeners )
				{
					AddParserListener( listener );
				}
			}
		} // RtfParserBase

		// ----------------------------------------------------------------------
		public boolean getIgnoreContentAfterRootGroup()
		{
			  return ignoreContentAfterRootGroup; 
		} // IgnoreContentAfterRootGroup
		

		public void setIgnoreContentAfterRootGroup(boolean value)
		{ ignoreContentAfterRootGroup = value; }

		// ----------------------------------------------------------------------
		public void AddParserListener( IRtfParserListener listener ) throws Exception
		{
			if ( listener == null )
			{
				throw new Exception( "listener" );
			}
			if ( this.listeners == null )
			{
				this.listeners = new ArrayList<IRtfParserListener>();
			}
			if ( !this.listeners.contains( listener ) )
			{
				this.listeners.add( listener );
			}
		} // AddParserListener

		// ----------------------------------------------------------------------
		public void RemoveParserListener( IRtfParserListener listener ) throws Exception
		{
			if ( listener == null )
			{
				throw new Exception( "listener" );
			}
			if ( this.listeners != null )
			{
				if ( this.listeners.contains( listener ) )
				{
					this.listeners.remove( listener );
				}
				if ( this.listeners.size() == 0 )
				{
					this.listeners = null;
				}
			}
		} // RemoveParserListener

		// ----------------------------------------------------------------------
		public void Parse( IRtfSource rtfTextSource ) throws Exception
		{
			if ( rtfTextSource == null )
			{
				throw new Exception( "rtfTextSource" );
			}
			DoParse( rtfTextSource );
		} // Parse

		// ----------------------------------------------------------------------
		protected abstract void DoParse( IRtfSource rtfTextSource ) throws Exception;

		// ----------------------------------------------------------------------
		protected void NotifyParseBegin() throws IOException
		{
			if ( this.listeners != null )
			{
				for ( IRtfParserListener listener : this.listeners )
				{
					listener.ParseBegin();
				}
			}
		} // NotifyParseBegin

		// ----------------------------------------------------------------------
		protected void NotifyGroupBegin()
		{
			if ( this.listeners != null )
			{
				for ( IRtfParserListener listener : this.listeners )
				{
					listener.GroupBegin();
				}
			}
		} // NotifyGroupBegin

		// ----------------------------------------------------------------------
		protected void NotifyTagFound( IRtfTag tag ) throws Exception
		{
			if ( this.listeners != null )
			{
				for ( IRtfParserListener listener : this.listeners )
				{
					listener.TagFound( tag );
				}
			}
		} // NotifyTagFound

		// ----------------------------------------------------------------------
		protected void NotifyTextFound( IRtfText text ) throws Exception
		{
			if ( this.listeners != null )
			{
				for( IRtfParserListener listener : this.listeners )
				{
					listener.TextFound( text );
				}
			}
		} // NotifyTextFound

		// ----------------------------------------------------------------------
		protected void NotifyGroupEnd() throws Exception
		{
			if ( this.listeners != null )
			{
				for ( IRtfParserListener listener : this.listeners )
				{
					listener.GroupEnd();
				}
			}
		} // NotifyGroupEnd

		// ----------------------------------------------------------------------
		protected void NotifyParseSuccess() throws IOException
		{
			if ( this.listeners != null )
			{
				for( IRtfParserListener listener : this.listeners )
				{
					listener.ParseSuccess();
				}
			}
		} // NotifyParseSuccess

		// ----------------------------------------------------------------------
		protected void NotifyParseFail( RtfException reason ) throws IOException
		{
			if ( this.listeners != null )
			{
				for( IRtfParserListener listener : this.listeners )
				{
					listener.ParseFail( reason );
				}
			}
		} // NotifyParseFail

		// ----------------------------------------------------------------------
		protected void NotifyParseEnd() throws Exception
		{
			if ( this.listeners != null )
			{
				for ( IRtfParserListener listener : this.listeners )
				{
					listener.ParseEnd();
				}
			}
		} // NotifyParseEnd

		// ----------------------------------------------------------------------
		// members
		private boolean ignoreContentAfterRootGroup;
		private ArrayList<IRtfParserListener> listeners;

	} // class RtfParserBase

