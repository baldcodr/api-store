from mockfirestore import MockFirestore
import unittest


class TestDocumentReference(unittest.TestCase):

    def test_document_get_documentId(self):
        fs = MockFirestore()
        fs._data = {'tf122324': {"tf12":{'zip': 'LL12 TW0', 'state': 'Manchester'}}}
        doc_ref = fs.collection('tf122324').document('tf12')
        self.assertEqual(doc_ref.id, 'tf12')

if __name__ == '__main__':
    unittest.main()