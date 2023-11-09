import textwrap

def wrap(string, max_width):
    result = ""
    wrapper = textwrap.TextWrapper(width=max_width) 
    word_list = wrapper.wrap(text=string) 
    
    for i in word_list:
        result+=i
        result+="\n"
    
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
