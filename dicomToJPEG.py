import DecompressNConvert

myMagic = DecompressNConvert.initialize()

# Argument for DecompressNConvert is path of the compressed dicom.
numOfFrame = myMagic.DecompressNConvert('./dicomImage/123.dcm')

# Print total number of frames in the compressed dicom.
print(numOfFrame)

myMagic.terminate()
