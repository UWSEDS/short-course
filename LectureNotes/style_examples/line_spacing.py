import unittest
import io
class test_LoadFile(unittest.TestCase):
    def test_loadFile_filenameType(self):
        with self.assertRaises(TypeError):
            io.loadFile(42)
    def test_loadFile_verboseType(self):
        with self.assertRaises(TypeError):
            io.loadFile('filename', 42)
    def test_loadFile_nonExistentFile(self):
        with self.assertRaises(IOError):
            io.loadFile('file_does_not_exist')
    def test_loadFile_directoryNotFile(self):
        with self.assertRaises(IOError):
            io.loadFile('examples')
    def test_loadFile_incorrectFieldCount(self):
        with self.assertRaises(ValueError):
            io.loadFile('examples/invalid/badRecordLength.phylodist')
    def test_loadFile_incorrectTaxFieldCount(self):
        with self.assertRaises(ValueError):
            io.loadFile('examples/invalid/badTaxRecordLength.phylodist')
    def test_loadFile_exampleValues(self):
        # check the length
        pdDF = io.loadFile(
            'examples/valid/' +
            'example_Metatranscriptome_9_HOW4_[LakWasMeta9_HOW4_2]/IMG_Data/' +
            '61177.assembled.faa.phylodist',
            verbose=True
        )
        self.assertEquals(len(pdDF.index), 10001)
        # spot check row 98's locus_tag
        self.assertEquals(pdDF.at[97, 'locus_tag'], 'Ga0066495_1324111')
class test_defaultSampleNameExtractionFunction(unittest.TestCase):
    def test_defaultSampleNameExtractionFunction_value(self):
        self.assertEquals(
            io.defaultSampleNameExtractionFunction(
                'examples/valid/example[exampleSample]/' +
                'IMG_Data/example.phylodist'
            ),
            'exampleSample'
        )
class test_sweepFiles(unittest.TestCase):
    def test_sweepFiles_fileNotDirectory(self):
            with self.assertRaises(IOError):
            io.sweepFiles('phylodist/test.py')
    def test_sweepFiles_nonExistentDir(self):
        with self.assertRaises(IOError):
            io.sweepFiles('directory_does_not_exist')
    def test_sweepFiles_directoryType(self):
        with self.assertRaises(TypeError):
            io.sweepFiles(42)
    def test_sweepFiles_metadataType(self):
        with self.assertRaises(TypeError):
            io.sweepFiles('examples', metadata=41)
    def test_sweepFiles_values(self):
        pdSD = io.sweepFiles('examples')
        # check the length of the dictionary
        self.assertEquals(len(pdSD), 2)
        # verify the sample key names are correct
        for key in pdSD.keys():
            self.assertIn(key, ['LakWasMeta9_HOW4', 'LakWasMeta9_HOW4_2'])
        # spot check specific values in the dictionary's data frame
        self.assertEquals(
            pdSD['LakWasMeta9_HOW4'].at[97, 'locus_tag'], 'Ga0066407_15607121'
        )
        self.assertEquals(
            pdSD['LakWasMeta9_HOW4_2'].at[1013, 'locus_tag'],
            'Ga0066495_1323232'
        )
if __name__ == '__main__':
    unittest.main()
