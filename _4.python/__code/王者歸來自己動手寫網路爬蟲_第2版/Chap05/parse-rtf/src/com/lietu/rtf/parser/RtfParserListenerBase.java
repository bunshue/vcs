package com.lietu.rtf.parser;

import java.io.IOException;

import com.lietu.rtf.IRtfParserListener;
import com.lietu.rtf.IRtfTag;
import com.lietu.rtf.IRtfText;
import com.lietu.rtf.RtfException;


	public class RtfParserListenerBase implements IRtfParserListener
	{

		// ----------------------------------------------------------------------
		public RtfParserListenerBase()
		{
		} // RtfParserListenerBase

		// ----------------------------------------------------------------------
		public int getLevel()
		{
			return this.level; 
		} // Level

		// ----------------------------------------------------------------------
		public void ParseBegin() throws IOException
		{
			this.level = 0; // in case something interrupted the normal flow of things previously ...
			DoParseBegin();
		} // ParseBegin

		// ----------------------------------------------------------------------
		protected  void DoParseBegin() throws IOException
		{
		} // DoParseBegin

		// ----------------------------------------------------------------------
		public void GroupBegin()
		{
			DoGroupBegin();
			this.level++;
		} // GroupBegin

		// ----------------------------------------------------------------------
		protected  void DoGroupBegin()
		{
		} // DoGroupBegin

		// ----------------------------------------------------------------------
		public void TagFound( IRtfTag tag ) throws Exception
		{
			if ( tag != null )
			{
				DoTagFound( tag );
			}
		} // TagFound

		// ----------------------------------------------------------------------
		protected  void DoTagFound( IRtfTag tag ) throws Exception
		{
		} // DoTagFound

		// ----------------------------------------------------------------------
		public void TextFound( IRtfText text ) throws Exception
		{
			if ( text != null )
			{
				DoTextFound( text );
			}
		} // TextFound

		// ----------------------------------------------------------------------
		protected  void DoTextFound( IRtfText text ) throws Exception
		{
		} // DoTextFound

		// ----------------------------------------------------------------------
		public void GroupEnd() throws Exception
		{
			this.level--;
			DoGroupEnd();
		} // GroupEnd

		// ----------------------------------------------------------------------
		protected  void DoGroupEnd() throws Exception
		{
		} // DoGroupEnd

		// ----------------------------------------------------------------------
		public void ParseSuccess() throws IOException
		{
			DoParseSuccess();
		} // ParseSuccess

		// ----------------------------------------------------------------------
		protected  void DoParseSuccess() throws IOException
		{
		} // DoParseSuccess

		// ----------------------------------------------------------------------
		public void ParseFail( RtfException reason ) throws IOException
		{
			DoParseFail( reason );
		} // ParseFail

		// ----------------------------------------------------------------------
		protected  void DoParseFail( RtfException reason ) throws IOException
		{
		} // DoParseFail

		// ----------------------------------------------------------------------
		public void ParseEnd() throws Exception
		{
			DoParseEnd();
		} // ParseEnd

		// ----------------------------------------------------------------------
		protected  void DoParseEnd() throws Exception
		{
		} // DoParseEnd

		// ----------------------------------------------------------------------
		// members
		protected int level;

	} // class RtfParserListenerBase

