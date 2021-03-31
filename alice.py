""" Alice knows that NSA agents use the following algorithm to cipher their messages.
    1) They delete all spaces and punctuation marks.
    2) They replace all successive identical letters with only one such letter.
    3) They insert two identical letters at an arbitrary place many times.
    Alice has intercepted some messages which are "meaningless" sequences of letters that NSA agent Bob
    has sent to another NSA agent Alice about possible Alice’s location. He wants to be able to restore
    the message as it was after step 2). Help Alice write a program in Python that removes all pairs of
    identical letters from the message inserted in the third step.
"""

from loguru import logger
logger.add('logger.log', level='INFO', format="{time} | {level} | {message}",
           rotation='1 MB', compression='zip')


@logger.catch
def remove_pairs():
    """
    Function removes all pairs of
    identical letters from the message
    :return: string
    """
    # open and read file
    text = open('cipheredmessage.txt').read()
    # convert string to list
    lst = [text[i] for i in range(len(text))]
    count = 0
    while count < (len(lst) - 1):
        # check pair of symbols
        if lst[count] == lst[count + 1]:
            # delete first element
            lst.pop(count)
            # delete second element
            lst.pop(count)
            # if remove two element back to check previous
            if count != 0:
                count -= 1
            continue
        else:
            # if symbols not equal go to next
            count += 1
    # convert list to string
    result = ''.join(lst)
    logger.info('Function completed successfully')
    return print(result)


if __name__ == '__main__':
    remove_pairs()
