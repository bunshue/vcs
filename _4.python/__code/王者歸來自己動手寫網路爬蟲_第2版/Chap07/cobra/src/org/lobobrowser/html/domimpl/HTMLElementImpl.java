/*    GNU LESSER GENERAL PUBLIC LICENSE
    Copyright (C) 2006 The Lobo Project

    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this library; if not, write to the Free Software
    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

    Contact info: xamjadmin@users.sourceforge.net
*/
/*
 * Created on Sep 3, 2005
 */
package org.lobobrowser.html.domimpl;

import org.lobobrowser.html.FormInput;
import org.lobobrowser.html.parser.HtmlParser;
import org.lobobrowser.html.style.*;
import org.lobobrowser.util.*;
import org.w3c.css.sac.InputSource;
import org.w3c.dom.*;
import org.w3c.dom.css.CSSStyleDeclaration;
import org.w3c.dom.html2.*;
import com.steadystate.css.parser.CSSOMParser;

import java.io.*;
import java.util.*;
import java.util.logging.*;

public class HTMLElementImpl extends ElementImpl implements HTMLElement, CSS2PropertiesContext {	
	private final boolean noStyleSheet;
	
	public HTMLElementImpl(String name, boolean noStyleSheet) {
		super(name);
		this.noStyleSheet = noStyleSheet;
	}
	
	public HTMLElementImpl(String name) {
		super(name);
		this.noStyleSheet = false;
	}
	
	private volatile CSS2PropertiesImpl currentStyleDeclarationState;	
	private volatile CSS2PropertiesImpl localStyleDeclarationState;	

	protected final void forgetLocalStyle() {
		synchronized(this) {
			this.currentStyleDeclarationState = null;
			this.localStyleDeclarationState = null;
		}
	}

	protected final void forgetStyle(boolean deep) {
		//TODO: Maybe this should redo style declarations in
		//CSS, not the whole properties object?
		synchronized(this) {
			this.currentStyleDeclarationState = null;
			this.isHoverStyle = null;
			if(deep) {
				java.util.ArrayList nl = this.nodeList;
				if(nl != null) {
					Iterator i = nl.iterator();
					while(i.hasNext()) {
						Object node = i.next();
						if(node instanceof HTMLElementImpl) {
							((HTMLElementImpl) node).forgetStyle(deep);
						}				
					}
				}
			}
		}
	}

	/**
	 * Gets the style object associated with the element.
	 * It may return null only if the type of element does not handle stylesheets.
	 */
	public CSS2PropertiesImpl getCurrentStyle() {
		CSS2PropertiesImpl sds;
		synchronized(this) {
			sds = this.currentStyleDeclarationState;
			if(sds != null) {
				return sds;
			}
		}
		// Can't do the following in synchronized block (reverse locking order with document).
		// First, add declarations from stylesheet
		sds = this.addStyleSheetDeclarations(sds);
		// Now add local style if any.
		CSS2PropertiesImpl localStyle = this.getStyle();
		if(sds == null) {
			sds = new CSS2PropertiesImpl(this);
			sds.setLocalStyleProperties(localStyle);
		}
		else {
			sds.setLocalStyleProperties(localStyle);
		}		
		synchronized(this) {
			// Check if style properties were set while outside
			// the synchronized block (can happen).
			CSS2PropertiesImpl setProps = this.currentStyleDeclarationState;
			if(setProps != null) {
				return setProps;
			}
			this.currentStyleDeclarationState = sds;
			return sds;
		}
	}
	
//	/**
//	 * This method may return <code>null</code> if
//	 * there's no style declaration applicable to
//	 * the element.
//	 */
//	public CSS2PropertiesImpl getCurrentStyle() {
//		if(this.noStyleSheet) {
//			return null;
//		}
//		synchronized(this) {
//			Object sdsObj = this.styleDeclarationNoCreate;
//			if(sdsObj == INVALID_CSS) {
//				CSS2PropertiesImpl sdsOrig = this.styleDeclarationState;
//				if(sdsOrig != null) {
//					this.styleDeclarationNoCreate = sdsOrig;
//					return sdsOrig;
//				}
//			}
//			else {
//				return (CSS2PropertiesImpl) sdsObj;
//			}
//		}
//		// Cannot run the following in synchronized block (reverse lock order with document).
//		// First, add declarations from stylesheet
//		CSS2PropertiesImpl sds = this.addStyleSheetDeclarations(null);
//		// Now add local style if any
//		CSS2PropertiesImpl localStyle = this.getStyleNoCreate();
//		if(localStyle != null) {
//			if(sds == null) {
//				sds = new CSS2PropertiesImpl(this);
//			}
//			sds.setLocalStyleProperties(localStyle);
//		}
//		synchronized(this) {
//			this.styleDeclarationNoCreate = sds;
//		}
//		return sds;
//	}

	/**
	 * Gets the local style object associated with the element. The properties
	 * object returned only includes properties from the local style attribute.
	 * It may return null only if the type of element does not handle stylesheets.
	 */
	public CSS2PropertiesImpl getStyle() {
		CSS2PropertiesImpl sds;
		synchronized(this) {
			sds = this.localStyleDeclarationState;
			if(sds != null) {
				return sds;
			}
			sds = new CSS2PropertiesImpl(this);
			// Add any declarations in style attribute (last takes precedence).
			String style = this.getAttribute("style");
			if(style != null && style.length() != 0) {
				CSSOMParser parser = new CSSOMParser();
				InputSource inputSource = this.getCssInputSourceForDecl(style);
				try {
					CSSStyleDeclaration sd = parser.parseStyleDeclaration(inputSource);	
					sds.addStyleDeclaration(sd);
				} catch(Exception err) {
					String id = this.getId();
					String withId = id == null ? "" : " with ID '" + id + "'"; 
					this.warn("Unable to parse style attribute value for element " + this.getTagName() + withId + ".", err);
				}
			}
			this.localStyleDeclarationState = sds;
		}
		// Synchronization note: Make sure getStyle() does not return multiple values.
		return sds;
	}
	
//	/**
//	 * This method may return <code>null</code> if
//	 * there's no style declaration applicable to
//	 * the element.
//	 */
//	public CSS2PropertiesImpl getStyleNoCreate() {
//		if(this.noStyleSheet) {
//			return null;
//		}
//		synchronized(this) {
//			Object sdsObj = this.localStyleDeclarationNoCreate;
//			if(sdsObj == INVALID_CSS) {
//				CSS2PropertiesImpl sdsOrig = this.localStyleDeclarationState;
//				if(sdsOrig != null) {
//					this.localStyleDeclarationNoCreate = sdsOrig;
//					return sdsOrig;
//				}
//				// Otherwise, fall through.
//			}
//			else {
//				return (CSS2PropertiesImpl) sdsObj;
//			}
//		}
//		// Then add any declarations in style attribute (last takes precedence).
//		CSS2PropertiesImpl sds = null;
//		String style = this.getAttribute("style");
//		if(style != null && style.length() != 0) {
//			CSSOMParser parser = new CSSOMParser();
//			InputSource inputSource = this.getCssInputSourceForDecl(style);
//			try {
//				CSSStyleDeclaration sd = parser.parseStyleDeclaration(inputSource);	
//				if(sds == null) {
//					sds = new CSS2PropertiesImpl(this);
//				}
//				sds.addStyleDeclaration(sd);
//			} catch(Exception err) {
//				String id = this.getId();
//				String withId = id == null ? "" : " with ID '" + id + "'"; 
//				this.warn("Unable to parse style attribute value for element " + this.getTagName() + withId + ".", err);
//			}
//		}
//		synchronized(this) {
//			this.localStyleDeclarationNoCreate = sds;
//			if(sds != null) {
//				Object gsp = this.styleDeclarationNoCreate;
//				if(gsp == null && sds != null) {
//					this.styleDeclarationNoCreate = INVALID_CSS;
//					this.styleDeclarationState = null;
//				}
//				else if(gsp != INVALID_CSS) {
//					((CSS2PropertiesImpl) gsp).setLocalStyleProperties(sds);
//				}
//			}
//		}
//		return sds;
//	}

	public void setStyle(Object value) {
		throw new DOMException(DOMException.NOT_SUPPORTED_ERR, "Cannot set style property");
	}	
	
	public void setCurrentStyle(Object value) {
		throw new DOMException(DOMException.NOT_SUPPORTED_ERR, "Cannot set currentStyle property");
	}	

	public String getClassName() {
		String className = this.getAttribute("class");
		// Blank required instead of null.
		return className == null ? "" : className;
	}
	
	public void setClassName(String className) {
		this.setAttribute("class", className);
	}
	
	public String getCharset() {
		return this.getAttribute("charset");
	}

	public void setCharset(String charset) {
		this.setAttribute("charset", charset);
	}

	public void warn(String message, Throwable err) {
		logger.log(Level.WARNING, message, err);
	}

	public void warn(String message) {
		logger.log(Level.WARNING, message);
	}

	protected int getAttributeAsInt(String name, int defaultValue) {
		String value = this.getAttribute(name);
		try {
			return Integer.parseInt(value);
		} catch(Exception err) {
			this.warn("Bad integer", err);
			return defaultValue;
		}
	}
	
	public boolean getAttributeAsBoolean(String name) {
		String value = this.getAttribute(name);
		return name.equalsIgnoreCase(value);
	}
	
	protected void assignAttributeField(String normalName, String value) {
		if(!this.notificationsSuspended) {
			this.informInvalidAttibute(normalName);
		}
		else {
			if("style".equals(normalName)) {
				this.forgetLocalStyle();
			}			
		}
		super.assignAttributeField(normalName, value);
	}
	
	protected final InputSource getCssInputSourceForDecl(String text) {
		java.io.Reader reader = new StringReader("{" + text + "}");
		InputSource is = new InputSource(reader);
		return is;
	}
	
/**
 * Adds style sheet declarations applicable
 * to this element.
 * A properties object is created if necessary
 * when the one passed is <code>null</code>.
 * @param style
 */	
	protected final CSS2PropertiesImpl addStyleSheetDeclarations(CSS2PropertiesImpl style) {
		Node pn = this.parentNode;
		if(pn == null) {
			// do later
			return style;
		}
		String classNames = this.getClassName();
		if(classNames != null && classNames.length() != 0) {
			String id = this.getId();
			String elementName = this.getTagName();
			String[] classNameArray = Strings.split(classNames);
			for(int i = classNameArray.length; --i >= 0;) {
				String className = classNameArray[i];
				Collection sds = this.findStyleDeclarations(elementName, id, className);
				if(sds != null) {
					Iterator sdsi = sds.iterator();
					while(sdsi.hasNext()) {
						CSSStyleDeclaration sd = (CSSStyleDeclaration) sdsi.next();
						if(style == null) {
							style = new CSS2PropertiesImpl(this);
						}
						style.addStyleDeclaration(sd);
					}
				}					
			}
		}
		else {
			String id = this.getId();
			String elementName = this.getTagName();
			Collection sds = this.findStyleDeclarations(elementName, id, null);
			if(sds != null) {
				Iterator sdsi = sds.iterator();
				while(sdsi.hasNext()) {
					CSSStyleDeclaration sd = (CSSStyleDeclaration) sdsi.next();
					if(style == null) {
						style = new CSS2PropertiesImpl(this);
					}
					style.addStyleDeclaration(sd);
				}
			}					
		}
		return style;
	}

	private boolean isMouseOver = false;
	
	public void setMouseOver(boolean mouseOver) {
		boolean prevMouseOver = this.isMouseOver;
		this.isMouseOver = mouseOver;
		if(this.hasHoverStyle() && prevMouseOver != mouseOver) {
			this.informInvalid();
		}
	}

	private Boolean isHoverStyle = null;
	
	private boolean hasHoverStyle() {
		Boolean ihs;
		synchronized(this) {
			ihs = this.isHoverStyle;
			if(ihs != null) {
				return ihs.booleanValue();
			}
		}
		HTMLDocumentImpl doc = (HTMLDocumentImpl) this.document;
		if(doc == null) {
			ihs = Boolean.FALSE;
		}
		else {
			StyleSheetAggregator ssa = doc.getStyleSheetAggregator();
			String id = this.getId();
			String elementName = this.getTagName();
			String classNames = this.getClassName();
			String[] classNameArray = null;
			if(classNames != null && classNames.length() != 0) {
				classNameArray = Strings.split(classNames);
			}
			ihs = Boolean.valueOf(ssa.hasPseudoName(this, elementName, id, classNameArray, "hover"));
		}
		synchronized(this) {
			this.isHoverStyle = ihs;
		}
		return ihs.booleanValue();
	}

	private Set getPseudoNames() {
		Set pnset = null;
		if(this.isMouseOver) {
			if(pnset == null) {
				pnset = new HashSet(1);
			}
			pnset.add("hover");
		}
		return pnset;
	}
	
	protected final Collection findStyleDeclarations(String elementName, String id, String className) {
		HTMLDocumentImpl doc = (HTMLDocumentImpl) this.document;
		if(doc == null) {
			return null;
		}
		StyleSheetAggregator ssa = doc.getStyleSheetAggregator();
		return ssa.getStyleDeclarations(this, elementName, id, className, this.getPseudoNames());
	}
	
	public void informInvalid() {
		// This is called when an attribute or child changes.
		this.forgetStyle(false);
		super.informInvalid();
	}
	
	public void informInvalidAttibute(String normalName) {
		// This is called when an attribute changes while
		// the element is allowing notifications.
		if("style".equals(normalName)) {
			this.forgetLocalStyle();
		}
		else if("id".equals(normalName) || "class".equals(normalName)) {
			this.forgetStyle(false);
		}
		// Call super implementation of informValid().
		super.informInvalid();
	}

	public void informLayoutInvalid() {
		// This is called by the style properties object
		// when certain properties change.
		super.informLayoutInvalid();
	}

	/**
	 * Gets form input due to the current element. It should
	 * return <code>null</code> except when the element is a form input element.
	 */
	protected FormInput[] getFormInputs() {
		// Override in input elements
		return null;
	}
	
	private boolean classMatch(String classTL) {
		String classNames = this.getClassName();
		if(classNames == null || classNames.length() == 0) {
			return classTL == null;
		}
		StringTokenizer tok = new StringTokenizer(classNames, " \t\r\n");
		while(tok.hasMoreTokens()) {
			String token = tok.nextToken();
			if(token.toLowerCase().equals(classTL)) {
				return true;
			}
		}
		return false;
	}
	
	/**
	 * Get an ancestor that matches the element tag name given and the
	 * style class given.
	 * @param elementTL An tag name in lowercase or an asterisk (*).
	 * @param classTL A class name in lowercase.
	 */
	public HTMLElementImpl getAncestorWithClass(String elementTL, String classTL) {
		Object nodeObj = this.getParentNode();
		if(nodeObj instanceof HTMLElementImpl) {
			HTMLElementImpl parentElement = (HTMLElementImpl) nodeObj;
			String pelementTL = parentElement.getTagName().toLowerCase();
			if(("*".equals(elementTL) || elementTL.equals(pelementTL)) && parentElement.classMatch(classTL)) {
				return parentElement;
			}
			return parentElement.getAncestorWithClass(elementTL, classTL);
		}
		else {
			return null;
		}
	}

	public HTMLElementImpl getAncestorWithId(String elementTL, String idTL) {
		Object nodeObj = this.getParentNode();
		if(nodeObj instanceof HTMLElementImpl) {
			HTMLElementImpl parentElement = (HTMLElementImpl) nodeObj;
			String pelementTL = parentElement.getTagName().toLowerCase();
			String pid = parentElement.getId();
			String pidTL = pid == null ? null : pid.toLowerCase();
			if(("*".equals(elementTL) || elementTL.equals(pelementTL)) && idTL.equals(pidTL)) {
				return parentElement;
			}
			return parentElement.getAncestorWithId(elementTL, idTL);
		}
		else {
			return null;
		}
	}

	public HTMLElementImpl getAncestor(String elementTL) {
		Object nodeObj = this.getParentNode();
		if(nodeObj instanceof HTMLElementImpl) {
			HTMLElementImpl parentElement = (HTMLElementImpl) nodeObj;
			if("*".equals(elementTL)) {
				return parentElement;
			}
			String pelementTL = parentElement.getTagName().toLowerCase();
			if(elementTL.equals(pelementTL)) {
				return parentElement;
			}
			return parentElement.getAncestor(elementTL);
		}
		else {
			return null;
		}
	}	
	
	protected Object getAncestorForJavaClass(Class javaClass) {
		Object nodeObj = this.getParentNode();
		if(nodeObj == null || javaClass.isInstance(nodeObj)) {
			return nodeObj;
		}
		else if(nodeObj instanceof HTMLElementImpl) {
			return ((HTMLElementImpl) nodeObj).getAncestorForJavaClass(javaClass);
		}
		else {
			return null;
		}
	}
	
	public void setInnerHTML(String newHtml) {
		HTMLDocumentImpl document = (HTMLDocumentImpl) this.document;
		if(document == null) {
			this.warn("setInnerHTML(): Element " + this + " does not belong to a document.");
			return;
		}
		HtmlParser parser = new HtmlParser(document.getUserAgentContext(), document, null, null, null);
		synchronized(this) {
			ArrayList nl = this.nodeList;
			if (nl != null) {
				nl.clear();
			}
		}
		// Should not synchronize around parser probably.
		try {
			Reader reader = new StringReader(newHtml);
			try {
				parser.parse(reader, this);
			} finally {
				reader.close();
			}
		} catch(Exception thrown) {
			this.warn("setInnerHTML(): Error setting inner HTML.", thrown);
		}
	}

	public String getInnerHTML() {
		StringBuffer buffer = new StringBuffer();
		synchronized(this) {
			this.appendInnerHTMLImpl(buffer);
		}
		return buffer.toString();
	}

	public String getOuterHTML() {
		StringBuffer buffer = new StringBuffer();
		synchronized(this) {
			this.appendOuterHTMLImpl(buffer);
		}
		return buffer.toString();
	}

	protected void appendInnerHTMLImpl(StringBuffer buffer) {
		ArrayList nl = this.nodeList;
		int size;
		if (nl != null && (size = nl.size()) > 0) {
			for (int i = 0; i < size; i++) {
				Node child = (Node) nl.get(i);
				if (child instanceof HTMLElementImpl) {
					((HTMLElementImpl) child).appendOuterHTMLImpl(buffer);
				}
				else if(child instanceof Comment) {
					buffer.append("<!--" + ((Comment) child).getTextContent() + "-->");
				}
				else if (child instanceof Text) {
					String text = ((Text) child).getTextContent();
					String encText = Strings.strictHtmlEncode(text);
					buffer.append(encText);
				}
			}
		}
	}

	protected void appendOuterHTMLImpl(StringBuffer buffer) {
		String tagName = this.getTagName();
		buffer.append('<');
		buffer.append(tagName);
		Map attributes = this.attributes;
		if(attributes != null) {
			Iterator i = attributes.entrySet().iterator();
			while(i.hasNext()) {
				Map.Entry entry = (Map.Entry) i.next();
				String value = (String) entry.getValue();
				if(value != null) {
					buffer.append(' ');
					buffer.append(entry.getKey());
					buffer.append("=\"");
					buffer.append(Strings.strictHtmlEncode(value));
					buffer.append("\"");				
				}
			}
		}
		ArrayList nl = this.nodeList;
		if(nl == null || nl.size() == 0) {
			buffer.append("/>");
			return;
		}
		buffer.append('>');
		this.appendInnerHTMLImpl(buffer);
		buffer.append("</");
		buffer.append(tagName);
		buffer.append('>');
	}	

	protected RenderState createRenderState(RenderState prevRenderState) {
		// Overrides NodeImpl method
		// Called in synchronized block already
		return new StyleSheetRenderState(prevRenderState, this);
	}
	
	public int getOffsetTop() {
		CSS2PropertiesImpl style = this.getCurrentStyle();
		if(style == null) {
			return 0;
		}
		String topText = style.getTop();
		return topText == null ? 0 : HtmlValues.getPixelSize(topText, this.getRenderState(), 0);
	}
	
	public int getOffsetLeft() {
		CSS2PropertiesImpl style = this.getCurrentStyle();
		if(style == null) {
			return 0;
		}
		String leftText = style.getLeft();
		return leftText == null ? 0 : HtmlValues.getPixelSize(leftText, this.getRenderState(), 0);
	}

	public int getOffsetWidth() {
		CSS2PropertiesImpl style = this.getCurrentStyle();
		if(style == null) {
			return 0;
		}
		String valueText = style.getWidth();
		return valueText == null ? 0 : HtmlValues.getPixelSize(valueText, this.getRenderState(), 0);
	}

	public int getOffsetHeight() {
		CSS2PropertiesImpl style = this.getCurrentStyle();
		if(style == null) {
			return 0;
		}
		String valueText = style.getHeight();
		return valueText == null ? 0 : HtmlValues.getPixelSize(valueText, this.getRenderState(), 0);
	}

	public CSS2PropertiesImpl getParentStyle() {
		Object parent = this.parentNode;
		if(parent instanceof HTMLElementImpl) {
			return ((HTMLElementImpl) parent).getCurrentStyle();
		}
		return null;
	}
	
	public String toString() {
		return super.toString() + "[currentStyle=" + this.getCurrentStyle() + "]";
	}
}
