using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;
using System.Drawing.Imaging;
using System.Drawing.Drawing2D;

namespace vcs_Exif
{
    public static class ExifStuff
    {
        // Orientations.
        private const int OrientationId = 0x0112;
        public enum ExifOrientations : byte
        {
            Unknown = 0,
            TopLeft = 1,
            TopRight = 2,
            BottomRight = 3,
            BottomLeft = 4,
            LeftTop = 5,
            RightTop = 6,
            RightBottom = 7,
            LeftBottom = 8,
        }

        // Return the image's orientation.
        public static ExifOrientations ImageOrientation(Image img)
        {
            // Get the index of the orientation property.
            int orientation_index = Array.IndexOf(img.PropertyIdList, OrientationId);

            // If there is no such property, return Unknown.
            if (orientation_index < 0) return ExifOrientations.Unknown;

            // Return the orientation value.
            return (ExifOrientations)img.GetPropertyItem(OrientationId).Value[0];
        }

        // Orient the image properly.
        public static void OrientImage(Image img)
        {
            // Get the image's orientation.
            ExifOrientations orientation = ImageOrientation(img);

            // Orient the image.
            switch (orientation)
            {
                case ExifOrientations.Unknown:
                case ExifOrientations.TopLeft:
                    break;
                case ExifOrientations.TopRight:
                    img.RotateFlip(RotateFlipType.RotateNoneFlipX);
                    break;
                case ExifOrientations.BottomRight:
                    img.RotateFlip(RotateFlipType.Rotate180FlipNone);
                    break;
                case ExifOrientations.BottomLeft:
                    img.RotateFlip(RotateFlipType.RotateNoneFlipY);
                    break;
                case ExifOrientations.LeftTop:
                    img.RotateFlip(RotateFlipType.Rotate90FlipX);
                    break;
                case ExifOrientations.RightTop:
                    img.RotateFlip(RotateFlipType.Rotate90FlipNone);
                    break;
                case ExifOrientations.RightBottom:
                    img.RotateFlip(RotateFlipType.Rotate90FlipY);
                    break;
                case ExifOrientations.LeftBottom:
                    img.RotateFlip(RotateFlipType.Rotate270FlipNone);
                    break;
            }

            // Set the image's orientation to TopLeft.
            SetImageOrientation(img, ExifOrientations.TopLeft);
        }

        // Set the image's orientation.
        public static void SetImageOrientation(Image img, ExifOrientations orientation)
        {
            // Get the index of the orientation property.
            int orientation_index = Array.IndexOf(img.PropertyIdList, OrientationId);

            // If there is no such property, do nothing.
            if (orientation_index < 0) return;

            // Set the orientation value.
            PropertyItem item = img.GetPropertyItem(OrientationId);
            item.Value[0] = (byte)orientation;
            img.SetPropertyItem(item);
        }

        // Possible image EXIF properties.
        // https://msdn.microsoft.com/de-de/library/ms534416.aspx
        // http://www.awaresystems.be/imaging/tiff/tifftags/privateifd/exif.html
        public enum ExifPropertyTypes
        {
            Exif_Image_ImageID = 0x800d,
            Exif_Image_CFARepeatPatternDim = 0x828d,
            Exif_Image_CFAPattern = 0x828e,
            Exif_Image_BatteryLevel = 0x828f,
            Copyright = 0x8298,
            ExifExposureTime = 0x829a,
            ExifFNumber = 0x829d,
            Exif_Image_IPTCNAA = 0x83bb,
            Exif_Image_ImageResources = 0x8649,
            ExifIFD = 0x8769,
            ICCProfile = 0x8773,
            ExifExposureProg = 0x8822,
            ExifSpectralSense = 0x8824,
            GpsIFD = 0x8825,
            ExifISOSpeed = 0x8827,
            ExifOECF = 0x8828,
            Exif_Image_Interlace = 0x8829,
            Exif_Image_TimeZoneOffset = 0x882a,
            Exif_Image_SelfTimerMode = 0x882b,
            Exif_Photo_SensitivityType = 0x8830,
            Exif_Photo_StandardOutputSensitivity = 0x8831,
            Exif_Photo_RecommendedExposureIndex = 0x8832,
            Exif_Photo_ISOSpeed = 0x8833,
            Exif_Photo_ISOSpeedLatitudeyyy = 0x8834,
            Exif_Photo_ISOSpeedLatitudezzz = 0x8835,
            ExifVer = 0x9000,
            ExifDTOrig = 0x9003,
            ExifDTDigitized = 0x9004,
            ExifCompConfig = 0x9101,
            ExifCompBPP = 0x9102,
            ExifShutterSpeed = 0x9201,
            ExifAperture = 0x9202,
            ExifBrightness = 0x9203,
            ExifExposureBias = 0x9204,
            ExifMaxAperture = 0x9205,
            ExifSubjectDist = 0x9206,
            ExifMeteringMode = 0x9207,
            ExifLightSource = 0x9208,
            ExifFlash = 0x9209,
            ExifFocalLength = 0x920a,
            Exif_Image_FlashEnergy = 0x920b,
            Exif_Image_SpatialFrequencyResponse = 0x920c,
            Exif_Image_Noise = 0x920d,
            Exif_Image_FocalPlaneXResolution = 0x920e,
            Exif_Image_FocalPlaneYResolution = 0x920f,
            Exif_Image_FocalPlaneResolutionUnit = 0x9210,
            Exif_Image_ImageNumber = 0x9211,
            Exif_Image_SecurityClassification = 0x9212,
            Exif_Image_ImageHistory = 0x9213,
            SubjectArea = 0x9214,
            Exif_Image_ExposureIndex = 0x9215,
            Exif_Image_TIFFEPStandardID = 0x9216,
            Exif_Image_SensingMethod = 0x9217,
            ExifMakerNote = 0x927c,
            ExifUserComment = 0x9286,
            ExifDTSubsec = 0x9290,
            ExifDTOrigSS = 0x9291,
            ExifDTDigSS = 0x9292,
            Exif_Image_XPTitle = 0x9c9b,
            Exif_Image_XPComment = 0x9c9c,
            Exif_Image_XPAuthor = 0x9c9d,
            Exif_Image_XPKeywords = 0x9c9e,
            Exif_Image_XPSubject = 0x9c9f,
            ExifFPXVer = 0xa000,
            ExifColorSpace = 0xa001,
            ExifPixXDim = 0xa002,
            ExifPixYDim = 0xa003,
            ExifRelatedWav = 0xa004,
            ExifInterop = 0xa005,
            ExifFlashEnergy = 0xa20b,
            ExifSpatialFR = 0xa20c,
            ExifFocalXRes = 0xa20e,
            ExifFocalYRes = 0xa20f,
            ExifFocalResUnit = 0xa210,
            ExifSubjectLoc = 0xa214,
            ExifExposureIndex = 0xa215,
            ExifSensingMethod = 0xa217,
            ExifFileSource = 0xa300,
            ExifSceneType = 0xa301,
            ExifCfaPattern = 0xa302,
            CustomRendered = 0xa401,
            ExposureMode = 0xa402,
            WhiteBalance = 0xa403,
            DigitalZoomRatio = 0xa404,
            FocalLengthIn35mmFilm = 0xa405,
            SceneCaptureType = 0xa406,
            GainControl = 0xa407,
            Contrast = 0xa408,
            Saturation = 0xa409,
            Sharpness = 0xa40a,
            DeviceSettingDescription = 0xa40b,
            SubjectDistanceRange = 0xa40c,
            ImageUniqueID = 0xa420,
            Exif_Photo_CameraOwnerName = 0xa430,
            Exif_Photo_BodySerialNumber = 0xa431,
            Exif_Photo_LensSpecification = 0xa432,
            Exif_Photo_LensMake = 0xa433,
            Exif_Photo_LensModel = 0xa434,
            Exif_Photo_LensSerialNumber = 0xa435,
            Exif_Image_PrintImageMatching = 0xc4a5,
            Exif_Image_DNGVersion = 0xc612,
            Exif_Image_DNGBackwardVersion = 0xc613,
            Exif_Image_UniqueCameraModel = 0xc614,
            Exif_Image_LocalizedCameraModel = 0xc615,
            Exif_Image_CFAPlaneColor = 0xc616,
            Exif_Image_CFALayout = 0xc617,
            Exif_Image_LinearizationTable = 0xc618,
            Exif_Image_BlackLevelRepeatDim = 0xc619,
            Exif_Image_BlackLevel = 0xc61a,
            Exif_Image_BlackLevelDeltaH = 0xc61b,
            Exif_Image_BlackLevelDeltaV = 0xc61c,
            Exif_Image_WhiteLevel = 0xc61d,
            Exif_Image_DefaultScale = 0xc61e,
            Exif_Image_DefaultCropOrigin = 0xc61f,
            Exif_Image_DefaultCropSize = 0xc620,
            Exif_Image_ColorMatrix1 = 0xc621,
            Exif_Image_ColorMatrix2 = 0xc622,
            Exif_Image_CameraCalibration1 = 0xc623,
            Exif_Image_CameraCalibration2 = 0xc624,
            Exif_Image_ReductionMatrix1 = 0xc625,
            Exif_Image_ReductionMatrix2 = 0xc626,
            Exif_Image_AnalogBalance = 0xc627,
            Exif_Image_AsShotNeutral = 0xc628,
            Exif_Image_AsShotWhiteXY = 0xc629,
            Exif_Image_BaselineExposure = 0xc62a,
            Exif_Image_BaselineNoise = 0xc62b,
            Exif_Image_BaselineSharpness = 0xc62c,
            Exif_Image_BayerGreenSplit = 0xc62d,
            Exif_Image_LinearResponseLimit = 0xc62e,
            Exif_Image_CameraSerialNumber = 0xc62f,
            Exif_Image_LensInfo = 0xc630,
            Exif_Image_ChromaBlurRadius = 0xc631,
            Exif_Image_AntiAliasStrength = 0xc632,
            Exif_Image_ShadowScale = 0xc633,
            Exif_Image_DNGPrivateData = 0xc634,
            Exif_Image_MakerNoteSafety = 0xc635,
            Exif_Image_CalibrationIlluminant1 = 0xc65a,
            Exif_Image_CalibrationIlluminant2 = 0xc65b,
            Exif_Image_BestQualityScale = 0xc65c,
            Exif_Image_RawDataUniqueID = 0xc65d,
            Exif_Image_OriginalRawFileName = 0xc68b,
            Exif_Image_OriginalRawFileData = 0xc68c,
            Exif_Image_ActiveArea = 0xc68d,
            Exif_Image_MaskedAreas = 0xc68e,
            Exif_Image_AsShotICCProfile = 0xc68f,
            Exif_Image_AsShotPreProfileMatrix = 0xc690,
            Exif_Image_CurrentICCProfile = 0xc691,
            Exif_Image_CurrentPreProfileMatrix = 0xc692,
            Exif_Image_ColorimetricReference = 0xc6bf,
            Exif_Image_CameraCalibrationSignature = 0xc6f3,
            Exif_Image_ProfileCalibrationSignature = 0xc6f4,
            Exif_Image_AsShotProfileName = 0xc6f6,
            Exif_Image_NoiseReductionApplied = 0xc6f7,
            Exif_Image_ProfileName = 0xc6f8,
            Exif_Image_ProfileHueSatMapDims = 0xc6f9,
            Exif_Image_ProfileHueSatMapData1 = 0xc6fa,
            Exif_Image_ProfileHueSatMapData2 = 0xc6fb,
            Exif_Image_ProfileToneCurve = 0xc6fc,
            Exif_Image_ProfileEmbedPolicy = 0xc6fd,
            Exif_Image_ProfileCopyright = 0xc6fe,
            Exif_Image_ForwardMatrix1 = 0xc714,
            Exif_Image_ForwardMatrix2 = 0xc715,
            Exif_Image_PreviewApplicationName = 0xc716,
            Exif_Image_PreviewApplicationVersion = 0xc717,
            Exif_Image_PreviewSettingsName = 0xc718,
            Exif_Image_PreviewSettingsDigest = 0xc719,
            Exif_Image_PreviewColorSpace = 0xc71a,
            Exif_Image_PreviewDateTime = 0xc71b,
            Exif_Image_RawImageDigest = 0xc71c,
            Exif_Image_OriginalRawFileDigest = 0xc71d,
            Exif_Image_SubTileBlockSize = 0xc71e,
            Exif_Image_RowInterleaveFactor = 0xc71f,
            Exif_Image_ProfileLookTableDims = 0xc725,
            Exif_Image_ProfileLookTableData = 0xc726,
            Exif_Image_OpcodeList1 = 0xc740,
            Exif_Image_OpcodeList2 = 0xc741,
            Exif_Image_OpcodeList3 = 0xc74e,
            Exif_Image_NoiseProfile = 0xc761,
            GpsVer = 0x0000,
            GpsLatitudeRef = 0x0001,
            GpsLatitude = 0x0002,
            GpsLongitudeRef = 0x0003,
            GpsLongitude = 0x0004,
            GpsAltitudeRef = 0x0005,
            GpsAltitude = 0x0006,
            GpsGpsTime = 0x0007,
            GpsGpsSatellites = 0x0008,
            GpsGpsStatus = 0x0009,
            GpsGpsMeasureMode = 0x000a,
            GpsGpsDop = 0x000b,
            GpsSpeedRef = 0x000c,
            GpsSpeed = 0x000d,
            GpsTrackRef = 0x000e,
            GpsTrack = 0x000f,
            GpsImgDirRef = 0x0010,
            GpsImgDir = 0x0011,
            GpsMapDatum = 0x0012,
            GpsDestLatRef = 0x0013,
            GpsDestLat = 0x0014,
            GpsDestLongRef = 0x0015,
            GpsDestLong = 0x0016,
            GpsDestBearRef = 0x0017,
            GpsDestBear = 0x0018,
            GpsDestDistRef = 0x0019,
            GpsDestDist = 0x001a,
            Exif_GPSInfo_GPSProcessingMethod = 0x001b,
            Exif_GPSInfo_GPSAreaInformation = 0x001c,
            Exif_GPSInfo_GPSDateStamp = 0x001d,
            Exif_GPSInfo_GPSDifferential = 0x001e,
            NewSubfileType = 0x00fe,
            SubfileType = 0x00ff,
            ImageWidth = 0x0100,
            ImageHeight = 0x0101,
            BitsPerSample = 0x0102,
            Compression = 0x0103,
            PhotometricInterp = 0x0106,
            ThreshHolding = 0x0107,
            CellWidth = 0x0108,
            CellHeight = 0x0109,
            FillOrder = 0x010a,
            DocumentName = 0x010d,
            ImageDescription = 0x010e,
            EquipMake = 0x010f,
            EquipModel = 0x0110,
            StripOffsets = 0x0111,
            Orientation = 0x0112,
            SamplesPerPixel = 0x0115,
            RowsPerStrip = 0x0116,
            StripBytesCount = 0x0117,
            MinSampleValue = 0x0118,
            MaxSampleValue = 0x0119,
            XResolution = 0x011a,
            YResolution = 0x011b,
            PlanarConfig = 0x011c,
            PageName = 0x011d,
            XPosition = 0x011e,
            YPosition = 0x011f,
            FreeOffset = 0x0120,
            FreeByteCounts = 0x0121,
            GrayResponseUnit = 0x0122,
            GrayResponseCurve = 0x0123,
            T4Option = 0x0124,
            T6Option = 0x0125,
            ResolutionUnit = 0x0128,
            PageNumber = 0x0129,
            TransferFunction = 0x012d,
            SoftwareUsed = 0x0131,
            DateTime = 0x0132,
            Artist = 0x013b,
            HostComputer = 0x013c,
            Predictor = 0x013d,
            WhitePoint = 0x013e,
            PrimaryChromaticities = 0x013f,
            ColorMap = 0x0140,
            HalftoneHints = 0x0141,
            TileWidth = 0x0142,
            TileLength = 0x0143,
            TileOffset = 0x0144,
            TileByteCounts = 0x0145,
            Exif_Image_SubIFDs = 0x014a,
            InkSet = 0x014c,
            InkNames = 0x014d,
            NumberOfInks = 0x014e,
            DotRange = 0x0150,
            TargetPrinter = 0x0151,
            ExtraSamples = 0x0152,
            SampleFormat = 0x0153,
            SMinSampleValue = 0x0154,
            SMaxSampleValue = 0x0155,
            TransferRange = 0x0156,
            Exif_Image_ClipPath = 0x0157,
            Exif_Image_XClipPathUnits = 0x0158,
            Exif_Image_YClipPathUnits = 0x0159,
            Exif_Image_Indexed = 0x015a,
            Exif_Image_JPEGTables = 0x015b,
            Exif_Image_OPIProxy = 0x015f,
            JPEGProc = 0x0200,
            JPEGInterFormat = 0x0201,
            JPEGInterLength = 0x0202,
            JPEGRestartInterval = 0x0203,
            JPEGLosslessPredictors = 0x0205,
            JPEGPointTransforms = 0x0206,
            JPEGQTables = 0x0207,
            JPEGDCTables = 0x0208,
            JPEGACTables = 0x0209,
            YCbCrCoefficients = 0x0211,
            YCbCrSubsampling = 0x0212,
            YCbCrPositioning = 0x0213,
            REFBlackWhite = 0x0214,
            Exif_Image_XMLPacket = 0x02bc,
            Gamma = 0x0301,
            ICCProfileDescriptor = 0x0302,
            SRGBRenderingIntent = 0x0303,
            ImageTitle = 0x0320,
            Exif_Iop_RelatedImageFileFormat = 0x1000,
            Exif_Iop_RelatedImageWidth = 0x1001,
            Exif_Iop_RelatedImageLength = 0x1002,
            Exif_Image_Rating = 0x4746,
            Exif_Image_RatingPercent = 0x4749,
            ResolutionXUnit = 0x5001,
            ResolutionYUnit = 0x5002,
            ResolutionXLengthUnit = 0x5003,
            ResolutionYLengthUnit = 0x5004,
            PrintFlags = 0x5005,
            PrintFlagsVersion = 0x5006,
            PrintFlagsCrop = 0x5007,
            PrintFlagsBleedWidth = 0x5008,
            PrintFlagsBleedWidthScale = 0x5009,
            HalftoneLPI = 0x500a,
            HalftoneLPIUnit = 0x500b,
            HalftoneDegree = 0x500c,
            HalftoneShape = 0x500d,
            HalftoneMisc = 0x500e,
            HalftoneScreen = 0x500f,
            JPEGQuality = 0x5010,
            GridSize = 0x5011,
            ThumbnailFormat = 0x5012,
            ThumbnailWidth = 0x5013,
            ThumbnailHeight = 0x5014,
            ThumbnailColorDepth = 0x5015,
            ThumbnailPlanes = 0x5016,
            ThumbnailRawBytes = 0x5017,
            ThumbnailSize = 0x5018,
            ThumbnailCompressedSize = 0x5019,
            ColorTransferFunction = 0x501a,
            ThumbnailData = 0x501b,
            ThumbnailImageWidth = 0x5020,
            ThumbnailImageHeight = 0x5021,
            ThumbnailBitsPerSample = 0x5022,
            ThumbnailCompression = 0x5023,
            ThumbnailPhotometricInterp = 0x5024,
            ThumbnailImageDescription = 0x5025,
            ThumbnailEquipMake = 0x5026,
            ThumbnailEquipModel = 0x5027,
            ThumbnailStripOffsets = 0x5028,
            ThumbnailOrientation = 0x5029,
            ThumbnailSamplesPerPixel = 0x502a,
            ThumbnailRowsPerStrip = 0x502b,
            ThumbnailStripBytesCount = 0x502c,
            ThumbnailResolutionX = 0x502d,
            ThumbnailResolutionY = 0x502e,
            ThumbnailPlanarConfig = 0x502f,
            ThumbnailResolutionUnit = 0x5030,
            ThumbnailTransferFunction = 0x5031,
            ThumbnailSoftwareUsed = 0x5032,
            ThumbnailDateTime = 0x5033,
            ThumbnailArtist = 0x5034,
            ThumbnailWhitePoint = 0x5035,
            ThumbnailPrimaryChromaticities = 0x5036,
            ThumbnailYCbCrCoefficients = 0x5037,
            ThumbnailYCbCrSubsampling = 0x5038,
            ThumbnailYCbCrPositioning = 0x5039,
            ThumbnailRefBlackWhite = 0x503a,
            ThumbnailCopyRight = 0x503b,
            LuminanceTable = 0x5090,
            ChrominanceTable = 0x5091,
            FrameDelay = 0x5100,
            LoopCount = 0x5101,
            GlobalPalette = 0x5102,
            IndexBackground = 0x5103,
            IndexTransparent = 0x5104,
            PixelUnit = 0x5110,
            PixelPerUnitX = 0x5111,
            PixelPerUnitY = 0x5112,
            PaletteHistogram = 0x5113,
        }

        // EXIF property types.
        // https://msdn.microsoft.com/en-us/library/system.drawing.imaging.propertyitem.type.aspx
        public enum ExifPropertyDataTypes : short
        {
            ByteArray = 1,
            String = 2,
            UShortArray = 3,
            ULongArray = 4,
            ULongFractionArray = 5,
            UByteArray = 6,
            LongArray = 7,
            LongFractionArray = 10,
        }

        // A structure to hold EXIF property data.
        // https://msdn.microsoft.com/en-us/library/system.drawing.imaging.propertyitem.aspx
        public struct ExifPropertyData
        {
            public int Id;
            public ExifPropertyTypes PropertyType;
            public ExifPropertyDataTypes DataType;
            public byte[] DataBuffer;
            public int DataLength;
            public string DataString;
        }

        // Get the data for an EXIF property.
        private static ExifPropertyData GetExifPropertyData(Image img, int index)
        {
            ExifPropertyData data = new ExifPropertyData();
            data.Id = img.PropertyIdList[index];
            data.PropertyType = (ExifPropertyTypes)data.Id;

            PropertyItem item = img.PropertyItems[index];
            data.DataBuffer = item.Value;
            data.DataType = (ExifPropertyDataTypes)item.Type;
            data.DataLength = item.Len;

            string result = "";
            int num_items, item_size;
            switch (data.DataType)
            {
                case ExifPropertyDataTypes.ByteArray:
                case ExifPropertyDataTypes.UByteArray:
                    data.DataString =
                        BitConverter.ToString(data.DataBuffer);
                    break;

                case ExifPropertyDataTypes.String:
                    data.DataString = Encoding.UTF8.GetString(
                        data.DataBuffer, 0, data.DataLength - 1);
                    break;

                case ExifPropertyDataTypes.UShortArray:
                    result = "";
                    item_size = 2;
                    num_items = data.DataLength / item_size;
                    for (int i = 0; i < num_items; i++)
                    {
                        ushort value = BitConverter.ToUInt16(
                            data.DataBuffer, i * item_size); 
                        result += ", " + value.ToString();
                    }
                    if (result.Length > 0) result = result.Substring(2);
                    data.DataString = "[" + result + "]";
                    break;

                case ExifPropertyDataTypes.ULongArray:
                    result = "";
                    item_size = 4;
                    num_items = data.DataLength / item_size;
                    for (int i = 0; i < num_items; i++)
                    {
                        uint value = BitConverter.ToUInt32(
                            data.DataBuffer, i * item_size);
                        result += ", " + value.ToString();
                    }
                    if (result.Length > 0) result = result.Substring(2);
                    data.DataString = "[" + result + "]";
                    break;

                case ExifPropertyDataTypes.ULongFractionArray:
                    result = "";
                    item_size = 8;
                    num_items = data.DataLength / item_size;
                    for (int i = 0; i < num_items; i++)
                    {
                        uint numerator = BitConverter.ToUInt32(
                            data.DataBuffer, i * item_size);
                        uint denominator = BitConverter.ToUInt32(
                            data.DataBuffer, i * item_size + item_size / 2);
                        result += ", " + numerator.ToString() +
                            "/" + denominator.ToString();
                    }
                    if (result.Length > 0) result = result.Substring(2);
                    data.DataString = "[" + result + "]";
                    break;
                                
                case ExifPropertyDataTypes.LongArray:
                    result = "";
                    item_size = 4;
                    num_items = data.DataLength / item_size;
                    for (int i = 0; i < num_items; i++)
                    {
                        int value = BitConverter.ToInt32(
                            data.DataBuffer, i * item_size);
                        result += ", " + value.ToString();
                    }
                    if (result.Length > 0) result = result.Substring(2);
                    data.DataString = "[" + result + "]";
                    break;
                
                case ExifPropertyDataTypes.LongFractionArray:
                    result = "";
                    item_size = 8;
                    num_items = data.DataLength / item_size;
                    for (int i = 0; i < num_items; i++)
                    {
                        int numerator = BitConverter.ToInt32(
                            data.DataBuffer, i * item_size);
                        int denominator = BitConverter.ToInt32(
                            data.DataBuffer, i * item_size + item_size / 2);
                        result += ", " + numerator.ToString() +
                            "/" + denominator.ToString();
                    }
                    if (result.Length > 0) result = result.Substring(2);
                    data.DataString = "[" + result + "]";
                    break;
            }
            return data;
        }

        // Make a list of EXIF properties for an image.
        public static List<ExifPropertyData> GetExifProperties(Image img)
        {
            List<ExifPropertyData> result = new List<ExifPropertyData>();

            for (int index = 0; index < img.PropertyIdList.Length; index++)
            {
                result.Add(GetExifPropertyData(img, index));
            }

            return result;
        }
    }
}
