package com.lietu.rtf.interpreter;

import com.lietu.rtf.IRtfFont;
import com.lietu.rtf.IRtfGroup;
import com.lietu.rtf.IRtfTag;
import com.lietu.rtf.IRtfText;
import com.lietu.rtf.RtfElementVisitorOrder;
import com.lietu.rtf.RtfFont;
import com.lietu.rtf.RtfFontKind;
import com.lietu.rtf.RtfFontPitch;
import com.lietu.rtf.RtfSpec;
import com.lietu.rtf.support.RtfElementVisitorBase;

public final class RtfFontBuilder extends RtfElementVisitorBase {

	// ----------------------------------------------------------------------
	public RtfFontBuilder() {
		super(RtfElementVisitorOrder.NonRecursive);
		// we iterate over our children ourselves -> hence non-recursive
		Reset();
	} // RtfFontBuilder

	// ----------------------------------------------------------------------
	public String getFontId() {
		return this.fontId;
	} // FontId

	// ----------------------------------------------------------------------
	public int getFontIndex() {
		return this.fontIndex;
	} // FontIndex

	// ----------------------------------------------------------------------
	public int getFontCharset() {
		return this.fontCharset;
	} // FontCharset

	// ----------------------------------------------------------------------
	public int getFontCodePage() {
		return this.fontCodePage;
	} // FontCodePage

	// ----------------------------------------------------------------------
	public RtfFontKind getFontKind() {
		return this.fontKind;
	} // FontKind

	// ----------------------------------------------------------------------
	public RtfFontPitch getFontPitch() {
		return this.fontPitch;
	} // FontPitch

	// ----------------------------------------------------------------------
	public String getFontName() {
		return this.fontName;
	} // FontName

	// ----------------------------------------------------------------------
	public IRtfFont CreateFont() {
		return new RtfFont(this.fontId, this.fontKind, this.fontPitch,
				this.fontCharset, this.fontCodePage, this.fontName);
	} // CreateFont

	// ----------------------------------------------------------------------
	public void Reset() {
		this.fontIndex = 0;
		this.fontCharset = 0;
		this.fontCodePage = 0;
		this.fontKind = RtfFontKind.Nil;
		this.fontPitch = RtfFontPitch.Default;
		this.fontName = null;
	} // Reset

	// ----------------------------------------------------------------------
	protected void DoVisitGroup(IRtfGroup group) throws Exception {
		if (RtfSpec.TagFont.equals(group.getDestination())) {
			VisitGroupChildren(group);
		}
	} // DoVisitGroup

	// ----------------------------------------------------------------------
	protected void DoVisitTag(IRtfTag tag) {
		String tagName = tag.getName();
		if (tagName.equals(RtfSpec.TagFont)) {
			this.fontId = tag.getFullName();
			this.fontIndex = tag.getValueAsNumber();
		} else if (tagName.equals(RtfSpec.TagFontKindNil)) {
			this.fontKind = RtfFontKind.Nil;
		} else if (tagName.equals(RtfSpec.TagFontKindRoman)) {
			this.fontKind = RtfFontKind.Roman;
		} else if (tagName.equals(RtfSpec.TagFontKindSwiss)) {
			this.fontKind = RtfFontKind.Swiss;
		} else if (tagName.equals(RtfSpec.TagFontKindModern)) {
			this.fontKind = RtfFontKind.Modern;
		} else if (tagName.equals(RtfSpec.TagFontKindScript)) {
			this.fontKind = RtfFontKind.Script;
		} else if (tagName.equals(RtfSpec.TagFontKindDecor)) {
			this.fontKind = RtfFontKind.Decor;
		} else if (tagName.equals(RtfSpec.TagFontKindTech)) {
			this.fontKind = RtfFontKind.Tech;
		} else if (tagName.equals(RtfSpec.TagFontKindBidi)) {
			this.fontKind = RtfFontKind.Bidi;
		} else if (tagName.equals(RtfSpec.TagFontCharset)) {
			this.fontCharset = tag.getValueAsNumber();
		} else if (tagName.equals(RtfSpec.TagCodePage)) {
			this.fontCodePage = tag.getValueAsNumber();
		} else if (tagName.equals(RtfSpec.TagFontPitch)) {
			switch (tag.getValueAsNumber()) {
			case 0:
				this.fontPitch = RtfFontPitch.Default;
				break;
			case 1:
				this.fontPitch = RtfFontPitch.Fixed;
				break;
			case 2:
				this.fontPitch = RtfFontPitch.Variable;
				break;
			}

		}

	} // DoVisitTag

	// ----------------------------------------------------------------------
	protected void DoVisitText(IRtfText text) {
		String fontDescr = text.getText();
		if (fontDescr.endsWith(";")) {
			this.fontName = fontDescr.substring(0, fontDescr.length() - 1)
					.trim();
		} else {
			this.fontName = fontDescr.trim();
		}
	} // DoVisitText

	// ----------------------------------------------------------------------
	// members
	private String fontId;
	private int fontIndex;
	private int fontCharset;
	private int fontCodePage;
	private RtfFontKind fontKind;
	private RtfFontPitch fontPitch;
	private String fontName;

} // class RtfFontBuilder

