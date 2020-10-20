"""
Wiki
20/10/2020
This program displays wikipedia pages chosen by user input.
"""

import wikipedia


def main():
    """While user input is not blank, display wikipedia page summary or possible options if page does not exist."""
    page = input("Page: ")
    while page != "":
        try:
            page_summary = wikipedia.summary(page)
            print(page_summary)
        except wikipedia.exceptions.PageError:
            print(f"Page \"{page}\" does not exist. Try another query!")
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"Here are some disambiguation pages for {page}:")
            for option in e.options:
                print(option)
        page = input("\nPage: ")
    print("Goodbye!")


if __name__ == '__main__':
    main()
