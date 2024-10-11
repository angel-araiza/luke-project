import requests  

#URL of the XML file for the Luke
url = "https://read.csbible.com/wp-content/themes/lwcsbread/CSB_XML//42-Luke.xml"

# Define headers to include a User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

def fetch_luke():
    try:
        # Send a GET request to the URL
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        response.raise_for_status() # Rasise an error for 4xx/5xx status codes

        # Get the content of the response
        content = response.text

        # Optional: Save to a file
        with open("luke.xml", "w", encoding="utf-8") as file:
            file.write(content)

        print("Successfully fetched the Book of Luke and saved to luke.txt")

    except requests.RequestException as e:
        print(f"Error fetching the book of Luke: {e}")

if __name__ == "__main__":
    fetch_luke()


