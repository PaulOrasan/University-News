import webbrowser
class Browser:
    @staticmethod
    def initialize():
        '''
        Register chrome as a web browser to be used
        '''
        webbrowser.register('chrome',None,
                            webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
    @staticmethod
    def openLink(link):
        '''
        Opens a new link using the registered web browser
        link - string that represents the address that needs to be accessed
        '''
        webbrowser.get('chrome').open(link)

