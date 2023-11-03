package com.lietu.rtf;

import java.util.ArrayList;

public interface IRtfGroup extends IRtfElement
{

		// ----------------------------------------------------------------------
		public ArrayList<IRtfElement> getContents();

		// ----------------------------------------------------------------------
		/// <summary>
		/// Returns the name of the first element if it is a tag, null otherwise.
		/// </summary>
		String getDestination();

		// ----------------------------------------------------------------------
		/// <summary>
		/// Determines whether the first element is a '\*' tag.
		/// </summary>
		boolean getIsExtensionDestination();

		// ----------------------------------------------------------------------
		/// <summary>
		/// Searches for the first child group which has a tag with the given name
		/// as its first child, e.g. the given destination.
		/// </summary>
		/// <param name="destination">the name of the start tag of the group to search</param>
		/// <returns>the first matching group or null if nothing found</returns>
		/// <exception cref="ArgumentNullException">in case of a null argument</exception>
		IRtfGroup SelectChildGroupWithDestination( String destination ) throws Exception;

} // interface IRtfGroup
