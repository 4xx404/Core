import sys
sys.dont_write_bytecode = True

from .Styling.Banners import sd
from .Styling.Colors import bc

class ErrorHandler:
    def __init__(self):
        self.DefinedErrors: list = [
            # Input Class Error Tags
            ## Link Tags
            "empty_link_value",
            "invalid_link_protocol",
            "invalid_link_domain_extension",
            "invalid_link_format"

            ## Email Tags
            "empty_email_value",
            "invalid_email_format",

            ## Phone Number Tags
            "empty_phone_number_value",
            "invalid_phone_number_format",

            # Command Class Error Tags
            ## File Command Tags
            "file_move_failed",
            "create_directory_failed",
            "list_directory_failed",
            "change_directory_failed",
            "rename_file_or_dir_failed",
            "remove_directory_failed",

            # Geolocation Class Error Tags
            "find_by_address_failed",
            "find_by_coordinates_failed",
            "get_distance_failed",

            # Request Class Error Tags
            "request_get_content_no_response",
            "request_collect_all_links_no_response",

            # FileSystem Class Error Tags
            "read_from_file_failed",
            "write_to_file_failed",
            "append_to_file_failed",

            # Natural Language Error Tags
            "language_invalid_token_type",
            "language_parse_words_failed",
            "language_parse_sentences_failed"

        ]

    def Throw(self, ErrorType: str, ErrorData: str or list = None):
        self.ErrorType: str = ErrorType.lower()
        self.ErrorData: str or list = ErrorData

        if(self.ErrorType in self.DefinedErrors):
            # Input Class Error Messages - Links
            if(self.ErrorType == "empty_link_value"):
                return f"\n{sd.eBan} Link value cannot be empty\n"
            elif(self.ErrorType == "invalid_link_protocol"):
                return f"\n{sd.eBan} Invalid protocol in {bc.RC}{self.ErrorData}{bc.BC}, include {bc.GC}http://{bc.BC} or {bc.GC}https://{bc.BC}\n"
            elif(self.ErrorType == "invalid_link_domain_extension"):
                return f"\n{sd.eBan} Invalid domain extension in {bc.RC}{self.ErrorData}{bc.BC}\n"
            elif(self.ErrorType == "invalid_link_format"):
                return f"\n{sd.eBan} Link {bc.RC}{self.ErrorData}{bc.BC} is an invalid format\n"

            # Input Class Error Messages - Emails
            elif(self.ErrorType == "empty_email_value"):
                return f"\n{sd.eBan} Email value cannot be empty\n"
            elif(self.ErrorType == "invalid_email_format"):
                return f"\n{sd.eBan} Email {bc.RC}{self.ErrorData}{bc.BC} is an invalid format\n"

            # Input Class Error Messages - Phone Numbers
            elif(self.ErrorType == "empty_phone_number_value"):
                return f"\n{sd.eBan} Phone Number value cannot be empty\n"
            elif(self.ErrorType == "invalid_phone_number_format"):
                return f"\n{sd.eBan} Phone Number {bc.RC}{self.ErrorData}{bc.BC} is an invalid format\n"

            # Command Class Error Messages - File Commands
            elif(self.ErrorType == "file_move_failed"):
                return f"\n{sd.eBan} Failed to move {bc.RC}{self.ErrorData[0]}{bc.BC} to {bc.RC}{self.ErrorData[1]}{bc.BC}\n"
            elif(self.ErrorType == "create_directory_failed"):
                return f"\n{sd.eBan} Failed to create directory {bc.RC}{self.ErrorData}{bc.BC}\n"
            elif(self.ErrorType == "list_directory_failed"):
                return f"\n{sd.eBan} Failed to list directory {bc.RC}{self.ErrorData}{bc.BC}\n"
            elif(self.ErrorType == "change_directory_failed"):
                return f"\n{sd.eBan} Failed to change directory to {bc.RC}{self.ErrorData}{bc.BC}\n"
            elif(self.ErrorType == "rename_file_or_dir_failed"):
                return f"\n{sd.eBan} Failed to rename file {bc.RC}{self.ErrorData[0]}{bc.BC} to new name {bc.RC}{self.ErrorData[1]}{bc.BC}\n"
            elif(self.ErrorType == "remove_directory_failed"):
                return f"\n{sd.eBan} Failed to remove directory {bc.RC}{self.ErrorData}{bc.BC}\n"

            # Geolocation Class Error Messages
            elif(self.ErrorType == "find_by_address_failed"):
                return f"\n{sd.eBan} Failed to collect any data from address {bc.RC}{self.ErrorData}{bc.BC}\n"
            elif(self.ErrorType == "find_by_coordinates_failed"):
                return f"\n{sd.eBan} Failed to collect any data from latitude {bc.RC}{self.ErrorData[0]}{bc.BC} || longitude {bc.RC}{self.ErrorData[1]}{bc.BC}\n"
            elif(self.ErrorType == "get_distance_failed"):
                return f"\n{sd.eBan} Failed to get distance between latitude {bc.RC}{self.ErrorData[0]}{bc.BC} & longitude {bc.RC}{self.ErrorData[1]}{bc.BC}\n"

            # Request Class Error Messages
            elif(self.ErrorType == "request_get_content_no_response"):
                return f"\n{sd.eBan} Got no response from {bc.RC}{self.ErrorData}{bc.BC}, failed to get content\n"
            elif(self.ErrorType == "request_collect_all_links_no_response"):
                return f"\n{sd.eBan} Got no response from {bc.RC}{self.ErrorData}{bc.BC}, failed to collect all links\n"

            # FileSystem class Error Messages
            elif(self.ErrorType == "read_from_file_failed"):
                return f"\n{sd.eBan} Failed to read from file {bc.RC}{self.ErrorData}{bc.BC}\n"
            elif(self.ErrorType == "write_to_file_failed"):
                return f"\n{sd.eBan} Failed to write to file {bc.RC}{self.ErrorData}{bc.BC}\n"
            elif(self.ErrorType == "append_to_file_failed"):
                return f"\n{sd.eBan} Failed to append {bc.RC}{self.ErrorData[0]}{bc.BC} to {bc.RC}{self.ErrorData[1]}{bc.BC}\n"

            # NaturalLanguage Error Messages
            elif(self.ErrorType == "language_invalid_token_type"):
                return f"\n{sd.eBan} Invalid Natural Language Token Type {bc.RC}{self.ErrorData}{bc.BC}. Allowed types are {bc.GC}word{bc.BC} or {bc.GC}sentence{bc.BC}\n"
            elif(self.ErrorType == "language_parse_words_failed"):
                return f"\n{sd.eBan} Natural Language failed to create word tokens\n"
            elif(self.ErrorType == "language_parse_sentences_failed"):
                return f"\n{sd.eBan} Natural Language failed to create sentence tokens\n"
    
            # The ErrorType is defined but no Error Message is set, set the message above this line
            else:
                return f"\n{sd.eBan} Error message is not set for ErrorType {bc.RC}{self.ErrorType}{bc. BC}\n"

        # ErrorType is undefined, define the Error Tag in DefinedErrors
        else:
            return f"\n{sd.eBan} Undefined ErrorType {bc.RC}{self.ErrorType}{bc.BC}\n"
