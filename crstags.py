#!/usr/bin/python
# http://www.sno.phy.queensu.ca/~phil/exiftool/TagNames/XMP.html

class DataType:
    BOOL=1
    INT=2
    STRING=3
    REAL=4

CRS_TAGS = {
  'AlreadyApplied': DataType.BOOL,
  'AutoBrightness': DataType.BOOL,
  'AutoContrast': DataType.BOOL,
  'AutoExposure': DataType.BOOL,
  'AutoLateralCA': DataType.INT,
  'AutoShadows': DataType.BOOL,
  'Blacks2012': DataType.INT,
  'BlueHue': DataType.INT,
  'BlueSaturation': DataType.INT,
  'Brightness': DataType.INT,
  'CameraProfile': DataType.STRING,
  'CameraProfileDigest': DataType.STRING,
  'ChromaticAberrationB': DataType.INT,
  'ChromaticAberrationR': DataType.INT,
  'Clarity': DataType.INT,
  'Clarity2012': DataType.INT,
  'ColorNoiseReduction': DataType.INT,
  'ColorNoiseReductionDetail': DataType.INT,
  'Contrast': DataType.INT,
  'Contrast2012': DataType.INT,
  'Converter': DataType.STRING,
  'ConvertToGrayscale': DataType.BOOL,
  #CropAngle real
  #CropBottom  real
  'CropConstrainToWarp': DataType.INT,
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
  'Defringe': DataType.INT,
  'Exposure': DataType.REAL,
  'Exposure2012': DataType.REAL,
  'FillLight': DataType.INT,
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
  'GrainAmount': DataType.INT,
  'GrainFrequency': DataType.INT,
  'GrainSize': DataType.INT,
  'GrayMixerAqua': DataType.INT,
  'GrayMixerBlue': DataType.INT,
  'GrayMixerGreen': DataType.INT,
  'GrayMixerMagenta': DataType.INT,
  'GrayMixerOrange': DataType.INT,
  'GrayMixerPurple': DataType.INT,
  'GrayMixerRed': DataType.INT,
  'GrayMixerYellow': DataType.INT,
  'GreenHue': DataType.INT,
  'GreenSaturation': DataType.INT,
  'HasCrop': DataType.BOOL,
  'HasSettings': DataType.BOOL,
  'HighlightRecovery': DataType.INT,
  'Highlights2012': DataType.INT,
  'HueAdjustmentAqua': DataType.INT,
  'HueAdjustmentBlue': DataType.INT,
  'HueAdjustmentGreen': DataType.INT,
  'HueAdjustmentMagenta': DataType.INT,
  'HueAdjustmentOrange': DataType.INT,
  'HueAdjustmentPurple': DataType.INT,
  'HueAdjustmentRed': DataType.INT,
  'HueAdjustmentYellow': DataType.INT,
  'IncrementalTemperature': DataType.INT,
  'IncrementalTint': DataType.INT,
  'LensManualDistortionAmount': DataType.INT,
  'LensProfileChromaticAberrationScale': DataType.INT,
  'LensProfileDigest': DataType.STRING,
  'LensProfileDistortionScale': DataType.INT,
  'LensProfileEnable': DataType.INT,
  'LensProfileFilename': DataType.STRING,
  'LensProfileName': DataType.STRING,
  'LensProfileSetup': DataType.STRING,
  'LensProfileVignettingScale': DataType.INT,
  'LuminanceAdjustmentAqua': DataType.INT,
  'LuminanceAdjustmentBlue': DataType.INT,
  'LuminanceAdjustmentGreen': DataType.INT,
  'LuminanceAdjustmentMagenta': DataType.INT,
  'LuminanceAdjustmentOrange': DataType.INT,
  'LuminanceAdjustmentPurple': DataType.INT,
  'LuminanceAdjustmentRed': DataType.INT,
  'LuminanceAdjustmentYellow': DataType.INT,
  'LuminanceNoiseReductionContrast': DataType.INT,
  'LuminanceNoiseReductionDetail': DataType.INT,
  'LuminanceSmoothing': DataType.INT,
  'MoireFilter': DataType.STRING,  #'Off' = Off    'On' = On
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
  'ParametricDarks': DataType.INT,
  'ParametricHighlights': DataType.INT,
  'ParametricHighlightSplit': DataType.INT,
  'ParametricLights': DataType.INT,
  'ParametricMidtoneSplit': DataType.INT,
  'ParametricShadows': DataType.INT,
  'ParametricShadowSplit': DataType.INT,
  'PerspectiveHorizontal': DataType.INT,
  'PerspectiveRotate': DataType.REAL,
  'PerspectiveScale': DataType.INT,
  'PerspectiveVertical': DataType.INT,
  'PostCropVignetteAmount': DataType.INT,
  'PostCropVignetteFeather': DataType.INT,
  'PostCropVignetteHighlightContrast': DataType.INT,
  'PostCropVignetteMidpoint': DataType.INT,
  'PostCropVignetteRoundness': DataType.INT,
  'PostCropVignetteStyle': DataType.INT,
  'ProcessVersion': DataType.STRING,
  'RawFileName': DataType.STRING,
  'RedEyeInfo': DataType.STRING,
  'RedHue': DataType.INT,
  'RedSaturation': DataType.INT,
  'RetouchInfo': DataType.STRING,
  'Saturation': DataType.INT,
  'SaturationAdjustmentAqua': DataType.INT,
  'SaturationAdjustmentBlue': DataType.INT,
  'SaturationAdjustmentGreen': DataType.INT,
  'SaturationAdjustmentMagenta': DataType.INT,
  'SaturationAdjustmentOrange': DataType.INT,
  'SaturationAdjustmentPurple': DataType.INT,
  'SaturationAdjustmentRed': DataType.INT,
  'SaturationAdjustmentYellow': DataType.INT,
  'Shadows': DataType.INT,
  'Shadows2012': DataType.INT,
  'ShadowTint': DataType.INT,
  'SharpenDetail': DataType.INT,
  'SharpenEdgeMasking': DataType.INT,
  'SharpenRadius': DataType.REAL,
  'Sharpness': DataType.INT,
  'Smoothness': DataType.INT,
  'SplitToningBalance': DataType.INT,
  'SplitToningHighlightHue': DataType.INT,
  'SplitToningHighlightSaturation': DataType.INT,
  'SplitToningShadowHue': DataType.INT,
  'SplitToningShadowSaturation': DataType.INT,
  'ColorTemperature': DataType.INT,
  'Tint': DataType.INT,
  'ToneCurve': DataType.STRING,
  'ToneCurveBlue': DataType.STRING,
  'ToneCurveGreen': DataType.STRING,
  'ToneCurveName': DataType.STRING,  #'Custom' = Custom    'Linear' = Linear
  #'Medium Contrast' = Medium Contrast
  #'Strong Contrast' = Strong Contrast
  'ToneCurveName2012': DataType.STRING,
  'ToneCurvePV2012': DataType.STRING,
  'ToneCurvePV2012Blue': DataType.STRING,
  'ToneCurvePV2012Green': DataType.STRING,
  'ToneCurvePV2012Red': DataType.STRING,
  'ToneCurveRed': DataType.STRING,
  'Version': DataType.STRING,
  'Vibrance': DataType.INT,
  'VignetteAmount': DataType.INT,
  'VignetteMidpoint': DataType.INT,
  #'WhiteBalance': DataType.STRING,
  #'As Shot' = As Shot
  #'Auto' = Auto
  #'Cloudy' = Cloudy
  #'Custom' = Custom
  #'Daylight' = Daylight
  #'Flash' = Flash
  #'Fluorescent' = Fluorescent
  #'Shade' = Shade
  #'Tungsten' = Tungsten
  'Whites2012': DataType.INT
}