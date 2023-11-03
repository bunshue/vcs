package com.lietu.webCat;

import java.io.BufferedReader;
import java.io.File;
import java.io.InputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

import java.util.StringTokenizer;

/**
 *  Implementation of a Ternary Search Trie, a data structure for storing <code>String</code> objects
 *  that combines the compact size of a binary search tree with the speed of a digital search trie, and is 
 *  therefore ideal for practical use in sorting and searching data.</p> <p>
 * 
 *  This data structure is faster than hashing for many typical search problems, and supports
 *  a broader range of useful problems and operations. Ternary searches are faster than
 *  hashing and more powerful, too.</p> <p>
 * 
 *  The theory of ternary search trees was described at a symposium in 1997 (see "Fast 
 *  Algorithms for Sorting and Searching Strings," by J.L. Bentley and R. Sedgewick,
 *  Proceedings of the 8th Annual ACM-SIAM Symposium on Discrete Algorithms, January 1997).
 *  Algorithms in C, Third Edition, by Robert Sedgewick (Addison-Wesley, 1998) provides 
 *  yet another view of ternary search trees. 
 * 
 * @author Bruno Martins
 *
 */
public class URLPattern {
	
	/**
	 *  An inner class of Ternary Search Trie that represents a node in the trie.
	 */
	protected final class TSTNode {
		
		/** The key to the node. */
		protected String data=null;

		/** The relative nodes. */
		protected TSTNode LOKID;
		protected TSTNode EQKID;
		protected TSTNode HIKID;

		/** The char used in the split. */
		protected char splitchar;

		/**
		 *  Constructor method.
		 *
		 *@param  splitchar  The char used in the split.
		 *@param  parent     The parent node.
		 */
		protected TSTNode(char splitchar) {
			this.splitchar = splitchar;
		}
	}
	
	protected static class TSTItem {
		/** The key to the node. */
		protected String data=null;

		/** The char used in the split. */
		protected String key;

		/**
		 *  Constructor method.
		 *
		 *@param  splitchar  The char used in the split.
		 *@param  parent     The parent node.
		 */
		protected TSTItem(String key, String data) {
			this.key = key;
			this.data = data;
		}
	}
	
	/** The base node in the trie. */
	public TSTNode root;
	
	private static URLPattern dicPhrase = null;
	
	public static URLPattern getInstance()
	{
		if (dicPhrase == null)
			dicPhrase = new URLPattern();
		return dicPhrase;
	}
	
	private URLPattern()
	{
		this("urlCat.txt");
	}
	
	public static String getDir()
	{
		String dir = System.getProperty("dic.dir");
		if (dir == null)
			dir = "/dic/";
		else if( !dir.endsWith("/"))
			dir += "/";
		return dir;
	}
	
	/**
	 *  Constructs a Ternary Search Trie and loads data from a <code>File</code> into the Trie. 
	 *  The file is a normal text document, where each line is of the form
	 *  word : integer.
	 *
	 *@param  file             The <code>File</code> with the data to load into the Trie.
	 *@exception  IOException  A problem occured while reading the data.
	 */
	public URLPattern(String dic){
		
		try{
			InputStream file = null;
			if (System.getProperty("dic.dir") == null)
				file = getClass().getResourceAsStream(URLPattern.getDir()+dic);
			else
				file = new FileInputStream(new File(URLPattern.getDir()+dic));
			
			BufferedReader in;
			in = new BufferedReader(new InputStreamReader(file,"GBK"));
			String word;
			
			while ((word = in.readLine()) != null) {
				
				StringTokenizer st = new StringTokenizer(word,"|" );
				
				String key = st.nextToken();
				String data = st.nextToken();
				word = key;
				if (root == null) {
					root = new TSTNode(key.charAt(0));
				}
				if (key.length() > 0 && root != null) {
					TSTNode currentNode = root;
					int charIndex = 0;
					while (true) {
						if (currentNode == null)
							break;
						int charComp =							
								(key.charAt(charIndex)-
								currentNode.splitchar);
						if (charComp == 0) {
							charIndex++;
							if (charIndex == key.length()) {
								break;
							}
							currentNode = currentNode.EQKID;
						} else if (charComp < 0) {
							currentNode = currentNode.LOKID;
						} else {
							currentNode = currentNode.HIKID;
						}
					}
					
					currentNode =
						getOrCreateNode(key);	
					
					currentNode.data = data;
				}
			}
			in.close();
		}catch( IOException e)
		{
			System.out.println("not find dictionary file");
		}
	}
	
	/**
	 *  Retrieve the object indexed by a key.
	 *
	 *@param      key  A <code>String</code> index.
	 *@return      The object retrieved from the Ternary Search Trie.
	 */
	public Object get(String key) {
		TSTNode node = getNode(key);
		if (node == null) { return null; }
		return node.data;
	}

	/**
	 *  Returns the node indexed by key, or <code>null</code> if that node doesn't exist.
	 *  Search begins at root node.
	 *
	 *@param  key  A <code>String</code> that indexes the node that is returned.
	 *@return   The node object indexed by key. This object is an
	 *      instance of an inner class named <code>TernarySearchTrie.TSTNode</code>.
	 */
	public TSTNode getNode(String key) {
		return getNode(key, root);
	}

    /**
     * get the handle set of a word
     */
	public String getHandle(String key) {
		TSTNode node= getNode(key, root);
		if (node==null)
			return null;
		return node.data;
	}

    /**
     * Weather the word exist in the dictionary
     * @param sWord
     * @return true if exist
     */
    public boolean isExist(String key)
    {
		String q= getHandle(key);
		if (q==null)
			return false;
		
    	return true;
    }
    
	/**
	 *  Returns the node indexed by key, or <code>null</code> if that node doesn't exist.
	 *  The search begins at root node.
	 *
	 *@param  key2        A <code>String</code> that indexes the node that is returned.
	 *@param  startNode  The top node defining the subtrie to be searched.
	 *@return            The node object indexed by key. This object is
	 *      an instance of an inner class named <code>TernarySearchTrie.TSTNode</code>.
	 */
	protected static TSTNode getNode(String key, TSTNode startNode) {
		if (key == null || startNode == null || "".equals(key)) {
			return null;
		}
		TSTNode currentNode = startNode;
		int charIndex = 0;
		while (true) {
			if (currentNode == null) {
				return null;
			}
			int charComp = key.charAt(charIndex) - currentNode.splitchar;
			if (charComp == 0) {
				charIndex++;
				if (charIndex == key.length()) {
					return currentNode;
				}
				currentNode = currentNode.EQKID;
			} else if (charComp < 0) {
				currentNode = currentNode.LOKID;
			} else {
				currentNode = currentNode.HIKID;
			}
		}
	}

	/**
	 *  Returns the node indexed by key, creating that node if it doesn't exist,
	 *  and creating any required intermediate nodes if they don't exist.
	 *
	 *@param  key                           A <code>String</code> that indexes the node that is returned.
	 *@return                                  The node object indexed by key. This object is an
	 *                                               instance of an inner class named <code>TernarySearchTrie.TSTNode</code>.
	 *@exception  NullPointerException      If the key is <code>null</code>.
	 *@exception  IllegalArgumentException  If the key is an empty <code>String</code>.
	 */
	protected TSTNode getOrCreateNode(String key)
		throws NullPointerException, IllegalArgumentException {
		if (key == null) {
			throw new NullPointerException("attempt to get or create node with null key");
		}
		if ("".equals(key)) {
			throw new IllegalArgumentException("attempt to get or create node with key of zero length");
		}
		if (root == null) {
			root = new TSTNode(key.charAt(0));
		}
		TSTNode currentNode = root;
		int charIndex = 0;
		while (true) {
			int charComp =(
					key.charAt(charIndex) -
					currentNode.splitchar);
			if (charComp == 0) {
				charIndex++;
				if (charIndex == key.length()) {
					return currentNode;
				}
				if (currentNode.EQKID == null) {
					currentNode.EQKID =
						new TSTNode(key.charAt(charIndex));
				}
				currentNode = currentNode.EQKID;
			} else if (charComp < 0) {
				if (currentNode.LOKID == null) {
					currentNode.LOKID =
						new TSTNode(key.charAt(charIndex));
				}
				currentNode = currentNode.LOKID;
			} else {
				if (currentNode.HIKID == null) {
					currentNode.HIKID =
						new TSTNode(key.charAt(charIndex));
				}
				currentNode = currentNode.HIKID;
			}
		}
	}

	public static final class Prefix {
		private byte value;
	    
		public Prefix(byte a)
		{ value = a; }
		
	    /** Match the word exactly */
	    public static final Prefix Match = new Prefix((byte)0);
	    /** MisMatch the word */
	    public static final Prefix MisMatch = new Prefix((byte)1);
	    /** Match the prefix */
	    public static final Prefix MatchPrefix = new Prefix((byte)2);
	    
	    public String toString()
	    {
	    	if( value == Match.value)
	    		return "Match";
	    	else if( value == MisMatch.value)
    			return "MisMatch";
	    	else if( value == MatchPrefix.value)
    			return "MatchPrefix";
	    	return "Invalid";
	    }
	}

	public static class PrefixRet {
		public Prefix value;
		public String data;
		
		public PrefixRet(Prefix v,String d)
		{
			value = v;
			data = d;
		}
	}
	
	public void checkPrefix(String prefix,PrefixRet ret) {
		TSTNode startNode = getNode(prefix);
		//System.out.println("the result of node split char:"+startNode.splitchar);
		if (startNode == null) {
			ret.value = Prefix.MisMatch;
			ret.data = null;
			return;
		}
		if (startNode.data != null) {
			ret.value = Prefix.Match;
			ret.data = startNode.data;
			return ;
		}
		boolean retb = sortKeyRecursion(
				startNode.EQKID,
				false);
		if( retb == false)
		{
			ret.value = Prefix.MisMatch;
			ret.data = null;
			return;
		}
		ret.value = Prefix.MatchPrefix;
		ret.data = null;
	}
	
	private static  boolean sortKeyRecursion(TSTNode currentNode,boolean sortKeyResult2) {
		//1
		if (currentNode == null) {
			return sortKeyResult2;
		}
		//System.out.println("the split char"+currentNode.splitchar);
		
		//2
		boolean sortKeyResult =
			sortKeyRecursion(
				currentNode.LOKID,sortKeyResult2);

		//3
		if (sortKeyResult) {
			return sortKeyResult;
		}
		//4
		//System.out.println("is current node is empty");
		if (currentNode.data != null) {
			return true;
		}
		//5
		//System.out.println("to find at high key");
		sortKeyResult =
			sortKeyRecursion(
				currentNode.EQKID,
				sortKeyResult);
		return sortKeyRecursion(
			currentNode.HIKID,
			sortKeyResult);
	}
}
