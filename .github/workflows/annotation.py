def fetch_google_doc(url):
    """Fetches the content from the Google Doc URL."""
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve document. Status code: {response.status_code}")
    return response.text

def parse_grid_data(doc_data):
    """Parses the document data into a list of tuples representing (x, y, character)."""
    lines = doc_data.splitlines()
    grid_data = []
    for line in lines:
        parts = line.split(',')
        if len(parts) == 3:
            x, y, char = int(parts[0]), int(parts[1]), parts[2]
            grid_data.append((x, y, char))
    return grid_data

def create_grid(grid_data):
    """Creates the grid with characters placed at the correct coordinates."""
    # Determine the size of the grid based on the max x and y values
    max_x = max(grid_data, key=lambda x: x[0])[0]
    max_y = max(grid_data, key=lambda x: x[1])[1]

    # Initialize an empty grid filled with spaces
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Place characters in the grid based on the coordinates
    for x, y, char in grid_data:
        grid[y][x] = char

    return grid

def print_grid(grid):
    """Prints the grid in a fixed-width font."""
    for row in grid:
        print(''.join(row))

def generate_secret_message(url):
    """Main function to generate and display the secret message from the Google Doc URL."""
    doc_data = fetch_google_doc(url)
    grid_data = parse_grid_data(doc_data)
    grid = create_grid(grid_data)
    print_grid(grid)

