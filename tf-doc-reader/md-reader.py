import re


token_specification = [
    ('REQUIRED_ARG', r'^.*`(?P<arg_name>\S.*)`.*\((?P<is_required>Required)\)\s+(?P<desc>.*)$' ),
    ('OPTIONAL_ARG', r''),
    ('BLOCK_START', r'`(?P<arg_name>\S.*)`.*block supports the following')
]

with open("azurerm_function_app_flex_consumption.md", "r") as file:
    for line in file:
        for t_spec in token_specification:
            for match in re.finditer(t_spec[1], line):
                if t_spec[0] == 'REQUIRED_ARG':
                    print(f'{t_spec[0]}: arg_name = {match.group("arg_name")}, is_required = {match.group("is_required")}, desc = {match.group("desc")}')
                elif t_spec[0] == 'OPTIONAL_ARG':
                    print(f'{t_spec[0]}: arg_name = {match.group("arg_name")}, is_required = {match.group("is_required")}, desc = {match.group("desc")}, default = {match.group("default")}')
                elif t_spec[0] == 'BLOCK_START':
                    print(f'{t_spec[0]}: arg_name = {match.group("arg_name")}')
                
                    
