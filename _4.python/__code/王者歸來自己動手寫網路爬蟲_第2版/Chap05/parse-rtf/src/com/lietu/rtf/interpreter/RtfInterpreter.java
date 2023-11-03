package com.lietu.rtf.interpreter;

import com.lietu.rtf.IRtfColor;
import com.lietu.rtf.IRtfElement;
import com.lietu.rtf.IRtfElementVisitor;
import com.lietu.rtf.IRtfFont;
import com.lietu.rtf.IRtfGroup;
import com.lietu.rtf.IRtfInterpreterListener;
import com.lietu.rtf.IRtfTag;
import com.lietu.rtf.IRtfText;
import com.lietu.rtf.RtfElementKind;
import com.lietu.rtf.RtfInterpreterState;
import com.lietu.rtf.RtfSpec;
import com.lietu.rtf.RtfTextAlignment;
import com.lietu.rtf.RtfVisualBreakKind;
import com.lietu.rtf.RtfVisualSpecialCharKind;

public final class RtfInterpreter extends RtfInterpreterBase implements IRtfElementVisitor
{

	// ----------------------------------------------------------------------
	public RtfInterpreter(  IRtfInterpreterListener... listeners ) throws Exception
	{
		super( listeners );
		this.fontTableBuilder = new RtfFontTableBuilder( getContext().getWritableFontTable() );
		this.colorTableBuilder = new RtfColorTableBuilder( getContext().getWritableColorTable());
		this.documentInfoBuilder = new RtfDocumentInfoBuilder( getContext().getWritableDocumentInfo());
		this.userPropertyBuilder = new RtfUserPropertyBuilder( getContext().getWritableUserProperties());
		this.imageBuilder = new RtfImageBuilder();
	} // RtfInterpreter

	// ----------------------------------------------------------------------
	public boolean IsSupportedDocument( IRtfGroup rtfDocument )
	{
		try
		{
			GetSupportedDocument( rtfDocument );
		}
		catch ( Exception e)
		{
			return false;
		}
		return true;
	} // IsSupportedDocument

	// ----------------------------------------------------------------------
	public IRtfGroup GetSupportedDocument( IRtfGroup rtfDocument ) throws Exception
	{
		if ( rtfDocument == null )
		{
			throw new Exception( "document is null" );
		}
		if ( rtfDocument.getContents().size() == 0 )
		{
			throw new Exception( "document has not contents" );
		}
		IRtfElement firstElement = rtfDocument.getContents().get(0);
		//System.out.println(firstElement.getKind());
		if ( firstElement.getKind() != RtfElementKind.Tag )
		{
			throw new Exception( "first element in document is not a tag" );
		}
		IRtfTag firstTag = (IRtfTag)firstElement;
		if ( !RtfSpec.TagRtf.equals( firstTag.getName() ) )
		{
			throw new Exception( "first tag in document is not " + RtfSpec.TagRtf );
		}
		if ( !firstTag.getHasValue() )
		{
			throw new Exception( "unspecified RTF version" );
		}
		if ( firstTag.getValueAsNumber() != RtfSpec.RtfVersion1 )
		{
			throw new Exception( "unsupported RTF version: " + firstTag.getValueAsText() );
		}
		return rtfDocument;
	} // GetSupportedDocument

	// ----------------------------------------------------------------------
	protected  void DoInterpret( IRtfGroup rtfDocument ) throws Exception
	{
		//System.out.println("root size:"+rtfDocument.getContents().size());
		InterpretContents( GetSupportedDocument( rtfDocument ) );
	} // DoInterpret

	// ----------------------------------------------------------------------
	private void InterpretContents( IRtfGroup rtfDocument ) throws Exception
	{
		// by getting here we already know that the given document is supported, and hence
		// we know it has version 1
		getContext().Reset(); // clears all previous content and sets the version to 1
		NotifyBeginDocument();
		VisitChildrenOf( rtfDocument );
		getContext().setState(RtfInterpreterState.Ended);
		NotifyEndDocument();
	} // InterpretContents

	// ----------------------------------------------------------------------
	private void VisitChildrenOf( IRtfGroup group ) throws Exception
	{
		boolean pushedTextFormat = false;
		if ( getContext().getState() == RtfInterpreterState.InDocument )
		{
			getContext().PushCurrentTextFormat();
			pushedTextFormat = true;
		}
		try
		{
			for ( IRtfElement child : group.getContents() )
			{
				//child.getClass().getSimpleName()+":"+
				//System.out.print(child.getClass().getSimpleName()+":"+child.toString()+" ");
				child.Visit( this );
			}
		}
		finally
		{
			if ( pushedTextFormat )
			{
				getContext().PopCurrentTextFormat();
			}
		}
	} // VisitChildrenOf

	// ----------------------------------------------------------------------
	public void VisitTag( IRtfTag tag ) throws Exception
	{
		if ( getContext().getState() != RtfInterpreterState.InDocument )
		{
			if ( getContext().getFontTable().size() > 0 && getContext().getColorTable().size() > 0 )
			{
				// somewhat of a hack to detect state change from header to in-document for
				// rtf-docs which do neither have a generator group nor encapsulate the
				// actual document content in a group.
				getContext().setState(RtfInterpreterState.InDocument);
			}
		}
		RtfInterpreterState state=getContext().getState();
		if(state==RtfInterpreterState.Init){
			if(RtfSpec.TagRtf.equals( tag.getName())){
				getContext().setState(RtfInterpreterState.InHeader);
				getContext().setRtfVersion(tag.getValueAsNumber());
			}else{
				throw new Exception( "Init: illegal state for tag '" + tag + "'" );
			}
		}else if(state==RtfInterpreterState.InHeader){
			String tagName=tag.getName();
			if(tagName==RtfSpec.TagDefaultFont){
				getContext().setDefaultFontId( RtfSpec.TagFont + tag.getValueAsNumber());
			}
		}else if(state==RtfInterpreterState.InDocument){
			String tagName=tag.getName();
			if(tagName.equals(RtfSpec.TagPlain)){
				getContext().setWritableCurrentTextFormat(getContext().getWritableCurrentTextFormat().DeriveNormal());
			}else if(tagName.equals(RtfSpec.TagParagraphDefaults)){
				;
			}else if(tagName.equals(RtfSpec.TagSectionDefaults)){
				getContext().setWritableCurrentTextFormat(getContext().getWritableCurrentTextFormat().DeriveWithAlignment( RtfTextAlignment.Left ));
				
			}else if(tagName.equals(RtfSpec.TagBold)){
				boolean bold = !tag.getHasValue() || tag.getValueAsNumber() != 0;
				getContext().setWritableCurrentTextFormat(getContext().getWritableCurrentTextFormat().DeriveWithBold( bold )); 						
			}else if(tagName.equals(RtfSpec.TagItalic)){
				boolean italic = !tag.getHasValue() || tag.getValueAsNumber() != 0;
				getContext().setWritableCurrentTextFormat (getContext().getWritableCurrentTextFormat().DeriveWithItalic( italic ));
					
			}else if(tagName.equals(RtfSpec.TagUnderLine)){
				boolean underline = !tag.getHasValue() || tag.getValueAsNumber() != 0;
				getContext().setWritableCurrentTextFormat(getContext().getWritableCurrentTextFormat().DeriveWithUnderline( underline ));
					
			}else if(tagName.equals(RtfSpec.TagUnderLineNone)){
				getContext().setWritableCurrentTextFormat(getContext().getWritableCurrentTextFormat().DeriveWithUnderline( false ));
					
			}else if(tagName.equals(RtfSpec.TagStrikeThrough)){
				boolean strikeThrough = !tag.getHasValue ()|| tag.getValueAsNumber() != 0;
				getContext().setWritableCurrentTextFormat(getContext().getWritableCurrentTextFormat().DeriveWithStrikeThrough( strikeThrough ));
					
			}else if(tagName.equals(RtfSpec.TagFont)){
				String fontId = tag.getFullName();
				//for(String e:getContext().getFontTable().keySet())
				//{
				//	System.out.println(e);
				//}
				if ( getContext().getFontTable().containsKey(fontId) )
				{
					getContext().setWritableCurrentTextFormat(getContext().getWritableCurrentTextFormat().DeriveWithFont(
							(IRtfFont)getContext().getFontTable().get(fontId)));
				}
				else
				{
					throw new Exception( "undefined font: " + fontId );
				}
			}else if(tagName.equals(RtfSpec.TagFontSize)){
				int fontSize = tag.getValueAsNumber();
				if ( fontSize > 0 )
				{
					getContext().setWritableCurrentTextFormat(getContext().getWritableCurrentTextFormat().DeriveWithFontSize( fontSize )); 
				}
				else
				{
					throw new Exception( "invalid font size: " + fontSize );
				}
			}else if(tagName.equals(RtfSpec.TagFontSubscript)){
				int subscript = tag.getValueAsNumber();
				getContext().setWritableCurrentTextFormat(getContext().getWritableCurrentTextFormat().DeriveWithSuperScript( -subscript )) ;
				
			}else if(tagName.equals(RtfSpec.TagFontSuperscript)){
				int superscript = tag.getValueAsNumber();
				getContext().setWritableCurrentTextFormat(getContext().getWritableCurrentTextFormat().DeriveWithSuperScript( superscript )); 
					
			}else if(tagName.equals(RtfSpec.TagAlignLeft)){
				getContext().setWritableCurrentTextFormat(getContext().getWritableCurrentTextFormat().DeriveWithAlignment( RtfTextAlignment.Left ));
					
			}else if(tagName.equals(RtfSpec.TagAlignCenter)){
				getContext().setWritableCurrentTextFormat(getContext().getWritableCurrentTextFormat().DeriveWithAlignment( RtfTextAlignment.Center ));
					
			}else if(tagName.equals(RtfSpec.TagAlignRight)){
				getContext().setWritableCurrentTextFormat (getContext().getWritableCurrentTextFormat().DeriveWithAlignment( RtfTextAlignment.Right ));
					
			}else if(tagName.equals(RtfSpec.TagAlignJustify)){
				getContext().setWritableCurrentTextFormat(getContext().getWritableCurrentTextFormat().DeriveWithAlignment( RtfTextAlignment.Justify )); 
					
			}else if(tagName.equals(RtfSpec.TagColorBackground)){
				;
			}else if(tagName.equals(RtfSpec.TagColorBackgroundWord)){
				;
			}else if(tagName.equals(RtfSpec.TagColorForeground)){
				int colorIndex = tag.getValueAsNumber();
				if ( colorIndex >= 0 && colorIndex < getContext().getColorTable().size() )
				{
					IRtfColor newColor =(IRtfColor) getContext().getColorTable().get(colorIndex);
					boolean isForeground = RtfSpec.TagColorForeground.equals( tag.getName() );
					getContext().setWritableCurrentTextFormat(isForeground ?getContext().getWritableCurrentTextFormat().DeriveWithForegroundColor( newColor ) :
						getContext().getWritableCurrentTextFormat().DeriveWithBackgroundColor( newColor )) ;
				}
				else
				{
					throw new Exception( "undefined color index: " + colorIndex );
				}
			}else if(tagName.equals(RtfSpec.TagSection)){
				NotifyInsertBreak( RtfVisualBreakKind.Section );
			}else if(tagName.equals(RtfSpec.TagParagraph)){
				NotifyInsertBreak( RtfVisualBreakKind.Paragraph );
			}else if(tagName.equals(RtfSpec.TagLine)){
				NotifyInsertBreak( RtfVisualBreakKind.Line );
			}else if(tagName.equals(RtfSpec.TagPage)){
				NotifyInsertBreak( RtfVisualBreakKind.Page );
			}else if(tagName.equals(RtfSpec.TagTabulator)){
				NotifyInsertSpecialChar( RtfVisualSpecialCharKind.Tabulator );
			}else if(tagName.equals(RtfSpec.TagTilde)){
				NotifyInsertSpecialChar( RtfVisualSpecialCharKind.NonBreakingSpace );
			}else if(tagName.equals(RtfSpec.TagEmDash)){
				NotifyInsertSpecialChar( RtfVisualSpecialCharKind.EmDash );
			}else if(tagName.equals(RtfSpec.TagEnDash)){
				NotifyInsertSpecialChar( RtfVisualSpecialCharKind.EnDash );
			}else if(tagName.equals(RtfSpec.TagEmSpace)){
				NotifyInsertSpecialChar( RtfVisualSpecialCharKind.EmSpace );
			}else if(tagName.equals(RtfSpec.TagEnSpace)){
				NotifyInsertSpecialChar( RtfVisualSpecialCharKind.EnSpace );
			}else if(tagName.equals(RtfSpec.TagQmSpace)){
				NotifyInsertSpecialChar( RtfVisualSpecialCharKind.QmSpace );
			}else if(tagName.equals(RtfSpec.TagBulltet)){
				NotifyInsertSpecialChar( RtfVisualSpecialCharKind.Bullet );
			}else if(tagName.equals(RtfSpec.TagLeftSingleQuote)){
				NotifyInsertSpecialChar( RtfVisualSpecialCharKind.LeftSingleQuote );
			}else if(tagName.equals(RtfSpec.TagRightSingleQuote)){
				NotifyInsertSpecialChar( RtfVisualSpecialCharKind.RightSingleQuote );
			}else if(tagName.equals(RtfSpec.TagLeftDoubleQuote)){
				NotifyInsertSpecialChar( RtfVisualSpecialCharKind.LeftDoubleQuote );
			}else if(tagName.equals(RtfSpec.TagRightDoubleQuote)){
				NotifyInsertSpecialChar( RtfVisualSpecialCharKind.RightDoubleQuote );
			}else if(tagName.equals(RtfSpec.TagHyphen)){
				NotifyInsertSpecialChar( RtfVisualSpecialCharKind.OptionalHyphen );
			}else if(tagName.equals(RtfSpec.TagUnderscore)){
				NotifyInsertSpecialChar( RtfVisualSpecialCharKind.NonBreakingHyphen );
			}							
		}
	} // IRtfElementVisitor.VisitTag

	// ----------------------------------------------------------------------
	public void VisitGroup( IRtfGroup group ) throws Exception
	{
		
		String groupDestination = group.getDestination();
		//System.out.print(" "+groupDestination);
		RtfInterpreterState getState=getContext().getState();
		//if("info".equals(groupDestination))
		//System.out.println("RtfInterpreterState "+getState);
		if(getState==RtfInterpreterState.Init){
			if ( RtfSpec.TagRtf.equals( groupDestination ) )
			{
				VisitChildrenOf( group );
			}
			else
			{
				throw new Exception( "Init: illegal state for group '" + groupDestination + "'" );
			}
		}else if(getState==RtfInterpreterState.InHeader){
			if(RtfSpec.TagFontTable.equals(groupDestination)){
				this.fontTableBuilder.VisitGroup( group );
			}else if(RtfSpec.TagColorTable.equals(groupDestination)){
				this.colorTableBuilder.VisitGroup( group );					
			}else if(RtfSpec.TagGenerator.equals(groupDestination)){
				//System.out.println("RtfSpec.TagGenerator");
				getContext().setState (RtfInterpreterState.InDocument) ;
				IRtfText generator = group.getContents().size() == 3 ?(IRtfText)group.getContents().get(2) : null;
				if ( generator != null )
				{
					String generatorName = generator.getText();
					getContext().setGenerator(generatorName.endsWith( ";" ) ?
							generatorName.substring( 0, generatorName.length() - 1 ) : generatorName);
				}
				else
				{
					throw new Exception( "invalid generator group: " + group );
				}
			}else if(groupDestination==null){
				getContext().setState(RtfInterpreterState.InDocument) ;
				if ( !group.getIsExtensionDestination() )
				{
					VisitChildrenOf( group );
				}
			}
		}else if(getState==RtfInterpreterState.InDocument){
			
			if(RtfSpec.TagUserProperties.equals(groupDestination)){
				this.userPropertyBuilder.VisitGroup( group );
			}else if(RtfSpec.TagInfo.equals(groupDestination)){
				//System.out.println(RtfSpec.TagInfo);
				this.documentInfoBuilder.VisitGroup( group );
			}else if(RtfSpec.TagUnicodeAlternativeChoices.equals(groupDestination)){
				IRtfGroup alternativeWithUnicodeSupport =
					group.SelectChildGroupWithDestination( RtfSpec.TagUnicodeAlternativeUnicode );
				if ( alternativeWithUnicodeSupport != null )
				{
					// there is an alternative with unicode formatted content -> use this
					VisitChildrenOf( alternativeWithUnicodeSupport );
				}
				else
				{
					// try to locate the alternative without unicode -> only ANSI fallbacks
					IRtfGroup alternativeWithoutUnicode = // must be the third element if present
						group.getContents().size() > 2 ? (IRtfGroup)group.getContents().get(2)  : null;
					if ( alternativeWithoutUnicode != null )
					{
						VisitChildrenOf( alternativeWithoutUnicode );
					}
				}
			}else if(RtfSpec.TagHeader.equals(groupDestination)){
				;
			}else if(RtfSpec.TagHeaderFirst.equals(groupDestination)){
				;
			}else if(RtfSpec.TagHeaderLeft.equals(groupDestination)){
				;
			}else if(RtfSpec.TagHeaderRight.equals(groupDestination)){
				;
			}else if(RtfSpec.TagFooter.equals(groupDestination)){
				;
			}else if(RtfSpec.TagFooterFirst.equals(groupDestination)){
				;
			}else if(RtfSpec.TagFooterLeft.equals(groupDestination)){
				;
			}else if(RtfSpec.TagFooterRight.equals(groupDestination)){
				;
			}else if(RtfSpec.TagFootnote.equals(groupDestination)){
				;
			}else if(RtfSpec.TagPicture.equals(groupDestination)){
				this.imageBuilder.VisitGroup( group );
				NotifyInsertImage(
					this.imageBuilder.getFormat(),
					this.imageBuilder.getWidth(),
					this.imageBuilder.getHeight(),
					this.imageBuilder.getDesiredWidth(),
					this.imageBuilder.getDesiredHeight(),
					this.imageBuilder.getScaleWidthPercent(),
					this.imageBuilder.getScaleHeightPercent(),
					this.imageBuilder.getImageDataHex() );
			}else if(RtfSpec.TagParagraphNumberText.equals(groupDestination)){
				;
			}else if(RtfSpec.TagListNumberText.equals(groupDestination)){
				NotifyInsertSpecialChar( RtfVisualSpecialCharKind.ParagraphNumberBegin );
				VisitChildrenOf( group );
				NotifyInsertSpecialChar( RtfVisualSpecialCharKind.ParagraphNumberEnd );
			}else {
				//System.out.println("enter VisitChildrenOf");
				if ( !group.getIsExtensionDestination ())
				{
					// nested text group
					VisitChildrenOf( group );
				}
			}
		}
	} // IRtfElementVisitor.VisitGroup

	// ----------------------------------------------------------------------
	public void VisitText( IRtfText text ) throws Exception
	{
		RtfInterpreterState getState=getContext().getState();
		if(getState==RtfInterpreterState.Init){
			throw new Exception( "Init: illegal state for text '" + text.getText() + "'" );
		}else if(getState==RtfInterpreterState.InHeader){
			getContext().setState(RtfInterpreterState.InDocument);
		}else if(getState==RtfInterpreterState.InDocument){
			;
		}
		
		NotifyInsertText( text.getText ());
	} // IRtfElementVisitor.VisitText

	// ----------------------------------------------------------------------
	// members
	private  RtfFontTableBuilder fontTableBuilder;
	private  RtfColorTableBuilder colorTableBuilder;
	private  RtfDocumentInfoBuilder documentInfoBuilder;
	private  RtfUserPropertyBuilder userPropertyBuilder;
	private  RtfImageBuilder imageBuilder;

} // class RtfInterpreter

