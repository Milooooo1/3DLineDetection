import pathlib
import subprocess
import os

files = [file for file in list(pathlib.Path(r'C:\Users\Milo\OneDrive - Universiteit Utrecht\Scriptie\Data\dutch_data\Test\individual_lines').resolve().iterdir()) if file.is_file() and file.suffix == '.txt']

tool_path = pathlib.Path(r"LineFromPointCloud.exe")

for file in files:
    output_file = file.with_name(file.stem + '-')
    command = [str(tool_path), f'--input_file="{str(file)}"', f'--output_folder="{str(output_file)}"', '-k', '200']
    
    print(f"Running command: {' '.join(command)} in {os.getcwd()}")
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True, shell=False, cwd=os.getcwd(), env=os.environ) 
        print(f"Exit code: {result.returncode}")
        print("Standard Output:")
        print(result.stdout)
        print("Standard Error:")
        print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code {e.returncode}")
        print(f"Output: {e.output}")
        print(f"Error: {e.stderr}")
    except Exception as ex:
        print(f"Unexpected error: {ex}")
    
    
    break  # Exit after one iteration for debugging