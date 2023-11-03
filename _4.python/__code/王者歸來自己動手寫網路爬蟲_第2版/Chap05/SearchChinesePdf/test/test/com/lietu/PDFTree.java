/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package test.com.lietu;

/**
 * A tree model that uses a cos document.
 *
 *
 * @author  wurtz
 * @author <a href="mailto:ben@benlitchfield.com">Ben Litchfield</a>
 * @version $Revision: 1.9 $
 */

//import java.awt.event.*;
import org.apache.pdfbox.cos.COSArray;
import org.apache.pdfbox.cos.COSBase;
import org.apache.pdfbox.cos.COSDictionary;
import org.apache.pdfbox.cos.COSDocument;
import org.apache.pdfbox.cos.COSName;
import org.apache.pdfbox.cos.COSObject;
import org.apache.pdfbox.exceptions.InvalidPasswordException;

import org.apache.pdfbox.pdfviewer.ArrayEntry;
import org.apache.pdfbox.pdfviewer.MapEntry;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.pdmodel.PDPage;

import java.util.Collections;
import java.util.List;

/**
 * A class to model a PDF document as a tree structure.
 * 
 * @author <a href="mailto:ben@benlitchfield.com">Ben Litchfield</a>
 * @version $Revision: 1.9 $
 */
public class PDFTree {
	private PDDocument document;

	/**
	 * constructor.
	 */
	public PDFTree() {
		// default constructor
	}

	/**
	 * Constructor to take a document.
	 * 
	 * @param doc
	 *            The document to display in the tree.
	 */
	public PDFTree(PDDocument doc) {
		setDocument(doc);
	}

	/**
	 * Set the document to display in the tree.
	 * 
	 * @param doc
	 *            The document to display in the tree.
	 */
	public void setDocument(PDDocument doc) {
		document = doc;
	}

	/**
	 * Returns the child of <code>parent</code> at index <code>index</code> in
	 * the parent's child array. <code>parent</code> must be a node previously
	 * obtained from this data source. This should not return <code>null</code>
	 * if <code>index</code> is a valid index for <code>parent</code> (that is
	 * <code>index >= 0 &&
	 * index < getChildCount(parent</code>)).
	 * 
	 * @param parent
	 *            a node in the tree, obtained from this data source
	 * @param index
	 *            The index into the parent object to location the child object.
	 * @return the child of <code>parent</code> at index <code>index</code>
	 * 
	 */
	public Object getChild(Object parent, int index) {
		Object retval = null;
		if (parent instanceof COSArray) {
			ArrayEntry entry = new ArrayEntry();
			entry.setIndex(index);
			entry.setValue(((COSArray) parent).getObject(index));
			retval = entry;
		} else if (parent instanceof COSDictionary) {
			COSDictionary dict = ((COSDictionary) parent);
			List keys = dict.keyList();
			//Collections.sort(keys);
			Object key = keys.get(index);
			Object value = dict.getDictionaryObject((COSName) key);
			MapEntry entry = new MapEntry();
			entry.setKey(key);
			entry.setValue(value);
			retval = entry;
		} else if (parent instanceof MapEntry) {
			retval = getChild(((MapEntry) parent).getValue(), index);
		} else if (parent instanceof ArrayEntry) {
			retval = getChild(((ArrayEntry) parent).getValue(), index);
		} else if (parent instanceof COSDocument) {
			retval = ((COSDocument) parent).getObjects().get(index);
		} else if (parent instanceof COSObject) {
			retval = ((COSObject) parent).getObject();
		} else {
			throw new RuntimeException("Unknown COS type "
					+ parent.getClass().getName());
		}
		return retval;
	}

	/**
	 * Returns the number of children of <code>parent</code>. Returns 0 if the
	 * node is a leaf or if it has no children. <code>parent</code> must be a
	 * node previously obtained from this data source.
	 * 
	 * @param parent
	 *            a node in the tree, obtained from this data source
	 * @return the number of children of the node <code>parent</code>
	 * 
	 */
	public int getChildCount(Object parent) {
		int retval = 0;
		if (parent instanceof COSArray) {
			retval = ((COSArray) parent).size();
		} else if (parent instanceof COSDictionary) {
			retval = ((COSDictionary) parent).size();
		} else if (parent instanceof MapEntry) {
			retval = getChildCount(((MapEntry) parent).getValue());
		} else if (parent instanceof ArrayEntry) {
			retval = getChildCount(((ArrayEntry) parent).getValue());
		} else if (parent instanceof COSDocument) {
			retval = ((COSDocument) parent).getObjects().size();
		} else if (parent instanceof COSObject) {
			retval = 1;
		}
		return retval;
	}

	/**
	 * Returns the index of child in parent. If <code>parent</code> is
	 * <code>null</code> or <code>child</code> is <code>null</code>, returns -1.
	 * 
	 * @param parent
	 *            a note in the tree, obtained from this data source
	 * @param child
	 *            the node we are interested in
	 * @return the index of the child in the parent, or -1 if either
	 *         <code>child</code> or <code>parent</code> are <code>null</code>
	 * 
	 */
	public int getIndexOfChild(Object parent, Object child) {
		int retval = -1;
		if (parent != null && child != null) {
			if (parent instanceof COSArray) {
				COSArray array = (COSArray) parent;
				if (child instanceof ArrayEntry) {
					ArrayEntry arrayEntry = (ArrayEntry) child;
					retval = arrayEntry.getIndex();
				} else {
					retval = array.indexOf((COSBase) child);
				}
			} else if (parent instanceof COSDictionary) {
				MapEntry entry = (MapEntry) child;
				COSDictionary dict = (COSDictionary) parent;
				List keys = dict.keyList();
				Collections.sort(keys);
				for (int i = 0; retval == -1 && i < keys.size(); i++) {
					if (keys.get(i).equals(entry.getKey())) {
						retval = i;
					}
				}
			} else if (parent instanceof MapEntry) {
				retval = getIndexOfChild(((MapEntry) parent).getValue(), child);
			} else if (parent instanceof ArrayEntry) {
				retval = getIndexOfChild(((ArrayEntry) parent).getValue(),
						child);
			} else if (parent instanceof COSDocument) {
				retval = ((COSDocument) parent).getObjects().indexOf(child);
			} else if (parent instanceof COSObject) {
				retval = 0;
			} else {
				throw new RuntimeException("Unknown COS type "
						+ parent.getClass().getName());
			}
		}
		return retval;
	}

	/**
	 * Returns the root of the tree. Returns <code>null</code> only if the tree
	 * has no nodes.
	 * 
	 * @return the root of the tree
	 * 
	 */
	public Object getRoot() {
		return document.getDocument().getTrailer();
	}

	/**
	 * Returns <code>true</code> if <code>node</code> is a leaf. It is possible
	 * for this method to return <code>false</code> even if <code>node</code>
	 * has no children. A directory in a filesystem, for example, may contain no
	 * files; the node representing the directory is not a leaf, but it also has
	 * no children.
	 * 
	 * @param node
	 *            a node in the tree, obtained from this data source
	 * @return true if <code>node</code> is a leaf
	 * 
	 */
	public boolean isLeaf(Object node) {
		boolean isLeaf = !(node instanceof COSDictionary
				|| node instanceof COSArray
				|| node instanceof COSDocument
				|| node instanceof COSObject
				|| (node instanceof MapEntry && !isLeaf(((MapEntry) node)
						.getValue())) || (node instanceof ArrayEntry && !isLeaf(((ArrayEntry) node)
				.getValue())));
		return isLeaf;
	}

	/**
	 * This will print the documents data.
	 * 
	 * @param args
	 *            The command line arguments.
	 * 
	 * @throws Exception
	 *             If there is an error parsing the document.
	 */
	public static void main(String[] args) throws Exception {
		String pdfFile = // "D:/lg/work/hblocaltax/D751503Dd01.pdf";
		// "D:/lg/work/hblocaltax/n11261961.pdf";
		// "D:/lg/work/hblocaltax/468456C0d01.pdf";
		// "D:/lg/work/hblocaltax/217712CEd01.pdf";
		 "D:/a.pdf";
		//"D:/lg/work/hblocaltax/7D19A80Ed01.pdf";

		// "D:/lg/work/hblocaltax/DB182628d01.pdf";

		// "D:/lg/work/hblocaltax/9BA17857d01.pdf";
		// "D:/lg/work/hblocaltax/9364DA0Dd01.pdf";
		// "D:/lg/work/hblocaltax/C8674AACd01.pdf";
		// "D:/lg/work/hblocaltax/D751503Dd01.pdf";
		args = new String[] { pdfFile };
		if (args.length != 1) {
			// usage();
		} else {
			PDDocument document = null;
			try {
				document = PDDocument.load(args[0]);
				if (document.isEncrypted()) {
					try {
						document.decrypt("");
					} catch (InvalidPasswordException e) {
						System.err
								.println("Error: Document is encrypted with a password.");
						System.exit(1);
					}
				}

				PDFTree pdfTree = new PDFTree(document);
				Object root = pdfTree.getRoot();
				pdfTree.print(root,"");
				/*int childCount = pdfTree.getChildCount(root);

				for (int i = 0; i < childCount; ++i) {
					System.out.println(pdfTree.getChild(root, i));
				}*/
			} finally {
				if (document != null) {
					document.close();
				}
			}
		}
	}

	public void print(Object parent, String indent) {
		
		if (parent == null) {
			return;
		}

		//System.out.print(indent);
		//System.out.println(parent);

		if(isLeaf(parent))
		{
			return;
		}
		int childCount = getChildCount(parent);

		for (int i = 0; i < childCount; ++i) {
			print(getChild(parent, i), indent+" ");
		}
	}
}
