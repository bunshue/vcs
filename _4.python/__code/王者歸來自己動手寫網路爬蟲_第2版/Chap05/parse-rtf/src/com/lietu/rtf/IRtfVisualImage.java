package com.lietu.rtf;

import java.awt.Image;

public interface IRtfVisualImage extends IRtfVisual
	{

		// ----------------------------------------------------------------------
		RtfVisualImageFormat getFormat ();

		// ----------------------------------------------------------------------
		RtfTextAlignment getAlignment ();

		// ----------------------------------------------------------------------
		int getWidth ();

		// ----------------------------------------------------------------------
		int getHeight ();

		// ----------------------------------------------------------------------
		int getDesiredWidth ();

		// ----------------------------------------------------------------------
		int getDesiredHeight ();

		// ----------------------------------------------------------------------
		int getScaleWidthPercent ();

		// ----------------------------------------------------------------------
		int getScaleHeightPercent ();

		// ----------------------------------------------------------------------
		String getImageDataHex ();

		// ----------------------------------------------------------------------
		byte[] getImageDataBinary () throws Exception;

		// ----------------------------------------------------------------------
		Image getImageForDrawing () throws Exception;

	} // interface IRtfVisualImage

