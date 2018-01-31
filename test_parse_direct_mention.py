import unittest

import slack_client


class TestParse_direct_mention(unittest.TestCase):
    def test_parse_direct_mention_witout_any_mention(self):
        # WHEN
        user_id, mention = slack_client.parse_direct_mention("toto")

        # THEN
        self.assertIsNone(user_id)
        self.assertIsNone(mention)

    def test_parse_direct_mention_with_user_mention(self):
        # WHEN
        user_id, mention = slack_client.parse_direct_mention("<@Wtoto>: tata")

        # THEN
        self.assertEqual(user_id, "Wtoto")
        self.assertEqual(mention, ": tata")


if __name__ == '__main__':
    unittest.main()
