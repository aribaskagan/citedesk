import unittest
from fastapi.testclient import TestClient
from app import app, CORPUS

class FlowTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_demo_and_grounding(self):
        result = self.client.post('/api/answer', json={'situation': 'Erasmus student in Romania needs a residence permit, learning agreement update and health insurance.\nStudy grade: 2'}).json()
        self.assertEqual({s['id'] for s in result['sources']}, {'R1', 'L1', 'H1'})
        self.assertTrue(all(t['source'] in {s['id'] for s in CORPUS} for t in result['checklist']))
        self.assertEqual(next(f['value'] for f in result['fields'] if f['label'] == 'Study grade'), '2')
        self.assertIn('not official deadlines', result['warning'])

    def test_unknown_and_unverified(self):
        result = self.client.post('/api/answer', json={'situation':'Can I bring my cat?', 'official_text':'unverified claim', 'source_url':'https://example.com'}).json()
        self.assertEqual(result['sources'], [])
        self.assertEqual(result['fields'], [])
        self.assertEqual(result['user_material']['text'], 'unverified claim')
        self.assertIn('cannot verify', result['missing'])

    def test_validation_and_page(self):
        self.assertEqual(self.client.post('/api/answer', json={'situation':''}).status_code, 422)
        self.assertEqual(self.client.get('/').status_code, 200)

if __name__ == '__main__':
    unittest.main()
