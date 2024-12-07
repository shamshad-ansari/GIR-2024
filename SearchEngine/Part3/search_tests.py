from search import keyword_to_titles, title_to_info, search, article_length,key_by_author, filter_to_author, filter_out, articles_from_year
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        dummy_keyword_dict = {
            'cat': ['title1', 'title2', 'title3'],
            'dog': ['title3', 'title4']
        }
        expected_search_results = ['title3', 'title4']
        self.assertEqual(search('dog', dummy_keyword_dict), expected_search_results)

    
    def test_keyword_to_titles(self):

        dummy_metadata = []
        expected_result = {}
        self.assertEqual(keyword_to_titles(dummy_metadata), expected_result)

        dummy_metadata = [[], [], []]
        expected_result = {}
        self.assertEqual(keyword_to_titles(dummy_metadata), expected_result)

        
        dummy_metadata = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526, ['beach', 'soccer', 'fifa', 'award']],
            ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 4144, ['kennedy', 'was', 'computer', 'and', 'the', 'for', 'award']]
        ]
        expected_result = {
            'beach':['Spain national beach soccer team'],
            'soccer':['Spain national beach soccer team'],
            'fifa': ['Spain national beach soccer team'],
            'award':['Spain national beach soccer team', 'Ken Kennedy (computer scientist)'],
            'kennedy':['Ken Kennedy (computer scientist)'],
             'was':['Ken Kennedy (computer scientist)'], 
             'computer':['Ken Kennedy (computer scientist)'], 
             'and':['Ken Kennedy (computer scientist)'], 
             'the':['Ken Kennedy (computer scientist)'], 
             'for':['Ken Kennedy (computer scientist)']

        }
        self.assertEqual(keyword_to_titles(dummy_metadata), expected_result)

        dummy_metadata = [
            ["Semaphore (programming)", "Nihonjoe", 1144850850, 7616, ["test keyword only"]],
            ["Wake Forest Demon Deacons men's soccer", "Burna Boy", 1260577388, 26745, ["test keyword only"]]
        ]

        expected_result = {
            'test keyword only' : ["Semaphore (programming)", "Wake Forest Demon Deacons men's soccer"]
        }
        self.assertEqual(keyword_to_titles(dummy_metadata), expected_result)


    def test_title_to_info(self):
        
        dummy_metadata = []
        expected_result = {}
        self.assertEqual(title_to_info(dummy_metadata), expected_result)

        dummy_metadata = [[], [], []]
        expected_result = {}
        self.assertEqual(title_to_info(dummy_metadata), expected_result)
        
        dummy_metadata = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526, ['beach', 'soccer', 'fifa', 'award']],
            ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 4144, ['kennedy', 'was', 'computer', 'and', 'the', 'for', 'award']],
            ["Semaphore (programming)", "Nihonjoe", 1144850850, 7616, ["test keyword only"]]
        ]
        expected_result = {
            'Spain national beach soccer team': {'author':'jack johnson', 'timestamp':1233458894, 'length':1526},
            'Ken Kennedy (computer scientist)': {'author': 'Mack Johnson', 'timestamp':1246308670, 'length':4144},
            "Semaphore (programming)": {'author':'Nihonjoe', 'timestamp':1144850850, 'length': 7616}
        }
        self.assertEqual(title_to_info(dummy_metadata), expected_result)


    def test_search(self):

        dummy_data = {
            'beach':['Spain national beach soccer team'],
            'fifa': ['Real Madrid', 'Barcelona'],
            'award':['Spain national beach soccer team', 'Ken Kennedy (computer scientist)'],
            'kennedy':['Ken Kennedy (computer scientist)']
        }

        expected_result = ['Spain national beach soccer team', 'Ken Kennedy (computer scientist)']
        self.assertEqual(search('award', dummy_data), expected_result)

        dummy_data = {
            'beach':['Spain national beach soccer team'],
            'fifa': ['Real Madrid', 'Barcelona'],
            'award':['Spain national beach soccer team', 'Ken Kennedy (computer scientist)'],
            'kennedy':['Ken Kennedy (computer scientist)']
        }

        expected_result = []
        self.assertEqual(search('Beach', dummy_data), expected_result)

        dummy_data = {
            'beach':['Spain national beach soccer team'],
            'fifa': ['Real Madrid', 'Barcelona'],
            'award':['Spain national beach soccer team', 'Ken Kennedy (computer scientist)'],
            'kennedy':['Ken Kennedy (computer scientist)'],
        }

        expected_result = []
        self.assertEqual(search('', dummy_data), expected_result)

        dummy_data = {
            'beach':['Spain national beach soccer team'],
            'fifa': ['Real Madrid', 'Barcelona'],
            'award':['Spain national beach soccer team', 'Ken Kennedy (computer scientist)'],
            'kennedy':['Ken Kennedy (computer scientist)'],
        }

        expected_result = []
        self.assertEqual(search('Viral', dummy_data), expected_result)

    

    def test_article_length(self):

        dummy_metadata = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526, ['beach', 'soccer', 'fifa', 'award']],
            ['German national beach soccer team', 'jack johnson', 1233458894, 4144, ['football', 'award']],
            ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 1300, ['kennedy', 'was', 'computer', 'and', 'the', 'for', 'award']]
        ]
        dummy_article_titles = search('award', keyword_to_titles(dummy_metadata))
        expected_result = ['Spain national beach soccer team', 'Ken Kennedy (computer scientist)']
        self.assertEqual(article_length(2000, dummy_article_titles, title_to_info(dummy_metadata)), expected_result)

        dummy_metadata = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526, ['beach', 'soccer', 'fifa', 'award']],
            ['German national beach soccer team', 'jack johnson', 1233458894, 4144, ['football', 'award']],
            ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 1300, ['kennedy', 'was', 'computer', 'and', 'the', 'for', 'award']]
        ]
        dummy_article_titles = search('Viral', keyword_to_titles(dummy_metadata))
        expected_result = []
        self.assertEqual(article_length(2000, dummy_article_titles, title_to_info(dummy_metadata)), expected_result)

        dummy_metadata = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526, ['beach', 'soccer', 'fifa', 'award']],
            ['German national beach soccer team', 'jack johnson', 1233458894, 4144, ['football', 'award']],
            ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 1300, ['kennedy', 'was', 'computer', 'and', 'the', 'for', 'award']]
        ]
        dummy_article_titles = search('award', keyword_to_titles(dummy_metadata))
        expected_result = []
        self.assertEqual(article_length(1000, dummy_article_titles, title_to_info(dummy_metadata)), expected_result)
        


    def test_key_by_author(self):

        dummy_metadata = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526, ['beach', 'soccer', 'fifa', 'award']],
            ['German national beach soccer team', 'jack johnson', 1233458894, 4144, ['football']],
            ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 1300, ['kennedy', 'was', 'computer', 'and', 'the', 'for', 'award']]
        ]
        dummy_article_titles = search('award', keyword_to_titles(dummy_metadata))
        expected_result ={
            'jack johnson' : ['Spain national beach soccer team'],
            'Mack Johnson' : ['Ken Kennedy (computer scientist)']
        }
        self.assertEqual(key_by_author(dummy_article_titles, title_to_info(dummy_metadata)), expected_result)

        dummy_metadata = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526, ['beach', 'soccer', 'fifa', 'award']],
            ['German national beach soccer team', 'jack johnson', 1233458894, 4144, ['football']],
            ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 1300, ['kennedy', 'was', 'computer', 'and', 'the', 'for', 'award']]
        ]
        dummy_article_titles = search('Award', keyword_to_titles(dummy_metadata))
        expected_result ={}
        self.assertEqual(key_by_author(dummy_article_titles, title_to_info(dummy_metadata)), expected_result)

        dummy_metadata = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526, ['beach', 'soccer', 'fifa', 'award']],
            ['German national beach soccer team', 'jack johnson', 1233458894, 4144, ['football', 'award']],
            ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 1300, ['kennedy', 'was', 'computer', 'and', 'the', 'for', 'award']]
        ]
        dummy_article_titles = search('award', keyword_to_titles(dummy_metadata))
        expected_result ={
            'jack johnson' : ['Spain national beach soccer team', 'German national beach soccer team'],
            'Mack Johnson' : ['Ken Kennedy (computer scientist)']
        }
        self.assertEqual(key_by_author(dummy_article_titles, title_to_info(dummy_metadata)), expected_result)


    def test_filter_to_author(self):

        dummy_metadata = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526, ['beach', 'soccer', 'fifa', 'award']],
            ['German national beach soccer team', 'Rack johnson', 1233458894, 4144, ['soccer']],
            ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 1300, ['kennedy', 'was', 'computer', 'and', 'the', 'for', 'award']]
        ]
        dummy_article_titles = search('soccer', keyword_to_titles(dummy_metadata))
        expected_result = ['Spain national beach soccer team']
        self.assertEqual(filter_to_author('jack johnson', dummy_article_titles, title_to_info(dummy_metadata)), expected_result)

        dummy_metadata = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526, ['beach', 'soccer', 'fifa', 'award']],
            ['German national beach soccer team', 'Rack johnson', 1233458894, 4144, ['soccer']],
            ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 1300, ['kennedy', 'was', 'computer', 'and', 'the', 'for', 'award']]
        ]
        dummy_article_titles = search('soccer', keyword_to_titles(dummy_metadata))
        expected_result = []
        self.assertEqual(filter_to_author('Jack johnson', dummy_article_titles, title_to_info(dummy_metadata)), expected_result)

        dummy_metadata = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526, ['beach', 'soccer', 'fifa', 'award']],
            ['German national beach soccer team', 'Rack johnson', 1233458894, 4144, ['soccer']],
            ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 1300, ['kennedy', 'was', 'computer', 'and', 'the', 'for', 'award']]
        ]
        dummy_article_titles = search('viral', keyword_to_titles(dummy_metadata))
        expected_result = []
        self.assertEqual(filter_to_author('jack johnson', dummy_article_titles, title_to_info(dummy_metadata)), expected_result)


    def test_filter_out(self):

        dummy_metadata = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526, ['beach', 'soccer', 'fifa', 'award']],
            ['German national beach soccer team', 'Rack johnson', 1233458894, 4144, ['soccer']],
            ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 1300, ['kennedy', 'was', 'computer', 'and', 'the', 'for', 'award']]
        ]
        dummy_article_titles = search('soccer', keyword_to_titles(dummy_metadata))
        expected_result = ['German national beach soccer team']
        self.assertEqual(filter_out('award', dummy_article_titles, keyword_to_titles(dummy_metadata)), expected_result)

        dummy_metadata = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526, ['beach', 'soccer', 'fifa', 'award']],
            ['German national beach soccer team', 'Rack johnson', 1233458894, 4144, ['soccer', 'award']],
            ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 1300, ['kennedy', 'was', 'computer', 'and', 'the', 'for', 'award']]
        ]
        dummy_article_titles = search('soccer', keyword_to_titles(dummy_metadata))
        expected_result = []
        self.assertEqual(filter_out('award', dummy_article_titles, keyword_to_titles(dummy_metadata)), expected_result)

        dummy_metadata = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526, ['beach', 'soccer', 'fifa', 'award']],
            ['German national beach soccer team', 'Rack johnson', 1233458894, 4144, ['soccer']],
            ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 1300, ['kennedy', 'was', 'computer', 'and', 'the', 'for', 'award']]
        ]
        dummy_article_titles = search('soccer', keyword_to_titles(dummy_metadata))
        expected_result = ['Spain national beach soccer team', 'German national beach soccer team']
        self.assertEqual(filter_out('', dummy_article_titles, keyword_to_titles(dummy_metadata)), expected_result)

        dummy_metadata = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526, ['beach', 'soccer', 'fifa', 'award']],
            ['German national beach soccer team', 'Rack johnson', 1233458894, 4144, ['soccer']],
            ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 1300, ['kennedy', 'was', 'computer', 'and', 'the', 'for', 'award']]
        ]
        dummy_article_titles = search('soccer', keyword_to_titles(dummy_metadata))
        expected_result = ['Spain national beach soccer team', 'German national beach soccer team']
        self.assertEqual(filter_out('Pele', dummy_article_titles, keyword_to_titles(dummy_metadata)), expected_result)

    
    def test_articles_from_year(self):

        dummy_metadata = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526, ['beach', 'soccer', 'fifa', 'award']],
            ['German national beach soccer team', 'Rack johnson', 1233458894, 4144, ['soccer', 'award']],
            ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 1300, ['kennedy', 'was', 'computer', 'and', 'the', 'for', 'award']]
        ]
        dummy_article_titles = search('soccer', keyword_to_titles(dummy_metadata))
        expected_result = []
        self.assertEqual(articles_from_year(2024, dummy_article_titles, title_to_info(dummy_metadata)), expected_result)

        dummy_metadata = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526, ['beach', 'soccer', 'fifa', 'award']],
            ['German national beach soccer team', 'Rack johnson', 133345889, 4144, ['soccer', 'award']],
            ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 1300, ['kennedy', 'was', 'computer', 'and', 'the', 'for', 'award']]
        ]
        dummy_article_titles = search('soccer', keyword_to_titles(dummy_metadata))
        expected_result = ['Spain national beach soccer team']
        self.assertEqual(articles_from_year(2009, dummy_article_titles, title_to_info(dummy_metadata)), expected_result)

        dummy_metadata = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526, ['beach', 'soccer', 'fifa', 'award']],
            ['German national beach soccer team', 'Rack johnson',1133458890, 4144, ['soccer', 'award']],
            ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 1300, ['kennedy', 'was', 'computer', 'and', 'the', 'for', 'award']]
        ]
        dummy_article_titles = search('award', keyword_to_titles(dummy_metadata))
        expected_result = ['Spain national beach soccer team', 'Ken Kennedy (computer scientist)']
        self.assertEqual(articles_from_year(2009, dummy_article_titles, title_to_info(dummy_metadata)), expected_result)


    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'soccer'
        advanced_option = 5
        advanced_response = 2009

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Spain national beach soccer team', 'Steven Cohen (soccer)']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_award_keyword_articles_500_length(self, input_mock):
        keyword = 'award'
        advanced_option = 1
        advanced_response = 500

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['The Hunchback of Notre Dame (musical)']\n"
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_award_keyword_articles_0_length(self, input_mock):
        keyword = 'award'
        advanced_option = 1
        advanced_response = 0

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nNo articles found\n"
        self.assertEqual(output, expected
        )
    @patch('builtins.input')
    def test_award_keyword_articles_key_by_author(self, input_mock):
        keyword = 'award'
        advanced_option = 2

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: {'Mack Johnson': ['Ken Kennedy (computer scientist)'], 'Nihonjoe': ['The Hunchback of Notre Dame (musical)']}\n"
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_no_award_keyword_articles_key_by_author(self, input_mock):
        keyword = 'Award'
        advanced_option = 2

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nNo articles found\n"
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_award_keyword_articles_filter_to_author(self, input_mock):
        keyword = 'award'
        advanced_option = 3
        advanced_response = 'Mack Johnson'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Ken Kennedy (computer scientist)']\n"
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_no_award_keyword_articles_filter_to_author(self, input_mock):
        keyword = 'award'
        advanced_option = 3
        advanced_response = 'jack Johnson'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nNo articles found\n"
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_award_keyword_articles_filter_out_dog(self, input_mock):
        keyword = 'award'
        advanced_option = 4
        advanced_response = 'dog'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Ken Kennedy (computer scientist)', 'The Hunchback of Notre Dame (musical)']\n"
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_award_keyword_articles_filter_out_computer(self, input_mock):
        keyword = 'award'
        advanced_option = 4
        advanced_response = 'computer'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['The Hunchback of Notre Dame (musical)']\n"
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_award_keyword_articles_from_2009(self, input_mock):
        keyword = 'award'
        advanced_option = 5
        advanced_response = 2009

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Ken Kennedy (computer scientist)']\n"
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_basic_search_award(self, input_mock):
        keyword = 'award'
        advanced_option = 6

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['Ken Kennedy (computer scientist)', 'The Hunchback of Notre Dame (musical)']\n"
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_basic_search_Award(self, input_mock):
        keyword = 'Award'
        advanced_option = 6

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nNo articles found\n"
        self.assertEqual(output, expected)


    

# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()

