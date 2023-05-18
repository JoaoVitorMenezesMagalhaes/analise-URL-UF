import subprocess
from urllib.parse import urlparse

# Open the text file with the URLs
with open('teste.txt', 'r') as file:
    urls = file.read().splitlines()

# Open the output file to save the results
with open('server_url.txt', 'w') as output_file:
    # Process each URL
    for url in urls:
        # Extract the host part of the URL
        parsed_url = urlparse(url)
        host = parsed_url.netloc

        # Execute the curl command
        command = ['curl', '-I', host]
        result = subprocess.run(command, capture_output=True, text=True)

        # Extract the server and URL information from the command output
        server_info = ''
        location_info = ''
        for line in result.stdout.splitlines():
            if line.startswith('Server:'):
                server_info = line
            elif line.startswith('Location:'):
                location_info = line

        # Write the server and URL information to the output file
        output_file.write(f'URL: {host}\n')
        output_file.write(f'{server_info}\n')
        output_file.write(f'{location_info}\n')
        output_file.write('\n')

        # Print the server and URL information
        print(f'URL: {host}')
        print(server_info)
        print(location_info)
        print()