def get_command_args(args:str) -> list:
    """Bot is getting arguments after the command"""
    return args.split()[1:]

def get_args(args:str) -> list:
    """Bot is getting arguments after the command"""
    return args.split()

def embrace_text(text:str,embrace_with:str="`") -> str:
    """Embracing text"""
    return embrace_with + text + embrace_with