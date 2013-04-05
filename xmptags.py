#!/usr/bin/python
# http://www.sno.phy.queensu.ca/~phil/exiftool/TagNames/XMP.html

class DataType:
    REAL=1
    INT=2
    SINT=3
    RATIONAL=4
    BOOL=5
    STRING=6

    MAX_TWEENABLE = SINT

XMP_TAGS = {
    'Rating': (DataType.INT, 0)
}

EXIF_TAGS = {
    'ExposureTime': (DataType.RATIONAL, 0),
    'FNumber': (DataType.RATIONAL, 0),
    'ISOSpeedRatings': (DataType.INT, 0)
}

CRS_GBC_CM_TAGS = {
    #GradientBasedCorrMaskCenterWeight real_ (GradientBasedCorrectionsCorrectionMasksCenterWeight)
    #GradientBasedCorrMaskDabs string_ (GradientBasedCorrectionsCorrectionMasksDabs)
    #GradientBasedCorrMaskFlow real_ (GradientBasedCorrectionsCorrectionMasksFlow)
    'FullX': (DataType.REAL, None),
    'FullY': (DataType.REAL, None),
    'MaskValue': (DataType.REAL, None),
    #GradientBasedCorrMaskRadius real_ (GradientBasedCorrectionsCorrectionMasksRadius)
    'What': (DataType.STRING, None),
    'ZeroX': (DataType.REAL, None),
    'ZeroY': (DataType.REAL, None)
}

CRS_GBC_TAGS = {
    #GradientBasedCorrections    struct+ --> Correction Struct
    'CorrectionActive': (DataType.BOOL, None),
    'CorrectionAmount': (DataType.REAL, None),
#    'CorrectionMasks': (DataType.SCHEMA, CRS_GBC_CM_TAGS),
    'LocalBrightness': (DataType.REAL, None),
#    'LocalClarity': (DataType.REAL, None),
    'LocalClarity2012': (DataType.REAL, None),
#    'LocalContrast': (DataType.REAL, None),
    'LocalContrast2012': (DataType.REAL, None),
    'LocalDefringe': (DataType.REAL, None),
#    'LocalExposure': (DataType.REAL, None),
    'LocalExposure2012': (DataType.REAL, None),
    'LocalHighlights2012': (DataType.REAL, None),
    'LocalLuminanceNoise': (DataType.REAL, None),
    'LocalMoire': (DataType.REAL, None),
    'LocalSaturation': (DataType.REAL, None),
    'LocalShadows2012': (DataType.REAL, None),
    'LocalSharpness': (DataType.REAL, None),
    'LocalTemperature': (DataType.REAL, None),
    'LocalTint': (DataType.REAL, None),
    'LocalToningHue': (DataType.REAL, None),
    'LocalToningSaturation': (DataType.REAL, None),
    'What': (DataType.STRING, None)
}

CRS_TC_TAGS = {
}

CRS_TAGS = {
    'AlreadyApplied': (DataType.BOOL, None),
    'AutoBrightness': (DataType.BOOL, None),
    'AutoContrast': (DataType.BOOL, None),
    'AutoExposure': (DataType.BOOL, None),
    'AutoLateralCA': (DataType.SINT, None),
    'AutoShadows': (DataType.BOOL, None),
    'Blacks2012': (DataType.SINT, None),
    'BlueHue': (DataType.SINT, None),
    'BlueSaturation': (DataType.SINT, None),
    'Brightness': (DataType.SINT, None),
    'CameraProfile': (DataType.STRING, None),
    'CameraProfileDigest': (DataType.STRING, None),
    'ChromaticAberrationB': (DataType.SINT, None),
    'ChromaticAberrationR': (DataType.SINT, None),
    # OLD PROCESS 'Clarity': (DataType.SINT, None),
    'Clarity2012': (DataType.SINT, None),
    'ColorNoiseReduction': (DataType.SINT, None),
    'ColorNoiseReductionDetail': (DataType.SINT, None),
    # OLD PROCESS 'Contrast': (DataType.SINT, 0),
    'Contrast2012': (DataType.SINT, 0),
    'Converter': (DataType.STRING, None),
    'ConvertToGrayscale': (DataType.BOOL, None),
    'CropAngle': (DataType.REAL, 0),
    'CropBottom': (DataType.REAL, 0),
    'CropConstrainToWarp': (DataType.SINT, None),
    'CropHeight': (DataType.REAL, 0),
    'CropLeft': (DataType.REAL, 0),
    'CropRight': (DataType.REAL, 0),
    'CropTop': (DataType.REAL, 0),
    #CropUnit    integer 0 = pixels
    #1 = inches
    #2 = cm
    #CropUnits integer 0 = pixels
    #1 = inches
    #2 = cm
    'CropWidth': (DataType.REAL, 0),
    'Defringe': (DataType.SINT, None),
    # OLD PROCESS 'Exposure': (DataType.REAL, 0),
    'Exposure2012': (DataType.REAL, 0),
    'FillLight': (DataType.SINT, None),
    #### CRS_GBC_TAGS 'GradientBasedCorrections'
    'GrainAmount': (DataType.SINT, None),
    'GrainFrequency': (DataType.SINT, None),
    'GrainSize': (DataType.SINT, None),
    'GrayMixerAqua': (DataType.SINT, None),
    'GrayMixerBlue': (DataType.SINT, None),
    'GrayMixerGreen': (DataType.SINT, None),
    'GrayMixerMagenta': (DataType.SINT, None),
    'GrayMixerOrange': (DataType.SINT, None),
    'GrayMixerPurple': (DataType.SINT, None),
    'GrayMixerRed': (DataType.SINT, None),
    'GrayMixerYellow': (DataType.SINT, None),
    'GreenHue': (DataType.SINT, None),
    'GreenSaturation': (DataType.SINT, None),
    'HasCrop': (DataType.BOOL, None),
    'HasSettings': (DataType.BOOL, None),
    # OLD PROCESS 'HighlightRecovery': (DataType.SINT, None),
    'Highlights2012': (DataType.SINT, None),
    'HueAdjustmentAqua': (DataType.SINT, None),
    'HueAdjustmentBlue': (DataType.SINT, None),
    'HueAdjustmentGreen': (DataType.SINT, None),
    'HueAdjustmentMagenta': (DataType.SINT, None),
    'HueAdjustmentOrange': (DataType.SINT, None),
    'HueAdjustmentPurple': (DataType.SINT, None),
    'HueAdjustmentRed': (DataType.SINT, None),
    'HueAdjustmentYellow': (DataType.SINT, None),
    'IncrementalTemperature': (DataType.SINT, None),
    'IncrementalTint': (DataType.SINT, None),
    'LensManualDistortionAmount': (DataType.SINT, None),
    'LensProfileChromaticAberrationScale': (DataType.SINT, None),
    'LensProfileDigest': (DataType.STRING, None),
    'LensProfileDistortionScale': (DataType.SINT, None),
    'LensProfileEnable': (DataType.SINT, None),
    'LensProfileFilename': (DataType.STRING, None),
    'LensProfileName': (DataType.STRING, None),
    'LensProfileSetup': (DataType.STRING, None),
    'LensProfileVignettingScale': (DataType.SINT, None),
    'LuminanceAdjustmentAqua': (DataType.SINT, None),
    'LuminanceAdjustmentBlue': (DataType.SINT, None),
    'LuminanceAdjustmentGreen': (DataType.SINT, None),
    'LuminanceAdjustmentMagenta': (DataType.SINT, None),
    'LuminanceAdjustmentOrange': (DataType.SINT, None),
    'LuminanceAdjustmentPurple': (DataType.SINT, None),
    'LuminanceAdjustmentRed': (DataType.SINT, None),
    'LuminanceAdjustmentYellow': (DataType.SINT, None),
    'LuminanceNoiseReductionContrast': (DataType.SINT, None),
    'LuminanceNoiseReductionDetail': (DataType.SINT, None),
    'LuminanceSmoothing': (DataType.SINT, None),
    'MoireFilter': (DataType.STRING, None),    #'Off' = Off        'On' = On
    #PaintBasedCorrections struct+ --> Correction Struct
    #PaintCorrectionActive boolean_    (PaintBasedCorrectionsCorrectionActive)
    #PaintCorrectionAmount real_ (PaintBasedCorrectionsCorrectionAmount)
    #PaintBasedCorrectionMasks struct_+    --> CorrectionMask Struct
    #(PaintBasedCorrectionsCorrectionMasks)
    #PaintCorrectionMaskCenterWeight real_ (PaintBasedCorrectionsCorrectionMasksCenterWeight)
    #PaintCorrectionMaskDabs string_ (PaintBasedCorrectionsCorrectionMasksDabs)
    #PaintCorrectionMaskFlow real_ (PaintBasedCorrectionsCorrectionMasksFlow)
    #PaintCorrectionMaskFullX    real_ (PaintBasedCorrectionsCorrectionMasksFullX)
    #PaintCorrectionMaskFullY    real_ (PaintBasedCorrectionsCorrectionMasksFullY)
    #PaintCorrectionMaskValue    real_ (PaintBasedCorrectionsCorrectionMasksMaskValue)
    #PaintCorrectionMaskRadius real_ (PaintBasedCorrectionsCorrectionMasksRadius)
    #PaintCorrectionMaskWhat string_ (PaintBasedCorrectionsCorrectionMasksWhat)
    #PaintCorrectionMaskZeroX    real_ (PaintBasedCorrectionsCorrectionMasksZeroX)
    #PaintCorrectionMaskZeroY    real_ (PaintBasedCorrectionsCorrectionMasksZeroY)
    #PaintCorrectionBrightness real_ (PaintBasedCorrectionsLocalBrightness)
    #PaintCorrectionClarity    real_ (PaintBasedCorrectionsLocalClarity)
    #PaintCorrectionContrast real_ (PaintBasedCorrectionsLocalContrast)
    #PaintCorrectionExposure real_ (PaintBasedCorrectionsLocalExposure)
    #PaintCorrectionSaturation real_ (PaintBasedCorrectionsLocalSaturation)
    #PaintCorrectionSharpness    real_ (PaintBasedCorrectionsLocalSharpness)
    #PaintCorrectionHue    real_ (PaintBasedCorrectionsLocalToningHue)
    #PaintCorrectionSaturation real_ (PaintBasedCorrectionsLocalToningSaturation)
    #PaintCorrectionWhat string_ (PaintBasedCorrectionsWhat)
    'ParametricDarks': (DataType.SINT, None),
    'ParametricHighlights': (DataType.SINT, None),
    'ParametricHighlightSplit': (DataType.SINT, None),
    'ParametricLights': (DataType.SINT, None),
    'ParametricMidtoneSplit': (DataType.SINT, None),
    'ParametricShadows': (DataType.SINT, None),
    'ParametricShadowSplit': (DataType.SINT, None),
    'PerspectiveHorizontal': (DataType.SINT, None),
    'PerspectiveRotate': (DataType.REAL, None),
    'PerspectiveScale': (DataType.SINT, None),
    'PerspectiveVertical': (DataType.SINT, None),
    'PostCropVignetteAmount': (DataType.SINT, None),
    'PostCropVignetteFeather': (DataType.SINT, None),
    'PostCropVignetteHighlightContrast': (DataType.SINT, None),
    'PostCropVignetteMidpoint': (DataType.SINT, None),
    'PostCropVignetteRoundness': (DataType.SINT, None),
    'PostCropVignetteStyle': (DataType.SINT, None),
    'ProcessVersion': (DataType.STRING, None),
    'RawFileName': (DataType.STRING, None),
    'RedEyeInfo': (DataType.STRING, None),
    'RedHue': (DataType.SINT, None),
    'RedSaturation': (DataType.SINT, None),
    'RetouchInfo': (DataType.STRING, None),
    'Saturation': (DataType.SINT, None),
    'SaturationAdjustmentAqua': (DataType.SINT, None),
    'SaturationAdjustmentBlue': (DataType.SINT, None),
    'SaturationAdjustmentGreen': (DataType.SINT, None),
    'SaturationAdjustmentMagenta': (DataType.SINT, None),
    'SaturationAdjustmentOrange': (DataType.SINT, None),
    'SaturationAdjustmentPurple': (DataType.SINT, None),
    'SaturationAdjustmentRed': (DataType.SINT, None),
    'SaturationAdjustmentYellow': (DataType.SINT, None),
    # OLD PROCESS 'Shadows': (DataType.SINT, None),
    'Shadows2012': (DataType.SINT, None),
    'ShadowTint': (DataType.SINT, None),
    'SharpenDetail': (DataType.SINT, None),
    'SharpenEdgeMasking': (DataType.SINT, None),
    'SharpenRadius': (DataType.REAL, None),
    'Sharpness': (DataType.SINT, None),
    'Smoothness': (DataType.SINT, None),
    'SplitToningBalance': (DataType.SINT, None),
    'SplitToningHighlightHue': (DataType.SINT, None),
    'SplitToningHighlightSaturation': (DataType.SINT, None),
    'SplitToningShadowHue': (DataType.SINT, None),
    'SplitToningShadowSaturation': (DataType.SINT, None),
    'ColorTemperature': (DataType.SINT, None),
    'Temperature': (DataType.SINT, 5500),
    'Tint': (DataType.SINT, 6),
    # OLD PROCESS 'ToneCurve': (DataType.STRING, None),
    # OLD PROCESS 'ToneCurveBlue': (DataType.STRING, None),
    # OLD PROCESS 'ToneCurveGreen': (DataType.STRING, None),
    # OLD PROCESS 'ToneCurveName': (DataType.STRING, None),    #'Custom' = Custom        'Linear' = Linear
    #'Medium Contrast' = Medium Contrast
    #'Strong Contrast' = Strong Contrast
    'ToneCurveName2012': (DataType.STRING, None),
#    'ToneCurvePV2012': (DataType.SCHEMA, CRS_TC_TAGS),
#    'ToneCurvePV2012': (DataType.STRING, None),
    'ToneCurvePV2012Blue': (DataType.STRING, None),
    'ToneCurvePV2012Green': (DataType.STRING, None),
    'ToneCurvePV2012Red': (DataType.STRING, None),
    'ToneCurveRed': (DataType.STRING, None),
    'Version': (DataType.STRING, None),
    'Vibrance': (DataType.SINT, None),
    'VignetteAmount': (DataType.SINT, None),
    'VignetteMidpoint': (DataType.SINT, None),
    #'WhiteBalance': (DataType.STRING, None),
    #'As Shot' = As Shot
    #'Auto' = Auto
    #'Cloudy' = Cloudy
    #'Custom' = Custom
    #'Daylight' = Daylight
    #'Flash' = Flash
    #'Fluorescent' = Fluorescent
    #'Shade' = Shade
    #'Tungsten' = Tungsten
    'Whites2012': (DataType.SINT, None)
}

TAGS = {
    'xmp': XMP_TAGS,
    'crs': CRS_TAGS,
    'exif': EXIF_TAGS,
}
