/*
 * Created on 2005-10-29
 *
 */
package com.lietu.keywords;

import java.util.ArrayList;
import java.util.StringTokenizer;

import java.io.BufferedReader;
import java.io.File;
import java.io.InputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * @author Administrator
 *
 */
public class CnPhraseDic {
	/**
	*  An inner class of Ternary Search Trie that represents a node in the trie.
	*/
	public class TSTNode 
	{
		/** Index values for accessing relatives array. */
		protected final static int PARENT = 0, LOKID = 1, EQKID = 2, HIKID = 3;

		/** The key to the node. */
		public int data=0;

		/** The relative nodes. */
		public TSTNode[] relatives = new TSTNode[4];

		/** The char used in the split. */
		public String splitchar;

		/**
		*  Constructor method.
		*
		*@param  splitchar  The char used in the split.
		*@param  parent     The parent node.
		*/
		public TSTNode(String splitchar, TSTNode parent) 
		{
			this.splitchar = splitchar;
			relatives[PARENT] = parent;
		}
	}
	private static CnPhraseDic dicPhrase = null;
	
	/**
	* 
	* @return the singleton of Binary gram dictionary
	*/
	public static CnPhraseDic getInstance()
	{
		if (dicPhrase == null)
			dicPhrase = new CnPhraseDic();
		return dicPhrase;
	}
	
	private CnPhraseDic()
	{
		this("phrase.txt");
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
	
	/** The base node in the trie. */
	private TSTNode rootNode;

	/**
	*  Constructs a Ternary Search Trie and loads data from a <code>File</code> into the Trie. 
	*  The file is a normal text document, where each line is of the form
	*  word : integer.
	*
	*@param  file             The <code>File</code> with the data to load into the Trie.
	*@exception  IOException  A problem occured while reading the data.
	*/
	private CnPhraseDic(String dic)
	{
		try{
			//InputStream fIn = new FileInputStream(new File(file));
			//BufferedReader srInput = new BufferedReader(new InputStreamReader(fIn,"GBK"));
			InputStream file = null;
			if (System.getProperty("dic.dir") == null)
				file = getClass().getResourceAsStream(getDir()+dic);
			else
				file = new FileInputStream(new File(getDir()+dic));
			
			BufferedReader in;
			in = new BufferedReader(new InputStreamReader(file,"GBK"));
			
			String word;
			int occur=0;
			
			while ((word = in.readLine()) != null) 
			{
				//System.out.println(word);
				StringTokenizer st = new StringTokenizer(word,":" );
				String w = st.nextToken();
				ArrayList key = getWordList(w);
				String intWord = st.nextToken();
				//System.Console.WriteLine(intWord);
				occur=Integer.parseInt(intWord);
				if (rootNode == null) 
				{
					rootNode = new TSTNode((String)(key.get(0)), null);
				}
				TSTNode node = null;
				if (key.size() > 0 && rootNode != null) 
				{
					TSTNode currentNode = rootNode;
					int charIndex = 0;
					while (true) 
					{
						if (currentNode == null)
							break;
						int charComp = 
							((String)(key.get(charIndex))).compareTo(currentNode.splitchar);
						if (charComp == 0)
						{
							charIndex++;
							if (charIndex == key.size()) 
							{
								node = currentNode;
								break;
							}
							currentNode = currentNode.relatives[TSTNode.EQKID];
						} 
						else if (charComp < 0) 
						{
							currentNode = currentNode.relatives[TSTNode.LOKID];
						}
						else 
						{
							currentNode = currentNode.relatives[TSTNode.HIKID];
						}
					}
					int occur2 = 0;
					if (node != null)
					{
						occur2 = node.data;
					}
					if (occur2 != 0) 
					{
						occur+=occur2;
					}
					currentNode =
						getOrCreateNode(key);
		
					occur2 = currentNode.data;
					if (occur2 != 0) 
					{
						//System.out.println("add");
						occur+=occur2;
					}
					currentNode.data = occur;
				}
			}
			in.close();
		}catch( IOException e)
		{
			System.out.println("not find dictionary file");
		}
	}

	public static ArrayList getWordList(String line)
	{
		//System.Console.WriteLine(line);
		ArrayList wordList = new ArrayList();
	
		/*TextReader input;
	
		input = new System.IO.StringReader(line);
	
		TokenStream tokenizer = new CnTokenizer(input);

		for (Token t = tokenizer.Next(); t != null; t = tokenizer.Next())
		{
			String word = t.TermText();				
			wordList.Add(word);
		}*/

		StringTokenizer st = new StringTokenizer(line,"," );

		while (st.hasMoreElements())
		{
			String word = st.nextToken();
			wordList.add(word);
		}

		return wordList;
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

	public Prefix checkPrefix(ArrayList prefix,int start,int end) 
	{
		TSTNode startNode = getNode(prefix,start,end);
		//System.out.println("the result of node split char:"+startNode.splitchar);
		if (startNode == null)
		{
			return Prefix.MisMatch;
		}
		if (startNode.data >0) 
		{
			return Prefix.Match;
		}
		boolean ret = sortKeyRecursion(
			startNode.relatives[TSTNode.EQKID],
			false);
		if( ret == false)
		{
			return Prefix.MisMatch;
		}
		return Prefix.MatchPrefix;
	}
	
	/**
	* Add item.
	*/
	public void add(ArrayList key, int freq)
	{
		int occur =  freq;

		if (rootNode == null) 
		{
			rootNode = new TSTNode((String)(key.get(0)), null);
		}
		TSTNode node = null;
		if (key.size() > 0 && rootNode != null) 
		{
			TSTNode currentNode = rootNode;
			int charIndex = 0;
			while (true) 
			{
				if (currentNode == null)
					break;
				int charComp = ((String)(key.get(charIndex))).compareTo(currentNode.splitchar) ;
				if (charComp == 0) 
				{
					charIndex++;
					if (charIndex == key.size()) 
					{
						node = currentNode;
						break;
					}
					currentNode = currentNode.relatives[TSTNode.EQKID];
				} 
				else if (charComp < 0) 
				{
					currentNode = currentNode.relatives[TSTNode.LOKID];
				} 
				else 
				{
					currentNode = currentNode.relatives[TSTNode.HIKID];
				}
			}
			int occur2 = 0;
			if (node != null)
			{
				occur2 = node.data;
			}
			if (occur2 != 0) 
			{
				occur+=occur2;
			}
			currentNode =
				getOrCreateNode(key);

			occur2 = currentNode.data;
			if (occur2 != 0) 
			{
				occur+=occur2;
			}
			currentNode.data = occur;
		}
	}

	/**
	*  Deletes the node passed in as an argument. If this node
	*  has non-null data, then both the node and the data will be deleted. It also
	*  deletes any other nodes in the trie that are no longer needed after the
	*  deletion of the node.
	*
	*@param  nodeToDelete  The node to delete.
	*/
	private boolean deleteNode(TSTNode nodeToDelete) 
	{
		if (nodeToDelete == null) 
		{
			return false;
		}
		nodeToDelete.data = -1;
		while (nodeToDelete != null) 
		{
			nodeToDelete = deleteNodeRecursion(nodeToDelete);
		}
		return true;
	}

	/**
	*  Recursivelly visits each node to be deleted.
	* 
	*  To delete a node, first set its data to null, then pass it into this method,
	*  then pass the node returned by this method into this method (make
	*  sure you don't delete the data of any of the nodes returned from this
	*  method!) and continue in this fashion until the node returned by this
	*  method is <code>null</code>.
	* 
	*  The TSTNode instance returned by this method will be next node to
	*  be operated on by <code>deleteNodeRecursion</code> (This emulates recursive 
	*  method call while avoiding the JVM overhead normally associated
	*  with a recursive method.)
	*
	*@param  currentNode  The node to delete.
	*@return   The next node to be called in deleteNodeRecursion.
	*/
	private TSTNode deleteNodeRecursion(TSTNode currentNode) 
	{
		if (currentNode == null) { return null; }
		if (currentNode.relatives[TSTNode.EQKID] != null || currentNode.data != -1) 
		{
			return null;
		}
		// can't delete this node if it has a non-null eq kid or data
		TSTNode currentParent = currentNode.relatives[TSTNode.PARENT];
		boolean lokidNull = currentNode.relatives[TSTNode.LOKID] == null;
		boolean hikidNull = currentNode.relatives[TSTNode.HIKID] == null;
		int childType;
		if (currentParent.relatives[TSTNode.LOKID] == currentNode) 
		{
			childType = TSTNode.LOKID;
		} 
		else if (currentParent.relatives[TSTNode.EQKID] == currentNode) 
		{
			childType = TSTNode.EQKID;
		} 
		else if (currentParent.relatives[TSTNode.HIKID] == currentNode) 
		{
			childType = TSTNode.HIKID;
		} 
		else 
		{
			rootNode = null;
			return null;
		}
		if (lokidNull && hikidNull) 
		{
			currentParent.relatives[childType] = null;
			return currentParent;
		}
		if (lokidNull) 
		{
			currentParent.relatives[childType] =
				currentNode.relatives[TSTNode.HIKID];
			currentNode.relatives[TSTNode.HIKID].relatives[TSTNode.PARENT] =
				currentParent;
			return currentParent;
		}
		if (hikidNull) 
		{
			currentParent.relatives[childType] =
				currentNode.relatives[TSTNode.LOKID];
			currentNode.relatives[TSTNode.LOKID].relatives[TSTNode.PARENT] =
				currentParent;
			return currentParent;
		}
		int deltaHi =
			currentNode.relatives[TSTNode.HIKID].splitchar.compareTo(currentNode.splitchar);
		int deltaLo =
			currentNode.splitchar.compareTo(currentNode.relatives[TSTNode.LOKID].splitchar);
		int movingKid;
		TSTNode targetNode;
		if (deltaHi == deltaLo) 
		{
			if (Math.random() < 0.5) {
				deltaHi++;
			} else {
				deltaLo++;
			}
		}
		if (deltaHi > deltaLo) 
		{
			movingKid = TSTNode.HIKID;
			targetNode = currentNode.relatives[TSTNode.LOKID];
		} 
		else 
		{
			movingKid = TSTNode.LOKID;
			targetNode = currentNode.relatives[TSTNode.HIKID];
		}
		while (targetNode.relatives[movingKid] != null) 
		{
			targetNode = targetNode.relatives[movingKid];
		}
		targetNode.relatives[movingKid] = currentNode.relatives[movingKid];
		currentParent.relatives[childType] = targetNode;
		targetNode.relatives[TSTNode.PARENT] = currentParent;
		if (!lokidNull) 
		{
			currentNode.relatives[TSTNode.LOKID] = null;
		}
		if (!hikidNull) 
		{
			currentNode.relatives[TSTNode.HIKID] = null;
		}
		return currentParent;
	}

	/**
	*  Returns the key that indexes the node argument.
	*
	*@param  node  The node whose index is to be calculated.
	*@return  The <code>String</code> that indexes the node argument.
	*/
	protected String getKey(TSTNode node) 
	{
		StringBuilder getKeyBuffer = new StringBuilder(0);
		getKeyBuffer.append("" + node.splitchar);
		TSTNode currentNode;
		TSTNode lastNode;
		currentNode = node.relatives[TSTNode.PARENT];
		lastNode = node;
		while (currentNode != null) 
		{
			if (currentNode.relatives[TSTNode.EQKID] == lastNode) 
			{
				getKeyBuffer.append("" + currentNode.splitchar);
			}
			lastNode = currentNode;
			currentNode = currentNode.relatives[TSTNode.PARENT];
		}
		getKeyBuffer.reverse();
		/*StringBuilder sb = new StringBuilder(getKeyBuffer.Length);

		int len = getKeyBuffer.Length;
		for(int i = len - 1; i >= 0; i--)
			sb.Append(getKeyBuffer[i]);*/

		//System.out.println("current key buffer:"+getKeyBuffer.toString());
		return getKeyBuffer.toString();
	}

	/**
	*  Returns the node indexed by key, or <code>null</code> if that node doesn't exist.
	*  Search begins at root node.
	*
	*@param  key  A <code>String</code> that indexes the node that is returned.
	*@return   The node object indexed by key. This object is an
	*      instance of an inner class named <code>TernarySearchTrie.TSTNode</code>.
	*/
	private TSTNode getNode(ArrayList key,int start ,int end) 
	{
		return getNode(key, rootNode,start,end);
	}

	/**
	* get frequency of the word with the handle
	* @param sWord
	* @param nHandle
	* @return frequency
	*/
	public int getFreq(ArrayList key,int start,int end)
	{
		TSTNode node= getNode(key, rootNode,start,end);
		if (node==null)
			return 0;
		return node.data;
	}

	/**
	* Weather the word exist in the dictionary
	* @param sWord
	* @return true if exist
	*/
	public boolean isExist(ArrayList key,int start,int end)
	{
		TSTNode node= getNode(key, rootNode,start,end);
		if (node==null || node.data <=0)
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
	protected TSTNode getNode(ArrayList key, TSTNode startNode,int start ,int end)
	{
		if (key == null || startNode == null || key.size() == 0) 
		{
			return null;
		}
		TSTNode currentNode = startNode;
		int charIndex = start;
		while (true)
		{
			if (currentNode == null) 
			{
				return null;
			}
			int charComp = ((String)key.get(charIndex)).compareTo(currentNode.splitchar) ;
			if (charComp == 0) 
			{
				charIndex++;
				if (charIndex == end) 
				{
					return currentNode;
				}
				currentNode = currentNode.relatives[TSTNode.EQKID];
			} 
			else if (charComp < 0) 
			{
				currentNode = currentNode.relatives[TSTNode.LOKID];
			} 
			else 
			{
				currentNode = currentNode.relatives[TSTNode.HIKID];
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
	protected TSTNode getOrCreateNode(ArrayList key)
	{
		if (key == null) 
		{
			throw new NullPointerException("attempt to get or create node with null key");
		}
		if (key.size() == 0) 
		{
			throw new IllegalArgumentException("attempt to get or create node with key of zero length");
		}
		if (rootNode == null) 
		{
			rootNode = new TSTNode((String)(key.get(0)), null);
		}
		TSTNode currentNode = rootNode;
		int charIndex = 0;
		while (true) 
		{
			int charComp = ((String)key.get(charIndex)).compareTo(currentNode.splitchar);
			if (charComp == 0) 
			{
				charIndex++;
				if (charIndex == key.size()) 
				{
					return currentNode;
				}
				if (currentNode.relatives[TSTNode.EQKID] == null) 
				{
					currentNode.relatives[TSTNode.EQKID] =
						new TSTNode((String)(key.get(charIndex)), currentNode);
				}
				currentNode = currentNode.relatives[TSTNode.EQKID];
			} 
			else if (charComp < 0) 
			{
				if (currentNode.relatives[TSTNode.LOKID] == null) 
				{
					currentNode.relatives[TSTNode.LOKID] =
						new TSTNode((String)(key.get(charIndex)), currentNode);
				}
				currentNode = currentNode.relatives[TSTNode.LOKID];
			} 
			else 
			{
				if (currentNode.relatives[TSTNode.HIKID] == null) 
				{
					currentNode.relatives[TSTNode.HIKID] =
						new TSTNode((String)(key.get(charIndex)), currentNode);
				}
				currentNode = currentNode.relatives[TSTNode.HIKID];
			}
		}
	}

	/**
	*  Returns the number of nodes in the trie that have non-null data.
	*
	*@return    The number of nodes in the trie that have non-null data.
	*/
	public int numDataNodes() 
	{
		return numDataNodes(rootNode);
	}

	/**
	*  Returns the number of nodes in the subtrie below and including the
	*  starting node. The method counts only nodes that have non-null data.
	*
	*@param  startingNode  The top node of the subtrie. the node that defines the subtrie.
	*@return               The total number of nodes in the subtrie.
	*/
	protected int numDataNodes(TSTNode startingNode) 
	{
		return recursiveNodeCalculator(startingNode, true, 0);
	}

	/**
	*  Returns the total number of nodes in the trie. The method counts nodes whether
	*  or not they have data.
	*
	*@return    The total number of nodes in the trie.
	*/
	public int numNodes() 
	{
		return numNodes(rootNode);
	}

	/**
	*  Returns the total number of nodes in the subtrie below and including the 
	*  starting Node. The method counts nodes whether or not they have data.
	*
	*@param  startingNode  The top node of the subtrie. The node that defines the subtrie.
	*@return               The total number of nodes in the subtrie.
	*/
	protected int numNodes(TSTNode startingNode) 
	{
		return recursiveNodeCalculator(startingNode, false, 0);
	}

	/**
	*  Recursivelly visists each node to calculate the number of nodes.
	*
	*@param  currentNode  The current node.
	*@param  checkData    If true we check the data to be different of <code>null</code>.
	*@param  numNodes2    The number of nodes so far.
	*@return              The number of nodes accounted.
	*/
	private int recursiveNodeCalculator(
		TSTNode currentNode,
		boolean checkData,
		int numNodes2) 
	{
		if (currentNode == null) 
		{
			return numNodes2;
		}
		int numNodes =
			recursiveNodeCalculator(
			currentNode.relatives[TSTNode.LOKID],
			checkData,
			numNodes2);
		numNodes =
			recursiveNodeCalculator(
			currentNode.relatives[TSTNode.EQKID],
			checkData,
			numNodes);
		numNodes =
			recursiveNodeCalculator(
			currentNode.relatives[TSTNode.HIKID],
			checkData,
			numNodes);
		if (checkData) 
		{
			if (currentNode.data != -1) 
			{
				numNodes++;
			}
		} 
		else 
		{
			numNodes++;
		}
		return numNodes;
	}

	/**
	*  Removes the value indexed by key. Also removes all nodes that are rendered
	*  unnecessary by the removal of this data.
	*
	*@param  key  A <code>string</code> that indexes the object to be removed from the Trie.
	*/
	public boolean remove(ArrayList key) 
	{
		return deleteNode(getNode(key,0,key.size()));
	}

	private boolean sortKeyRecursion(TSTNode currentNode,boolean sortKeyResult2) 
	{
		//1
		if (currentNode == null) 
		{
			return sortKeyResult2;
		}
		//System.out.println("the split char"+currentNode.splitchar);
	
		//2
		boolean sortKeyResult =
			sortKeyRecursion(
			currentNode.relatives[TSTNode.LOKID],sortKeyResult2);

		//3
		if (sortKeyResult) 
		{
			return sortKeyResult;
		}
		//4
		//System.out.println("is current node is empty");
		if (currentNode.data >0) 
		{
			return true;
		}
		//5
		//System.out.println("to find at high key");
		sortKeyResult =
			sortKeyRecursion(
			currentNode.relatives[TSTNode.EQKID],
			sortKeyResult);
		return sortKeyRecursion(
			currentNode.relatives[TSTNode.HIKID],
			sortKeyResult);
	}
}
