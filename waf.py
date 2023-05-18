import subprocess
import time

# Open the text file with the URLs
with open('universidades.txt', 'r') as file:
    urls = file.read().splitlines()


with open('waf.txt', 'w') as file:
    # Run WAFW00F for each URL
    for url in urls:
        # Run the WAFW00F command with the URL
        command = ['wafw00f', url]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        result, error = process.communicate()

        # Write the output to a file
        file.write(f'URL: {url}\n')
        file.write(result)
        file.write('\n ---------------- \n ---------------- \n')

        # Print the output
        print(result)
        print(error)


        time.sleep(10)