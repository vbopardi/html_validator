#!/bin/python3


def validate_html(html):
    '''
    Checks whether every opening tag has a
    corresponding closing tag.
    '''

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
    Extract HTML tags from string
    '''
    l1 = []
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
                        l1.append(html[i:j + 1])
        for i in range(len(l1)):
            if l1[i].count('<') == 1:
                l2.append(l1[i])

        return l2
