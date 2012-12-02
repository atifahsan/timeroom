## Summary
Interpolate values between keyframes in a sequence of sidecar files (XMPs).

This can be used in place of LRTimeLapse for very basic value interpolation.  Right now,
keyframes are hard coded to the first and last images in the input sequence.

## Motivation

This is the last missing piece of (Free) software you need to make quality timelapses using Adobe LightRoom. There are a number of great free pieces of software that will deshake, stabilize, and compress your timelapse for you. With this software, you can edit frames of your timelapse in Lightroom then smooth those changes out across your entire sequence.

For instance, if you have a sunset timelapse, you may want to adjust the white balance as the sun goes down and transitions into night.  You can edit the whie balance on the last frame, and this will smoothly transition the frames into that white balance.  Post processing is discussed more at the end of this readme.

## Usage

### Generate XMP files for your sequence
In LightRoom, generate xmp (sidecar) files for your image sequence by selecting them, then right click -> Metadata -> Save Metadata to files.

### Edit your keyframes
Right now, TimeRoom only supports keyframes in the first and last image in your sequence.  I'll be working on more flexibility of this when I have time (or help me!).

Edit the first and last image in LightRoom, then save the metadata again.

### Run TimeRoom
#### Warning: Back up any xmp files before running TimeRoom. This is still experimental software and I make no guarantees it will work correctly.
Then execute the timeroom.py with a list of xmp files as arguments.

```bash
	$ ./timeroom.py *.xmp
```

or 

```bash
	$ ./timeroom.py 20121129-EOS30D-001-0001.xmp 20121129-EOS30D-001-0002.xmp 20121129-EOS30D-001-0003.xmp
```

Input files will automatically be sorted alphabetically.  Key frames will become the first and last files in this sorted list.

All integer and real values will be 'tweened' from the first frame to the last frame.  It will save all the interpolated data into the sidecare sequence.

### Reload 
Now tell LightRoom to reload metadata on your image sequence!


### Post processing

Now deflicker and stabilize the frames in a tool such as [virtualdub](http://www.virtualdub.org/)

[Deflicker plugin for virtualdub](http://neuron2.net/deflick/flick.html)

You can follow the same basics for stabilization as LRTimeLapse
[Deshake workflow](http://forum.lrtimelapse.com/Thread-removal-of-blurring-with-deshaker)


## Summarized Workflow

* LightRoom - Save all metadata to files
* LightRoom - Edit keyframes (first and last), then save metadata
* TimeRoom - Execute
* Lightroom - Read metadata from files