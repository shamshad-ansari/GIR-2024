from search import search, article_length, unique_authors, most_recent_article, favorite_author, title_and_author, refine_search, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    # def test_example_unit_test(self):
    #     expected_search_soccer_results = [
    #         ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526],
    #         ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562],
    #         ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]
    #     ]
    #     self.assertEqual(search('soccer'), expected_search_soccer_results)


    def test_article_length(self):
        expected_search_thandiram_3k_results = []
        self.assertEqual(article_length(3000, search('thandiram')), expected_search_thandiram_3k_results)

        expected_search_soccer_0_results = []
        self.assertEqual(article_length(0, search('soccer')), expected_search_soccer_0_results)

        expected_search_fisk_100_results = []
        self.assertEqual(article_length(100, search('fisk')), expected_search_fisk_100_results)

        expected_search_this_1000_results = [['Lua (programming language)', 'Burna Boy', 1113957128, 0], ['The Hunchback of Notre Dame (musical)', 'Nihonjoe', 1192176615, 42]]
        self.assertEqual(article_length(1000, search('this')), expected_search_this_1000_results)

    def test_unique_authors(self):
        expected_authors_3_the_results = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['French pop music', 'Mack Johnson', 1172208041, 5569], ['1922 in music', 'Gary King', 1242717698, 11576]]
        self.assertEqual(unique_authors(3, search('the')), expected_authors_3_the_results)

        expected_authors_0_eye_results = []
        self.assertEqual(unique_authors(0, search('eye')), expected_authors_0_eye_results)

        expected_no_author = []
        self.assertEqual(unique_authors(3, search('thandiram')), expected_no_author)

        expected_authors_100_eye_results = [['Kevin Cadogan', 'Mr Jake', 1144136316, 3917]]
        self.assertEqual(unique_authors(100, search('eye')), expected_authors_100_eye_results)
    
    def test_refine_search(self):
        expected_intersection = [['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562], ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]]
        metadata_soccer = search('soccer')
        self.assertEqual(refine_search('his', metadata_soccer), expected_intersection)

        expected_intersection2 = [['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562]]
        self.assertEqual(refine_search('team', metadata_soccer), expected_intersection2)

        expected_no_intersection = []
        metadata_fisk = search('fisk')
        self.assertEqual(refine_search('his', metadata_fisk), expected_no_intersection)

        expected_both_empty = []
        metadata_both_empty = []
        self.assertEqual(refine_search('thandiram', metadata_both_empty), expected_both_empty)

        expected_single_empty = []
        metadata_single_empty = []
        self.assertEqual(refine_search('his', metadata_single_empty), expected_single_empty)

        



    #####################
    # INTEGRATION TESTS #
    #####################

    # @patch('builtins.input')
    # def test_example_integration_test(self, input_mock):
    #     keyword = 'soccer'
    #     advanced_option = 1
    #     advanced_response = 3000

    #     output = get_print(input_mock, [keyword, advanced_option, advanced_response])
    #     expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]]\n"

    #     self.assertEqual(output, expected)

# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
