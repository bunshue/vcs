package com.lietu.filter;

import java.awt.Color;

/**
 * @author http://cfsearching@blogspot.com
 * 
 *         Convert CharacterProperties.getIco24() values to RGB or Hex
 * 
 *         Version: JDK 1.6.0_13
 */
public class ConvertIco24ToRGB {

	/**
	 * Converts a CharacterProperties.getIco24() value into rgb format. Ico24
	 * (or ColorRef) values, have the hexadecimal form: 0x00BBGGRR. (Applies to
	 * binary file formats only)
	 * 
	 * Note, getIco24() returns -1 to represent "Auto". It is not clear how to
	 * determine that color value. So for now, the color "black" is used for
	 * "Auto".
	 * 
	 * @param ico24
	 *            - Word colorRef value returned by
	 *            CharacterProperties.getIco24()
	 * @return Array of color values [0] red, [1] green, [2] blue
	 */
	public static int[] ico24ToRGB(int ico24) {
		int[] rgb = new int[3];

		// If the colorRef is not "Auto", unpack the rgb values
		if (ico24 != -1) {
			rgb[0] = (ico24 >> 0) & 0xff; // red;
			rgb[1] = (ico24 >> 8) & 0xff; // green
			rgb[2] = (ico24 >> 16) & 0xff; // blue
		}

		return rgb;
	}

	/**
	 * Convenience method. Returns the ico24 value as as hexadecimal string,
	 * form: 0x00BBGGRR
	 * 
	 * @param ico24
	 *            - Word colorRef value returned by
	 *            CharacterProperties.getIco24()
	 * @return hexadecimal string in form: 0x00BBGGRR
	 */
	public static String ico24AsHex(int ico24) {
		return Integer.toHexString(ico24);
	}

	/**
	 * Converts a CharacterProperties.getIco24() value to rgb hexadecimal
	 * format. Ico24 (or ColorRef) values, have the hexadecimal form:
	 * 0x00BBGGRR. (Applies to binary file formats only)
	 * 
	 * @param ico24
	 *            - Word colorRef value returned by
	 *            CharacterProperties.getIco24()
	 * @return hexadecimal color. Returns 0 if it cannot be determined
	 */
	public static String ico24ToHex(int ico24) {
		int r = (ico24 >> 0) & 0xff; // red;
		int g = (ico24 >> 8) & 0xff; // green
		int b = (ico24 >> 16) & 0xff; // blue
		int rgb = (r << 16) | (g << 8) | b;

		// Find a better way to maintain leading zeroes
		return Integer.toHexString(0xC000000 | rgb).substring(1);
	}

	/**
	 * Converts a six digit hexadecimal value (RRGGBB) to a
	 * CharacterProperties.setIco24(int) compatible value. Ico24 (or ColorRef)
	 * values, have the hexadecimal form: 0x00BBGGRR. (Applies to binary file
	 * formats only)
	 * 
	 * @param hexColor
	 *            - Word colorRef value returned by
	 *            CharacterProperties.getIco24()
	 * @return colorRef value
	 */
	public static int hexToIco24(String hexColor) {
		if (hexColor == null || hexColor.length() != 6) {
			throw new IllegalArgumentException(
					"hexColor must be 6 characters in length. Example: ffffff");
		}
		int r = Integer.parseInt(hexColor.substring(0, 2), 16);
		int g = Integer.parseInt(hexColor.substring(2, 4), 16);
		int b = Integer.parseInt(hexColor.substring(4, 6), 16);
		return rgbToIco24(r, g, b);
	}

	/**
	 * Converts an rgb color to a Word colorRef value that should be compatible
	 * with CharacterProperties.setIco24(int). Ico24 (or ColorRef) values, have
	 * the hexadecimal form: 0x00BBGGRR. (Applies to binary file formats only)
	 * 
	 * @param r
	 *            red
	 * @param g
	 *            green
	 * @param b
	 *            blue
	 * @return ico24 (or ColorRef) value
	 */
	public static int rgbToIco24(int r, int g, int b) {
		return (0xff << 24) | (b << 16) | (g << 8) | r;
	}

	public static void main(String[] args) {
		//String inputPath = "input/blank.doc";
		//String outputPath = "output/InsertStyledTextA.doc";
		//inputPath = "output/InsertStyledText.doc";

		try {
			System.out.println("Test Color");
			System.out.println("=======================");

			Color c = Color.RED;//Color.BLACK;
			// Extract the hex and rgb values of the selected color
			int r = c.getRed();
			int g = c.getGreen();
			int b = c.getBlue();
			String hex = Integer.toHexString(c.getRGB() | 0x000000)
					.substring(2);
			System.out.printf("red=%d green=%d blue=%d | hex= %s \r", r, g, b,
					hex);

			// Convert the rgb values to a ColorRef
			int ico24 = rgbToIco24(r, g, b);
			// Display parameters and result
			System.out.printf("rgbToIco24(red=%d, green=%d, blue=%d) = %d \r",
					r, g, b, ico24);

			// Convert the hex color to a ColorRef
			ico24 = hexToIco24(hex);
			System.out.printf("hexToIco24(hex=%s ) = %d \r", hex, ico24);

			// Convert the ColorRef back to rgb
			int[] rgb = ico24ToRGB(ico24);
			System.out.printf(
					"ico24ToRGB(ico24=%d) = red=%d, green=%d, blue=%d \r",
					ico24, rgb[0], rgb[1], rgb[2]);

			// Convert the ColorRef back to hex
			hex = ico24ToHex(ico24);
			System.out.printf("ico24ToHex(ico24=%d) = hex=%6s \r", ico24, hex);

		} catch (Exception e) {
			e.printStackTrace();
		}

	}

}