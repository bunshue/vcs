package com.lietu.rtf.interpreter;

import java.util.Hashtable;

import com.lietu.rtf.IRtfFont;
import com.lietu.rtf.IRtfGroup;
import com.lietu.rtf.RtfElementKind;
import com.lietu.rtf.RtfElementVisitorOrder;
import com.lietu.rtf.RtfSpec;
import com.lietu.rtf.support.RtfElementVisitorBase;

public final class RtfFontTableBuilder extends RtfElementVisitorBase {

	// ----------------------------------------------------------------------
	public RtfFontTableBuilder(Hashtable<String, IRtfFont> hashtable)
			throws Exception {
		super(RtfElementVisitorOrder.NonRecursive);
		// we iterate over our children ourselves -> hence non-recursive
		if (hashtable == null) {
			throw new Exception("fontTable");
		}
		this.fontTable = hashtable;
	} // RtfFontTableBuilder

	// ----------------------------------------------------------------------
	public void Reset() {
		this.fontTable.clear();
	} // Reset

	// ----------------------------------------------------------------------
	protected void DoVisitGroup(IRtfGroup group) throws Exception {
		if (RtfSpec.TagFont.equals(group.getDestination())) {
			BuildFontFromGroup(group);
		} else if (RtfSpec.TagFontTable.equals(group.getDestination())) {
			if (group.getContents().size() > 1) {
				if (group.getContents().get(1).getKind() == RtfElementKind.Group) {
					// the 'new' style where each font resides in a group of its
					// own
					VisitGroupChildren(group);
				} else {
					// the 'old' style where individual fonts are 'terminated'
					// by their
					// respective name content text (which ends with ';')
					// -> need to manually iterate from here
					int childCount = group.getContents().size();
					this.fontBuilder.Reset();
					for (int i = 1; i < childCount; i++) // skip over the
															// initial \fonttbl
															// tag
					{
						group.getContents().get(i).Visit(this.fontBuilder);
						if (this.fontBuilder.getFontName() != null) {
							// fonts are 'terminated' by their name (as content
							// text)
							AddCurrentFont();
							this.fontBuilder.Reset();
						}
					}
					// BuildFontFromGroup( group ); // a single font info
				}
			}
		}
	} // DoVisitGroup

	// ----------------------------------------------------------------------
	private void BuildFontFromGroup(IRtfGroup group) throws Exception {
		this.fontBuilder.Reset();
		this.fontBuilder.VisitGroup(group);
		AddCurrentFont();
	} // BuildFontFromGroup

	// ----------------------------------------------------------------------
	private void AddCurrentFont() throws Exception {
		// if(this.fontBuilder==null)
		// System.out.println("this.fontBuilder.getFontId()"+this.fontBuilder.
		// getFontId());
		if (!this.fontTable.contains(this.fontBuilder.getFontId())) {
			this.fontTable.put(this.fontBuilder.getFontId(), fontBuilder
					.CreateFont());
		} else {
			throw new Exception("duplicate font id '"
					+ this.fontBuilder.getFontId() + "'");
		}
	} // AddCurrentFont

	// ----------------------------------------------------------------------
	// members
	private RtfFontBuilder fontBuilder = new RtfFontBuilder();
	private Hashtable<String, IRtfFont> fontTable;

} // class RtfFontBuilder
