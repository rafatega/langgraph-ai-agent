import os

creds = None
working_dir = r"C:\Users\Tega\Documents\Projetos\APIs"
token_dir = ''
token_file = f'token_calendar_mcp_0001.json'

# Check if token dir exists first, if not, create the folder
if not os.path.exists(os.path.join(working_dir, token_dir)):
    os.mkdir(os.path.join(working_dir, token_dir))
if os.path.exists(os.path.join(working_dir, token_dir, token_file)):
    print("existe")