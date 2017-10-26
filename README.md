# DecompressDicomToJPEG
Convert multi-frame dicom image first to single-frame dicoms and then to PNG images. Both single-frame dicom files and PNG images will be saved in current folder.
#### Note: The code alone with the package are not compatible with python 3.6, but they work well with python 3.5.

Steps to use:

1. Open a command prompt in the `for_redistribution_files_only` folder.
2. Run the setup script to install the package: `python setup.py install`
3. Open the code `dicomToJPEG.py` and change the dicom image path. Save.
4. In command prompt, run the the code: `python dicomToJPEG.py`

Single-frame dicom images and JPEG images associated with each dicom image will be created in the current folder. The total number of frames will be shown in the command prompt.


