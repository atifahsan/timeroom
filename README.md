## Summary
Interpolate values between keyframes in a sequence of sidecar files (XMPs).

This can be used in place of LRTimelapse for interpolation of basic values, point curves and graduated filters.  Keyframes are detected by their Lightroom star rating.

### WARNING
Treat this software as alpha at best.  When you come across errors, please get in touch.

## Windows binaries
Windows binaries are available in another repository.  Click the big download zip button.

Windows binaries are available at https://github.com/lewisthompson/timeroombinaries

## Motivation

This is the last missing piece of (Free) software you need to make quality timelapses using Adobe Lightroom. There are a number of great free pieces of software that will deshake, stabilize, and compress your timelapse for you. With this software, you can edit frames of your timelapse in Lightroom then smooth those changes out across your entire sequence.

For instance, if you have a sunset timelapse, you may want to adjust the white balance as the sun goes down and transitions into night.  You can edit the whie balance on the last frame, and this will smoothly transition the frames into that white balance.  Post processing is discussed more at the end of this readme.

## Usage

### Generate XMP sidecar files for your sequence
In Lightroom, prior to any edits or changes, select all images in a specific folder, right click and select Metadata -> Save Metadata to files.

### Initialize in Timeroom
Navigate to the folder and click Read to load basic metadata from the sidecars.  If you are happy to proceed click Initialize which will autodetect keyframes (the first & last in the directory, as well as images either side of an EV change (e.g. change of aperture, shutter speed or ISO)) as well as set a default White Balance.

Select Save to write these ratings and other adjustments back to the sidecar files.

### Edit keyframes in Lightroom
In Lightroom select all images in the folder, right click and select Metadata -> Read Metadata from files.  Ratings should show up for keyframe images and white balance may be adjusted in image previews.  To show just keyframes select >= 1 in the Grid view filter.
#### You can safely add/remove keyframes by changing the star rating in Lightroom
Timeroom will transition settings between any pair of keyframes, so edit as required.  Keyframes either side of an EV change are given the ratings 2 and 3, respectively.  You can use the LRTimelapse Holy Grail method of matching total exposures for complicated transitions.

Once all edits are made revert to showing all images in Grid view and right click and select Metadata -> Save Metadata to files.
#### Unlike LRTimelapse *you must save metadata for all images*, not just keyframes

### Reload and process in Timeroom
Reload changes metadata by clicking Read in Timeroom.  Currently the GUI does not provide much visual feedback.

By default Timeroom will not try and transition tone curves and graduated filters.  If you wish to transition either, click the relevant toolbar button.  If you choose to do this you must ensure that *all* images have the same number of graduated filters (and that they were added in the same order - I recommend syncing Develop settings for these adjustments) and that any given tone curve has the same number of points (e.g. if one image has 4 points on the green tone curve so must every other image).

Click Process to interpolate values and save to write changes back to metadata.

### Reload 
Tell Lightroom to reload metadata from files.

## Summarized Workflow

* Lightroom: Make no adjustments, save metadata to files
* Timeroom: Read, Initialize, Save
* Lightroom: Read metadata from files, make adjustments to keyframes, save metadata to files
* Timeroom: Read, Process, Save
* Lightroom: Read metadata from files
