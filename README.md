<div align="center">
  <h2>Jobsyk Bot</h2>
  <p><strong>A discord bot that helps you with your job search!</strong><br>(It is currently a script but I will make it a discord bot trust)</p>
</div>

<div align="center">
<p>
Todo:
<br> add linkedin support (i want to try calling an API instead of scraping)
<br> add database to keep track of postings that were already seen
<br> make a discord bot out of this for friends :)
<br> get an internship (optional (not really))
</p> 
</div>

<div align="center">
<h3>Languages and Tools Used</h3>
<a href="https://www.python.org/" target="blank"><img alt="Python" width="30px" style="padding-right:10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" /></a>
<a href="https://www.selenium.dev/" target="blank"><img alt="Selenium" width="30px" style="padding-right:10px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/selenium/selenium-original.svg" /></a>
</div>
<br>

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com), [Python](https://www.python.org/downloads/), and [pip](https://pip.pypa.io/en/stable/) (which comes with Python) installed on your computer.<br><br> From your command line:

```bash
# Clone this repository
$ git clone https://github.com/jasutiin/jobsyk-bot

# Navigate into the project directory
$ cd jobsyk-bot

# Create a virtual environment
$ python -m venv venv

# Activate the virtual environment
# On macOS/Linux:
$ source venv/bin/activate

# On Windows:
$ venv\Scripts\activate

# Install the required Python packages
$ pip install -r requirements.txt

# Exit out of venv
$ deactivate
```

You also need to install [ChromeDriver](https://developer.chrome.com/docs/chromedriver/downloads). Make sure to install the version compatible with your Chrome browser. You can check this by:

1. Opening Chrome on your computer
2. Click the 3 vertical dots in the top-right corner
3. Click Settings
4. Click About Chrome

After that, put the chromedriver.exe file in the same directory as the script.py file.

Now you can run the script!

```
# Run the Python app
$ python script.py <location>

# Example
$ python script.py canada
```
