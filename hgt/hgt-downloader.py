# SRTM:
# http://builder.osmand.net/terrain-aster-srtm-eudem/
# http://rmd.neoknet.com/srtm3/

import os
import sys
import re
import urllib.request
import zipfile

if ( len( sys.argv ) != 3 ):
	print( 'Spatny pocet argumentu. Pouzijte ve tvrau poly-downloader.py <tif-dir> <hgt-dir>' )
	exit()

# Opravim vystupni adresar
inputDir = sys.argv[1]
if( inputDir[-1] != '/' ):
	inputDir = inputDir + '/'

outputDir = sys.argv[2]
if( outputDir[-1] != '/' ):
	outputDir = outputDir + '/'


# Ctu soubor po radcich
for file in os.listdir( inputDir ):
	# Ziskam souradnice z radku
	fileName = re.search('([NS]\d{2}[EW]\d{3})\.tif', file)

	if ( fileName == None ):
		continue

	fileName = fileName.group( 1 )


	# Pokud soubor neexistuje, pokusim se ho stahnout
	if ( not os.path.isfile( outputDir + fileName + '.hgt' ) ):
		print ( '\r' + fileName + ': Stahuji hgt', end = '' )
		sys.stdout.flush()

		urllib.request.urlretrieve( 'http://rmd.neoknet.com/srtm3/' + fileName + '.hgt.zip', outputDir + fileName + '.zip' )
		
		print ( '\r' + fileName + ': Rozbaluji  ', end = '' )
		sys.stdout.flush()

		zipRef = zipfile.ZipFile( outputDir + fileName + '.zip', 'r')
		zipRef.extractall( outputDir )
		zipRef.close()
		os.remove( outputDir + fileName + '.zip' )

	# if ( not os.path.isfile( outputDir + 'SRTM3v3.0/' + fileName + '.tif' ) ):
		# print ( '\r' + fileName + ': Stahuji tif', end = '' )
		# sys.stdout.flush()

		# urllib.request.urlretrieve( 'http://builder.osmand.net/terrain-aster-srtm-eudem/' + fileName + '.tif', outputDir + 'SRTM3v3.0/' + fileName + '.tif' )
		
	print ( '\r' + fileName + ': Stazeno    ' )
	sys.stdout.flush()
