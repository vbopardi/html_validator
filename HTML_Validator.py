#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    # HINT:
    # use the _extract_tags function below to generate a list of html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm from the class/book
    # the main difference between your code and the code from class will be that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags


    if type(html) == list:
        html = ''.join(html)

    # Base case
    if len(html) == 0:
        return True

    # Run extract tags
    taglist = _extract_tags(html)
    stack = []

    if taglist[0][0] == '<':
        stack.append(taglist[0])
        f = list(taglist[0])
        f.insert(1, '/')
        if f == list(taglist[-1]):
            stack.pop()
            return validate_html(taglist[1:-1])
        elif f == list(taglist[1]):
            stack.pop()
            return validate_html(taglist[2:])
        else:
            return False


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''


    l = []
    l2 = []
    if len(html) == 0:
        return l2
    elif '<' not in html:
        return l2
    else:
        for i in range(len(html)):
            if html[i] == '<':
                for j in range(i, len(html)):
                    if html[j] == '>':
                        l.append(html[i:j + 1])
        for i in range(len(l)):
            if l[i].count('<') == 1:
                l2.append(l[i])

        return l2
