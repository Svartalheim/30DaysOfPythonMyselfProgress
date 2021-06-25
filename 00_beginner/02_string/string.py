message = 'Svartalheim\'s world'
message_space = """"This will recognize the value if we enter it as long as the end of the
tick"""
# \ (backslash) for recognize with ' as a string in the middle
print(len(message))
print(message_space[0])
print(message[0:5])
# the first number (0) is real value then the last (5) is decreased by 1,
# if there is no second number then it will show til the end of index
# =============== function ==========================
# ============message.function()===================== 
msg_low = message.lower()
# .lower() make all string to lowercase, .upper() sebaliknya
msg_count = message.count('world')
# .count('your text want to find'), show how much string what u want to find
# in that variable
msg_find = message.find('v')
# .find('your text want to find), find first index of what u want to find
#  if not found then the result is -1
msg_replace = message.replace('world', 'Domain')
# .replace('message in variable','new replaced string') but this must have
# sent in new variable because this return
msg_format = '{}, {}. Welcome!'.format(message, message_space)
# .format() fill the bracket according to variable inside the format
msg_fstring = f'{message}, {message_space}. Welcome!'
#F string is just for make simple using variable inside string,
# and inside the bracket you can pass function
msg_dir = dir(message)
# dir is for show all the attributes and method that can be found inside that
# variable

# if you confuse you can just type print(help(str)) and you
# can search for specific function ex: print(help(str.lower))
