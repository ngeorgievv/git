import yaml


def load_yaml_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except yaml.YAMLError as exc:
        print(f"Error while parsing YAML file: {exc}")
        return None


# Function to extract titles and format them as "title1", "title2", "title3"
def extract_titles(yaml_data):
    if yaml_data is None:
        return ""

    titles = []
    for entry in yaml_data:
        title = entry.get('title', 'No title found')
        titles.append(f'"{title}"')

    # Join titles with commas and return the formatted string
    return ', '.join(titles)


# File path to your YAML file
file_path = r"C:\Users\nikol\Downloads\habanero.yaml"

# Load the YAML file
yaml_data = load_yaml_file(file_path)

# Extract and format titles
if yaml_data:
    formatted_titles = extract_titles(yaml_data)
    print(formatted_titles)
else:
    print("Failed to load or parse YAML file.")