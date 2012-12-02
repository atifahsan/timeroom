#!/usr/bin/python
# http://www.sno.phy.queensu.ca/~phil/exiftool/TagNames/XMP.html

class DataType:
    REAL=1
    INT=2
    SINT=3
    BOOL=4
    STRING=5

CRS_DEFAULTS = {

}

CRS_TAGS = {
  'AlreadyApplied': (DataType.BOOL, None),
  'AutoBrightness': (DataType.BOOL, None),
  'AutoContrast': (DataType.BOOL, None),
  'AutoExposure': (DataType.BOOL, None),
  'AutoLateralCA': (DataType.INT, None),
  'AutoShadows': (DataType.BOOL, None),
  'Blacks2012': (DataType.INT, None),
  'BlueHue': (DataType.INT, None),
  'BlueSaturation': (DataType.INT, None),
  'Brightness': (DataType.INT, None),
  'CameraProfile': (DataType.STRING, None),
  'CameraProfileDigest': (DataType.STRING, None),
  'ChromaticAberrationB': (DataType.INT, None),
  'ChromaticAberrationR': (DataType.INT, None),
  'Clarity': (DataType.INT, None),
  'Clarity2012': (DataType.INT, None),
  'ColorNoiseReduction': (DataType.INT, None),
  'ColorNoiseReductionDetail': (DataType.INT, None),
  'Contrast': (DataType.INT, 0),
  'Contrast2012': (DataType.SINT, 0),
  'Converter': (DataType.STRING, None),
  'ConvertToGrayscale': (DataType.BOOL, None),
  #CropAngle real
  #CropBottom  real
  'CropConstrainToWarp': (DataType.INT, None),
  #CropHeight  real
  #CropLeft  real
  #CropRight real
  #CropTop real
  #CropUnit  integer 0 = pixels
  #1 = inches
  #2 = cm
  #CropUnits integer 0 = pixels
  #1 = inches
  #2 = cm
  #CropWidth real
  'Defringe': (DataType.INT, None),
  'Exposure': (DataType.REAL, 0),
  'Exposure2012': (DataType.REAL, 0),
  'FillLight': (DataType.INT, None),
  #GradientBasedCorrections  struct+ --> Correction Struct
  #GradientBasedCorrActive boolean_  (GradientBasedCorrectionsCorrectionActive)
  #GradientBasedCorrAmount real_ (GradientBasedCorrectionsCorrectionAmount)
  #GradientBasedCorrMasks  struct_+  --> CorrectionMask Struct
  #(GradientBasedCorrectionsCorrectionMasks)
  #GradientBasedCorrMaskCenterWeight real_ (GradientBasedCorrectionsCorrectionMasksCenterWeight)
  #GradientBasedCorrMaskDabs string_ (GradientBasedCorrectionsCorrectionMasksDabs)
  #GradientBasedCorrMaskFlow real_ (GradientBasedCorrectionsCorrectionMasksFlow)
  #GradientBasedCorrMaskFullX  real_ (GradientBasedCorrectionsCorrectionMasksFullX)
  #GradientBasedCorrMaskFullY  real_ (GradientBasedCorrectionsCorrectionMasksFullY)
  #GradientBasedCorrMaskValue  real_ (GradientBasedCorrectionsCorrectionMasksMaskValue)
  #GradientBasedCorrMaskRadius real_ (GradientBasedCorrectionsCorrectionMasksRadius)
  #GradientBasedCorrMaskWhat string_ (GradientBasedCorrectionsCorrectionMasksWhat)
  #GradientBasedCorrMaskZeroX  real_ (GradientBasedCorrectionsCorrectionMasksZeroX)
  #GradientBasedCorrMaskZeroY  real_ (GradientBasedCorrectionsCorrectionMasksZeroY)
  #GradientBasedCorrBrightness real_ (GradientBasedCorrectionsLocalBrightness)
  #GradientBasedCorrClarity  real_ (GradientBasedCorrectionsLocalClarity)
  #GradientBasedCorrContrast real_ (GradientBasedCorrectionsLocalContrast)
  #GradientBasedCorrExposure real_ (GradientBasedCorrectionsLocalExposure)
  #GradientBasedCorrSaturation real_ (GradientBasedCorrectionsLocalSaturation)
  #GradientBasedCorrSharpness  real_ (GradientBasedCorrectionsLocalSharpness)
  #GradientBasedCorrHue  real_ (GradientBasedCorrectionsLocalToningHue)
  #GradientBasedCorrSaturation real_ (GradientBasedCorrectionsLocalToningSaturation)
  #GradientBasedCorrWhat string_ (GradientBasedCorrectionsWhat)
  'GrainAmount': (DataType.INT, None),
  'GrainFrequency': (DataType.INT, None),
  'GrainSize': (DataType.INT, None),
  'GrayMixerAqua': (DataType.INT, None),
  'GrayMixerBlue': (DataType.INT, None),
  'GrayMixerGreen': (DataType.INT, None),
  'GrayMixerMagenta': (DataType.INT, None),
  'GrayMixerOrange': (DataType.INT, None),
  'GrayMixerPurple': (DataType.INT, None),
  'GrayMixerRed': (DataType.INT, None),
  'GrayMixerYellow': (DataType.INT, None),
  'GreenHue': (DataType.INT, None),
  'GreenSaturation': (DataType.INT, None),
  'HasCrop': (DataType.BOOL, None),
  'HasSettings': (DataType.BOOL, None),
  'HighlightRecovery': (DataType.INT, None),
  'Highlights2012': (DataType.INT, None),
  'HueAdjustmentAqua': (DataType.INT, None),
  'HueAdjustmentBlue': (DataType.INT, None),
  'HueAdjustmentGreen': (DataType.INT, None),
  'HueAdjustmentMagenta': (DataType.INT, None),
  'HueAdjustmentOrange': (DataType.INT, None),
  'HueAdjustmentPurple': (DataType.INT, None),
  'HueAdjustmentRed': (DataType.INT, None),
  'HueAdjustmentYellow': (DataType.INT, None),
  'IncrementalTemperature': (DataType.INT, None),
  'IncrementalTint': (DataType.INT, None),
  'LensManualDistortionAmount': (DataType.INT, None),
  'LensProfileChromaticAberrationScale': (DataType.INT, None),
  'LensProfileDigest': (DataType.STRING, None),
  'LensProfileDistortionScale': (DataType.INT, None),
  'LensProfileEnable': (DataType.INT, None),
  'LensProfileFilename': (DataType.STRING, None),
  'LensProfileName': (DataType.STRING, None),
  'LensProfileSetup': (DataType.STRING, None),
  'LensProfileVignettingScale': (DataType.INT, None),
  'LuminanceAdjustmentAqua': (DataType.INT, None),
  'LuminanceAdjustmentBlue': (DataType.INT, None),
  'LuminanceAdjustmentGreen': (DataType.INT, None),
  'LuminanceAdjustmentMagenta': (DataType.INT, None),
  'LuminanceAdjustmentOrange': (DataType.INT, None),
  'LuminanceAdjustmentPurple': (DataType.INT, None),
  'LuminanceAdjustmentRed': (DataType.INT, None),
  'LuminanceAdjustmentYellow': (DataType.INT, None),
  'LuminanceNoiseReductionContrast': (DataType.INT, None),
  'LuminanceNoiseReductionDetail': (DataType.INT, None),
  'LuminanceSmoothing': (DataType.INT, None),
  'MoireFilter': (DataType.STRING, None),  #'Off' = Off    'On' = On
  #PaintBasedCorrections struct+ --> Correction Struct
  #PaintCorrectionActive boolean_  (PaintBasedCorrectionsCorrectionActive)
  #PaintCorrectionAmount real_ (PaintBasedCorrectionsCorrectionAmount)
  #PaintBasedCorrectionMasks struct_+  --> CorrectionMask Struct
  #(PaintBasedCorrectionsCorrectionMasks)
  #PaintCorrectionMaskCenterWeight real_ (PaintBasedCorrectionsCorrectionMasksCenterWeight)
  #PaintCorrectionMaskDabs string_ (PaintBasedCorrectionsCorrectionMasksDabs)
  #PaintCorrectionMaskFlow real_ (PaintBasedCorrectionsCorrectionMasksFlow)
  #PaintCorrectionMaskFullX  real_ (PaintBasedCorrectionsCorrectionMasksFullX)
  #PaintCorrectionMaskFullY  real_ (PaintBasedCorrectionsCorrectionMasksFullY)
  #PaintCorrectionMaskValue  real_ (PaintBasedCorrectionsCorrectionMasksMaskValue)
  #PaintCorrectionMaskRadius real_ (PaintBasedCorrectionsCorrectionMasksRadius)
  #PaintCorrectionMaskWhat string_ (PaintBasedCorrectionsCorrectionMasksWhat)
  #PaintCorrectionMaskZeroX  real_ (PaintBasedCorrectionsCorrectionMasksZeroX)
  #PaintCorrectionMaskZeroY  real_ (PaintBasedCorrectionsCorrectionMasksZeroY)
  #PaintCorrectionBrightness real_ (PaintBasedCorrectionsLocalBrightness)
  #PaintCorrectionClarity  real_ (PaintBasedCorrectionsLocalClarity)
  #PaintCorrectionContrast real_ (PaintBasedCorrectionsLocalContrast)
  #PaintCorrectionExposure real_ (PaintBasedCorrectionsLocalExposure)
  #PaintCorrectionSaturation real_ (PaintBasedCorrectionsLocalSaturation)
  #PaintCorrectionSharpness  real_ (PaintBasedCorrectionsLocalSharpness)
  #PaintCorrectionHue  real_ (PaintBasedCorrectionsLocalToningHue)
  #PaintCorrectionSaturation real_ (PaintBasedCorrectionsLocalToningSaturation)
  #PaintCorrectionWhat string_ (PaintBasedCorrectionsWhat)
  'ParametricDarks': (DataType.INT, None),
  'ParametricHighlights': (DataType.INT, None),
  'ParametricHighlightSplit': (DataType.INT, None),
  'ParametricLights': (DataType.INT, None),
  'ParametricMidtoneSplit': (DataType.INT, None),
  'ParametricShadows': (DataType.INT, None),
  'ParametricShadowSplit': (DataType.INT, None),
  'PerspectiveHorizontal': (DataType.INT, None),
  'PerspectiveRotate': (DataType.REAL, None),
  'PerspectiveScale': (DataType.INT, None),
  'PerspectiveVertical': (DataType.INT, None),
  'PostCropVignetteAmount': (DataType.INT, None),
  'PostCropVignetteFeather': (DataType.INT, None),
  'PostCropVignetteHighlightContrast': (DataType.INT, None),
  'PostCropVignetteMidpoint': (DataType.INT, None),
  'PostCropVignetteRoundness': (DataType.INT, None),
  'PostCropVignetteStyle': (DataType.INT, None),
  'ProcessVersion': (DataType.STRING, None),
  'RawFileName': (DataType.STRING, None),
  'RedEyeInfo': (DataType.STRING, None),
  'RedHue': (DataType.INT, None),
  'RedSaturation': (DataType.INT, None),
  'RetouchInfo': (DataType.STRING, None),
  'Saturation': (DataType.INT, None),
  'SaturationAdjustmentAqua': (DataType.INT, None),
  'SaturationAdjustmentBlue': (DataType.INT, None),
  'SaturationAdjustmentGreen': (DataType.INT, None),
  'SaturationAdjustmentMagenta': (DataType.INT, None),
  'SaturationAdjustmentOrange': (DataType.INT, None),
  'SaturationAdjustmentPurple': (DataType.INT, None),
  'SaturationAdjustmentRed': (DataType.INT, None),
  'SaturationAdjustmentYellow': (DataType.INT, None),
  'Shadows': (DataType.INT, None),
  'Shadows2012': (DataType.INT, None),
  'ShadowTint': (DataType.INT, None),
  'SharpenDetail': (DataType.INT, None),
  'SharpenEdgeMasking': (DataType.INT, None),
  'SharpenRadius': (DataType.REAL, None),
  'Sharpness': (DataType.INT, None),
  'Smoothness': (DataType.INT, None),
  'SplitToningBalance': (DataType.INT, None),
  'SplitToningHighlightHue': (DataType.INT, None),
  'SplitToningHighlightSaturation': (DataType.INT, None),
  'SplitToningShadowHue': (DataType.INT, None),
  'SplitToningShadowSaturation': (DataType.INT, None),
  'ColorTemperature': (DataType.INT, None),
  'Temperature': (DataType.INT, 5500),
  'Tint': (DataType.INT, 6),
  'ToneCurve': (DataType.STRING, None),
  'ToneCurveBlue': (DataType.STRING, None),
  'ToneCurveGreen': (DataType.STRING, None),
  'ToneCurveName': (DataType.STRING, None),  #'Custom' = Custom    'Linear' = Linear
  #'Medium Contrast' = Medium Contrast
  #'Strong Contrast' = Strong Contrast
  'ToneCurveName2012': (DataType.STRING, None),
  'ToneCurvePV2012': (DataType.STRING, None),
  'ToneCurvePV2012Blue': (DataType.STRING, None),
  'ToneCurvePV2012Green': (DataType.STRING, None),
  'ToneCurvePV2012Red': (DataType.STRING, None),
  'ToneCurveRed': (DataType.STRING, None),
  'Version': (DataType.STRING, None),
  'Vibrance': (DataType.INT, None),
  'VignetteAmount': (DataType.INT, None),
  'VignetteMidpoint': (DataType.INT, None),
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
  'Whites2012': (DataType.INT, None)
}