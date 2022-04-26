import requests
from bs4 import BeautifulSoup

class Word:
    ROOT = 'https://www.duden.de'
    WORD_ROOT = 'https://www.duden.de/rechtschreibung/'

    def __init__(self, word):
        url = self.WORD_ROOT + word
        response = requests.get(url)
        html = response.content
        self.soup = BeautifulSoup(html, 'html.parser')
        self.grammatik = self.__get_grammatik()

    @property
    def title(self) -> str:
        """
        Returns:
            str: Word with article.
        """
        text = self.soup.h1.text
        return self.__clear_text(text)

    @property
    def name(self) -> str:
        """
        Returns:
            str: Word without article.
        """
        text = self.soup.find('span', {'class': 'lemma__main'}).text
        return self.__clear_text(text)

    @property
    def pos(self) -> str:
        """
        Returns:
            str: Part of speech.
        """
        return self.__search_wortart()

    @property
    def article(self) -> str:
        """
        Returns:
            str: Article
        """
        if 'Substantiv' not in self.pos or ', ' not in self.title:
            return None

        return self.title.split(', ')[1]

    @property
    def plural(self) -> str:
        """
        Returns:
            str: Plural
        """
        if 'Substantiv' in self.pos:
            plural = self.grammatik.find_all('div', {'class': 'accordion-table'})[1].text
            return plural

        return None


    def __search_wortart(self, element=None):
        if element is None:
            element = self.soup

        dls = self.soup.find_all('dl', {'class': 'tuple'})
        for dl in dls:
            dt = dl.find('dt')
            if 'Wortart' in dt.text:
                return dl.find('dd').text

        return None

    def __clear_text(self, text) -> str:
        """Clears text from soft spaces.

        Returns:
            str: Cleared text
        """
        return text.replace('\xad', '')

    def __get_grammatik(self) -> BeautifulSoup:
        """Returns the page for the grammatik section.

        Returns:
            BeautifulSoup: Grammatik section.
        """
        link = self.ROOT + self.soup.find('a', {'id': 'grammatik'}).attrs['href']
        html = requests.get(link).content
        return BeautifulSoup(html, 'html.parser')

w = Word('arbeiten')
print(w.pos)