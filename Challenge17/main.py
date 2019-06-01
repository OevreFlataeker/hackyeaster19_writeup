import png
import array

r = png.Reader(filename="eggdesign.png")

'''
def cp(a):
    return array('B', a)
def testUnfilterScanline(self):
    reader = png.Reader(bytes='')
    reader.psize = 3
    scanprev = array('B', [20, 21, 22, 210, 211, 212])
    scanline = array('B', [30, 32, 34, 230, 233, 236])



    out = reader.undo_filter(0, cp(scanline), cp(scanprev))
    self.assertEqual(list(out), list(scanline))  # none
    out = reader.undo_filter(1, cp(scanline), cp(scanprev))
    self.assertEqual(list(out), [30, 32, 34, 4, 9, 14])  # sub
    out = reader.undo_filter(2, cp(scanline), cp(scanprev))
    self.assertEqual(list(out), [50, 53, 56, 184, 188, 192])  # up
    out = reader.undo_filter(3, cp(scanline), cp(scanprev))
    self.assertEqual(list(out), [40, 42, 45, 99, 103, 108])  # average
    out = reader.undo_filter(4, cp(scanline), cp(scanprev))
    self.assertEqual(list(out), [50, 53, 56, 184, 188, 192])  # paeth

w = png.Writer()


for i in r.iter_straight_byte_rows()
r.undo_filter(filter_type=2),cp(scanline),cp(scanprev)
'''