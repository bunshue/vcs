package com.lietu.rtf;

import java.io.IOException;

public interface IRtfParserListener
	{

		// ----------------------------------------------------------------------
		/// <summary>
		/// Called before any other of the methods upon starting parsing of new input.
		/// </summary>
		void ParseBegin() throws IOException;

		// ----------------------------------------------------------------------
		/// <summary>
		/// Called when a new group began.
		/// </summary>
		void GroupBegin();

		// ----------------------------------------------------------------------
		/// <summary>
		/// Called when a new tag was found.
		/// </summary>
		/// <param name="tag">the newly found tag</param>
		void TagFound( IRtfTag tag ) throws Exception;

		// ----------------------------------------------------------------------
		/// <summary>
		/// Called when a new text was found.
		/// </summary>
		/// <param name="text">the newly found text</param>
		void TextFound( IRtfText text ) throws Exception;

		// ----------------------------------------------------------------------
		/// <summary>
		/// Called after a group ended.
		/// </summary>
		void GroupEnd() throws Exception;

		// ----------------------------------------------------------------------
		/// <summary>
		/// Called if parsing finished sucessfully.
		/// </summary>
		void ParseSuccess() throws IOException;

		// ----------------------------------------------------------------------
		/// <summary>
		/// Called if parsing failed.
		/// </summary>
		/// <param name="reason">the reason for the failure</param>
		void ParseFail( RtfException reason ) throws IOException;

		// ----------------------------------------------------------------------
		/// <summary>
		/// Called after parsing finished. Always called, also in case of a failure.
		/// </summary>
		void ParseEnd() throws Exception;

	} // interface IRtfParserListener

