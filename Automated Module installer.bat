@echo off
color 4
echo (" First you should Install PYTHON on your PC before you run this Module")
pause
echo EXECUTE AUTO MODULE INSTALLER
color 3
echo ( Processes Completed 0%)
pip install pyautogui
pip install pyttsx4
echo ( Processes Completed 5%)
pip install pyaudio
echo (Processes Completed 10%)
pip install SpeechRecognition
echo ( Processes Completed 30%)
pip install wikipedia
echo (Processes Completed 40%)
color F
pip install pyjokes
pip install nltk
echo ( Processes Completed 70%)
pip install setuptools
pip install wikipedia-api
echo ( Processes Completed 80%)
pip install colorama
color 3
echo ( Processes Complete 90%)
:: Download necessary NLTK resources
python -m nltk.downloader punkt
python -m nltk.downloader stopwords
python -m nltk.downloader wordnet

color 2
echo ( Processes Completed 100%)
echo All modules installed successfully!
pause

