from cx_Freeze import setup, Executable
setup(name="Password generator", version="1.0", description="Get your password", executables=[Executable("pass_generate.py")])
