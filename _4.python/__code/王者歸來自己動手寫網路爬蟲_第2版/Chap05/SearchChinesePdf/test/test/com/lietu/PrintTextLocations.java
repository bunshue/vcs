package test.com.lietu;

import org.apache.pdfbox.exceptions.InvalidPasswordException;

import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.pdmodel.PDPage;
import org.apache.pdfbox.pdmodel.font.PDFont;
import org.apache.pdfbox.util.PDFTextStripper;
import org.apache.pdfbox.util.TextPosition;

import java.io.IOException;

import java.util.List;
import java.util.Map;

/**
 * This is an example on how to get some x/y coordinates of text.
 *
 * Usage: java org.pdfbox.examples.util.PrintTextLocations &lt;input-pdf&gt;
 *
 * @author <a href="mailto:ben@benlitchfield.com">Ben Litchfield</a>
 * @version $Revision: 1.6 $
 */
public class PrintTextLocations extends PDFTextStripper
{
	private String titleGuess = null;
	float bigestFontSize = -1.00f;
	boolean consistent = false;
    private boolean onFirstPage = true;
	
    /**
     * Default constructor.
     * 
     * @throws IOException If there is an error loading text stripper properties.
     */
    public PrintTextLocations() throws IOException
    {
        super.setSortByPosition( true );
    }
    
    /**
     * This will print the documents data.
     *
     * @param args The command line arguments.
     *
     * @throws Exception If there is an error parsing the document.
     */
    public static void main( String[] args ) throws Exception
    {
    	String pdfFile = //"D:/lg/work/hblocaltax/D751503Dd01.pdf";
    		"D:/lg/work/hblocaltax/n11261961.pdf";
    		//"D:/lg/work/hblocaltax/468456C0d01.pdf";
    		//"D:/lg/work/hblocaltax/217712CEd01.pdf";
    		//"D:/lg/work/hblocaltax/49B10CA1d01.pdf";
    		//"D:/lg/work/hblocaltax/7D19A80Ed01.pdf";
    		
    	//"D:/lg/work/hblocaltax/DB182628d01.pdf";
    		
    	//"D:/lg/work/hblocaltax/9BA17857d01.pdf";
    		//"D:/lg/work/hblocaltax/9364DA0Dd01.pdf";
    		//"D:/lg/work/hblocaltax/C8674AACd01.pdf";
    		//"D:/lg/work/hblocaltax/D751503Dd01.pdf";
    	args = new String[] {pdfFile};
        if( args.length != 1 )
        {
            usage();
        }
        else
        {
            PDDocument document = null;
            try
            {
                document = PDDocument.load( args[0] );
                if( document.isEncrypted() )
                {
                    try
                    {
                        document.decrypt( "" );
                    }
                    catch( InvalidPasswordException e )
                    {
                        System.err.println( "Error: Document is encrypted with a password." );
                        System.exit( 1 );
                    }
                }
                PrintTextLocations printer = new PrintTextLocations();
                /*List allPages = document.getDocumentCatalog().getAllPages();
                //for( int i=0; i<allPages.size(); i++ )
                for( int i=0; i<1; i++ )
                {
                    PDPage page = (PDPage)allPages.get( i );
                    System.out.println( "Processing page: " + i );
                    if(page.findResources() == null)
                    {
                    	System.out.println( "page.findResources(): isnull"  );
                    }
                    if(page.getContents().getStream() == null)
                    {
                    	System.out.println( "page.getContents().getStream(): isnull"  );
                    }
                    //System.out.println( page.findResources().getColorSpaces()  );
                    Map a = page.findResources().getColorSpaces();
                    for(Object e:a.keySet())
                    {
                    	System.out.println( e.getClass().getName() );
                    	System.out.println(a.get(e) );
                    }
                    //printer.processStream( page, page.findResources(), page.getContents().getStream() );
                }*/
                
                printer.getText(document);

                System.out.println( "titleGuess:" + printer.titleGuess );
                //System.out.println( "bigestFontSize :" + printer.bigestFontSize );
                
                //System.out.println(printer.getColorSpaces());
            }
            finally
            {
                if( document != null )
                {
                    document.close();
                }
            }
        }
    }
    
    @Override
    protected void writePage() throws IOException 
    {
        if (onFirstPage) 
        {
            onFirstPage = false;
        }
        super.writePage();
    }
    
    @Override
    protected void processTextPosition( TextPosition text )
    {
    	PDFont font = text.getFont();
    	System.out.println("font name:"+font.getBaseFont());
    	if(!onFirstPage)
    		return;
    	float currentFontSize = text.getFontSize()*text.getXScale();
    	
        System.out.println( "String[" + text.getX() + "," + 
        		" InPt="+currentFontSize+" "+
                text.getY() + " fs=" + text.getFontSize() + " xscale=" + 
                text.getXScale() + " height=" + text.getHeight() + " width=" + 
                text.getWidth() + "]" + text.getCharacter() );
        
        if(currentFontSize< bigestFontSize)
        {
        	consistent = false;
        }
        else if (currentFontSize> bigestFontSize//currentFontSize.compareTo(bigestFontSize)>0
        		&& !"".equals(text.getCharacter().trim()) )
        {
        	titleGuess = text.getCharacter();
        	bigestFontSize = currentFontSize;
        	consistent = true;
        }
        else if(currentFontSize == bigestFontSize//currentFontSize.compareTo(bigestFontSize)==0
        		&& consistent
        		&& !"".equals(text.getCharacter().trim()))
        {
        	System.out.println("bigestFontSize:"+bigestFontSize +" "+currentFontSize+(currentFontSize == bigestFontSize));
        	titleGuess += text.getCharacter().trim();
        }
    }
    
    /**
     * This will print the usage for this document.
     */
    private static void usage()
    {
        System.err.println( "Usage: java org.pdfbox.examples.pdmodel.PrintTextLocations <input-pdf>" );
    }

}