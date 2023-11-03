package com.lietu.rtf;

import com.lietu.rtf.sys.HashTool;

public class RtfFont implements IRtfFont {

	// ----------------------------------------------------------------------
	public RtfFont(String id, RtfFontKind kind, RtfFontPitch pitch,
			int charSet, int codePage, String name) {
		try {
			if (id == null) {
				throw new Exception("id");
			}
			if (charSet < 0) {
				throw new Exception("charset may not be negative but is "
						+ charSet);
			}
			if (codePage < 0) {
				throw new Exception("charset may not be negative but is "
						+ codePage);
			}
			if (name == null) {
				throw new Exception("name");
			}
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		this.id = id;
		this.kind = kind;
		this.pitch = pitch;
		this.charSet = charSet;
		this.codePage = codePage;
		this.name = name;
	} // RtfFont

	// ----------------------------------------------------------------------
	public String getId() {
		return this.id;
	} // Id

	// ----------------------------------------------------------------------
	public RtfFontKind getKind() {
		return this.kind;
	} // Kind

	// ----------------------------------------------------------------------
	public RtfFontPitch getPitch() {
		return this.pitch;
	} // Pitch

	// ----------------------------------------------------------------------
	public int getCharSet() {
		return this.charSet;
	} // CharSet

	// ----------------------------------------------------------------------
	public int getCodePage() {

		{
			// if a codepage is specified, it overrides the charset setting
			if (this.codePage == 0) {
				// unspecified codepage: use the one derived from the charset:
				return RtfSpec.GetCodePage(this.charSet);
			}
			return this.codePage;
		}
	} // CodePage

	// ----------------------------------------------------------------------
	/*
	 * public Encoding GetEncoding() { return Encoding.GetEncoding( CodePage );
	 * } // GetEncoding
	 */
	// ----------------------------------------------------------------------
	public String getName() {
		return this.name;
	} // Name

	// ----------------------------------------------------------------------
	public boolean equals(Object obj) {
		if (obj == this) {
			return true;
		} else if (obj == null || this.getClass() != obj.getClass()) {
			return false;
		}
		return isEqual(obj);
	} // Equals

	// ----------------------------------------------------------------------
	public int hashCode() {
		return HashTool.AddHashCode(this.hashCode(), ComputeHashCode());
	} // GetHashCode

	// ----------------------------------------------------------------------

	public String toString() {
		return this.id + ":" + this.name;
	} // ToString

	// ----------------------------------------------------------------------
	private boolean isEqual(Object obj) {
		RtfFont compare = (RtfFont) obj; // guaranteed to be non-null
		return this.id.equals(compare.id) && this.kind == compare.kind
				&& this.pitch == compare.pitch
				&& this.charSet == compare.charSet
				&& this.codePage == compare.codePage
				&& this.name.equals(compare.name);
	} // IsEqual

	// ----------------------------------------------------------------------
	private int ComputeHashCode() {
		int hash = this.id.hashCode();
		hash = HashTool.AddHashCode(hash, this.kind);
		hash = HashTool.AddHashCode(hash, this.pitch);
		hash = HashTool.AddHashCode(hash, this.charSet);
		hash = HashTool.AddHashCode(hash, this.codePage);
		hash = HashTool.AddHashCode(hash, this.name);
		return hash;
	} // ComputeHashCode

	// ----------------------------------------------------------------------
	// members
	private String id;
	private RtfFontKind kind;
	private RtfFontPitch pitch;
	private int charSet;
	private int codePage;
	private String name;

} // class RtfFont
