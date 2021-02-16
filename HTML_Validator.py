#!/bin/python3


def validate_html(html):
    '''
    Checks whether every opening tag has a
    corresponding closing tag.
    '''

    # Base case
    if len(html) == 0:
        return True

    if type(html) == list:
        html = ''.join(html)

    # No closing tag
    if '</' not in html:
        return False

    # Run extract tags
    taglist = _extract_tags(html)
    stack = []

    # If it has only one tag, false
    if len(taglist) == 1:
        return False

    # closing cannot be first element in taglist
    if '</' in taglist[0]:
        return False

    # All other cases
    for i in range(len(taglist)):
        if '</' not in taglist[i]:
            stack.append(taglist[i])
        elif '</' in taglist[i]:
            f = list(stack[-1])
            f.insert(1, '/')
            if f == list(taglist[i]):
                stack.pop()
            else:
                return False
    return len(stack) == 0


def _extract_tags(html):
    '''
    Extract HTML tags from string
    '''
    taglist = []
    if len(html) == 0:
        return taglist
    elif '<' not in html:
        return taglist
    else:
        for i in range(len(html)):
            if html[i] == '<':
                f = i
            if html[i] == '>':
                e = i
                taglist.append(html[f:e + 1])
            if (html[i] == ' ') & ('<' in html[:i]):
                g = i
                taglist.append(html[f:g] + '>')
    fl = [k for k in taglist if (k.count('<')) == 1]
    fl = [k for k in fl if k.count('>') == 1]
    fl = [k for k in fl if ' ' not in k]

    return fl
