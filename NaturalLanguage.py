import sys
sys.dont_write_bytecode = True
import nltk

from .Commands import Command
from .Error import ErrorHandler

class LanguageParser:
    def __init__(self):
        self.Cmd = Command()
        self.Error = ErrorHandler()

    def CreateTokens(self, TokenType: str = "word", Content: str or list = "" or []):
        self.TokenType: str = TokenType
        self.Content: str or list = Content

        if(self.TokenType == "word" or self.TokenType == "words"):
            if(type(self.Content) == str):
                return nltk.word_tokenize(self.Content)
            elif(type(self.Content) == list and len(self.Content) != 0):
                if(len(self.Content) == 1):
                    return nltk.word_tokenize(self.Content[0])
                else:
                    return nltk.word_tokenize('\n'.join(self.Content))
            else:
                self.Cmd.Clear()
                print(self.Error.Throw("language_parse_words_failed"))
                return None
        elif(self.TokenType == "sentence" or self.TokenType == "sentences"):
            if(type(self.Content) == str):
                return nltk.sent_tokenize(self.Content)
            elif(type(self.Content) == list and len(self.Content) != 0):
                if(len(self.Content) == 1):
                    return nltk.sent_tokenize(self.Content[0])
                else:
                    return nltk.sent_tokenize('\n'.join(self.Content))
            else:
                self.Cmd.Clear()
                print(self.Error.Throw("language_parse_sentences_failed"))
                return None
        else:
            self.Cmd.Clear()
            print(self.Error.Throw("language_invalid_token_type", self.TokenType))
            return None

    def CreateTokensWithoutPunctuation(self, Content: str = ""):
        self.Tokenizer = nltk.RegexpTokenizer(r"\w+")
        return self.Tokenizer.tokenize(Content)
