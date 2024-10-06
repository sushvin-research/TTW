from pandocfilters import toJSONFilter, Link, RawInline, RawBlock, Str


def open_in_new_tab(key, value, format, meta):
    if key == 'Link':
        [[ident, classes, kvs], text, [url, title]] = value
        kvs.append(['target', '_blank'])
        kvs.append(['class', 'action-button'])
        return Link([ident, classes, kvs], text, [url, title])


if __name__ == "__main__":
    toJSONFilter(open_in_new_tab)
