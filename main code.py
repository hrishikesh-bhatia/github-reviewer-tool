import os
import requests
import base64

# Function to generate HTML report
def generate_html_report(repo_data):
    html_content = """
    <html>
    <head>
        <title>GitHub Repository Complexity Report</title>
        <style>
            body { font-family: Arial, sans-serif; }
            table { width: 100%; border-collapse: collapse; margin: 20px 0; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
            h1 { text-align: center; }
        </style>
    </head>
    <body>
        <h1>GitHub Repository Complexity Report</h1>
        <table>
            <tr>
                <th>Repository Name</th>
                <th>Total LOC</th>
                <th>Total Functions</th>
                <th>Complexity Score</th>
            </tr>
    """

    for repo in repo_data:
        html_content += f"""
            <tr>
                <td>{repo['name']}</td>
                <td>{repo['total_loc']}</td>
                <td>{repo['total_functions']}</td>
                <td>{repo['complexity_score']}</td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """

    # Write the HTML content to a file
    with open("complexity_report.html", "w") as report_file:
        report_file.write(html_content)

    print("HTML report generated: complexity_report.html")

# Main Code
github_username = input("Enter your GitHub username: ")
github_token = input("Enter your GitHub Personal Access Token: ")

headers = {"Authorization": f"token {github_token}"}
api_url = "https://api.github.com/user/repos"
response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    repos = response.json()
    print(f"Found {len(repos)} repositories")

    # Initialize an empty list to store repository data
    repo_data = []

    for repo in repos:
        repo_name = repo['name']
        print(f"Analyzing Repository: {repo_name}")
        repo_url = f"https://api.github.com/repos/{repo['owner']['login']}/{repo_name}/git/trees/main?recursive=1"
        repo_response = requests.get(repo_url, headers=headers)

        if repo_response.status_code == 200:
            repo_files = repo_response.json().get('tree', [])
            code_files = [
                file for file in repo_files
                if file['path'].endswith(('.py', '.cpp', '.js'))
            ]

            total_loc = 0
            total_functions = 0
            complexity_score = 0

            for code_file in code_files:
                print(f"Fetching code file: {code_file['path']}")
                file_url = code_file['url']
                file_response = requests.get(file_url, headers=headers)

                if file_response.status_code == 200:
                    file_content = file_response.json().get('content', '')
                    file_content_decoded = base64.b64decode(
                        file_content).decode('utf-8')

                    loc = file_content_decoded.count('\n')
                    total_loc += loc
                    function_count = file_content_decoded.count(
                        'def ') + file_content_decoded.count('function ')
                    total_functions += function_count
                    complexity_score += loc / 100 + function_count * 2

                    print(
                        f"File: {code_file['path']}, LOC: {loc}, Functions: {function_count}"
                    )

            # Collect repository data
            repo_info = {
                'name': repo_name,
                'total_loc': total_loc,
                'total_functions': total_functions,
                'complexity_score': complexity_score
            }
            repo_data.append(repo_info)

            print(
                f"Repository: {repo_name}, Total LOC: {total_loc}, Total Functions: {total_functions}, Complexity Score: {complexity_score}"
            )
        else:
            print(f"Failed to fetch files for repository: {repo_name}")

    # Generate HTML report after analyzing all repositories
    generate_html_report(repo_data)

    # Download the HTML report
    from google.colab import files
    files.download("complexity_report.html")
else:
    print(
        f"Failed to fetch repositories. Status code: {response.status_code}, Error: {response.text}"
    )
