def __x_parse(code):
    output = []
    Code   = code.replace('\n', ' ')
    iter_  = 1
    for c in Code.split('"'):
        if iter_ % 2 == 1:
            output.append(c.replace(' ', ''))
            iter_ += 1
        else:
            output.append(c)
            iter_ += 1

    return output