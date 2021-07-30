import pyIGRF

mag = pyIGRF.igrf_value(60,60,600,2015.34)
print(mag)