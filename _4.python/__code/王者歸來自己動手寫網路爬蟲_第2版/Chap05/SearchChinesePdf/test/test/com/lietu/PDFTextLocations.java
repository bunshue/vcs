package test.com.lietu;


import org.apache.pdfbox.exceptions.InvalidPasswordException;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.util.PDFTextStripper;
import org.apache.pdfbox.util.TextPosition;
import java.io.IOException;
import java.util.TreeSet;

/**
 * This is an example on how to get some x/y coordinates of text.
 *
 * Usage: java org.pdfbox.examples.util.PrintTextLocations &lt;input-pdf&gt;
 *
 * @author <a href="mailto:ben@benlitchfield.com">Ben Litchfield</a>
 * @version $Revision: 1.6 $
 */
public class PDFTextLocations extends PDFTextStripper
{
	private String titleGuess = null;
	float bigestFontSize = -1.00f;
	boolean consistent = false;
    private boolean onFirstPage = true;
    static int hitCount = 0;
    static TreeSet<Integer> ts = new TreeSet<Integer>();
    static String keyword = null;
    /**
     * Default constructor.
     * @throws IOException If there is an error loading text stripper properties.
     */
    public PDFTextLocations() throws IOException
    {
        super.setSortByPosition( true );
    }
    
    /**
     * This will print the documents data.
     * @param args The command line arguments.
     * @throws Exception If there is an error parsing the document.
     */
    public static void main( String[] args ) throws Exception
    {
    	String pdfFile = "D:/lg/work/sciencep/陳省身傳.pdf";
    	keyword = "北京大學";
    	args = new String[] {pdfFile};
        if( args.length != 1 ){
            usage();
        } else {
            PDDocument document = null;
            try {
                document = PDDocument.load( args[0] );
                if( document.isEncrypted() ) {
                    try {
                        document.decrypt("");
                    }
                    catch( InvalidPasswordException e ) {
                        System.err.println( "Error: Document is encrypted with a password." );
                        System.exit(1);
                    }
                }
                PDFTextLocations printer = new PDFTextLocations();
                int pagecounts = document.getNumberOfPages();
                printer.setStartPage(1);
//              printer.setEndPage(1);
                
                System.out.println("查詢關鍵字："+keyword+"\t\t檔案總頁數："+pagecounts);
                
                System.out.println("頁號\t\t坐標(X,Y)\t\t長度\t\t高度\t\t字體大小");
                
                String text= printer.getText(document);

                System.out.println("共出現次數："+hitCount);
                
                StringBuilder sb = new StringBuilder();
                for(Integer i : ts){
                	sb.append(i).append("、");
                }
                System.out.println("出現在第"+sb.toString()+"頁。");
            }
            finally {
                if( document != null ) {
                    document.close();
                }
            }
        }
    }
    
    @Override
    protected void writePage() throws IOException 
    {
    	//只取首頁
//      if (onFirstPage) {
//        onFirstPage = false;
//      }
        super.writePage();
    }
    
    @Override
    protected void processTextPosition(TextPosition text) 
    {
    	if(!onFirstPage)
    		return;
    	float currentFontSize = text.getFontSize()*text.getXScale()*-1;
    	String str = text.getCharacter();
    	
    	if(str.indexOf(keyword) >=0){
		System.out.println(getCurrentPageNo()+"\t\t"+"("+text.getX()+","+text.getY()+")"+"\t\t"+keyword.length()+"\t\t"+text.getHeight()+"\t\t"+currentFontSize);
			
//    		System.out.println("在第 "+getCurrentPageNo()+" 坐標("+text.getX()+","+text.getY()+")，長度:"+keyword.length()+"，高度:"+text.getHeight()+"字體大小:"+currentFontSize);

    		hitCount +=1;
    		ts.add(getCurrentPageNo());
    	}
    	
        if(currentFontSize< bigestFontSize)
        {
        	consistent = false;
        }
        else if (currentFontSize> bigestFontSize
        		&& !"".equals(text.getCharacter().trim()) )
        {
        	titleGuess = text.getCharacter();
        	bigestFontSize = currentFontSize;
        	consistent = true;
        }
        else if(currentFontSize == bigestFontSize
        		&& consistent
        		&& !"".equals(text.getCharacter().trim()))
        {
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