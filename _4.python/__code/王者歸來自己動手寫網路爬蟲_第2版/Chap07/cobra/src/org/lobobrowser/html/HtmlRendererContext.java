/*
    GNU LESSER GENERAL PUBLIC LICENSE
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
 * Created on Aug 28, 2005
 */
package org.lobobrowser.html;

import java.net.URL;
import org.w3c.dom.html2.*;

/**
 * The <code>HtmlRendererContext</code> interface must be implemented 
 * in order to use the Cobra HTML renderer. In many ways this
 * interface parallers the Javascript <code>Window</code> class, which
 * in reality represents a browser frame, not a window.
 * @author J. H. S.
 */
public interface HtmlRendererContext {	
	/**
	 * Navigates to the location given. Implementations should
	 * retrieve the URL content, parse it and render it.
	 * @param url The destination URL.
	 * @param target Same as the target attribute in the HTML anchor tag, i.e. _top, _blank, etc.
	 */	
	public void navigate(URL url, String target);

	/**
	 * Performs a link click. Implementations should
	 * invoke {@link #navigate(URL, String)}.
	 * @param linkNode The HTML node that was clicked.
	 * @param url The destination URL.
	 * @param target Same as the target attribute in the HTML anchor tag, i.e. _top, _blank, etc.
	 */		
	public void linkClicked(org.w3c.dom.html2.HTMLElement linkNode, URL url, String target);
	
	/**
	 * Gets a collection of frames from the document
	 * currently in the context.
	 */
	public HTMLCollection getFrames();
	
	/**
	 * Submits a HTML form. Note that when the the method is "GET", parameters
	 * are still expected to be part of <code>formInputs</code>.
	 * @param method The request method, GET or POST.
	 * @param action The destination URL.
	 * @param target Same as the target attribute in the FORM tag, i.e. _blank, _top, etc.
	 * @param enctype The encoding type.
	 * @param formInputs An array of {@link org.lobobrowser.html.FormInput} instances.
	 */
	public void submitForm(String method, URL action, String target, String enctype, FormInput[] formInputs);

	/**
	 * Creates a {@link org.lobobrowser.html.BrowserFrame} instance.
	 */
	public BrowserFrame createBrowserFrame();
	
//	/**
//	 * Gets the parser context associated with this
//	 * renderer context.
//	 */
//	public HtmlParserContext getHtmlParserContext();
	
	/**
	 * Gets the browser context.
	 */
	public UserAgentContext getUserAgentContext();
	
	/**
	 * Gets a <code>HtmlObject</code> instance that implements
	 * a OBJECT tag from HTML. 
	 * @param element The DOM element for the object, which may
	 *                either represent an OBJECT, EMBED or an APPLET tag.
	 * @return Implementations of this method must return <code>null</code>
	 * if they have any problems producing a <code>HtmlObject</code> instance.
	 * This is particularly true of OBJECT tags, where inner HTML of
	 * the tag must be rendered if the OBJECT content cannot be handled.
	 */
	public HtmlObject getHtmlObject(org.w3c.dom.html2.HTMLElement element);

	/**
	 * This method is called when a visual element is right-clicked.
	 * @param element The narrowest element enclosing the mouse location.
	 * @param event The mouse event.
	 */
	public void onContextMenu(org.w3c.dom.html2.HTMLElement element, java.awt.event.MouseEvent event);

	/**
	 * This method is called when the mouse first hovers over an element.
	 * @param element The element that the mouse has just entered.
	 * @param event The mouse event.
	 */
	public void onMouseOver(org.w3c.dom.html2.HTMLElement element, java.awt.event.MouseEvent event);

	/**
	 * This method is called when the mouse no longer hovers a given element.
	 * @param element The element that the mouse has just exited.
	 * @param event The mouse event.
	 */
	public void onMouseOut(org.w3c.dom.html2.HTMLElement element, java.awt.event.MouseEvent event);

	//------ Methods useful for Window implementation:
	
	/**
	 * Opens an alert dialog.
	 * @param message Message shown by the dialog.
	 */
	public void alert(String message);
	
	/**
	 * Goes to the previous page in the browser's history. 
	 */
	public void back();
	
	/**
	 * Relinquishes focus.
	 */
	public void blur();
	
	/**
	 * Closes the browser window, provided this
	 * is allowed for the current context.
	 */
	public void close();

	/**
	 * Opens a confirmation dialog.
	 * @param message The message shown by the confirmation dialog.
	 * @return True if the user selects YES. 
	 */
	public boolean confirm(String message);

	/**
	 * Requests focus for the current window.
	 */
	public void focus();
	
	/**
	 * Opens a separate browser window and renders a URL. 
	 * @param absoluteUrl The URL to be rendered.
	 * @param windowName The name of the new window.
	 * @param windowFeatures The features of the new window (same as in Javascript open method). 
	 * @param replace 
	 * @return A new {@link org.lobobrowser.html.HtmlRendererContext} instance.
	 * @deprecated Use {@link #open(URL, String, String, boolean)} instead.
	 */
	public HtmlRendererContext open(String absoluteUrl, String windowName, String windowFeatures, boolean replace);
	
	/**
	 * Opens a separate browser window and renders a URL. 
	 * @param url The URL to be rendered.
	 * @param windowName The name of the new window.
	 * @param windowFeatures The features of the new window (same as in Javascript open method). 
	 * @param replace 
	 * @return A new {@link org.lobobrowser.html.HtmlRendererContext} instance.
	 */
	public HtmlRendererContext open(java.net.URL url, String windowName, String windowFeatures, boolean replace);

	/**
	 * Shows a prompt dialog.
	 * @param message The message shown by the dialog.
	 * @param inputDefault The default input value.
	 * @return The user's input value.
	 */
	public String prompt(String message, String inputDefault);
	
	/**
	 * Scrolls the client area.
	 * @param x Document's x coordinate.
	 * @param y Document's y coordinate.
	 */
	public void scroll(int x, int y);
	
	/**
	 * Gets a value indicating if the window is closed.
	 */
	public boolean isClosed();
	
	public String getDefaultStatus();	
	public void setDefaultStatus(String value);
		
	/**
	 * Gets the window name.
	 */
	public String getName();
	
	/**
	 * Gets the parent of the window in the current context.
	 */
	public HtmlRendererContext getParent();
	
	/**
	 * Gets the opener of the window in the current context.
	 */
	public HtmlRendererContext getOpener();
	
	/**
	 * Sets the context that opened the window of the current one.
	 * @param opener A {@link org.lobobrowser.html.HtmlRendererContext}. 
	 */
	public void setOpener(HtmlRendererContext opener);
	
	/**
	 * Gets the window status text.
	 */
	public String getStatus();
	
	/**
	 * Sets the window status text.
	 * @param message A string.
	 */
	public void setStatus(String message);
	
	/**
	 * Gets the top-most browser window.
	 */
	public HtmlRendererContext getTop();

	/**
	 * It should return true if the link provided has been visited.
	 */
	public boolean isVisitedLink(HTMLLinkElement link);
	
//	/**
//	 * Returns true if the current media matches the name provided.
//	 * @param mediaName Media name, which
//	 * may be screen, tty, etc. (See <a href="http://www.w3.org/TR/REC-html40/types.html#type-media-descriptors">HTML Specification</a>).
//	 */
//	public boolean isMedia(String mediaName);
	
	/**
	 * Reloads the current document.
	 */
	public void reload();
}
