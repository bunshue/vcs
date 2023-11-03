package com.lietu.pdfbox;

import java.awt.Color;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Properties;

import org.apache.pdfbox.exceptions.WrappedIOException;
import org.apache.pdfbox.pdmodel.text.PDTextState;
import org.apache.pdfbox.util.PDFStreamEngine;
import org.apache.pdfbox.util.ResourceLoader;
import org.apache.pdfbox.util.TextPosition;
import org.apache.pdfbox.util.operator.OperatorProcessor;

public class TextPageDrawer extends PDFStreamEngine
{
	boolean isBegin = true;
	boolean consistent = true;
	Color lastColor = null;
	float lastFontSize = -1.00f;
	float lastY = -1f;
	float lastX = -1f;
	float lastHeightDir = -1f;
	String lastBaseFront = "";
	public ArrayList<PdfTitle> candidateTitle = null;
	float maxHeight;
	StringBuilder allContent;
	ArrayList<TextPosition> texts = new ArrayList<TextPosition>();
	
    /**
     * Default constructor, loads properties from file.
     *
     * @throws IOException If there is an error loading properties from the file.
     */
    public TextPageDrawer(ArrayList<PdfTitle> titles,
    						float maxH,
    						StringBuilder allC) throws IOException
    {
    	allContent = allC;
    	maxHeight = maxH;
    	candidateTitle = titles;
    	Properties properties = ResourceLoader.loadProperties( "Resources/PageDrawer.properties", true );
        if( properties == null ) 
        {
            throw new NullPointerException( "properties cannot be null" );
        }
        try
        {
            Iterator keys = properties.keySet().iterator();
            OperatorSet operators = OperatorSet.getInstance();
            while( keys.hasNext() )
            {
                String operator = (String)keys.next();
                
                if(operators.contains(operator))
                {
                	continue;
                }
                
                String operatorClass = properties.getProperty( operator );
                OperatorProcessor op = (OperatorProcessor)Class.forName( operatorClass ).newInstance();
                registerOperatorProcessor(operator, op);
            }
        }
        catch( Exception e )
        {
            throw new WrappedIOException( e );
        }
    }

    /**
     * You should override this method if you want to perform an action when a
     * text is being processed. 
     *
     * @param text The text to process 
     */
    protected void processTextPosition( TextPosition text )
    {
        //should use colorspaces for the font color but for now assume that
        //the font color is black
        try
        {
            float currentX = text.getX();
            float currentY = text.getY();
            if(currentY>maxHeight)
            {
            	allContent.append(text.getCharacter());
            	return;
            }
        	Color currentColor = null;
        	
            if( this.getGraphicsState().getTextState().getRenderingMode() == PDTextState.RENDERING_MODE_FILL_TEXT )
            {
                //graphics.setColor( this.getGraphicsState().getNonStrokingColorSpace().createColor() );
            	
            	currentColor = this.getGraphicsState().getNonStrokingColorSpace().createColor();
            	//System.out.println(currentColor);
            	//System.out.println(text.getCharacter());
            }
            else if( this.getGraphicsState().getTextState().getRenderingMode() 
                        == PDTextState.RENDERING_MODE_STROKE_TEXT )
            {
                //graphics.setColor( this.getGraphicsState().getStrokingColorSpace().createColor() );
            	
            	//System.out.println(text.getCharacter());
            	currentColor = this.getGraphicsState().getStrokingColorSpace().createColor();
            	//System.out.println(currentColor);
            }
            else
            {
                // TODO : need to implement....
                //logger().warning("Unsupported RenderingMode "+this.getGraphicsState().getTextState().getRenderingMode()
                //            +" in PageDrawer.processTextPosition()");
                //logger().warning("Using RenderingMode "+PDTextState.RENDERING_MODE_FILL_TEXT+" instead");
                //graphics.setColor( this.getGraphicsState().getNonStrokingColorSpace().createColor() );
            	
            	currentColor = this.getGraphicsState().getNonStrokingColorSpace().createColor();
            }
            float currentFontSize = text.getFontSize()*text.getYScale();
            String currentBaseFont = text.getFont().getBaseFont();
            float currentHeightDir = text.getHeightDir();
            
            //System.out.println("X "+text.getX() +" Y "+text.getY() +" " +text.getCharacter()+
            //		" "+text.getHeight());
            consistent = true;
            if(!lastBaseFront.equals(currentBaseFont) &&
            		(currentY - lastY)>(Math.max(currentFontSize, lastFontSize)+lastHeightDir))
            {
            	consistent = false;
            	//System.out.println("BaseFront inconsistent"+" " +text.getCharacter() 
            	//		+" y diff:"+(currentY - lastY)
            	//		+" FontSize"+Math.max(currentFontSize, lastFontSize)
            	//		+" lastHeightDir:"+lastHeightDir);
            }
            if(Math.abs(currentFontSize - lastFontSize)>3.0f)
            {
            	consistent = false;
            	//System.out.println("FontSize inconsistent "+Math.abs(currentFontSize - lastFontSize)+" " +text.getCharacter());
            }
            if(!currentColor.equals(lastColor) && currentY != lastY)
            {
            	consistent = false;
            	//System.out.println("Color inconsistent"+" " +text.getCharacter());
            }

            if((currentY - lastY)>(Math.max(currentFontSize, lastFontSize) +lastHeightDir+currentHeightDir))
            {
            	consistent = false;
            	//System.out.println("Y inconsistent " +(Math.max(currentFontSize, lastFontSize) +lastHeightDir+currentHeightDir)
            	//		+" " +text.getCharacter());
            }
            if(isBegin)
            {
            	consistent = true;
            	isBegin = false;
            }
            
            //System.out.println(text.getCharacter()+ " font:"+text.getFont().getBaseFont() 
            //		+" consistent:"+consistent+" "+text.getY() +" "+Math.abs(currentFontSize - lastFontSize)
            //		+" "+(currentY - lastY)+" "+lastHeightDir);
        	String contText = text.getCharacter();
            if(!consistent)
            {
            	candidateTitle.add(new PdfTitle(lastColor,lastFontSize,lastY,texts));
            	
        		texts = new ArrayList<TextPosition>();
                texts.add(text);
            	//title = contText;
            }
            else
            {
                //System.out.println(text.getCharacter());
            	//if(!PdfTitleExtractor.isFileNum(contText,currentColor))
                texts.add(text);
            }
            allContent.append(contText) ;

        	lastColor = currentColor;
        	lastFontSize = currentFontSize;
        	lastY = currentY;
        	lastBaseFront = currentBaseFont;
        	lastHeightDir = currentHeightDir;
        	lastX = currentX;
        }
        catch( IOException io )
        {
            io.printStackTrace();
        }
    }
    
    public PdfTitle getLastTile()
    {
    	return new PdfTitle(lastColor,lastFontSize,lastY,texts);
    }
}
