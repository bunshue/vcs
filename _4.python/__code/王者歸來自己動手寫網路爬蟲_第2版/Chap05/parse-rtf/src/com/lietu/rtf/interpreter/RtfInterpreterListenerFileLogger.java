package com.lietu.rtf.interpreter;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

import com.lietu.rtf.IRtfInterpreterContext;
import com.lietu.rtf.RtfVisualBreakKind;
import com.lietu.rtf.RtfVisualImageFormat;
import com.lietu.rtf.RtfVisualSpecialCharKind;


	public class RtfInterpreterListenerFileLogger extends RtfInterpreterListenerBase //implements IDisposable
	{

		// ----------------------------------------------------------------------
		public final String DefaultLogFileExtension = ".interpreter.log";

		// ----------------------------------------------------------------------
		public RtfInterpreterListenerFileLogger( String fileName ) throws Exception
			
		{
			this( fileName, new RtfInterpreterLoggerSettings() );
		} // RtfInterpreterListenerFileLogger

		// ----------------------------------------------------------------------
		public RtfInterpreterListenerFileLogger( String fileName, RtfInterpreterLoggerSettings settings ) throws Exception
		{
			if ( fileName == null )
			{
				throw new Exception( "fileName" );
			}
			if ( settings == null )
			{
				throw new Exception( "settings" );
			}

			this.fileName = fileName;
			this.settings = settings;
		} // RtfInterpreterListenerFileLogger

		// ----------------------------------------------------------------------
		public String getFileName()
		{
			 return this.fileName; 
		} // FileName

		// ----------------------------------------------------------------------
		public RtfInterpreterLoggerSettings getSettings()
		{
			return this.settings; 
		} // Settings

		// ----------------------------------------------------------------------
		public  void Dispose() throws IOException
		{
			CloseStream();
		} // Dispose

		// ----------------------------------------------------------------------
		protected  void DoBeginDocument( IRtfInterpreterContext context ) throws IOException
		{
			EnsureDirectory();
			OpenStream();

			if ( this.settings.getEnabled() &&  this.settings.getBeginDocumentText ()!=null && ""!=this.settings.getBeginDocumentText ())
			{
				WriteLine( this.settings.getBeginDocumentText() );
			}
		} // DoBeginDocument

		// ----------------------------------------------------------------------
		protected  void DoInsertText( IRtfInterpreterContext context, String text ) throws IOException
		{
			if ( this.settings.getEnabled() &&  this.settings.getTextFormatText()!=null && ""!=this.settings.getTextFormatText()  )
			{
				String msg = text;
				if ( msg.length()> this.settings.getTextMaxLength() && this.settings.getTextOverflowText()!=null && ""!= this.settings.getTextOverflowText() )
				{
					msg = msg.substring( 0, msg.length() - this.settings.getTextOverflowText().length() ) + this.settings.getTextOverflowText();
				}
				WriteLine( String.format(
					//CultureInfo.InvariantCulture,
					this.settings.getTextFormatText(),
					msg,
					context.getCurrentTextFormat() ) );
			}
		} // DoInsertText

		// ----------------------------------------------------------------------
		protected  void DoInsertSpecialChar( IRtfInterpreterContext context, RtfVisualSpecialCharKind kind ) throws IOException
		{
			if ( this.settings.getEnabled() && this.settings.getBreakFormatText()!=null && ""!=this.settings.getBreakFormatText() )
			{
				WriteLine( String.format(
					//CultureInfo.InvariantCulture,
					this.settings.getSpecialCharFormatText(),
					kind ) );
			}
		} // DoInsertSpecialChar

		// ----------------------------------------------------------------------
		protected  void DoInsertBreak( IRtfInterpreterContext context, RtfVisualBreakKind kind ) throws IOException
		{
			if ( this.settings.getEnabled() && this.settings.getBreakFormatText()!=null && ""!=this.settings.getBreakFormatText()  )
			{
				WriteLine( String.format(
					//CultureInfo.InvariantCulture,
					this.settings.getBreakFormatText(),
					kind ) );
			}
		} // DoInsertBreak

		// ----------------------------------------------------------------------
		protected  void DoInsertImage( IRtfInterpreterContext context,
			RtfVisualImageFormat format,
			int width, int height, int desiredWidth, int desiredHeight,
			int scaleWidthPercent, int scaleHeightPercent,
			String imageDataHex
		) throws IOException
		{
			if ( this.settings.getEnabled() &&  this.settings.getImageFormatText()!=null && ""!=this.settings.getImageFormatText())
			{
				WriteLine( String.format(
					//CultureInfo.InvariantCulture,
					this.settings.getImageFormatText(),
					format,
					width,
					height,
					desiredWidth,
					desiredHeight,
					scaleWidthPercent,
					scaleHeightPercent,
					imageDataHex,
					(imageDataHex.length()/ 2) ) );
			}
		} // DoInsertImage

		// ----------------------------------------------------------------------
		protected  void DoEndDocument( IRtfInterpreterContext context ) throws IOException
		{
			if ( this.settings.getEnabled() &&  this.settings.getImageFormatText()!=null && ""!=this.settings.getImageFormatText() )
			{
				WriteLine( this.settings.getEndDocumentText() );
			}

			CloseStream();
		} // DoEndDocument

		// ----------------------------------------------------------------------
		private void WriteLine( String message ) throws IOException
		{
			if ( this.streamWriter == null )
			{
				return;
			}

			this.streamWriter.write( message );
			this.streamWriter.flush();
		} // WriteLine

		// ----------------------------------------------------------------------
		private void EnsureDirectory()
		{
			File fi = new File( this.fileName );
			if ( ! new File( fi.getAbsolutePath() ).exists() )
			{
				fi.mkdir();
				//Directory.CreateDirectory( fi.DirectoryName );
			}
		} // EnsureDirectory

		// ----------------------------------------------------------------------
		private void OpenStream() throws IOException
		{
			if ( this.streamWriter != null )
			{
				return;
			}
			this.streamWriter = new BufferedWriter( new FileWriter(this.fileName)); 
		} // OpenStream

		// ----------------------------------------------------------------------
		private void CloseStream() throws IOException
		{
			if ( this.streamWriter == null )
			{
				return;
			}
			this.streamWriter.close();
			//this.streamWriter.Dispose();
			this.streamWriter = null;
		} // OpenStream

		// ----------------------------------------------------------------------
		// members
		private  String fileName;
		private  RtfInterpreterLoggerSettings settings;
		private  BufferedWriter streamWriter;

	} // class RtfInterpreterListenerFileLogger

