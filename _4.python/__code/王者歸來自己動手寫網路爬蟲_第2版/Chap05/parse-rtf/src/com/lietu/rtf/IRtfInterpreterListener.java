package com.lietu.rtf;

import java.io.IOException;

public interface IRtfInterpreterListener
{

		// ----------------------------------------------------------------------
		void BeginDocument( IRtfInterpreterContext context ) throws IOException;

		// ----------------------------------------------------------------------
		public void InsertText( IRtfInterpreterContext context, String text ) throws Exception;

		// ----------------------------------------------------------------------
		void InsertSpecialChar( IRtfInterpreterContext context, RtfVisualSpecialCharKind kind ) throws Exception;

		// ----------------------------------------------------------------------
		void InsertBreak( IRtfInterpreterContext context, RtfVisualBreakKind kind ) throws Exception;

		// ----------------------------------------------------------------------
		void InsertImage( IRtfInterpreterContext context, RtfVisualImageFormat format,
			int width, int height, int desiredWidth, int desiredHeight,
			int scaleWidthPercent, int scaleHeightPercent, String imageDataHex
		)throws Exception;

		// ----------------------------------------------------------------------
		void EndDocument( IRtfInterpreterContext context )throws Exception;

	} // interface IRtfInterpreterListener
