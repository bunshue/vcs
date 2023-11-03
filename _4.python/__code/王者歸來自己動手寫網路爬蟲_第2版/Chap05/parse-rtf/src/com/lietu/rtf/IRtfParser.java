package com.lietu.rtf;

public interface IRtfParser
	{

		// ----------------------------------------------------------------------
		/// <summary>
		/// Determines whether to ignore all content after the root group ends.
		/// Set this to true when parsing content from streams which contain other
		/// data after the RTF or if the writer of the RTF is known to terminate the
		/// actual RTF content with a null byte (as some popular sources such as
		/// WordPad are known to behave).
		/// </summary>
		boolean getIgnoreContentAfterRootGroup ();

		void setIgnoreContentAfterRootGroup (boolean icar);
		// ----------------------------------------------------------------------
		/// <summary>
		/// Adds a listener that will get notified along the parsing process.
		/// </summary>
		/// <param name="listener">the listener to add</param>
		/// <exception cref="ArgumentNullException">in case of a null argument</exception>
		void AddParserListener( IRtfParserListener listener ) throws Exception;

		// ----------------------------------------------------------------------
		/// <summary>
		/// Removes a listener from this instance.
		/// </summary>
		/// <param name="listener">the listener to remove</param>
		/// <exception cref="ArgumentNullException">in case of a null argument</exception>
		void RemoveParserListener( IRtfParserListener listener ) throws Exception;

		// ----------------------------------------------------------------------
		/// <summary>
		/// Parses the given RTF text that is read from the given source.
		/// </summary>
		/// <param name="rtfTextSource">the source with RTF text to parse</param>
		/// <exception cref="RtfException">in case of invalid RTF syntax</exception>
		/// <exception cref="IOException">in case of an IO error</exception>
		/// <exception cref="ArgumentNullException">in case of a null argument</exception>
		void Parse( IRtfSource rtfTextSource ) throws Exception;

	} // interface IRtfParser
