import pathlib
import subprocess

files = [file for file in list(pathlib.Path(r'C:\Users\Milo\OneDrive - Universiteit Utrecht\Scriptie\Data\dutch_data\Test\individual_lines').resolve().iterdir()) if file.is_file() and file.suffix == '.txt']

tool_path = pathlib.Path(r"LineFromPointCloud.exe")

for file in files:
    output_file = file.with_name(file.stem + '-')
    command = f'{tool_path} --input_file="{file}" --output_folder="{output_file}" -k 20'
    print(f"Running command: {command}")
    result = subprocess.run(command, capture_output=True, text=True, shell=True)

    print(f"Exit code: {result.returncode}")
    print(result.stdout)
    print(result.stderr)
    exit()