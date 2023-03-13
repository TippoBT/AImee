# Installation

1. Clone the repo, open in VSCode, and then open a terminal within VSCode

2. Create a virtual-environment by typing the following into your terminal
```
python -m venv .venv
```

3. Activate the virtual environment
```
.venv/Source/activate
```

4. Install project requirements
```
pip install -r requirements.txt
```

5. You will also need to install RedBot with this command
```
pip install git+{the repo url}
```

6. Make a file called `.env` and put the ElevenLabs API key in there like this
```
ELEVENLABS_API_KEY={the key}
```

7. In your terminal navigate to the aimee folder
```
cd .\aimee\
```

8. To run the program use
```
python aimee.py
```


### Recommended - Built-in Downloader
```
[p]repo add AImee https://github.com/TippoBT/AImee
[p]cog install AImee aimee
[p]load aimee
```
