import webbrowser
def checkError(func):
    def Decorated(*arg,**kwarg):
        try:
            func(*arg,**kwarg)
        except Exception as Error:
            question = '+'.join(str(Error).split())
            print(question)
            webbrowser.open('https://www.google.com/search?q=python+'+ question)  
    return Decorated