# GitHub Repository Complexity Analyzer

## Project Overview

This project analyzes the complexity of repositories on your GitHub account. It calculates metrics such as:

- **Lines of Code (LOC)**: The total number of lines of code in the repository.
- **Number of Functions**: The total number of functions in the repository's code files.
- **Complexity Score**: A calculated complexity score based on the LOC and number of functions in the repository.

The results of the analysis are presented in an HTML report, which includes details of each repository's complexity.

## Features

- **Automated GitHub Authentication**: The script uses a GitHub token for authentication.
- **Repository Analysis**: Fetches repositories from the authenticated GitHub account and analyzes each repository's code files.
- **Complexity Metrics**: Calculates and displays the LOC, number of functions, and a custom complexity score.
- **HTML Report Generation**: Generates an HTML file containing the analysis results.

## How to Run the Project

### Prerequisites

1. **Python 3.x**: Make sure you have Python installed on your system. You can download it [here](https://www.python.org/downloads/).
2. **GitHub Token**: You will need a personal access token from GitHub to authenticate API requests.
   - Follow [this guide](https://docs.github.com/en/enterprise-server@3.0/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) to generate your GitHub token.
   - Set the token as an environment variable called `GITHUB_TOKEN` in your environment.

### Running the Project

1. Clone the repository to your local machine:
   ```bash
   git clone <repository_url>
