from search import search, title_length, article_count, random_article, favorite_article, multiple_keywords, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_titles
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############
    def test_search(self):
        expected_cat_search_results = ['Voice classification in non-classical music']
        self.assertEqual(search('cat'), expected_cat_search_results)
        expected_empty_string_search_results = []
        self.assertEqual(search(''), expected_empty_search_string_results)
        expected_non_existent_search_results = []
        self.assertEqual(search('aashish'), expected_empty_search_string_results)
        expected_hi_string_search_result = ['Fiskerton, Lincolnshire', 'China national soccer team']
        self.assertEqual(search('hi'), expected_hi_string_search_result)
        expected_dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        self.assertEqual(search('dog'), expected_dog_search_results)
    

    def test_title_length(self):
        self.assertEqual(title_length(5, ['Aashish Panthi', 'Aasis']), ['Aasis'])
        self.assertEqual(title_length(9, ["The Matrix", "The Matrix Reloaded", "The Matrix Revolutions"]), [])
        self.assertEqual(title_length(10, ["The Matrix", "The Matrix Reloaded", "The Matrix Revolutions"]), ["The Matrix"])
        self.assertEqual(title_length(0, ['a', 'bb', 'ccc', 'dddd', 'eeeee']), [])
        self.assertEqual(title_length(0, []), [])
        self.assertEqual(title_length(10000, ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']), ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)'])

    def test_article_count(self):
        self.assertEqual(article_count(200, ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']), ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)'])
        self.assertEqual(article_count(1, ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']), ['Edogawa, Tokyo'])
        self.assertEqual(article_count(32, []), [])

    def test_random_article(self):
        self.assertEqual(random_article(-1, ['hello', 'world']), '')
        self.assertEqual(random_article(4, ['hello', 'world']), '')
        self.assertEqual(random_article(1, ['hello', 'world']), 'world')
        self.assertEqual(random_article(0, ['hello', 'world']), 'hello')



    def test_favorite_article(self):
        self.assertEqual(favorite_article('Sun dog', ['Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs']), True)
        self.assertEqual(favorite_article('sun Dog', ['Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs']), True)
        self.assertEqual(favorite_article('Aasis', ['Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs']), False)
        self.assertEqual(favorite_article('', ['Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs']), False)
        self.assertEqual(favorite_article('sundog', ['Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs']), False)
        self.assertEqual(favorite_article('Tech', []), False)
        self.assertEqual(favorite_article('', []) False)
    
    def test_multiple_keywords(self):
        #here cat(the later search) existed, but not the keyword previously searched
        self.assertEqual(multiple_keywords('cat', []), ['Voice classification in non-classical music'])
        #neither the first search nor the 'world' existed
        self.assertEqual(multiple_keywords('world', []), [])
        #both of the searches existed
        self.assertEqual(multiple_keywords('tokyo', ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']),['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)', 'Edogawa, Tokyo'])
        self.assertEqual(multiple_keywords('mexican', ['2007 Bulldogs RLFC season']), ['2007 Bulldogs RLFC season', 'Mexican dog-faced bat'])
        self.assertEqual(multiple_keywords('', ['2007 Bulldogs RLFC season']), ['2007 Bulldogs RLFC season'])
    
    




        

    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
        
    def test_opt1(self, input_mock):
        keyword = 'dog'
        advanced_option = 1
        user_input = 10

        output = get_print(input_mock, [keyword, advanced_option, user_input])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(user_input)  + "\nHere are your articles: ['Guide dog', 'Endoglin', 'Sun dog']\n"

        self.assertEqual(output, expected)


    def test_opt2(self, input_mock):
        keyword = 'cat'
        advanced_option = 2
        user_input = 3

        output = get_print(input_mock, [keyword, advanced_option, user_input])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(user_input) + "\nHere are your articles: ['Voice classification in non-classical music']\n"

        self.assertEqual(output, expected)


    def test_opt3(self, input_mock):
        keyword = 'football'
        advanced_option = 3
        user_input = 2

        output = get_print(input_mock, [keyword, advanced_option, user_input])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(user_input) + '\nHere are your articles: Georgia Bulldogs football under Robert Winston\n'

        self.assertEqual(output, expected)


    def test_opt4(self, input_mock):
        keyword = 'dog'
        advanced_option = 4
        user_input = 'Kevin Cadogan'

        output = get_print(input_mock, [keyword, advanced_option, user_input])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + user_input + "\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']" + '\nYour favorite article is in the returned articles!\n'

        self.assertEqual(output, expected)
    

    def test_opt5(self, input_mock):
        keyword = 'dog'
        advanced_option = 5
        user_input = 'tokyo'

        output = get_print(input_mock, [keyword, advanced_option, user_input])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + user_input + "\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)', 'Edogawa, Tokyo']\n"

        self.assertEqual(output, expected)


    def test_opt6(self, input_mock):
        keyword = 'Tech'
        advanced_option = 6
        
        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option)+ "\nHere are your articles: ['2009 Louisiana Tech Bulldogs football team']\n"

        self.assertEqual(output, expected)


# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()