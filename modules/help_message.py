from colored import fg, attr


def color_word(color, word):
    return fg(color) + word + attr('reset')


help_message = f"""
{color_word('light_green', '.calendar')}: changes display to the calendar
    {color_word('light_green', '.week')}: proceeds to the next week
    {color_word('light_green', '.month')} {color_word('red', '[month name]')}: view [month name]
    {color_word('light_green', '.event')} {color_word('red', '[event name]')}: view event information
        {color_word('light_green', '.confirm')}: confirm event selection
"""
