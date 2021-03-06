import unittest
import meta.query


class TestQueryStuff(unittest.TestCase):

    def test_date(self):
        args = {'query': 'foo',
                'StartDate': '1.1.2016', 'EndDate': '31.12.2016',
                'StudyDescription': 'lorem'}
        result = meta.query.query_body(args)
        self.assertEqual(result['query'],
                         'foo AND StudyDate:[20160101 TO 20161231]')

    def test_filter_single(self):
        args = {'query': 'foo',
                'StartDate': '1.1.2016', 'EndDate': '31.12.2016',
                'StudyDescription': 'lorem ipsum'}
        result = meta.query.query_body(args)

        self.assertEqual(result['filter'],
                         ['StudyDescription:lorem ipsum'])

    def test_filter_multiple(self):
        args = {'query': 'foo',
                'StartDate': '1.1.2016', 'EndDate': '31.12.2016',
                'StudyDescription': 'lorem ipsum',
                'SeriesDescription': 'dolor sit amet'}
        result = meta.query.query_body(args)

        self.assertEqual(result['filter'],
                         ['StudyDescription:lorem ipsum',
                          'SeriesDescription:dolor sit amet'])

    def test_filter_all(self):
        args = {'query': 'foo',
                'StartDate': '1.1.2016', 'EndDate': '31.12.2016',
                'StudyDescription': 'lorem ipsum',
                'SeriesDescription': 'dolor sit amet',
                'PatientID': '123',
                'PatientName': 'Hans Mueller',
                'AccessionNumber': 'A123456789'}
        result = meta.query.query_body(args)

        self.assertEqual(result['filter'],
                         ['StudyDescription:lorem ipsum',
                          'SeriesDescription:dolor sit amet',
                          'PatientID:123',
                          'PatientName:Hans Mueller',
                          'AccessionNumber:A123456789'])

    def test_filter_single_modality(self):
        args = {'query': 'foo', 'StartDate': '1.1.2016',
                'EndDate': '31.12.2016',
                'Modality': 'CT'}
        result = meta.query.query_body(args)

        self.assertEqual(result['filter'],
                         ['Modality:CT'])

    def test_filter_multiple_modality(self):
        args = {'query': 'foo', 'StartDate': '1.1.2016',
                'EndDate': '31.12.2016',
                'Modality': ['CT', 'MR']}
        result = meta.query.query_body(args)

        self.assertEqual(result['filter'],
                         ["Modality:['CT', 'MR']"])

if __name__ == '__main__':
    unittest.main()
