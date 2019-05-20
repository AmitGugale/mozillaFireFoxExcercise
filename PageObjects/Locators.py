class Locators(object):

    # Google Search Page Locators

    search_textbox = "q"
    search_result_set = "//ul[@role='listbox']//li/descendant::div[@class='sbl1']/span"

    # Google Search Results Page Locators
    search_result_result_links = "//h3[@class='LC20lb']"

    # Mozilla Firefox Main Page
    all_languages_link = "//a[contains(text(), 'Download in another language')]"

    mozilla_main_logo = "//*[@id='outer-wrapper']/main/div[1]/div[2]/div[1]/h2[1]/a/img"

    # Mozilla All Language Page
    all_languages_logo = "//*[@id='masthead']/h2/a/img"

    language_table = "//table/tbody/tr/th/strong"

